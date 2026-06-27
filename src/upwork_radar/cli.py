"""Command-line entry point: parse -> score -> rank -> write outputs.

Usage:
    python -m upwork_radar analyze --feed data/feed_sample.txt \
        --profile profile.json --top 5 --out out
"""

from __future__ import annotations

import argparse
import csv
import os
import sys

from .parse import parse_feed_file
from .parse_nuxt import parse_feed_json_file
from .proposal import proposal_opener
from .score import load_profile, score_and_rank
from .models import Job

# Terms that define Derek's Microsoft "wheelhouse" for the summary count.
_WHEELHOUSE = (
    "power automate",
    "power apps",
    "power platform",
    "sharepoint",
    "copilot",
    "power bi",
    "fabric",
    "dynamics 365",
    "microsoft 365",
    "m365",
    "office 365",
    "azure",
)


def _in_wheelhouse(job: Job) -> bool:
    # Title + skills only (not description) — a passing mention of "Azure" in a
    # paragraph isn't a real Microsoft-stack job.
    blob = f"{job.title} {' '.join(job.skills)}".lower()
    return any(term in blob for term in _WHEELHOUSE)


def _pay_str(job: Job) -> str:
    if job.pricing_type == "fixed" and job.budget is not None:
        return f"${int(job.budget)} fixed"
    if job.pricing_type == "hourly":
        if job.rate_low is not None and job.rate_high is not None:
            return f"${int(job.rate_low)}-${int(job.rate_high)}/hr"
        if job.rate_low is not None:
            return f"${int(job.rate_low)}/hr"
        return "hourly"
    return "—"


def write_csv(jobs: list[Job], path: str) -> None:
    fields = [
        "score", "fit", "competition", "budget_score", "freshness",
        "client_quality", "eligible", "eligibility_note", "title",
        "pricing_type", "budget", "rate_low", "rate_high", "experience",
        "proposals_raw", "posted_raw", "posted_minutes", "payment_verified",
        "client_rating", "client_spent_raw", "client_country",
        "matched_keywords", "skills",
    ]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for job in jobs:
            writer.writerow(job.to_dict())


def write_markdown(jobs: list[Job], path: str, top: int) -> None:
    lines: list[str] = []
    lines.append("# Upwork shortlist\n")
    lines.append(
        f"Ranked **{len(jobs)} jobs** by `fit × low-competition × budget × "
        f"freshness × client`. Top **{top}** include a draft proposal opener.\n"
    )

    lines.append("## Ranked top jobs\n")
    lines.append("| # | Score | Fit | Title | Pay | Proposals | Posted | Eligible |")
    lines.append("|--:|------:|----:|-------|-----|-----------|--------|----------|")
    for i, job in enumerate(jobs[: max(top, 25)], 1):
        elig = "✅" if job.eligible else "⛔"
        title = job.title.replace("|", "\\|")[:70]
        lines.append(
            f"| {i} | {job.score:.3f} | {job.fit:.2f} | {title} | "
            f"{_pay_str(job)} | {job.proposals_raw or '—'} | "
            f"{job.posted_raw or '—'} | {elig} |"
        )
    lines.append("")

    lines.append(f"## Top {top}: detail + draft proposal openers\n")
    for i, job in enumerate(jobs[:top], 1):
        heading = f"### {i}. {job.title}"
        if job.url:
            heading = f"### {i}. [{job.title}]({job.url})"
        lines.append(heading + "\n")
        lines.append(
            f"- **Score {job.score:.3f}** — fit {job.fit:.2f}, "
            f"competition {job.competition:.2f}, budget {job.budget_score:.2f}, "
            f"freshness {job.freshness:.2f}, client {job.client_quality:.2f}"
        )
        lines.append(
            f"- **Pay:** {_pay_str(job)} · **Level:** {job.experience or '—'} · "
            f"**Proposals:** {job.proposals_raw or '—'} · **Posted:** "
            f"{job.posted_raw or '—'} ago"
        )
        client = (
            f"{job.client_country or '—'}, "
            f"{'payment verified' if job.payment_verified else 'payment unverified'}"
            f"{', ' + str(job.client_rating) + '★' if job.client_rating else ''}"
            f"{', ' + job.client_spent_raw if job.client_spent_raw else ''}"
        )
        lines.append(f"- **Client:** {client}")
        if job.eligibility_note:
            lines.append(f"- **Note:** {job.eligibility_note}")
        if not job.eligible:
            lines.append(f"- ⛔ **Ineligible:** {job.eligibility_note}")
        if job.matched_keywords:
            uniq = list(dict.fromkeys(job.matched_keywords))
            lines.append(f"- **Matched:** {', '.join(uniq[:10])}")
        lines.append("")
        lines.append("> **Draft proposal opener** (review & edit before sending):")
        lines.append(">")
        for para in proposal_opener(job).split("\n"):
            lines.append(f"> {para}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def cmd_analyze(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile)
    # A .json feed is the clean bookmarklet export; anything else is saved page text.
    if args.feed.lower().endswith(".json"):
        jobs = parse_feed_json_file(args.feed)
    else:
        jobs = parse_feed_file(args.feed)
    if not jobs:
        print(f"No jobs parsed from {args.feed!r}.", file=sys.stderr)
        return 1
    ranked = score_and_rank(jobs, profile)

    os.makedirs(args.out, exist_ok=True)
    md_path = os.path.join(args.out, "shortlist.md")
    csv_path = os.path.join(args.out, "shortlist.csv")
    write_markdown(ranked, md_path, args.top)
    write_csv(ranked, csv_path)

    wheelhouse = sum(1 for j in ranked if _in_wheelhouse(j))
    eligible = sum(1 for j in ranked if j.eligible)
    print(f"Parsed {len(ranked)} unique jobs "
          f"({wheelhouse} in wheelhouse, {eligible} eligible).")
    print(f"\nTop {min(args.top, len(ranked))}:")
    for i, job in enumerate(ranked[: args.top], 1):
        flag = "" if job.eligible else "  [ineligible]"
        print(f"  {i}. {job.score:.3f}  {job.title[:72]}{flag}")
    print(f"\nWrote:\n  {md_path}\n  {csv_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="upwork-radar",
        description="Rank a saved Upwork feed by fit to your profile.",
    )
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("analyze", help="parse, score and rank a feed file")
    a.add_argument("--feed", required=True, help="path to saved feed text")
    a.add_argument("--profile", default="profile.json", help="profile JSON")
    a.add_argument("--top", type=int, default=5, help="how many to detail")
    a.add_argument("--out", default="out", help="output directory")
    a.set_defaults(func=cmd_analyze)
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
