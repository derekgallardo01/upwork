"""Tests for the bookmarklet JSON parser."""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from upwork_radar.parse_nuxt import parse_feed_json, _fmt_spent  # noqa: E402

SAMPLE = json.dumps({
    "source": "most-recent",
    "jobs": [
        {
            "title": "Asana → SharePoint flow",
            "url": "https://www.upwork.com/jobs/~02aaa",
            "description": "Power Automate flow.",
            "pricing_type": "fixed", "budget": 200,
            "experience": "Intermediate", "proposals_raw": "5 to 10",
            "posted_raw": "2026-06-27T19:36:10Z", "posted_minutes": 54,
            "skills": ["Asana", "Microsoft Power Automate"],
            "payment_verified": False, "client_rating": None,
            "client_spent": 0, "client_country": "Portugal",
        },
        {
            "title": "AI Engineer for RAG platform",
            "url": "https://www.upwork.com/jobs/~02bbb",
            "description": "LangChain, RAG, Python.",
            "pricing_type": "hourly", "rate_low": 30, "rate_high": 60,
            "experience": "Expert", "proposals_raw": "20 to 50",
            "posted_raw": "2026-06-27T19:04:14Z", "posted_minutes": 86,
            "skills": ["Python", "Machine Learning"],
            "payment_verified": True, "client_rating": 5.0,
            "client_spent": 5082.99, "client_country": "Pakistan",
        },
    ],
})


def test_parses_two_jobs():
    assert len(parse_feed_json(SAMPLE)) == 2


def test_fixed_job_fields():
    job = parse_feed_json(SAMPLE)[0]
    assert job.pricing_type == "fixed"
    assert job.budget == 200
    assert job.proposals_raw == "5 to 10"
    assert job.posted_minutes == 54
    assert job.payment_verified is False
    assert job.client_country == "Portugal"
    assert job.client_spent_raw == "$0 spent"
    assert job.url.endswith("~02aaa")
    assert "Microsoft Power Automate" in job.skills


def test_hourly_job_fields():
    job = parse_feed_json(SAMPLE)[1]
    assert job.pricing_type == "hourly"
    assert job.rate_low == 30 and job.rate_high == 60
    assert job.rate_mid == 45
    assert job.payment_verified is True
    assert job.client_rating == 5.0
    assert job.client_spent_raw == "$5K+ spent"


def test_accepts_bare_list():
    bare = json.dumps([{"title": "X", "pricing_type": "fixed", "budget": 50}])
    jobs = parse_feed_json(bare)
    assert len(jobs) == 1 and jobs[0].budget == 50


def test_dedupe_by_url():
    doubled = json.loads(SAMPLE)
    doubled["jobs"] = doubled["jobs"] + doubled["jobs"]
    text = json.dumps(doubled)
    assert len(parse_feed_json(text, dedupe=True)) == 2
    assert len(parse_feed_json(text, dedupe=False)) == 4


def test_fmt_spent():
    assert _fmt_spent(0) == "$0 spent"
    assert _fmt_spent(5082.99) == "$5K+ spent"
    assert _fmt_spent(610557) == "$611K+ spent"
    assert _fmt_spent(None) is None
    assert _fmt_spent(450) == "$450 spent"
