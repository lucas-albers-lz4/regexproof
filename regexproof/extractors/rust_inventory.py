"""Inventory-only walker for rust-lang/regex (no fraction / go-no-go)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def inventory_rust_regex(root: Path) -> dict[str, Any]:
    files = sorted(p for p in root.rglob("*.rs") if p.is_file())
    return {
        "schema_version": "1",
        "pilot": "rust_regex",
        "scope": "inventory_only",
        "extracted": len(files),
        "note": "No fraction / go-no-go; fold interesting patterns into golden suite manually.",
        "sample_files": [str(p.relative_to(root)) for p in files[:20]],
    }


def write_rust_inventory(root: Path, out: Path) -> dict[str, Any]:
    report = inventory_rust_regex(root)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report
