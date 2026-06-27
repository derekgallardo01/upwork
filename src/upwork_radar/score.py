"""Score and rank parsed jobs against a profile.

Each component is normalized to 0..1 and combined with configurable weights:

    final = w_fit*fit + w_comp*competition + w_budget*budget
            + w_fresh*freshness + w_client*client_quality

Ineligible jobs (residency requirements Derek can't meet) are heavily penalized
so they sink to the bottom of the shortlist rather than disappearing silently.
"""

from __future__ import annotations

import json
import re

from .models import Job

# Competition: fewer competing proposals is better. Keyed by substrings that
# appear in Upwork's "Proposals:" ranges.
_PROPOSAL_SCORE = [
    ("less than 5", 1.0),
    ("fewer than 5", 1.0),
    ("5 to 10", 0.75),
    ("10 to 15", 0.55),
    ("15 to 20", 0.4),
    ("20 to 50", 0.2),
    ("50+", 0.1),
    ("more than 50", 0.1),
]

# Microsoft / AI term groups used for the "intersection" sweet-spot bonus.
_MS_TERMS = re.compile(
    r"power automate|power apps|power platform|sharepoint|dynamics 365|"
    r"power bi|microsoft fabric|microsoft 365|m365|office 365|copilot studio|"
    r"azure",
    re.I,
)
_AI_TERMS = re.compile(
    r"\bai\b|artificial intelligence|copilot|claude|agent|agentic|llm|gpt|"
    r"openai|rag|chatbot|automation",
    re.I,
)

# Fixed budgets below this (USD) are treated as placeholder/junk, not real scope.
MIN_PLAUSIBLE_FIXED = 20

# Nationality adjectives mapped to the country term used in the exclude list, so
# a title like "Australian Power Platform Contractor" is caught even without a
# "based in ..." phrase.
_NATIONALITY = {
    "canadian": "canada",
    "australian": "australia",
    "british": "united kingdom",
    "indian": "india",
    "german": "germany",
    "french": "france",
    "filipino": "philippines",
    "portuguese": "portugal",
}


