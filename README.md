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
text you paste from your own logged-in feed.

## Quick start

```bash
# 1. Open your Upwork "Find work" feed, select-all, and save the page text to a file.
#    (a sample 604-job scrape is included at data/feed_sample.txt)

# 2. Run the analyzer
PYTHONPATH=src python3 -m upwork_radar analyze \
    --feed data/feed_sample.txt \
    --profile profile.json \
    --top 8 \
    --out out

# 3. Read the results
#    out/shortlist.md   ranked table + top-N detail + draft proposal openers
#    out/shortlist.csv  every job with full score columns (open in Excel and sort)
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
| Parse | `src/upwork_radar/parse.py` | Splits the feed on each `moreabout "<title>"` anchor and extracts title, posted age, proposal count, pricing, skills, and client signals. |
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
data/feed_sample.txt      sample 604-job feed, runs out of the box
src/upwork_radar/         parse · score · proposal · cli
tests/                    parser + scoring tests
out/                      generated shortlist.md / shortlist.csv (gitignored)
```
