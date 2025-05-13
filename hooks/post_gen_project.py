#!/usr/bin/env python3
# {% raw %}
"""Cookiecutter post-generation hook.

• Reads the user's answers.
• Removes code paths for any feature that was turned **off**.
• Prunes now-empty parent directories.
• Prints a friendly "what next?" banner.

Update PRUNE_MAP if you add new flags later.
"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Dict, List

# --------------------------------------------------------------------------- #
# 1. Load context provided by Cookiecutter
# --------------------------------------------------------------------------- #
try:
    # Cookiecutter ≤ 2.1
    from cookiecutter.utils import load_context  # type: ignore
    ROOT = Path(".").resolve()
    CTX  = load_context(ROOT)["cookiecutter"]  # type: ignore[index]
except ImportError:
    # Cookiecutter ≥ 2.2 – context is provided via env-var
    import json, os
    try:
        CTX = json.loads(os.environ["COOKIECUTTER_CONTEXT"])["cookiecutter"]
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"⚠️  Unable to load Cookiecutter context: {exc}")

# convenience alias
PKG = CTX["package_name"]
ROOT = Path(".").resolve()

# --------------------------------------------------------------------------- #
# 2. Map flags ➜ list[paths] to delete when flag == "no"
#    Paths may contain other Jinja placeholders.
# --------------------------------------------------------------------------- #
PRUNE_MAP: Dict[str, List[str]] = {
    # ── Core feature-crosscuts ───────────────────────────────────────────────
    "use_prompts": [
        "src/{PKG}/prompts",
    ],
    "include_rag": [
        "src/{PKG}/services/rag_service.py",
    ],
    "use_summarization": [
        "src/{PKG}/services/summarization_service.py",
    ],
    # ── GenAI & agents ───────────────────────────────────────────────────────
    "use_genai": [
        "src/{PKG}/models/genai",
        "src/{PKG}/api/routers/genai_router.py",
    ],
    "use_agents": [
        "src/{PKG}/models/agents",
        "src/{PKG}/api/routers/agent_router.py",
    ],
    # ── ML umbrella & fine-grained tasks ─────────────────────────────────────
    "use_ml": [
        "src/{PKG}/models/ml",
        "src/{PKG}/api/routers/ml_router.py",
    ],
    "use_classification": [
        "src/{PKG}/models/ml/classification",
        "src/{PKG}/services/classification_service.py",
    ],
    "use_forecasting": [
        "src/{PKG}/models/ml/forecasting",
        "src/{PKG}/services/forecasting_service.py",
    ],
    "use_regression": [
        "src/{PKG}/models/ml/regression",
    ],
    "use_sentiment": [
        "src/{PKG}/services/sentiment_service.py",
    ],
    # ── Storage / infra switches ─────────────────────────────────────────────
    "use_feature_store": [
        "src/{PKG}/infrastructure/storage/feature_store.py",
    ],
    "use_vector_db": [
        "src/{PKG}/infrastructure/storage/vector_db.py",
    ],
    "use_messaging": [
        "src/{PKG}/infrastructure/messaging",
    ],
    "use_mlflow": [
        "src/{PKG}/infrastructure/tracking",
    ],
    # ── Lightweight mode: if 'yes', delete expanded dirs; if 'no', delete collapsed files
    "lightweight_mode": [
        # If lightweight_mode == "yes", expanded dirs are absent anyway.
        # If == "no", remove the collapsed stubs:
        "src/{PKG}/core.py",
        "src/{PKG}/pipelines.py",
    ],
}

# --------------------------------------------------------------------------- #
# 3. Helpers
# --------------------------------------------------------------------------- #
def render(path_template: str) -> Path:
    result = path_template
    for key, val in CTX.items():
        result = result.replace(f"{{{{ cookiecutter.{key} }}}}", val)
    return ROOT / result


def prune(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def prune_empty_ancestors(start: Path) -> None:
    for parent in start.parents:
        if parent == ROOT:
            break
        if any(parent.iterdir()):
            break
        parent.rmdir()


# --------------------------------------------------------------------------- #
# 4. Execute pruning
# --------------------------------------------------------------------------- #
for flag, paths in PRUNE_MAP.items():
    # Special: lightweight_mode "yes" keeps collapsed stubs, "no" keeps expanded dirs
    if flag == "lightweight_mode" and CTX[flag] == "yes":
        # remove expanded dirs (they shouldn't exist) --> skip
        continue

    if CTX.get(flag, "yes") == "no":
        for raw in paths:
            p = render(raw)
            prune(p)
            prune_empty_ancestors(p)

# --------------------------------------------------------------------------- #
# 5. Success banner
# --------------------------------------------------------------------------- #
print(
    "\n✅  Post-generation cleanup complete."
    "\n👉  Next:"
    "\n   1.  git init && git add . && git commit -m 'initial'"
    "\n   2.  poetry install  (or pip install -e .)"
    "\n   3.  make dev-up  # spin up services"
)
# {% endraw %}
