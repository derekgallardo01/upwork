# 05 · Copilot Studio agent starter

> A Microsoft 365 AI agent that answers staff/customer questions from your
> SharePoint documents, cites its sources, and hands off to a human when it's
> unsure or the topic is sensitive.

**Covers (feed clusters):** the biggest demand cluster — "AI agents on M365"
(Telecom AI-Agent consultancy, "Setup Microsoft Copilot & Claude Agents," Copilot
Studio enterprise-agent jobs).

## What's inside

- `agent-template/` — the declarative agent design (`agent.yaml`, `topics.json`,
  `prompt-library.md`) you recreate in Copilot Studio.
- `deploy-guide.md` — step-by-step tenant build + go-live checklist (references
  asset 04 for privacy/no-training config).
- `sim/` — an **offline simulator** that proves the logic without a tenant:
  grounded answers with citations + escalation on sensitive/low-confidence
  questions. Stdlib-only, deterministic; a real model plugs in via `LLM_PROVIDER`.
- `README` / `OFFER` / `CASE-STUDY` / `DEMO`.

## Run the simulator

```bash
python sim/run.py            # answers + two escalation cases
python -m pytest sim/tests/ -q
```

You'll see it answer "how do I reset my password?" from the IT FAQ with a citation,
route a PTO question to the HR doc, and **escalate** a refund request (sensitive)
and an off-topic question (low confidence) instead of guessing.

## Make it real

Build the agent in Copilot Studio per `deploy-guide.md`, point it at the client's
SharePoint, and publish to Teams/web. The sim's question set doubles as your
acceptance test.
