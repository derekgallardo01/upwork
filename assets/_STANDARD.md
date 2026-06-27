# Asset package standard

Every asset folder contains a consistent set of files so they read as a portfolio
and double as deliverables.

```
NN-asset-name/
  README.md        # what it is · which feed clusters it covers · how to use/deploy · what's inside
  OFFER.md         # paste-ready Upwork Project Catalog listing: scope, 3 tiers, price, timeline, what client provides
  CASE-STUDY.md    # portfolio proof: problem → approach → architecture → result → "how I'd do this for you"
  DEMO.md          # 90-second Loom script (only ~8% of clients get a video — big differentiator)
  ...              # the asset itself (templates, code, sample data, solution package)
```

## For code-shaped accelerators

- **Runs offline today**: mock Microsoft services + bundled sample data; a
  deterministic local LLM stub by default. `python run.py` produces visible output.
- **Pluggable for real later**: one env switch points the LLM/Graph client at
  Azure OpenAI / Microsoft Graph — no code change. No secrets committed.
- Python 3, **stdlib-only at runtime** (portability is a selling point); web demos
  use `http.server`. Tests under `tests/`.

## For tenant-bound accelerators (Copilot Studio, SharePoint, Power Automate, Power BI)

These live in a Microsoft tenant and can't run headless, so they ship:
- a **solution template** (exported/declarative config: JSON, YAML, or a
  documented schema),
- bundled **sample data**,
- a **deploy guide** (import steps + a screenshot checklist),
- and where useful, a small **offline simulator** so the logic is demonstrable
  without a tenant.

## Voice & quality

Mirror the existing repo: concise, client-facing, no fluff. Each README opens with
one sentence a prospective client would understand. Case studies are seeded from
real feed domains (Asana payroll, KOA/QuickBooks, telecom M365) so they read as
real engagements, not toys.
