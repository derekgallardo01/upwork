#!/usr/bin/env python3
"""Run every runnable demo in this repo end to end.

Covers the job radar plus the six code-shaped accelerators (the four horizontal
assets are templates/checklists, nothing to run). Each demo is stdlib-only and
prints visible output; this just sequences them with a header and a pass/fail
line so you can sanity-check the whole portfolio in one command:

    python run_all.py

Exit code is non-zero if any demo fails.
"""

from __future__ import annotations

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# (label, argv, extra-env) — argv is run from ROOT.
DEMOS = [
    ("Job radar (604-job sample feed)",
     [sys.executable, "-m", "upwork_radar", "analyze",
      "--feed", "data/feed_sample.txt", "--profile", "profile.json",
      "--top", "8", "--out", "out"],
     {"PYTHONPATH": os.path.join(ROOT, "src")}),
    ("05 · Copilot Studio agent",
     [sys.executable, "assets/accelerators/05-copilot-studio-agent/sim/run.py"], {}),
    ("06 · Power Automate flow pack",
     [sys.executable, "assets/accelerators/06-power-automate-flow-pack/sim/run.py"], {}),
    ("07 · Power BI / Fabric model",
     [sys.executable, "assets/accelerators/07-powerbi-fabric-model/run.py"], {}),
    ("08 · SharePoint intranet",
     [sys.executable, "assets/accelerators/08-sharepoint-intranet/run.py"], {}),
    ("09 · RAG kit",
     [sys.executable, "assets/accelerators/09-rag-kit/run.py"], {}),
    ("10 · No-code AI workflow",
     [sys.executable, "assets/accelerators/10-nocode-ai-workflow/run.py"], {}),
]


def main() -> int:
    failures = []
    for label, argv, extra_env in DEMOS:
        print("\n" + "=" * 70)
        print(f"▶ {label}")
        print("=" * 70)
        env = dict(os.environ, **extra_env)
        result = subprocess.run(argv, cwd=ROOT, env=env)
        if result.returncode != 0:
            failures.append(label)
            print(f"  ✗ FAILED (exit {result.returncode})")

    print("\n" + "=" * 70)
    if failures:
        print(f"✗ {len(failures)} demo(s) failed: {', '.join(failures)}")
        return 1
    print(f"✓ All {len(DEMOS)} demos ran clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
