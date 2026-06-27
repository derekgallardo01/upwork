# Go-to-market playbook

The assets are the inventory. This is how you turn them into won jobs. Work top to
bottom — the order is deliberate (profile and proof gate everything downstream).

---

## 0 · The thesis (why this works)

The 604-job feed analysis is clear: the generic "AI engineer / Python / LLM" pile is
saturated and a race to the bottom. The jobs you win sit at the **Microsoft × AI
intersection** — Copilot Studio, Power Automate, SharePoint, Power BI/Fabric, Power
Apps. Clients there overwhelmingly ask you to *prove* capability: ~55% want an
architecture/approach, ~41% want a sample/pilot, ~32% want similar past examples. Every
asset in this repo is built to be that proof. Don't compete on price in the generic
pile; compete on **demonstrated Microsoft delivery** in the intersection.

---

## 1 · Profile (do this first — nothing converts without it)

- [ ] **Title:** lead with the intersection, not "developer." e.g.
      *"Microsoft AI & Power Platform Developer — Copilot Studio · Power Automate · SharePoint."*
- [ ] **Overview:** first two lines must land above the fold — what you build + proof.
      Open with the win ("I build Copilot Studio agents and Power Automate flows that
      ship and get maintained"), then name the assets as evidence.
- [ ] **Specialized Profiles (Upwork allows 2–3):** create separate ones so each reads
      as a specialist, not a generalist:
      1. *Copilot Studio & AI agents on M365* (assets 05, 09)
      2. *Power Automate & M365 automation* (assets 06, 10)
      3. *Power BI / Fabric & SharePoint* (assets 07, 08)
- [ ] **Rate:** `profile.json` is set to $75/hr. Hold it for intersection work; the
      radar already down-weights the low-budget generic jobs.

## 2 · Portfolio (upload the proof)

- [ ] Add one Upwork **portfolio item per accelerator** (6 total to start).
- [ ] Image = the matching file in [`proof/screenshots/`](proof/screenshots/) (Power BI
      dashboard, SharePoint intranet) or a screenshot of the relevant transcript.
- [ ] Description = the asset's `CASE-STUDY.md` (problem → approach → result), trimmed.
- [ ] Skills/tags = the Microsoft products named in that asset.

## 3 · Project Catalog (publish buy-now offers)

Each accelerator's `OFFER.md` is a paste-ready listing. **Launch 2–3 first**, not all
six — pick by demand × your confidence:

- [ ] **06 · Power Automate flow pack** — biggest, most repeatable demand.
- [ ] **05 · Copilot Studio agent** — highest-value intersection cluster.
- [ ] **07 · Power BI / Fabric model** — fewer competitors, clear deliverable.

Add 08/09/10 once the first three have a review each. Reviews compound — a catalog order
is the fastest path to your first ratings.

## 4 · Proposals (the weekly engine)

**Weekly, ~20 min:**
1. [ ] Open your feed, click the bookmarklet → `feed.json` (see [`BOOKMARKLET.md`](BOOKMARKLET.md)).
2. [ ] `PYTHONPATH=src python3 -m upwork_radar analyze --feed feed.json --profile profile.json --top 10 --out out`
3. [ ] Open `out/shortlist.md`. Work top-down; **skip anything marked ⛔** (you can't meet it).
4. [ ] For each target: use the draft opener as a starting point, then attach the
       matching proof from [`proof/`](proof/) and link the asset's case study.

**Connects discipline:** spend on the top ~5–8 ranked jobs only. The score already
encodes fit × low-competition × budget × freshness, so the cheapest connects-per-win are
near the top. Don't spray the generic pile.

**Asset → job-cluster cheat sheet:**

| If the job is about… | Lead with asset | Attach proof |
|----------------------|-----------------|--------------|
| Copilot/AI agent on M365 | 05 Copilot Studio agent | demo-transcripts (citations + escalation) |
| RAG / chatbot over docs | 09 RAG kit | demo-transcripts (sources) |
| Power Automate / scheduled sync / Asana→SharePoint | 06 flow pack | demo-transcripts (retry + dedupe) |
| Make/Zapier/n8n + AI, lead/inbox automation | 10 no-code workflow | demo-transcripts (lead triage) |
| Power BI / Fabric / multi-entity reporting | 07 Power BI model | powerbi-dashboard.png |
| SharePoint intranet / document mgmt | 08 SharePoint intranet | sharepoint-intranet.png |
| Any engagement (scoping, HLD, handover, privacy) | horizontal 01–04 | the template itself |

## 5 · Delivery (where the rate comes from)

When you win, the asset isn't just proof — it's the accelerator. Each `OFFER.md` has
tiers/timeline; each accelerator ships a deploy guide (`deploy-guide.md` / `import-guide.md`)
to wire the real tenant. Reusing the asset is what makes the effective hourly rate work:
you're delivering from a tested base, not from scratch.

---

## First-week checklist (condensed)

1. [ ] Rewrite title + overview; create 2–3 specialized profiles.
2. [ ] Upload 6 portfolio items from `proof/`.
3. [ ] Publish Project Catalog listings 06, 05, 07.
4. [ ] Run the radar; send 5 proposals from the top of `shortlist.md`, each with proof.
5. [ ] Repeat step 4 weekly; add catalog listings 08/09/10 after first reviews land.
