"""Data model for a parsed Upwork job posting."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Job:
    """A single job parsed from an Upwork feed scrape.

    Most fields are optional because not every block in the feed carries every
    signal (e.g. brand-new clients have no rating or spend).
    """

    title: str
    description: str = ""
    skills: list[str] = field(default_factory=list)
    url: Optional[str] = None

    # Posting metadata
    posted_raw: Optional[str] = None          # e.g. "19 minutes ago"
    posted_minutes: Optional[int] = None       # parsed age in minutes
    proposals_raw: Optional[str] = None        # e.g. "Fewer than 5"

    # Pricing
    pricing_type: Optional[str] = None         # "fixed" | "hourly"
    budget: Optional[float] = None             # fixed budget, USD
    rate_low: Optional[float] = None           # hourly low, USD
    rate_high: Optional[float] = None          # hourly high, USD
    experience: Optional[str] = None           # Entry | Intermediate | Expert
    est_time: Optional[str] = None

    # Client signals
    payment_verified: Optional[bool] = None
    client_rating: Optional[float] = None
    client_spent_raw: Optional[str] = None     # e.g. "$5K+ spent"
    client_country: Optional[str] = None

    # --- Scoring output (populated by score.py) ---
    score: float = 0.0
    fit: float = 0.0
    competition: float = 0.0
    budget_score: float = 0.0
    freshness: float = 0.0
    client_quality: float = 0.0
    eligible: bool = True
    eligibility_note: str = ""
    matched_keywords: list[str] = field(default_factory=list)

    @property
    def rate_mid(self) -> Optional[float]:
        if self.rate_low is not None and self.rate_high is not None:
            return (self.rate_low + self.rate_high) / 2
        return self.rate_low or self.rate_high

    def to_dict(self) -> dict:
        d = asdict(self)
        d["skills"] = "; ".join(self.skills)
        d["matched_keywords"] = "; ".join(self.matched_keywords)
        return d
