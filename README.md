# Upwork success kit — Microsoft AI & Power Platform

A complete system for winning Microsoft-niche work on Upwork, in three layers:

1. **Find the right jobs** — a job-feed analyzer (`upwork-radar`) that ranks a saved
   feed by fit to your profile, so you stop chasing the saturated generic-AI pile.
2. **Prove you can deliver** — 10 portfolio assets that each run offline, double as
   reusable delivery accelerators, and ship as paste-ready Project Catalog offers.
3. **Convert** — viewable proof and a go-to-market playbook that turn the above into
   sent proposals and published listings.

Built for a Microsoft AI & Power Platform freelancer. The whole thing is **stdlib-only
Python 3.11**, runs offline with no keys or scraping, and commits no secrets.

```bash
python run_all.py          # run the radar + all 6 runnable accelerators end to end
python -m pytest -q        # 52 tests across the radar + assets
```

## What's here

| Path | What it is |
|------|------------|
| [`RADAR.md`](RADAR.md) | **The job-feed analyzer** — full docs: capture a feed, rank it, draft openers. |
| [`assets/`](assets/README.md) | **The 10 portfolio assets** — 4 horizontal (every engagement) + 6 accelerators (one per niche cluster). Each runs offline with pluggable real adapters. |
| [`proof/`](proof/README.md) | **Viewable evidence** — rendered dashboards, screenshots, transcripts. What you paste into proposals and portfolio items. |
| [`standalone/`](standalone/README.md) | **Publish-ready copies** of all 10 assets — each a clean, self-contained, repo-ready package (no radar/playbook/pricing references) for use as a public portfolio repo. |
| [`PLAYBOOK.md`](PLAYBOOK.md) | **Go-to-market** — profile rewrite, Project Catalog launch order, weekly proposal engine, asset→job cheat sheet. |
| [`BOOKMARKLET.md`](BOOKMARKLET.md) | One-click capture of your Upwork feed into clean JSON (ToS-safe, runs in your browser). |
| `src/upwork_radar/` | The analyzer source (parse · score · proposal · cli). |
| `run_all.py` | Runs every demo in the repo with a pass/fail summary. |

## The strategy in one paragraph

The 604-job feed analysis showed the generic "AI engineer" jobs are a race to the
bottom; the wins are at the **Microsoft × AI intersection** (Copilot Studio, Power
Automate, SharePoint, Power BI/Fabric, Power Apps), where clients ask you to *prove*
capability. So: the **radar** points you at the right jobs, the **assets** are the proof
and the accelerator that lets you deliver them profitably, the **proof** folder makes
that visible to clients who'll never run code, and the **playbook** sequences it into a
repeatable weekly motion. Start with [`PLAYBOOK.md`](PLAYBOOK.md).

## Layout

```
README.md          this file — start here
PLAYBOOK.md        go-to-market checklist
RADAR.md           job-feed analyzer docs
BOOKMARKLET.md     feed capture
run_all.py         run every demo
profile.json       your skills/weights/rate (drives the radar)
src/upwork_radar/   analyzer: parse_nuxt · parse · score · proposal · cli
assets/            10 portfolio assets (horizontal/ + accelerators/)
proof/             screenshots + transcripts for proposals
data/              sample feeds (json + 604-job text)
tests/             analyzer tests (assets carry their own)
```

## License

[MIT](LICENSE).
