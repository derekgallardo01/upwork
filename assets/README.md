# Reusable assets

Ten assets that apply across the jobs in the Upwork feed — each one is **proof**
(portfolio), a **delivery accelerator** (reuse → faster → higher effective rate),
and a **Project Catalog offer** (buy-now → reviews compound).

Two layers:

- **Horizontal** (`horizontal/`) — apply to *every* engagement regardless of tech.
  Mostly templates/checklists; clients in the feed explicitly ask for these
  (handover guides, HLD docs, knowledge transfer, privacy config).
- **Accelerators** (`accelerators/`) — apply across all jobs in one niche cluster.
  Code-shaped ones run offline (mock services + pluggable real adapters);
  tenant-bound ones ship a solution template + deploy guide.

| # | Asset | Layer | Covers (feed clusters) |
|--|-------|-------|------------------------|
| 01 | Discovery & scoping kit | horizontal | every engagement (Telecom "Phase 1") |
| 02 | Architecture / HLD + diagram | horizontal | 55% of jobs want "architecture/approach" |
| 03 | Handover & enablement pack | horizontal | Asana, Amazon Connect, Copilot&Claude, Telecom |
| 04 | M365 privacy / no-AI-training config | horizontal | Copilot&Claude (regulated clients) |
| 05 | Copilot Studio agent starter | accelerator | AI agents on M365 (biggest cluster) |
| 06 | Power Automate flow pack | accelerator | Asana→SharePoint, M365 email automation |
| 07 | Power BI / Fabric multi-entity model | accelerator | KOA "Data analysis", Azure FinOps |
| 08 | SharePoint intranet / docs template | accelerator | SharePoint cluster |
| 09 | RAG-over-your-docs kit | accelerator | agents/chatbots/RAG cluster |
| 10 | No-code AI workflow blueprint | accelerator | "AI System Builders", SMB automations |

Every asset folder follows the same package standard — see [`_STANDARD.md`](_STANDARD.md).

## How these connect to the rest of the repo

`upwork-radar` (in `src/`) finds the jobs; these assets are what you *deliver*
once you win them. Each asset's `OFFER.md` is a paste-ready Project Catalog
listing, and each `CASE-STUDY.md` is portfolio proof.
