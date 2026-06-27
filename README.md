# upwork-radar

Turn a saved Upwork **"Find work" feed** into a ranked shortlist of the jobs
worth your time — scored against your own profile — plus a draft proposal opener
for the top matches.

Built for a Microsoft AI & Power Platform freelancer: the feed is dominated by
generic Python/LLM "AI engineer" posts, but the jobs *you* win are the ones at
the **Microsoft × AI intersection** (Copilot Studio, Power Automate, SharePoint,
Azure AI). Chasing the most common job type is a race to the bottom; this tool
ranks by **fit × low-competition × budget × freshness** so the right jobs float
to the top.

No scraping, no login, no API keys, **no third-party dependencies** — it works on
data from your own logged-in feed.

## Two ways to feed it

**A. One-click bookmarklet (recommended).** A browser bookmark that reads the
job data Upwork already embeds in the page and downloads a clean `feed.json` —
no select-all, more accurate fields (exact spend, real timestamps, hourly
min/max). It runs in your own browser when you click it; it's not a bot. Setup:
[`BOOKMARKLET.md`](BOOKMARKLET.md). A sample export is at `data/feed_sample.json`.

**B. Paste the page text (fallback).** Open the feed, select-all, save to a
`.txt`. A sample 604-job scrape is at `data/feed_sample.txt`.

The analyzer auto-detects the format from the file extension (`.json` → bookmarklet
export, anything else → page text).

## Quick start

```bash
# Bookmarklet JSON (recommended)
PYTHONPATH=src python3 -m upwork_radar analyze \
    --feed data/feed_sample.json --profile profile.json --top 8 --out out

# …or saved page text
PYTHONPATH=src python3 -m upwork_radar analyze \
    --feed data/feed_sample.txt --profile profile.json --top 8 --out out

# Read the results
#   out/shortlist.md   ranked table + top-N detail (with job links) + draft proposal openers
#   out/shortlist.csv  every job with full score columns (open in Excel and sort)
```

Example console output:

```
Parsed 604 unique jobs (192 in wheelhouse, 601 eligible).

Top 8:
  1. 0.948  CIPP Expert Needed - MSP Policy Standardization (Intune, SharePoint)
  2. 0.897  Set up Asana Automate flow: Asana Timesheets → Excel/SharePoint
  3. 0.837  SharePoint Intranet Design & Document Management Optimization Review
  4. 0.829  Implementation partner
  5. 0.802  Power Automate, SharePoint, Microsoft Lists, MS Teams, Excel expert
  ...
```

## How it works

| Stage | File | What it does |
|-------|------|--------------|
| Capture | `bookmarklet.js` | One click in your browser → clean `feed.json` from Upwork's embedded data. |
| Parse (JSON) | `src/upwork_radar/parse_nuxt.py` | Loads the bookmarklet export into `Job` records (the accurate path). |
| Parse (text) | `src/upwork_radar/parse.py` | Fallback: splits saved page text on each `moreabout "<title>"` anchor and extracts the same fields. |
| Score | `src/upwork_radar/score.py` | Computes five 0–1 components and combines them with weights from `profile.json`. Flags jobs with residency requirements you can't meet. |
| Propose | `src/upwork_radar/proposal.py` | Drafts a tailored 2–3 sentence opener for each top job (review before sending — never auto-submitted). |
| Output | `src/upwork_radar/cli.py` | Writes `shortlist.md` + `shortlist.csv`. |

### Scoring components

- **fit** — weighted keyword match (title/skills count more than description),
  with a bonus when a job names **both** a Microsoft product and AI/agent work.
- **competition** — inverse of the proposal count (`Fewer than 5` is best).
- **budget** — hourly midpoint vs your target rate, or a log scale for fixed jobs.
- **freshness** — decays from "just posted" to ~zero over two weeks.
- **client_quality** — payment verified, spend, rating.
- **eligibility** — residency requirements you can't meet penalize the score and
  the job is marked `⛔` in the shortlist.

## Tuning

Everything lives in `profile.json` — no code changes needed:

- `keywords` — the strong/medium/weak term tiers that drive **fit**. Add your own.
- `weights` — how much each component counts toward the final score.
- `intersection_bonus` — extra fit for Microsoft × AI jobs.
- `exclude_country_requirements` — residencies to flag as ineligible.
- `target_rate` — your hourly rate, used to normalize pay.

## Tests

```bash
python3 -m pytest tests/ -q
```

## Layout

```
profile.json              your skills, weights, target rate (edit this)
bookmarklet.js            one-click feed capture (readable source)
bookmarklet.url.txt       the same, minified into a clickable bookmark
BOOKMARKLET.md            how to install + use the bookmarklet
data/feed_sample.json     sample bookmarklet export (recommended input)
data/feed_sample.txt      sample 604-job page-text scrape (fallback input)
src/upwork_radar/         parse_nuxt · parse · score · proposal · cli
tests/                    parser + scoring tests
out/                      generated shortlist.md / shortlist.csv (gitignored)
```
