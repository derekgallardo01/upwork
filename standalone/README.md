# Standalone repos — ready to publish

Each folder here is a **self-contained, repo-ready package**: its own clean
client-facing `README.md`, `LICENSE`, `.gitignore`, code, sample data, and tests —
with all references to the private tooling (the job radar, the go-to-market playbook,
internal asset numbers, pricing/offer docs) stripped out.

These are meant to become **separate public GitHub repos** you link from your
portfolio. The repo this folder lives in should stay **private** — it contains the
radar, the playbook, and mock-data proof that you don't want a client to browse.

> Present these as **capability demos built on sample data**, not as past client
> deliverables. The code genuinely runs; the data is illustrative.

## The 10 packages

| Folder / suggested repo name | What it demonstrates | Runs? |
|------------------------------|----------------------|-------|
| `copilot-studio-support-agent` | M365 AI agent: cited answers + human escalation | ✅ `sim/run.py` |
| `power-automate-flow-pack` | Scheduled sync with retry + idempotent dedupe | ✅ `sim/run.py` |
| `powerbi-fabric-consolidation` | Multi-entity P&L consolidation → dashboard | ✅ `run.py` |
| `sharepoint-intranet-generator` | Generate a modern intranet from one definition | ✅ `run.py` |
| `rag-over-docs-kit` | RAG with source citations (stdlib only) | ✅ `run.py` |
| `nocode-ai-lead-workflow` | Lead triage → CRM → follow-up (+ tool blueprint) | ✅ `run.py` |
| `ms-delivery-discovery-kit` | Discovery questionnaire + SOW template | templates |
| `solution-architecture-hld` | HLD + Mermaid architecture templates | templates |
| `project-handover-pack` | Handover guide + runbook + walkthrough script | templates |
| `m365-privacy-config` | Copilot/M365 data-privacy config checklist | template |

## Publishing one as its own repo

For each folder, create an **empty** repo on GitHub (no README/license — these
already have them), then:

```bash
cd standalone/<folder>
git init
git add -A
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<you>/<repo-name>.git
git push -u origin main
```

Or use the helper, which does the `git init` + first commit for every folder and
prints the remaining `remote add` / `push` commands for you to run:

```bash
bash standalone/init-repos.sh
```

The helper never creates GitHub repos or pushes on its own — you stay in control of
what goes public and when.

## Suggested order

You don't need all 10 public at once. Start with the 2–3 that match the specialist
profiles you lead with, get a portfolio item + a star or two on each, then add more.
The six runnable ones make the strongest portfolio links because a reviewer can
actually run them.