def load_profile(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _competition_score(proposals_raw: str | None) -> float:
    if not proposals_raw:
        return 0.5  # unknown -> neutral
    low = proposals_raw.lower()
    for key, val in _PROPOSAL_SCORE:
        if key in low:
            return val
    return 0.5


def _freshness_score(minutes: int | None) -> float:
    """1.0 for just-posted, decaying to ~0 over two weeks."""
    if minutes is None:
        return 0.5
    two_weeks = 60 * 24 * 14
    return max(0.0, 1.0 - minutes / two_weeks)


def _budget_score(job: Job, target_rate: float) -> float:
    """Normalize pay into 0..1. Hourly is compared to the target rate; fixed
    budgets are mapped on a log-ish scale (a $1K+ project scores high)."""
    if job.pricing_type == "hourly":
        mid = job.rate_mid
        if mid is None:
            return 0.5
        return min(1.0, mid / (target_rate * 1.5))
    if job.pricing_type == "fixed" and job.budget is not None:
        # Implausibly low fixed budgets (e.g. "$5") are almost always placeholder
        # values, not the real scope — de-rank them rather than letting a strong
        # fit float them to the top.
        if job.budget < MIN_PLAUSIBLE_FIXED:
            return 0.1
        # $50 -> ~0.16, $200 -> ~0.46, $500 -> ~0.66, $1000 -> ~0.8, $2k+ -> ~1
        import math

        return min(1.0, math.log10(max(job.budget, 1)) / math.log10(3000))
    return 0.4


def _fit_score(job: Job, profile: dict) -> tuple[float, list[str]]:
    """Weighted keyword match. Title and skill matches count more than a hit
    buried in the description. Returns (score 0..1, matched terms)."""
    title = job.title.lower()
    skills = " ".join(job.skills).lower()
    desc = job.description.lower()

    matched: list[str] = []
    strong_raw = 0.0   # accumulation from strong-tier (Microsoft) terms
    other_raw = 0.0    # medium + weak tiers
    for tier_name, tier in profile.get("keywords", {}).items():
        w = tier.get("weight", 0.5)
        for term in tier.get("terms", []):
            t = term.lower()
            hit_weight = 0.0
            if t in title:
                hit_weight = 1.0
            elif t in skills:
                hit_weight = 0.8
            elif t in desc:
                hit_weight = 0.4
            if hit_weight:
                contribution = w * hit_weight
                if tier_name == "strong":
                    strong_raw += contribution
                else:
                    other_raw += contribution
                matched.append(term)

    # Diminishing returns on the medium/weak pile so a job can't reach the top of
    # the fit scale on generic AI buzzwords alone — strong Microsoft terms are
    # what actually separate Derek's wheelhouse from the generic-AI crowd.
    other_capped = min(other_raw, 1.2)
    raw = strong_raw + other_capped

    # Sweet-spot bonus: the job names BOTH a Microsoft product AND AI/agent work.
    blob = f"{title} {skills} {desc}"
    if _MS_TERMS.search(blob) and _AI_TERMS.search(blob):
        raw += profile.get("intersection_bonus", 0.0)

    # Squash to 0..1. Reaching ~1.0 now needs several strong matches, not just a
    # long tail of weak ones.
    return min(1.0, raw / 4.0), matched


def _client_quality_score(job: Job) -> float:
    score = 0.5
    if job.payment_verified is True:
        score += 0.25
    elif job.payment_verified is False:
        score -= 0.15
    if job.client_rating is not None:
        score += (job.client_rating - 4.0) * 0.1  # 5.0 -> +0.1, 4.0 -> 0
    if job.client_spent_raw and job.client_spent_raw != "$0 spent":
        score += 0.15
    return max(0.0, min(1.0, score))


def _check_eligibility(job: Job, profile: dict) -> tuple[bool, str]:
    """Detect residency requirements Derek (US-based) can't meet."""
    blob = f"{job.title} {job.description}".lower()
    excluded = {c.lower() for c in profile.get("exclude_country_requirements", [])}

    # Nationality adjective in the TITLE (e.g. "Australian ... Contractor") is a
    # strong location signal even with no "based in" phrasing.
    title_low = job.title.lower()
    for adj, country in _NATIONALITY.items():
        if country in excluded and re.search(rf"\b{adj}\b", title_low):
            return False, f"requires {country.title()} residency"

    for country in excluded:
        if country in blob and re.search(
            r"(based in|located in|resident|residing|must be (?:a )?|only)\s*[^.]{0,30}"
            + re.escape(country),
            blob,
        ):
            return False, f"requires {country.title()} residency"
        # Common phrasing: "<country> resident" / "<country>-based"
        if re.search(rf"\b{re.escape(country)}\b[ -](resident|based|only)", blob):
            return False, f"requires {country.title()} residency"
        # Nationality adjective anywhere with a person/role noun nearby.
        for adj, c2 in _NATIONALITY.items():
            if c2 == country and re.search(
                rf"\b{adj}\b\s*(resident|citizen|contractor|developer|freelancer|"
                rf"based|only)",
                blob,
            ):
                return False, f"requires {country.title()} residency"
    note = ""
    if re.search(r"\b(u\.s\.|us|united states)[ -]?(based|only|resident)", blob):
        note = "US-based preferred (eligible+)"
    if "spanish" in blob and "spanish" in [
        l.lower() for l in profile.get("languages", [])
    ]:
        note = (note + "; " if note else "") + "Spanish a plus (bilingual)"
    return True, note


def score_job(job: Job, profile: dict) -> Job:
    weights = profile.get("weights", {})
    target_rate = profile.get("target_rate", 75)

    job.fit, job.matched_keywords = _fit_score(job, profile)
    job.competition = _competition_score(job.proposals_raw)
    job.budget_score = _budget_score(job, target_rate)
    job.freshness = _freshness_score(job.posted_minutes)
    job.client_quality = _client_quality_score(job)
    job.eligible, job.eligibility_note = _check_eligibility(job, profile)

    base = (
        weights.get("fit", 0.45) * job.fit
        + weights.get("competition", 0.20) * job.competition
        + weights.get("budget", 0.15) * job.budget_score
        + weights.get("freshness", 0.12) * job.freshness
        + weights.get("client_quality", 0.08) * job.client_quality
    )
    if not job.eligible:
        base *= 0.25  # push ineligible jobs far down, but keep them visible
    job.score = round(base, 4)
    return job


def score_and_rank(jobs: list[Job], profile: dict) -> list[Job]:
    for job in jobs:
        score_job(job, profile)
    return sorted(jobs, key=lambda j: j.score, reverse=True)
