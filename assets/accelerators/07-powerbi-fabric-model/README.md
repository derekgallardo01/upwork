# 07 · Power BI / Fabric multi-entity model

> Consolidate several companies with different charts of accounts into one
> standardized executive view — MTD/YTD, Budget vs Actual, and Prior Year — in
> Power BI / Microsoft Fabric.

**Covers (feed clusters):** the live "Data analysis" job (six QuickBooks Online
companies / KOA campgrounds) and the Azure FinOps / multi-entity reporting cluster.

## What's inside

- `consolidate.py` + `run.py` — an **offline implementation** that ingests 3 mock
  QuickBooks entities, maps each entity's accounts to a standardized chart, builds
  a consolidated fact table, and renders a self-contained `out/dashboard.html`
  (MTD/YTD, Budget vs Actual, Prior Year, YoY) plus `out/consolidated.csv`.
- `generate_data.py` — deterministic sample data (3 entities, 2025 + 2026).
- `dax-library.md` — the reusable **DAX measures** for the real Power BI model.
- `account-mapping.example.csv` — entity account → standardized category map.
- `README` / `OFFER` / `CASE-STUDY` / `DEMO`.

## Run it

```bash
python run.py                 # consolidates and writes the dashboard
python -m pytest tests/ -q
open out/dashboard.html       # the executive view
```

You'll get a consolidated dashboard across the three entities with Budget-vs-Actual
variance and YoY growth — the exact shape the KOA/QuickBooks client asked for.

## Make it real

In Fabric/Power BI: do the entity-account → standardized-category mapping in the
dataflow/pipeline, build a star schema with a marked Date table, and add the
measures from `dax-library.md`. The Python model here proves the logic and the
numbers; the DAX library is what goes into the semantic model.
