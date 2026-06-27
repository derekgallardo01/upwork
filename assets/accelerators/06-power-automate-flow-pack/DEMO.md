# Loom script — Power Automate flow pack (~90s)

**0:00 (15s)** — "This is the pattern behind reliable Power Automate automations:
pull data on a schedule, map it, write it to SharePoint — without duplicates, and
without silently failing."

**0:15 (35s)** — Run `python sim/run.py`. "Watch run 1: it pulls five entries,
keeps the four approved ones, then the write *fails once* — a transient timeout — and
it automatically retries and succeeds. Every step is in the run log."

**0:50 (25s)** — "Now run 2, same data: it adds **zero** rows because they're already
there. That idempotency is what stops the duplicate-rows problem that breaks naive
automations."

**1:15 (15s)** — "That's a simulator of the real flow. In a tenant I build this in
Power Automate from the templates here, test on sample data first, and hand it over
documented. Same logic, same guarantees."
