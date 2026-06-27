# 02 · Architecture / HLD + diagram template

> Lead every proposal and project with a clear high-level design — a one-page
> architecture and a topology diagram — so clients see you think in systems, not
> just tasks.

**Covers (feed clusters):** ~55% of feed jobs ask for an "architecture / approach /
how you would do it." The Telecom job *required* an HLD deliverable; the AI Platform
Architect and consult jobs are bought on design quality.

## What's inside

- [`hld-template.md`](hld-template.md) — fill-in High-Level Design: context,
  components, data flow, integrations, security, risks.
- [`diagram-template.md`](diagram-template.md) — reusable **Mermaid** topology
  diagrams (M365 automation + Copilot agent patterns) you edit per client.
- [`OFFER.md`](OFFER.md) — paste-ready Project Catalog listing.

## How to use

1. In a proposal: paste a trimmed HLD (context + 1 diagram + risks). This alone
   beats 90% of applicants who reply with "I can do this."
2. In delivery: the HLD is the agreed blueprint before you build, and it becomes
   part of the handover pack (asset 03).
3. Render the Mermaid diagrams anywhere (GitHub, VS Code, mermaid.live) or export
   to PNG for a client deck.

Diagrams are plain text (Mermaid), so they version with the repo and edit in
seconds — no Visio license, no drift between "the doc" and "the design."
