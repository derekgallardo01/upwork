"""Parse a raw Upwork "Find work" feed scrape into structured Job records.

The scrape is the visible text of the feed page. Each job is a block that
begins with a ``Posted ... ago`` line and runs until the next one. Inside a
block the fields appear in a consistent order, which we anchor on:

    Posted 19 minutes ago
    •
    Proposals: Fewer than 5
    <TITLE>
    Fixed-price - Intermediate - Est. Budget: $200       (or Hourly: $a-$b - ...)
    <description paragraph>
    moreabout "<TITLE>"
    Skills
    [Skip skills]
    <skill>
    ...
    Verified | Unverified
    Payment verified | Payment unverified
    [rating e.g. 5.0]
    $5K+ spent
      <Country>
"""

from __future__ import annotations

import re

from .models import Job

POSTED_RE = re.compile(r"^Posted\s+(.+?)\s+ago\s*$")
PROPOSALS_RE = re.compile(r"^Proposals:\s*(.+?)\s*$")
MOREABOUT_RE = re.compile(r'^moreabout\s+"(.*)"\s*$')
PRICING_RE = re.compile(r"^(Fixed-price|Hourly)")
RATING_RE = re.compile(r"^([0-5]\.\d)$")
SPENT_RE = re.compile(r"^\$\S+\s+spent$")
BUDGET_RE = re.compile(r"Est\.\s*Budget:\s*\$([\d.,]+)\s*([KkMm]?)")
HOURLY_RANGE_RE = re.compile(r"\$([\d.,]+)\s*-\s*\$([\d.,]+)")
HOURLY_SINGLE_RE = re.compile(r"Hourly:\s*\$([\d.,]+)\b")
EXPERIENCE_RE = re.compile(r"\b(Entry level|Intermediate|Expert)\b")
EST_TIME_RE = re.compile(r"Est\.\s*Time:\s*(.+?)\s*$")

_NUM_SUFFIX = {"k": 1_000, "m": 1_000_000, "": 1}


def _to_amount(num: str, suffix: str = "") -> float | None:
    try:
        return float(num.replace(",", "")) * _NUM_SUFFIX[suffix.lower()]
    except (ValueError, KeyError):
        return None


def parse_posted_minutes(raw: str) -> int | None:
    """Convert '19 minutes', '3 hours', '2 days', '1 week' -> minutes."""
    m = re.match(r"(\d+)\s+(minute|hour|day|week|month)s?", raw.strip(), re.I)
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2).lower()
    factor = {
        "minute": 1,
        "hour": 60,
        "day": 60 * 24,
        "week": 60 * 24 * 7,
        "month": 60 * 24 * 30,
    }[unit]
    return n * factor


def _parse_pricing(line: str, job: Job) -> None:
    if line.startswith("Fixed-price"):
        job.pricing_type = "fixed"
        m = BUDGET_RE.search(line)
        if m:
            job.budget = _to_amount(m.group(1), m.group(2))
    elif line.startswith("Hourly"):
        job.pricing_type = "hourly"
        m = HOURLY_RANGE_RE.search(line)
        if m:
            job.rate_low = _to_amount(m.group(1))
            job.rate_high = _to_amount(m.group(2))
        else:
            m = HOURLY_SINGLE_RE.search(line)
            if m:
                job.rate_low = _to_amount(m.group(1))
    em = EXPERIENCE_RE.search(line)
    if em:
        job.experience = em.group(1)
    tm = EST_TIME_RE.search(line)
    if tm:
        job.est_time = tm.group(1)


def _parse_pre(pre: list[str], job: Job) -> None:
    """Parse the lines that precede the moreabout anchor: posted, proposals,
    pricing, on-page title and description.

    ``pre`` is the slice between the previous anchor and this one, so its tail
    holds THIS job's fields (its head may hold the previous job's client block,
    which we ignore by starting at this job's 'Posted'/pricing line)."""
    # Locate this job's start: the last 'Posted ... ago', else the last pricing
    # line (some jobs in the feed have no 'Posted' line).
    start = None
    for i in range(len(pre) - 1, -1, -1):
        if POSTED_RE.match(pre[i].strip()):
            start = i
            break
    pricing_idx = None
    for i in range(len(pre) - 1, -1, -1):
        if PRICING_RE.match(pre[i].strip()):
            pricing_idx = i
            break
    if start is None:
        start = pricing_idx - 1 if pricing_idx else 0

    for ln in pre[start:]:
        t = ln.strip()
        pm = POSTED_RE.match(t)
        if pm and job.posted_raw is None:
            job.posted_raw = pm.group(1)
            job.posted_minutes = parse_posted_minutes(pm.group(1))
            continue
        prm = PROPOSALS_RE.match(t)
        if prm and job.proposals_raw is None:
            job.proposals_raw = prm.group(1)
            continue

    if pricing_idx is not None:
        _parse_pricing(pre[pricing_idx].strip(), job)
        # Description is everything between the pricing line and the anchor,
        # skipping blanks.
        desc_lines = [ln.strip() for ln in pre[pricing_idx + 1 :] if ln.strip()]
        job.description = " ".join(desc_lines).strip()


def _parse_post(post: list[str], job: Job) -> None:
    """Parse the lines after the moreabout anchor: skills + client signals.

    Stops at the next job's 'Posted ... ago' line (the boundary between this
    job's client block and the following job)."""
    in_skills = False
    for ln in post:
        t = ln.strip()
        if not t:
            continue
        if POSTED_RE.match(t):
            break  # reached the next job
        if t in ("Skills", "Skip skills"):
            in_skills = True
            continue
        if t in ("Verified", "Unverified"):
            in_skills = False
            continue
        if t == "Payment verified":
            job.payment_verified = True
            continue
        if t == "Payment unverified":
            job.payment_verified = False
            continue
        if SPENT_RE.match(t):
            job.client_spent_raw = t
            continue
        if RATING_RE.match(t) and job.client_rating is None:
            job.client_rating = float(t)
            continue
        if in_skills:
            job.skills.append(t)
            continue
        # Country: first short, alphabetic line once we've passed the spend line.
        if (
            job.client_spent_raw is not None
            and job.client_country is None
            and len(t) < 40
            and t[0].isalpha()
        ):
            job.client_country = t


def parse_feed(text: str, dedupe: bool = True) -> list[Job]:
    """Parse the full feed text into a list of unique Job records.

    Anchored on the ``moreabout "<title>"`` line, which appears exactly once per
    job and is the most reliable record marker in the scrape.
    """
    lines = text.splitlines()
    anchors = [i for i, ln in enumerate(lines) if MOREABOUT_RE.match(ln.strip())]

    jobs: list[Job] = []
    for k, a in enumerate(anchors):
        prev = anchors[k - 1] if k > 0 else -1
        nxt = anchors[k + 1] if k + 1 < len(anchors) else len(lines)
        title = MOREABOUT_RE.match(lines[a].strip()).group(1).strip()
        if not title:
            continue
        job = Job(title=title)
        _parse_pre(lines[prev + 1 : a], job)
        _parse_post(lines[a + 1 : nxt], job)
        jobs.append(job)

    if dedupe:
        seen: set[str] = set()
        unique: list[Job] = []
        for j in jobs:
            key = j.title.strip().lower()
            if key not in seen:
                seen.add(key)
                unique.append(j)
        jobs = unique
    return jobs


def parse_feed_file(path: str, dedupe: bool = True) -> list[Job]:
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return parse_feed(fh.read(), dedupe=dedupe)
