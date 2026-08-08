"""Question inventory loader + corpus-coverage gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

INVENTORY_DIR = Path(__file__).resolve().parents[2] / "batch" / "inventories"
CORPUS_TYPE_FILES = {
    "rule_corpus": "rule_corpus.json",
    "validator": "validator.json",
}


def load_inventory(
    corpus_type: str,
    *,
    inventory_dir: Path | None = None,
) -> dict[str, Any]:
    inventory_dir = inventory_dir or INVENTORY_DIR
    name = CORPUS_TYPE_FILES.get(corpus_type)
    if not name:
        raise ValueError(f"unknown corpus_type {corpus_type!r}")
    path = inventory_dir / name
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("corpus_type") != corpus_type:
        raise ValueError(f"{path}: corpus_type mismatch")
    return data


def check_corpus_coverage(
    *,
    inventory_dir: Path | None = None,
    required_types: tuple[str, ...] = ("rule_corpus", "validator"),
) -> list[str]:
    """Return violation messages (empty = ok)."""
    inventory_dir = inventory_dir or INVENTORY_DIR
    violations: list[str] = []
    for ctype in required_types:
        try:
            inv = load_inventory(ctype, inventory_dir=inventory_dir)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            violations.append(f"{ctype}: {exc}")
            continue
        shapes = {int(q["shape"]) for q in inv.get("questions") or []}
        missing = {1, 2, 3, 4} - shapes
        if missing:
            violations.append(f"{ctype}: missing shapes {sorted(missing)}")
    return violations
