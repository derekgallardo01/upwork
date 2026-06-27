# Loom script — RAG kit (~90s)

**0:00 (15s)** — "This is a document Q&A bot. It answers questions using *your*
documents and cites the source — so people can trust the answer."

**0:15 (30s)** — Run `python run.py "what is the refund policy?"`. "It found the
refund policy, answered in plain language, and listed the source document and the
exact chunk it used — that [1] is a real citation."

**0:45 (25s)** — Run `python run.py "how many PTO days do new employees get?"`.
"Different question, different source — it pulled from the HR handbook this time.
Retrieval picks the right document automatically."

**1:10 (20s)** — "Today it runs offline with a local model for the demo. For a
client I point it at their SharePoint, plug in Azure OpenAI or Claude, and put it in
Teams or a web widget — their data stays in their tenant. That's the whole pattern."
