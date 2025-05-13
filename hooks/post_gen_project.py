#!/usr/bin/env python3
# {% raw %}
"""Cookiecutter post-generation hook.

• Reads the user’s answers.
• Deletes code paths for any feature that was turned **off**.
• Prunes now-empty parent directories.
• Prints a friendly “what next?” banner.
"""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List

ROOT = Path(".").resolve()                 # project root

# --------------------------------------------------------------------------- #
# 1. Load the cookiecutter context (supports all CC versions)                 #
# --------------------------------------------------------------------------- #
try:                                       # Cookiecutter ≤ 2.1
    from cookiecutter.utils import load_context  # type: ignore
    CTX = load_context(ROOT)["cookiecutter"]      # type: ignore[index]
except ImportError:
    # Cookiecutter ≥ 2.2
    if "COOKIECUTTER_CONTEXT" in os.environ:      # JSON embedded in env-var
        CTX = json.loads(os.environ["COOKIECUTTER_CONTEXT"])["cookiecutter"]
    elif (fp := os.environ.get("COOKIECUTTER_CONTEXT_FILE")) and Path(fp).exists():
        CTX = json.loads(Path(fp).read_text())["cookiecutter"]
    else:                                         # should never happen
        raise SystemExit("❌  Cannot load Cookiecutter context.")

PKG = CTX["package_name"]                         # convenience alias

# --------------------------------------------------------------------------- #
# 2. Flag  →  paths to delete when flag == "no"                               #
# --------------------------------------------------------------------------- #
PRUNE_MAP: Dict[str, List[str]] = {
    # ── Core feature cross-cuts ────────────────────────────────────────────
    "use_prompts":       [f"src/{PKG}/prompts"],
    "include_rag":       [f"src/{PKG}/services/rag_service.py"],
    "use_summarization": [f"src/{PKG}/services/summarization_service.py"],

    # ── GenAI & agents ─────────────────────────────────────────────────────
    "use_genai": [
        f"src/{PKG}/models/genai",
        f"src/{PKG}/api/routers/genai_router.py",
    ],
    "use_agents": [
        f"src/{PKG}/models/agents",
        f"src/{PKG}/api/routers/agent_router.py",
    ],

    # ── ML umbrella & task switches ───────────────────────────────────────
    "use_ml": [
        f"src/{PKG}/models/ml",
        f"src/{PKG}/api/routers/ml_router.py",
    ],
    "use_classification": [
        f"src/{PKG}/models/ml/classification",
        f"src/{PKG}/services/classification_service.py",
    ],
    "use_forecasting": [
        f"src/{PKG}/models/ml/forecasting",
        f"src/{PKG}/services/forecasting_service.py",
    ],
    "use_regression":    [f"src/{PKG}/models/ml/regression"],
    "use_sentiment":     [f"src/{PKG}/services/sentiment_service.py"],

    # ── Infrastructure switches ───────────────────────────────────────────
    "use_feature_store": [f"src/{PKG}/infrastructure/storage/feature_store.py"],
    "use_vector_db":     [f"src/{PKG}/infrastructure/storage/vector_db.py"],
    "use_messaging":     [f"src/{PKG}/infrastructure/messaging"],
    "use_mlflow":        [f"src/{PKG}/infrastructure/tracking"],

    # ── Lightweight mode cleanup ──────────────────────────────────────────
    # If lightweight_mode == "yes", keep collapsed stubs; if "no", delete them
    "lightweight_mode": [
        f"src/{PKG}/core.py",
        f"src/{PKG}/pipelines.py",
    ],
}

# --------------------------------------------------------------------------- #
# 3. Helpers                                                                  #
# --------------------------------------------------------------------------- #
def prune(path: Path) -> None:
    if not path.exists():
        return
    shutil.rmtree(path) if path.is_dir() else path.unlink()

def prune_empty_upwards(start: Path) -> None:
    for parent in start.parents:
        if parent == ROOT:
            break
        if any(parent.iterdir()):
            break
        parent.rmdir()

# --------------------------------------------------------------------------- #
# 4. Prune                                                                    #
# --------------------------------------------------------------------------- #
for flag, paths in PRUNE_MAP.items():
    if flag == "lightweight_mode" and CTX[flag] == "yes":
        continue                     # keep collapsed files in lightweight mode
    if CTX.get(flag, "yes") == "no":
        for p in map(Path, paths):
            prune(ROOT / p)
            prune_empty_upwards(ROOT / p)

# --------------------------------------------------------------------------- #
# 5. Success banner                                                           #
# --------------------------------------------------------------------------- #
print(
    "\n✅  Post-generation cleanup complete."
    "\n👉  Next:"
    "\n   1) git init && git add . && git commit -m 'initial'"
    "\n   2) poetry install     (or pip install -e .)"
    "\n   3) make dev-up        # spin up local stack"
)
# {% endraw %}
