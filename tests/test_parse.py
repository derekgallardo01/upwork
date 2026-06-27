"""Tests for the feed parser."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from upwork_radar.parse import parse_feed, parse_posted_minutes  # noqa: E402

SAMPLE = """\
Posted 19 minutes ago
•
Proposals: Fewer than 5
Set up Asana flow: Timesheets to SharePoint
Fixed-price - Intermediate - Est. Budget: $200
I need a simple automation for a 15-user pilot. Use Power Automate (preferred).
moreabout "Set up Asana flow: Timesheets to SharePoint"
Skills
Skip skills
Asana
Microsoft Power Automate
Office 365
Unverified

Payment unverified
$0 spent
  Portugal
Posted 1 hour ago
•
Proposals: 20 to 50
Generic AI Engineer for RAG Platform
Hourly: $30-$60 - Expert - Est. Time: Less than 1 month, Less than 30 hrs/week
Build RAG pipelines with vector databases and LLM orchestration in Python.
moreabout "Generic AI Engineer for RAG Platform"
Skills
Python
Artificial Intelligence
Machine Learning
Verified

Payment verified
5.0
$5K+ spent
  United States
"""


def test_parses_two_jobs():
    jobs = parse_feed(SAMPLE)
    assert len(jobs) == 2


def test_first_job_fields():
    job = parse_feed(SAMPLE)[0]
    assert job.title == "Set up Asana flow: Timesheets to SharePoint"
    assert job.pricing_type == "fixed"
    assert job.budget == 200.0
    assert job.experience == "Intermediate"
    assert job.proposals_raw == "Fewer than 5"
    assert job.posted_minutes == 19
    assert "Microsoft Power Automate" in job.skills
    assert "Asana" in job.skills
    assert job.payment_verified is False
    assert job.client_country == "Portugal"
    assert "15-user pilot" in job.description


def test_second_job_hourly_fields():
    job = parse_feed(SAMPLE)[1]
    assert job.pricing_type == "hourly"
    assert job.rate_low == 30.0 and job.rate_high == 60.0
    assert job.rate_mid == 45.0
    assert job.experience == "Expert"
    assert job.payment_verified is True
    assert job.client_rating == 5.0
    assert job.client_country == "United States"


def test_dedupe():
    doubled = SAMPLE + SAMPLE
    assert len(parse_feed(doubled, dedupe=True)) == 2
    assert len(parse_feed(doubled, dedupe=False)) == 4


def test_posted_minutes_units():
    assert parse_posted_minutes("19 minutes") == 19
    assert parse_posted_minutes("3 hours") == 180
    assert parse_posted_minutes("2 days") == 2880
    assert parse_posted_minutes("1 week") == 10080
