# Loom script — No-code AI workflow (~90s)

**0:00 (15s)** — "Most 'AI automation' jobs are really one pattern: a lead comes
in, an AI reads it, and it gets routed and answered — without spam slipping through
or messages landing in the wrong bucket. Here's that pattern, running."

**0:15 (35s)** — Run `python run.py`. "Six leads across a form, an inbox, and a
CRM. Watch each one get summarized and categorized — quote, support, partnership,
billing — each with a drafted reply. The SEO spam lead is recognized and logged,
but it does **not** get a follow-up."

**0:50 (25s)** — Open `out/crm.csv` and `out/follow_ups.json`. "Everything's
written to a CRM with a summary, and five follow-up emails are drafted and queued —
five, not six, because the spam was filtered. That's the safety the real automation
needs."

**1:15 (15s)** — "This is the logic running offline. For a client I build it in
Make, Zapier, n8n, or Power Automate — the node-by-node mapping is in blueprint.md —
wire their LLM key, and test on their real messages first. Same design, their
stack."
