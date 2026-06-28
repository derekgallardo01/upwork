# Upwork profile copy + cover-letter templates

Source-of-truth for the text you paste into Upwork. Last revised 2026-06-27.

---

## Main profile

### Title (recommended)

`Microsoft 365 Copilot & AI Agent Developer — Power Platform, RAG, Automation`

### Overview

> I build AI agents and automation that live *inside* your Microsoft 365
> estate — Copilot Studio agents that cite your SharePoint and escalate to a
> human when they're not sure, Power Automate flows with the retry-and-
> dedupe logic missing from most demos, RAG over your own docs with source
> links a reviewer can click, and Power BI consolidation that turns multi-
> entity spreadsheets into one dashboard.
>
> Most "AI on M365" work I see is either a tenant-admin checking a Copilot
> license box, or a generic AI consultant who's never touched a Power
> Platform connector. I do both halves: the AI behaviour design (grounding,
> citations, escalation, evals) **and** the M365 plumbing (SharePoint
> sites, Power Automate triggers, Fabric/Power BI models, privacy/DLP
> config).
>
> **You can actually run my proof.** Six of the capability demos below ship
> with sample data and a one-command setup. Clone, run, see it work — no
> slide deck required:
>
> - **Copilot Studio support agent** — answers from M365 sources with
>   inline citations, hands off to a human when confidence drops →
>   github.com/derekgallardo01/copilot-studio-support-agent
> - **Power Automate flow pack** — scheduled sync with retries and
>   idempotent dedupe (the part teams skip and regret) →
>   github.com/derekgallardo01/power-automate-flow-pack
> - **Power BI / Fabric consolidation** — multi-entity P&L into one
>   dashboard → github.com/derekgallardo01/powerbi-fabric-consolidation
> - **SharePoint intranet generator** — full intranet provisioned from a
>   single definition file →
>   github.com/derekgallardo01/sharepoint-intranet-generator
> - **RAG-over-docs kit** — retrieval pipeline with cited sources, ready
>   to point at your corpus →
>   github.com/derekgallardo01/rag-over-docs-kit
> - **No-code AI lead workflow** — lead triage with a portable blueprint
>   (Make / Zapier / n8n / Power Automate) →
>   github.com/derekgallardo01/nocode-ai-lead-workflow
>
> **Typical engagements:** stand up a cited Copilot agent on your
> SharePoint content; replace a brittle flow that's quietly failing or
> duplicating records; consolidate scattered finance/ops reporting into a
> single Fabric model; pilot a RAG assistant on a defined doc set with
> evals before scaling.
>
> Happy to start with a paid 1–2 hour scoping call: I'll review what you
> have, identify the highest-leverage first build, and price the next step
> honestly — including telling you when a no-code tool already does the job.

### Skills tags (suggested)

Copilot Studio · Microsoft Power Platform · Power Automate · Power BI ·
Microsoft Fabric · SharePoint Online · Azure OpenAI · Retrieval-Augmented
Generation · Python · Microsoft 365 · AI Agents · Make.com · Zapier · n8n

---

## Specialized profile A — Microsoft / Power Platform

### Title (recommended)

`Copilot Studio + Power Platform Developer — M365 Automation & BI`

### Overview

> If you're already on Microsoft 365 and want more out of the tools you're
> paying for — Copilot Studio agents that actually cite their sources,
> Power Automate flows that don't quietly fail or duplicate rows, multi-
> entity Fabric/Power BI consolidation that ties out the first time — I'm
> the person to bring in.
>
> I build inside your tenant, not around it. The same engagement gives you
> the AI behaviour design *and* the M365 plumbing — connectors, permissions,
> DLP, retention — because the projects that fail are the ones where those
> two halves had different owners.
>
> **Capability demos you can actually run** (one-command setup, sample
> data, no keys required):
>
> - **Copilot Studio support agent** — answers from SharePoint with
>   citations, escalates sensitive topics, ships with an eval harness so
>   behaviour doesn't regress →
>   github.com/derekgallardo01/copilot-studio-support-agent
> - **Power Automate flow pack** — scheduled sync with retry, idempotent
>   dedupe, a dead-letter queue, and a dry-run mode →
>   github.com/derekgallardo01/power-automate-flow-pack
> - **Power BI / Fabric consolidation** — multi-entity P&L into one
>   dashboard, with an unmapped-account report so totals tie out →
>   github.com/derekgallardo01/powerbi-fabric-consolidation
> - **SharePoint intranet generator** — full intranet provisioned from one
>   JSON definition, with schema validation →
>   github.com/derekgallardo01/sharepoint-intranet-generator
>
> **Typical engagements:** stand up a cited Copilot Studio agent on your
> SharePoint; replace a Power Automate flow that's quietly failing or
> duplicating; consolidate scattered finance reporting into a single
> Fabric model; design a SharePoint intranet from one source-controlled
> definition.
>
> Happy to start with a paid 1-hour scoping call: I'll review what you
> have and price the next step honestly — including telling you when a
> no-code tool already does the job.

