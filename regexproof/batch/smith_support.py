"""Operator helpers for post-GO Smith (issue #149). Not an auto-GO path."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]

INFLATION_DIR_NAMES = frozenset(
    {
        "locale",
        "locales",
        "i18n",
        "translations",
        "vendor",
        "third_party",
        "third-party",
        "node_modules",
        "testdata",
        "test",
        "tests",
        "corpus",
        "fixtures",
    }
)

DIALECT_TO_EXTRACTOR = {
    "py_re": ("python_dir", "**/*.py"),
    "python": ("python_dir", "**/*.py"),
    "ecma": ("js_precise_dir", "**/*.{js,mjs,cjs,ts,tsx}"),
    "yara": ("yara", "**/*.yar"),
    "re2": ("go_regexp", "**/*.go"),
    "pcre": ("rule_file", "**/*.{rules,conf}"),
    "posix-shell": ("shell_posix", "**/*.sh"),
}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a JSON object")
    return data


def owner_slug_from_url(url: str) -> tuple[str, str]:
    path = urlparse(url).path.strip("/")
    parts = [p for p in path.split("/") if p]
    if len(parts) < 2:
        raise ValueError(f"cannot parse owner/repo from {url!r}")
    return parts[0], parts[1]


def clone_dest(url: str, corpus: str) -> Path:
    """Unique /tmp path so APFS does not collide yara-rules vs yara_rules."""
    owner, repo = owner_slug_from_url(url)
    safe_owner = owner.lower()
    safe_repo = repo.replace("/", "-")
    return Path("/tmp") / f"{safe_owner}-{safe_repo}-{corpus}"


def inflation_hits(sites_per_file: dict[str, Any]) -> list[str]:
    hits: list[str] = []
    for rel in sites_per_file:
        top = str(rel).replace("\\", "/").split("/", 1)[0].lower()
        if top in INFLATION_DIR_NAMES:
            hits.append(str(rel))
    return hits


def guess_extractor(dialect_counts: dict[str, Any]) -> tuple[str, str]:
    if not dialect_counts:
        return "python_dir", "**/*.py"
    top = max(dialect_counts, key=lambda k: int(dialect_counts.get(k) or 0))
    return DIALECT_TO_EXTRACTOR.get(str(top), ("python_dir", "**/*.py"))


def wave_checklist(corpus: str) -> str:
    return (
        f"WAVE: add {corpus!r} to WAVE_CORPORA only after a local complete_run. "
        "CI does not clone this corpus (detect-secrets is the only CI materialize). "
        "Do not infer smith_decision from fraction >= 0.30."
    )
