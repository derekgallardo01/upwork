"""Tests for scoring and ranking."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from upwork_radar.models import Job  # noqa: E402
from upwork_radar.score import score_job, score_and_rank  # noqa: E402

PROFILE = {
    "target_rate": 75,
    "languages": ["English", "Spanish"],
    "keywords": {
        "strong": {"weight": 1.0, "terms": ["power automate", "sharepoint", "copilot studio"]},
        "medium": {"weight": 0.6, "terms": ["copilot", "claude", "ai agent", "automation"]},
        "weak": {"weight": 0.3, "terms": ["ai", "python"]},
    },
    "intersection_bonus": 0.25,
    "weights": {"fit": 0.45, "competition": 0.20, "budget": 0.15,
                "freshness": 0.12, "client_quality": 0.08},
    "exclude_country_requirements": ["canada"],
}


def _ms_ai_job():
    return Job(
        title="Copilot Studio agent + Power Automate flow",
        description="Build a Copilot Studio AI agent with Power Automate automation.",
        skills=["Copilot Studio", "Power Automate"],
        proposals_raw="Fewer than 5",
        pricing_type="fixed", budget=500.0, posted_minutes=30,
        payment_verified=True,
    )


def _generic_ai_job():
    return Job(
        title="AI Engineer for Python platform",
        description="Build RAG pipelines in Python with vector databases.",
        skills=["Python", "Machine Learning"],
        proposals_raw="20 to 50",
        pricing_type="hourly", rate_low=20.0, rate_high=35.0, posted_minutes=4000,
        payment_verified=False,
    )


def test_ms_ai_outranks_generic():
    ms = score_job(_ms_ai_job(), PROFILE)
    generic = score_job(_generic_ai_job(), PROFILE)
    assert ms.score > generic.score
    assert ms.fit > generic.fit


def test_intersection_bonus_applied():
    # The MS+AI job hits both groups, so fit should be strong.
    ms = score_job(_ms_ai_job(), PROFILE)
    assert ms.fit > 0.6


def test_low_competition_beats_high():
    low = Job(title="x", proposals_raw="Fewer than 5")
    high = Job(title="x", proposals_raw="50+")
    score_job(low, PROFILE)
    score_job(high, PROFILE)
    assert low.competition > high.competition


def test_ineligible_penalized():
    job = Job(
        title="Power Automate Specialist",
        description="We are looking for a freelancer based in Canada to maintain flows.",
        proposals_raw="Fewer than 5", pricing_type="fixed", budget=500.0,
        posted_minutes=10,
    )
    score_job(job, PROFILE)
    assert job.eligible is False
    assert "Canada" in job.eligibility_note
    # Penalty pushes it below a clean eligible job of similar shape.
    clean = score_job(_ms_ai_job(), PROFILE)
    assert job.score < clean.score


def test_ranking_orders_by_score():
    jobs = [_generic_ai_job(), _ms_ai_job()]
    ranked = score_and_rank(jobs, PROFILE)
    assert ranked[0].title.startswith("Copilot Studio")
