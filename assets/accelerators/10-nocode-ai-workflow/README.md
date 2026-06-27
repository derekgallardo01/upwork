# 10 · No-code AI workflow blueprint

> The pattern behind the "AI System Builder" jobs: a lead arrives (web form,
> email, CRM) → an LLM summarizes, categorizes, and drafts a reply → the result
> is written to a CRM/sheet → a follow-up is queued. Buildable in
> Make.com / Zapier / n8n / Power Automate — proven here in runnable code.

**Covers (feed clusters):** the large "AI System Builder / automation expert"
and SMB "automate my inbound" cluster (Make/Zapier/n8n + an LLM step).

## What's inside

- `pipeline.py` — an **offline simulator** of the workflow: classify each lead
  with deterministic keyword rules, summarize it, draft a category-specific
  reply, write a mock CRM (CSV + JSON), and queue follow-ups (spam filtered out).
  Stdlib-only; a `LLM_PROVIDER=azure|anthropic` adapter is wired but never called
  in the default path (no keys, reproducible output).
- `data/leads.json` — six realistic sample leads (quote, support, partnership,
  billing, and one spam) across three channels.
- `blueprint.md` — the **node-by-node mapping** of this logic onto Make.com,
  Zapier, n8n, and Power Automate, so the same design ships in whichever tool the
  client already pays for.
- `README` / `OFFER` / `CASE-STUDY` / `DEMO`.

## Run the simulator

```bash
python run.py                 # processes 6 leads, drafts 5 follow-ups
python -m pytest tests/ -q
```

You'll see each lead classified (quote / support / partnership / billing / spam),
summarized, and given a drafted reply — with the spam lead written to the CRM but
**excluded from follow-ups**. Output (CRM + drafts) lands in `out/`.

## Why this is the proof clients want

No-code AI jobs are really "can you design a reliable lead/intake pipeline and not
have it spam or mis-route people." This shows the *logic* — routing, a safe
default category, spam suppression, an auditable CRM write — independent of the
tool. `blueprint.md` then drops it into their stack.
