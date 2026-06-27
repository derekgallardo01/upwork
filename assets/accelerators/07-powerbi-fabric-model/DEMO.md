# Loom script — Power BI / Fabric consolidation (~90s)

**0:00 (15s)** — "If you run several companies with different charts of accounts,
this consolidates them into one executive view — MTD, YTD, Budget vs Actual, and
prior year."

**0:20 (30s)** — Run `python run.py`. "It ingests three mock QuickBooks
campgrounds, each with *different* account names, maps them to one standardized
chart, and consolidates. Here's the summary: YTD revenue, expenses, net across all
three."

**0:50 (25s)** — Open `out/dashboard.html`. "Here's the dashboard — by category,
with YTD actual versus budget and the variance, plus year-over-year growth. One view,
all entities, same chart of accounts."

**1:15 (15s)** — "This is the offline proof. For a client I build this in Microsoft
Fabric and Power BI with the DAX measures in dax-library.md, refreshing from their
real QuickBooks companies."
