#!/usr/bin/env python3
"""Cookiecutter post-generation hook.

• Removes folders/files for every feature the user switched **off**
• Cleans up empty parent dirs
• Prints “what next” instructions
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List

ROOT = Path(".").resolve()                # repo root

# ------------------------------------------------------------------ #
# 1. Load the cookiecutter answers                                   #
# ------------------------------------------------------------------ #
CTX = {
    "package_name": "{{ cookiecutter.package_name }}",
    "lightweight_mode": "{{ cookiecutter.lightweight_mode }}",
    "use_prompts": "{{ cookiecutter.use_prompts }}",
    "include_rag": "{{ cookiecutter.include_rag }}",
    "use_summarization": "{{ cookiecutter.use_summarization }}",
    "use_genai": "{{ cookiecutter.use_genai }}",
    "use_agents": "{{ cookiecutter.use_agents }}",
    "use_ml": "{{ cookiecutter.use_ml }}",
    "use_classification": "{{ cookiecutter.use_classification }}",
    "use_forecasting": "{{ cookiecutter.use_forecasting }}",
    "use_regression": "{{ cookiecutter.use_regression }}",
    "use_sentiment": "{{ cookiecutter.use_sentiment }}",
    "use_feature_store": "{{ cookiecutter.use_feature_store }}",
    "use_vector_db": "{{ cookiecutter.use_vector_db }}",
    "use_messaging": "{{ cookiecutter.use_messaging }}",
    "use_mlflow": "{{ cookiecutter.use_mlflow }}",
}


PKG = CTX["package_name"]                # convenience alias

# ------------------------------------------------------------------ #
# 2. Flag → paths to delete when flag == "no"                        #
# ------------------------------------------------------------------ #
PRUNE_MAP: Dict[str, List[str]] = {
    # ── Cross-cut helpers ──────────────────────────────────────────
    "use_prompts":       [f"src/{PKG}/prompts"],
    "include_rag":       [f"src/{PKG}/services/rag_service.py"],
    "use_summarization": [f"src/{PKG}/services/summarization_service.py"],
    # ── GenAI & agents ─────────────────────────────────────────────
    "use_genai": [
        f"src/{PKG}/models/genai",
        f"src/{PKG}/api/routers/genai_router.py",
    ],
    "use_agents": [
        f"src/{PKG}/models/agents",
        f"src/{PKG}/api/routers/agent_router.py",
    ],
    # ── ML umbrella & tasks ────────────────────────────────────────
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
    # ── Infrastructure switches ────────────────────────────────────
    "use_feature_store": [f"src/{PKG}/infrastructure/storage/feature_store.py"],
    "use_vector_db":     [f"src/{PKG}/infrastructure/storage/vector_db.py"],
    "use_messaging":     [f"src/{PKG}/infrastructure/messaging"],
    "use_mlflow":        [f"src/{PKG}/infrastructure/tracking"],
    # ── Lightweight mode cleanup ───────────────────────────────────
    "lightweight_mode": [
        f"src/{PKG}/core.py",
        f"src/{PKG}/pipelines.py",
    ],
}

# ------------------------------------------------------------------ #
# 3. Helpers                                                         #
# ------------------------------------------------------------------ #
def prune(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path, ignore_errors=True)
    elif path.exists():
        path.unlink(missing_ok=True)

def prune_empty(start: Path) -> None:
    for parent in start.parents:
        if parent == ROOT:
            break
        if any(parent.iterdir()):
            break
        parent.rmdir()

# ------------------------------------------------------------------ #
# 4. Apply pruning                                                   #
# ------------------------------------------------------------------ #
for flag, paths in PRUNE_MAP.items():
    if flag == "lightweight_mode" and CTX["lightweight_mode"] == "yes":
        continue                                    # keep collapsed stubs
    if CTX.get(flag, "yes") == "no":
        for p in map(lambda s: ROOT / s, paths):
            prune(p)
            prune_empty(p)

# ------------------------------------------------------------------ #
# 5. Banner                                                          #
# ------------------------------------------------------------------ #
print(
    "\n✅  Post-generation cleanup complete."
    "\n👉  Next:"
    "\n   1) git init && git add . && git commit -m 'initial'"
    "\n   2) poetry install     (or pip install -e .)"
    "\n   3) make dev-up        # spin up local stack"
)