# Case study — Asana timesheets → SharePoint for payroll

## Problem
A team ran a 15-user pilot where approved time entries lived in Asana but payroll
needed them in an Excel table in SharePoint. Someone was copying rows by hand every
week — slow, error-prone, and impossible to audit. They wanted a clean, maintainable
automation a non-technical owner could monitor.

## Approach
A scheduled Power Automate flow that pulls approved entries, maps them to the payroll
columns, and upserts them into the SharePoint Excel table — idempotently (no
duplicates on re-runs), with retry on transient failures and a run log.

```mermaid
flowchart LR
    T["⏰ Daily schedule"] --> P["Pull approved entries\n(Asana)"]
    P --> M["Map fields\nEmployee · Date · Hours · Cost Center"]
    M --> U["Upsert rows (dedupe on EntryId)\n(Excel table in SharePoint)"]
    U --> R["Retry + run log\n(error log + alert on failure)"]
    R --> N["📧 Success notification"]
```

## Result
Payroll data lands automatically and accurately; re-runs never duplicate rows;
failures are logged and alerted instead of silently lost. The owner monitors it from
run history and edits it with the handover runbook.

## How I'd do this for you
The simulator in `sim/` runs this exact logic offline (with a forced failure to show
the retry). For your project I build the real flow per `import-guide.md`, test on a
sandbox first, and hand it over documented. See `OFFER.md` for packages.
