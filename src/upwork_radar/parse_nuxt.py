"""Parse the clean ``feed.json`` produced by the browser bookmarklet.

The bookmarklet (see ``bookmarklet.js``) reads Upwork's embedded
``window.__NUXT__`` state in your own logged-in browser and writes a small,
already-normalized JSON file. This is far cleaner than scraping rendered page
text: real post timestamps, exact spend, hourly min/max, etc.

Expected shape (tolerant of a bare list, or ``{"jobs": [...]}``)::

    {
      "captured_at": "2026-06-27T20:15:00.000Z",
      "source": "most-recent",
      "jobs": [
        {
          "title": "...", "url": "https://www.upwork.com/jobs/~02...",
          "description": "...",
          "pricing_type": "fixed" | "hourly",
          "budget": 200,                 # fixed only
          "rate_low": 30, "rate_high": 60,   # hourly only
          "experience": "Intermediate",
          "proposals_raw": "5 to 10",
          "posted_minutes": 73, "posted_raw": "2026-06-27T19:36:10Z",
          "skills": ["Asana", "Microsoft Power Automate"],
          "payment_verified": false,
          "client_rating": null, "client_spent": 0,
          "client_country": "Portugal"
        }
      ]
    }
"""

from __future__ import annotations

import json

from .models import Job


def _fmt_spent(value) -> str | None:
    """Mirror the feed's "$X spent" string so the existing client-quality
    scorer (which special-cases "$0 spent") works unchanged."""
    if value is None:
        return None
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    if n <= 0:
        return "$0 spent"
    if n >= 1_000_000:
        return f"${n / 1_000_000:.0f}M+ spent"
    if n >= 1_000:
        return f"${n / 1_000:.0f}K+ spent"
    return f"${int(n)} spent"


def _record_to_job(rec: dict) -> Job | None:
    title = (rec.get("title") or "").strip()
    if not title:
        return None
    job = Job(
        title=title,
        description=(rec.get("description") or "").strip(),
        skills=[s for s in (rec.get("skills") or []) if s],
        posted_raw=rec.get("posted_raw"),
        posted_minutes=rec.get("posted_minutes"),
        proposals_raw=rec.get("proposals_raw"),
        pricing_type=rec.get("pricing_type"),
        budget=rec.get("budget"),
        rate_low=rec.get("rate_low"),
        rate_high=rec.get("rate_high"),
        experience=rec.get("experience"),
        est_time=rec.get("est_time"),
        payment_verified=rec.get("payment_verified"),
        client_rating=rec.get("client_rating"),
        client_spent_raw=_fmt_spent(rec.get("client_spent")),
        client_country=rec.get("client_country"),
        url=rec.get("url"),
    )
    return job


def parse_feed_json(text: str, dedupe: bool = True) -> list[Job]:
    """Parse bookmarklet JSON text into Job records."""
    data = json.loads(text)
    records = data.get("jobs", []) if isinstance(data, dict) else data

    jobs: list[Job] = []
    for rec in records:
        if isinstance(rec, dict):
            job = _record_to_job(rec)
            if job:
                jobs.append(job)

    if dedupe:
        seen: set[str] = set()
        unique: list[Job] = []
        for j in jobs:
            key = (j.url or j.title).strip().lower()
            if key not in seen:
                seen.add(key)
                unique.append(j)
        jobs = unique
    return jobs


def parse_feed_json_file(path: str, dedupe: bool = True) -> list[Job]:
    with open(path, "r", encoding="utf-8") as fh:
        return parse_feed_json(fh.read(), dedupe=dedupe)