---

## Specialized profile B — AI agents / RAG / enterprise knowledge

### Title (recommended)

`RAG & AI Agent Developer — Source-Cited Answers, Evaluations, Production Patterns`

### Overview

> Most "AI agent" projects fail the first time leadership reads a wrong
> answer with no source. I build retrieval-grounded agents that **cite the
> exact document and chunk** for every claim, **escalate when they're
> unsure**, and ship with an **evaluation harness** so the next prompt
> tweak doesn't quietly regress.
>
> I'm provider-agnostic (Azure OpenAI, Anthropic, OpenAI) and runtime-
> agnostic (Copilot Studio, custom Python, Make.com / Zapier / n8n / Power
> Automate for no-code patterns). What I bring is the production
> behaviours teams skip on the first build: grounding, citations, evals,
> audit trails, confidence-based human handoff, and dedupe.
>
> **Capability demos you can actually run** (stdlib Python, no API keys
> needed):
>
> - **RAG-over-your-docs kit** — TF-IDF retrieval + sentence-overlap
>   re-ranker, every answer carries `[doc, chunk]` citations, golden eval
>   set gates regressions →
>   github.com/derekgallardo01/rag-over-docs-kit
> - **Copilot Studio support agent** — multi-turn conversation, sensitive-
>   topic detection, human escalation, 16-case eval harness →
>   github.com/derekgallardo01/copilot-studio-support-agent
> - **No-code AI lead workflow** — cross-channel dedupe, classify-then-
>   draft, low-confidence leads routed to a human-review queue instead of
>   being mis-replied to →
>   github.com/derekgallardo01/nocode-ai-lead-workflow
>
> **Typical engagements:** stand up a RAG pilot on a defined doc set with
> evals before scaling; replace a brittle classification rule with an LLM
> + confidence-based escalation; design an AI lead-triage workflow that
> doesn't auto-reply to ambiguous messages.
>
> If you've never run an eval harness on an LLM build, that conversation
> is the one most likely to save you money — happy to scope a paid 1-hour
> review of what you have today.

---

## Cover letter template A — M365 / Power Platform jobs

Replace the bracketed bits per proposal. 3-5 minutes per send.

```
Hi <first name>,

I read your post on <one-line restatement of the problem in your words>.
The pattern of "we have data here, we want it there, automation breaks
silently or duplicates rows" is exactly what my Power Automate flow pack
demonstrates — scheduled sync with retry, idempotent dedupe, a
dead-letter queue, and a dry-run mode. The simulator and 9-case eval
runner are all clone-and-run:

  github.com/derekgallardo01/power-automate-flow-pack

How I'd approach yours specifically: a 1-hour paid scoping call to map
your source / destination / dedup-key and any throttling or compliance
constraints, then a fixed-price build against agreed acceptance criteria
(I use the structured SOW template at
github.com/derekgallardo01/ms-delivery-discovery-kit so the out-of-scope
and acceptance are explicit, not assumed).

Two questions to keep this short:
  1. <one specific question that proves you read the job — e.g. "Is the
     dedupe key stable across re-runs?" or "Does the source connector
     have a webhook we can use instead of polling?">
  2. What does success look like 30 days after go-live — saved time,
     zero missed records, both?

Talk soon,
Derek
```

---

## Cover letter template B — AI / RAG / automation jobs

```
Hi <first name>,

I read your post on <one-line restatement>. The thing that usually sinks
"AI over our docs" projects is grounding — when the bot makes something
up or can't show where an answer came from, leadership pulls the plug. My
RAG kit is built citation-first (every answer returns the exact source
document + chunk) and ships with a golden eval set so prompt or model
changes have a measurable pass/fail outcome:

  github.com/derekgallardo01/rag-over-docs-kit

For a more agent-flavoured build (sensitive-topic escalation, multi-turn,
confidence-based human handoff), this is the matching pattern in
Copilot Studio:

  github.com/derekgallardo01/copilot-studio-support-agent

How I'd run yours: a 1-hour paid scoping call to look at the doc set
size, sensitivity, and the questions users actually ask, then a small
pilot scoped to one doc collection with an eval set agreed up front.
The pilot becomes the regression net for the production rollout.

Two questions:
  1. <one specific question — e.g. "What's the worst-case answer the bot
     could give that would force a takedown?" or "Is there a labelled
     set of historical Q&A we can seed evals from?">
  2. What's the bar for "good enough to ship" — pass rate on an eval
     set, reviewer sign-off, or both?

Talk soon,
Derek
```

---

## Operating notes

- **Don't send a cover letter unmodified.** The bracketed-and-replaced
  parts are the entire signal that you read the job. If you can't write
  the question, don't bid.
- **Worked example proposals** for three specific job types live in
  [upwork-playbook.md §3](upwork-playbook.md).
- **Pricing benchmarks** for each engagement type live in
  [upwork-playbook.md §5](upwork-playbook.md).
- **A/B the cover letters** — after ~10 sends of each, look at which got
  more replies. Iterate the opening hook on the underperformer.
