# 09 · RAG-over-your-docs kit

> Ask questions and get answers grounded in *your* documents, with citations — the
> reusable engine behind enterprise AI agents and source-cited chatbots.

**Covers (feed clusters):** the large "AI agent / RAG chatbot / document Q&A"
cluster (e.g. "AI Engineer for RAG & AI Agents… Source-Cited Chatbot"). This is
the core that powers accelerator #05's Copilot Studio agent and most chatbot gigs.

## What's inside

- `ragkit.py` — load → chunk → **stdlib TF-IDF index** → retrieve → cited answer.
- `run.py` — CLI. `data/` — sample policy docs. `tests/` — pytest.
- Pluggable generation: deterministic **local stub** by default (reproducible, no
  keys); Azure OpenAI / Anthropic adapters wired behind `LLM_PROVIDER` (never
  called in the default path — no network, no secrets).

## Run it

```bash
python run.py "what is the refund policy?"   # one question
python run.py                                 # a few sample questions
python -m pytest tests/ -q
```

Example: a refund question retrieves `refunds.md`, a PTO question retrieves
`hr-policy.md`, each answer ending in a numbered **Sources** list.

## Make it real

Point it at a client's documents (drop files in `data/`) and flip to a real model:
```bash
export LLM_PROVIDER=azure   # or anthropic
export AZURE_OPENAI_ENDPOINT=... AZURE_OPENAI_API_KEY=...
```
For production, swap the TF-IDF index for a vector store (Azure AI Search / a
vector DB) and the file loader for SharePoint/Graph — the retrieve→ground→cite
shape stays identical.
