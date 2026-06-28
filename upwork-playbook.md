# Upwork operating playbook

Last revised 2026-06-27. Designed for daily-use scanning of new postings.

---

## 1. 30-second filter — should I even bid?

Skip the posting if **any one** of these is true:

- Total budget below USD 500 (or "low budget" + no fixed amount).
- Posting age > 48 hours AND > 30 proposals already.
- Required tools you don't have (e.g. specific SaaS you've never used) AND
  no transferable angle.
- Client has zero reviews AND no verified payment method.
- Asks for free unpaid sample work, NDA before scoping, or "we'll pay after
  it works."
- The work is a one-shot Excel macro or single Power Automate flow under
  4 hours — these go to the $20/hr pool and you can't win on price.

Otherwise: bid. Don't over-think the bid/no-bid decision; spend the saved
time on a better proposal.

---

## 2. Job-category → lead repo + cover letter

Use this lookup the moment you decide to bid. Pick the repo whose demo
most resembles the client's described problem. Cover letter starts from
the matching template, then 5-10 min of tailoring.

| Job mentions… | Lead with | Cover letter | Why |
|---------------|-----------|--------------|-----|
| Copilot Studio, Copilot for M365, chatbot over docs, AI assistant in Teams | [copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent) | M365 / Power Platform | Live demo + sensitive-topic escalation pattern is the differentiator |
| RAG, retrieval, "chatbot over our knowledge base", Azure OpenAI, Anthropic Claude, citations | [rag-over-docs-kit](https://github.com/derekgallardo01/rag-over-docs-kit) | AI / RAG / automation | Eval harness + re-ranker + citations are the differentiators |
| Power Automate, scheduled sync, SharePoint Excel automation, Asana → anything | [power-automate-flow-pack](https://github.com/derekgallardo01/power-automate-flow-pack) | M365 / Power Platform | DLQ + dry-run + idempotent dedupe is what cheap consultants skip |
| Power BI, Microsoft Fabric, multi-entity finance reporting, consolidation, "we have multiple QuickBooks files" | [powerbi-fabric-consolidation](https://github.com/derekgallardo01/powerbi-fabric-consolidation) | M365 / Power Platform | Unmapped-account report alone wins this — talk to it specifically |
| SharePoint intranet, modern intranet, communication site, intranet redesign | [sharepoint-intranet-generator](https://github.com/derekgallardo01/sharepoint-intranet-generator) | M365 / Power Platform | Schema validation + definition-as-source-of-truth is the differentiator |
| Make.com, Zapier, n8n, AI lead workflow, inbound triage, AI agent for sales | [nocode-ai-lead-workflow](https://github.com/derekgallardo01/nocode-ai-lead-workflow) | AI / RAG / automation | Dedupe + human-review queue + cross-tool blueprint is the differentiator |
| HIPAA / GDPR / regulated industry adopting Copilot or AI | [m365-privacy-config](https://github.com/derekgallardo01/m365-privacy-config) | (compose: M365 angle + the privacy assurance) | Worked HIPAA + regulated-advisory checklists are unusual on Upwork |
| Microsoft consulting, "we need someone to scope a project", discovery, SOW | [ms-delivery-discovery-kit](https://github.com/derekgallardo01/ms-delivery-discovery-kit) + relevant runnable | M365 / Power Platform | Lead with discovery rigour, back it up with a runnable |

**If the job mentions multiple categories**, link the strongest match in the
opening line and mention 1-2 others in passing ("…and if a Power BI roll-up
on the data lands later, that one's here: …").

---

## 3. Worked example pairs

These three pairs show what a proposal looks like at the bar that converts
on Upwork. Use the format as a template, not the exact words — paraphrase
or you'll all start sounding the same.

### Example A — Power Automate flow job

**Posting (paraphrased to a typical real one):**

> Looking for a Power Automate expert to build a flow that syncs approved
> expense reports from our internal portal API into a SharePoint Online
> list, with retry on transient errors and email alerts on failure. 50-150
> rows per day. Test environment available. Need by end of next month.
> Budget: USD 2,000-3,500 fixed price.

**My proposal:**

```
Hi Sarah,

I've built this exact pattern - scheduled M365 sync with retry, idempotent
dedupe, dead-letter queue for the rows that can't be saved, and a dry-run
mode for safe testing. It's clone-and-run here:

  github.com/derekgallardo01/power-automate-flow-pack

Two scenarios are tested end-to-end in the eval set (Asana time entries
and Microsoft Forms responses); your portal API is a third source that
slots into the same `mapping-config.json` shape.

Concretely how I'd run yours:

  Week 1 - 1-hour paid scoping call ($150, credited against the fixed
  price). I'd want to confirm: the portal API auth (OAuth? API key?),
  the stable per-row id we'll dedupe on, and whether 50-150 rows might
  spike on month-end.

  Weeks 1-3 - Build against a copy of your portal data with the eval
  harness gating each merge. Promotion to production at the end of
  week 3.

  Week 4 - Handover (runbook + 5-min Loom video) and 14 days of
  defect-fix support included.

Fixed price USD 2,800 (50% on signature, 50% at production acceptance).
Priced just above the bottom of your range because I'd rather have
slightly more time on the eval cases for the spike scenario.

Two questions to keep this short:
  1. Is the portal API's per-row id stable across rebuilds, or generated
     fresh each time? (This is THE dedupe decision.)
  2. Who at your end signs off "this is now in production" - the IT
     manager, or finance?

Talk soon,
Derek
```

**Why this lands:**

- The specific differentiator (DLQ + dry-run + dedupe) appears in the
  first sentence, with a link.
- The "two questions" at the end demonstrate I read the job.
- The price is *just above* the bottom of their range with a reason -
  signals competence, not desperation.

---

### Example B — RAG over docs job

**Posting (paraphrased):**

> Need a Python developer to build a chatbot that answers questions from
> our company's policy documents (~200 PDFs). Must show which document
> each answer came from. We're open to OpenAI or Azure OpenAI. Internal
> tool for staff, ~50 users. Budget: USD 4,000-6,000.

**My proposal:**

```
Hi Marcus,

Citation-first RAG (every answer returns the source document + chunk) is
exactly the pattern of my open kit:

  github.com/derekgallardo01/rag-over-docs-kit

It ships with a golden eval set + CI - so when we change the prompt or
the chunk size or the model, we get a measurable pass/fail rather than
"feels better". For an internal tool with 50 users that's the difference
between a launch and a slow death of trust.

How I'd run yours:

  Week 1 - 1-hour paid scoping call ($175, credited against fixed price).
  I'd want to see 10-20 typical questions your staff actually ask, plus
  3-5 they should NOT be answered by a bot (commission disputes, etc).
  Those become the seed eval set.

  Weeks 1-2 - Document ingestion + chunking + retrieval against a copy
  of your PDFs. I'd add an Azure OpenAI adapter (it's already wired in
  the kit) - you'd see Azure costs from week 2.

  Week 3 - Evaluation tuning, escalation rules (the "should NOT answer"
  cases route to a human), Slack or Teams delivery surface.

  Week 4 - Handover (runbook + Loom video) and 30 days of post-go-live
  support included.

Fixed price USD 5,200. Includes Azure OpenAI setup notes but not the
Azure consumption itself (estimate ~$15-30/month for 50 users at typical
volume).

Two questions:
  1. PDFs - are they text-based or scanned? If scanned, we need an OCR
     step which I'd quote separately.
  2. Do you have a list of "must not answer" topics already, or do we
     build it from scratch?

Talk soon,
Derek
```

**Why this lands:**

- Eval harness as the headline (it's the differentiator)
- Honest scoping question about PDF vs. scanned that proves I've done
  this before
- "Must not answer" framing positions the escalation pattern naturally

---

### Example C — Multi-entity Power BI consolidation

**Posting (paraphrased):**

> We own three property management companies, each in QuickBooks Online.
> Need someone to build a Power BI dashboard that consolidates them with
> budget vs actual and prior-year comparison. Different account names in
> each company. We can't get our existing bookkeeper to do it. Budget
> USD 3,500-5,000.

**My proposal:**

```
Hi Aisha,

The "different account names in each QuickBooks file" is the part that
breaks 90% of consolidation builds, and it's exactly the pattern of my
open kit - 3 mock entities mapped to one standardized chart of accounts,
with an unmapped-accounts report so the bookkeeper sees exactly what's
missing the first time:

  github.com/derekgallardo01/powerbi-fabric-consolidation
  Live demo: derekgallardo01.github.io/powerbi-fabric-consolidation

Two datasets ship in the kit (campgrounds and hospitality) so you can see
the same engine working on different account names.

How I'd run yours:

  Week 1 - 1-hour paid scoping call ($150, credited). I'd want a sample
  GL extract from one entity and your draft "standardized chart of
  accounts" - even a one-page sketch. The mapping CSV is the actual
  deliverable; the dashboard is downstream of getting that right.

  Week 2 - Mapping + consolidation engine running offline against the
  sample data, with the unmapped-accounts CSV for the bookkeeper to
  triage.

  Week 3 - Fabric / Power BI model + dashboard built from the same
  measures (my kit includes the DAX library matching the offline
  engine).

  Week 4 - Handover + 30 days support. Your bookkeeper can run the
  unmapped-accounts report monthly so reporting stays clean.

Fixed price USD 4,200. Includes both the mapping engine AND the Power BI
model.

Two questions:
  1. Is the mapping from each QB file to the standardized chart locked,
     or do you expect it to drift (new accounts added)?
  2. Who's signing off the monthly close - is the dashboard for them, or
     for an above-them exec?

Talk soon,
Derek
```

**Why this lands:**

- Unmapped-accounts report is the *specific* differentiator named in the
  first paragraph; that's the thing every consolidation client has
  burned hours on
- Live demo URL is in the proposal - they can click it before deciding
  to reply
- The "scoping call deliverable is the mapping CSV" framing reframes the
  conversation away from "just build the dashboard"

---

## 4. 30-60-90 day plan

### Days 0-30 — Find the floor

**Goal:** 1 paid scoping call booked. 2-3 short engagements completed
(even small) to get reviews on the platform.

- Send **5 proposals/day** for 20 working days = 100 sends total.
- Bid on jobs at the upper half of your target rate, not below. Don't
  win on price.
- Track in a sheet: posting URL, date sent, reply (yes/no), reason
  (interview / declined / no response). Look for patterns weekly.
- Expect a **3-8% reply rate** to start. That's ~3-8 replies, of which
  1-2 convert to a paid call.
- Cash flow target: USD 2,000-5,000.

### Days 30-60 — Tighten and raise

**Goal:** First 3 reviews on the profile. Reply rate above 10%.

- Drop the bottom 30% of categories (the ones that get the worst reply
  rate from your tracker).
- Raise hourly rate by 20%. Reduce proposal volume to 3/day with more
  tailoring each.
- Update the profile overview with one specific result from a completed
  engagement.
- Cash flow target: USD 5,000-10,000.

### Days 60-90 — Specialize

**Goal:** Most leads come INBOUND (Upwork searches and invites). One
"specialized" profile (M365 or RAG) is generating most of the work.

- Move to "Top Rated" track if eligible (need consistent earnings +
  JSS score).
- Raise rate another 25%. At this point you're at USD 100+/hr for
  AI work.
- Start declining (politely) jobs that don't match your specialty -
  protects future search ranking.
- Cash flow target: USD 10,000-15,000.

### What kills momentum

- **Bidding on jobs you don't actually want.** Each win locks you out
  of new work for the duration. Win the wrong job and lose 2-4 weeks.
- **Underbidding.** Easier to start at $80/hr and discount than to
  start at $30 and try to raise it later. Reviews anchor to rate.
- **Going dark for >5 days.** Search ranking decays fast on Upwork.
  If you're going on holiday, set the profile to "Unavailable" so it
  doesn't show in search at all.

---

## 5. Pricing benchmarks (USD, mid-2026, for the target categories)

| Engagement type | Floor | Mid | Top |
|------------------|-------|-----|-----|
| Power Automate flow build (one flow, scoped) | $1,200 | $2,500 | $5,000 |
| Copilot Studio agent (pilot scope, 3 SharePoint sites) | $4,000 | $8,000 | $15,000 |
| RAG pilot (defined doc set, with evals) | $3,500 | $6,500 | $12,000 |
| Power BI / Fabric consolidation (3-5 entities) | $3,000 | $5,500 | $10,000 |
| SharePoint intranet (1 hub + 4-6 sections) | $5,000 | $9,000 | $18,000 |
| Discovery + scoping (just the discovery + SOW, no build) | $500 | $1,200 | $2,500 |
| Hourly rate (any of the above as ongoing) | $75 | $110 | $175 |

These are guides — adjust for client size, urgency, and how much you
actually want the work. Always quote the **mid** for clients with verified
payment + 5+ reviews; quote the **top** for enterprise contacts.

---

## 6. Anti-patterns to skip

- **"I'll do a sample for free"** — never. Counter with: "I'll do a
  paid 1-hour scoping call which credits against the fixed price if we
  proceed."
- **"We need this yesterday"** — usually means scope creep + non-payment
  later. Counter with: "Happy to move fast; a written change-process is
  in my SOW."
- **"Hourly only, no fixed price"** — sometimes legit; often a sign the
  scope is unbounded. Push for fixed price on milestone 1 (a defined
  deliverable) before agreeing to hourly on the rest.
- **"Can you just join our team's call?"** — only after the paid
  scoping call is booked.

---

## 7. What's in this repo that supports the above

- Profile copy: `profile-and-proposals.md` (TODO: create if not yet saved)
  with the 3 profile drafts and 2 cover-letter templates produced earlier.
- Public capability demos: 10 repos under `standalone/`, all live at
  `github.com/derekgallardo01/<name>` with green CI badges and live demos
  for the visual ones.

If the playbook here ever feels stale, rebuild §3 with a fresh handful of
real postings you actually sent on — that's the easiest way to keep the
worked examples honest.
