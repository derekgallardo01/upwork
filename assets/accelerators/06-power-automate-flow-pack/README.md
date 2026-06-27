# 06 · Power Automate flow pack

> Reusable Power Automate patterns for Microsoft 365 automation — pull data on a
> schedule, map fields, write to an Excel table in SharePoint, with retry,
> de-duplication, and a run log baked in.

**Covers (feed clusters):** the live Asana→Excel/SharePoint payroll job, plus the
broad "scheduled sync / email automation / approvals" cluster.

## What's inside

- `flows/` — documented flow definitions: `scheduled-sync`, `approval`, the
  reusable `error-handling` sub-pattern, and an example field-mapping config.
- `import-guide.md` — build/import steps + a **test-with-sample-data-first**
  checklist (the Asana client explicitly required this).
- `sim/` — an **offline simulator** of the scheduled-sync flow: pull mock Asana
  entries → map fields → idempotently upsert to a mock Excel table, with a
  simulated transient failure to show the retry + run log. Stdlib-only.
- `README` / `OFFER` / `CASE-STUDY` / `DEMO`.

## Run the simulator

```bash
python sim/run.py            # two runs: one with a retry, one idempotent
python -m pytest sim/tests/ -q
```

You'll see it filter to approved rows, recover from a transient failure on retry,
write the table, then add **0 rows on the second run** (deduped) — the exact
behaviour the real flow needs.
