# 04 · M365 privacy / no-AI-training config checklist

> A repeatable checklist to configure Microsoft 365 + Copilot + Azure OpenAI so
> client data stays in the tenant and is **never used to train public models** —
> the exact assurance regulated clients demand before they'll let you build.

**Covers (feed clusters):** the Copilot&Claude job *explicitly* required "configure
these tools to ensure data privacy and block public AI model training" under
"strict Australian professional standards." This recurs for any finance/health/legal
client — being able to answer it confidently wins the job.

## What's inside

- [`privacy-config-checklist.md`](privacy-config-checklist.md) — the settings to
  verify across M365, Copilot, Power Platform, and Azure OpenAI, with the
  client-facing assurances each one backs.
- [`OFFER.md`](OFFER.md) — paste-ready Project Catalog listing.

## How to use

1. In a proposal to a regulated client: name the 3–4 specific controls (data
   residency, tenant-bound processing, no-training guarantees, DLP). This instantly
   separates you from applicants who hand-wave "it's secure."
2. In delivery: walk the checklist with the client's admin, record what's set, and
   include the result in the handover pack (asset 03).

## Important

This is an **enablement checklist and talking-points guide**, not legal advice.
Microsoft's product behaviour and admin settings change — always confirm current
settings against Microsoft's official documentation for the client's specific
licenses and region, and let the client's compliance owner sign off.
