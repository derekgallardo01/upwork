# Demo transcripts

Real console output from running the accelerators offline (`python run.py`).
Reproduce any of these yourself with `python run_all.py` from the repo root.

---

## 05 · Copilot Studio agent — cited answers + escalation

```
USER: How do I reset my password?
AGENT: ## Resetting your password — You can reset your password from the self-service
       portal at portal.example.com. [1]
       sources: [1] it-support.md, [2] hr-policy.md

USER: How many PTO days do new employees get?
AGENT: ## Paid time off (PTO) — New employees receive 15 days of paid time off per year,
       accrued monthly. [1]
       sources: [1] hr-policy.md, [2] it-support.md

USER: Who do I contact about a security incident?
AGENT: ## Reporting a security incident — contact the security team immediately at
       security@example.com or call the 24/7 hotline. [1]
       sources: [1] security.md, [2] it-support.md

USER: I want a refund on my subscription
AGENT → 🤝 escalated (sensitive topic): I'm connecting you with a specialist.

USER: What is the airspeed velocity of an unladen swallow?
AGENT → 🤝 escalated (low confidence): I don't have a confident answer — let me hand
       you to a team member.
```

**What it proves:** answers are grounded in the loaded docs *with citations*, sensitive
topics (refunds) escalate to a human, and off-topic questions escalate instead of
hallucinating.

---

## 06 · Power Automate flow pack — retry + idempotent dedupe

```
=== Run 1 (with a simulated transient failure) ===
  • trigger: scheduled run started
  • pull: 5 entries from source
  • map: 4 approved rows after field mapping
  • write to Excel table: attempt 1 failed (transient connector timeout); retrying
  • wrote table: 4 new rows, 4 total (0 duplicates skipped)
  • write to Excel table: succeeded on attempt 2
  • notify: success notification sent
result: {'added': 4, 'total': 4, 'skipped': 0}

=== Run 2 (idempotent — nothing new) ===
  • wrote table: 0 new rows, 4 total (4 duplicates skipped)
result: {'added': 0, 'total': 4, 'skipped': 4}
```

**What it proves:** the flow recovers from a transient failure on retry, and a re-run
adds **zero** duplicate rows — the two things that break naive automations.

---

## 07 · Power BI / Fabric model — multi-entity consolidation

See the rendered dashboard at [`screenshots/powerbi-dashboard.png`](screenshots/powerbi-dashboard.png).
Three mock QuickBooks entities with *different* charts of accounts are mapped to one
standardized chart and consolidated: **YTD Revenue $732,240**, variance **+3.1%** vs
budget, **+8.0%** YoY — with MTD, YTD, Budget-vs-Actual, and prior-year columns.

---

## 08 · SharePoint intranet — generated site preview

See [`screenshots/sharepoint-intranet.png`](screenshots/sharepoint-intranet.png). A full
modern intranet (home, news, HR, IT, Policies, Document Center) is generated as static
HTML from a single `site-definition.json` — the structure you'd provision in a real
tenant.

---

## 09 · RAG kit — retrieval with sources

```
Q: What is the refund policy?
  → Customers may request a refund within 30 days of purchase. Submit a refund request
    through the support portal with your order number. [1]
  Sources: [1] refunds.md (chunk 0), [2] security.md (chunk 1), [3] security.md (chunk 0)

Q: How many days of PTO do new employees get?
  → New employees receive 15 days of paid time off per year, accrued monthly. [1]
  Sources: [1] hr-policy.md (chunk 0), ...
```

**What it proves:** answers cite the exact source document and chunk — the auditability
clients need before they trust an AI over their own docs.

---

## 10 · No-code AI workflow — lead triage

```
Processed 6 leads; drafted 5 follow-ups.

[L1] web_form  quote_request      Dana Lewis    → quote reply drafted
[L2] email     support_request    Marco Diaz    → support reply drafted
[L3] crm       partnership        Priya Nair    → partnership reply drafted
[L4] email     billing            Tom Becker    → billing reply drafted
[L5] web_form  spam_or_irrelevant SEO Outreach  → (none — filtered as spam)
[L6] email     quote_request      Aisha Khan    → quote reply drafted
```

**What it proves:** every lead is categorized and given a drafted reply, the spam lead is
logged to the CRM but **excluded** from follow-ups (5 drafts, not 6), and nothing is
silently dropped.

---

## Job radar — ranked shortlist

See [`radar-shortlist.md`](radar-shortlist.md): 604 real feed jobs ranked by
`fit × low-competition × budget × freshness × client`, with the top match (a CIPP/Intune
MSP job, **fit 1.00, fewer than 5 proposals**) scoring 0.948, and draft proposal openers
for the top 8.
