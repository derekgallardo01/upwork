"""Generate tailored proposal openers for top-ranked jobs.

These are DRAFTS meant to be reviewed and edited before sending — never
auto-submitted. The goal is to save the blank-page time, not to replace Derek's
judgement on each client.
"""

from __future__ import annotations

import re

from .models import Job

# Map a matched skill/keyword to a concrete, credible credential line.
_CREDENTIAL_LINES = {
    "power automate": "I build production Power Automate flows (incl. connectors and the underlying APIs when a connector falls short)",
    "asana": "I've wired up Asana → Microsoft 365 syncs before",
    "sharepoint": "I deliver SharePoint solutions end to end (lists, document workflows, intranet sites)",
    "copilot studio": "I package and deploy enterprise agents in Copilot Studio",
    "copilot": "I work hands-on with Microsoft Copilot across M365",
    "power apps": "I build canvas and model-driven Power Apps on Dataverse",
    "power bi": "I build executive Power BI dashboards (MTD/YTD, Budget vs Actual)",
    "microsoft fabric": "I model multi-entity data in Microsoft Fabric",
    "dynamics 365": "I configure and extend Dynamics 365",
    "azure": "I ship Azure AI / Azure OpenAI solutions",
    "claude": "I integrate Claude and other LLMs into business workflows",
    "rag": "I build RAG pipelines over enterprise knowledge",
    "automation": "I design clean, well-documented automations a non-technical owner can maintain",
}

_DEFAULT_CRED = (
    "I'm a Microsoft AI & Power Platform developer (Copilot Studio, Power "
    "Automate, SharePoint, Azure AI) who ships clean, documented solutions"
)


def _first_sentence(text: str, limit: int = 220) -> str:
    text = text.strip()
    if not text:
        return ""
    m = re.split(r"(?<=[.!?])\s", text, maxsplit=1)
    s = m[0].strip()
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0] + "…"
    return s


def _pick_credential(job: Job) -> str:
    """Choose the credential line whose keyword best matches this job."""
    matched_lower = [m.lower() for m in job.matched_keywords]
    # Prefer the most specific (longest) matching credential key.
    candidates = [
        line
        for key, line in _CREDENTIAL_LINES.items()
        if any(key in m or m in key for m in matched_lower)
    ]
    if candidates:
        # Order by how specific the matched key is.
        candidates.sort(key=len, reverse=True)
        return candidates[0]
    return _DEFAULT_CRED


def proposal_opener(job: Job) -> str:
    """Return a 2-3 sentence draft opener tailored to the job."""
    ask = (_first_sentence(job.description) or job.title).rstrip(".!? ")
    credential = _pick_credential(job)

    pay = ""
    if job.pricing_type == "fixed" and job.budget:
        pay = f" I can scope this to your ${int(job.budget)} budget"
    elif job.pricing_type == "hourly" and job.rate_mid:
        pay = " Happy to work hourly within your range"

    note = ""
    if "Spanish" in job.eligibility_note:
        note = " (and I'm fully bilingual EN/ES if that helps)"

    return (
        f"Hi — I read your post: “{ask}”. {credential}, so this is squarely "
        f"in my wheelhouse{note}.{pay}. "
        f"A couple of quick questions so I can give you an accurate plan: "
        f"what's your current setup, and what does “done” look like for the first milestone? "
        f"I can share a similar build I've delivered and a rough timeline."
    )
