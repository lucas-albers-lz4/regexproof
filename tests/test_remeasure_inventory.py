"""Frozen-inventory re-measurement primitive (scripts/remeasure-from-inventory.py)."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_script() -> object:
    path = ROOT / "scripts" / "remeasure-from-inventory.py"
    spec = importlib.util.spec_from_file_location("remeasure_from_inventory", path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write_inventory(tmp_path, records) -> Path:
    path = tmp_path / "inv.ndjson"
    path.write_text(
        "\n".join(json.dumps(r, sort_keys=True) for r in records) + "\n",
        encoding="utf-8",
    )
    return path


def test_remeasure_reports_fraction_and_writes_artifact(tmp_path):
    mod = _load_script()
    records = [
        {
            "regex_id": f"rid-{i}",
            "site": f"x.js:{i}",
            "pattern": "a+",
            "flags": "",
            "dialect": "py_re",
            "call_kind": "search",
            "encodable": True,
            "compile_reason": None,
        }
        for i in range(3)
    ]
    inv = _write_inventory(tmp_path, records)
    mod.OUT = tmp_path  # keep the committed artifact untouched
    report = mod.remeasure("gitleaks", inventory=inv)
    assert report["sample_size"] == 3
    assert report["fraction"] == 1.0
    assert report["remeasure"]["flips"]["unchanged"] == 3
    assert report["remeasure"]["from"] == "frozen_inventory"
    art = json.loads((tmp_path / "gitleaks_encodable_fraction.json").read_text())
    assert art["fraction"] == 1.0
    assert "remeasure" in art
    assert "compiler_fingerprint" in art


def test_remeasure_dry_run_writes_nothing(tmp_path):
    mod = _load_script()
    records = [
        {
            "regex_id": "rid-1",
            "site": "x.js:1",
            "pattern": r"\bword\b",
            "flags": "",
            "dialect": "py_re",
            "call_kind": "search",
            "encodable": False,
            "compile_reason": "word-boundary",
        }
    ]
    inv = _write_inventory(tmp_path, records)
    mod.OUT = tmp_path
    report = mod.remeasure("gitleaks", inventory=inv, dry_run=True)
    assert not (tmp_path / "gitleaks_encodable_fraction.json").exists()
    assert report["fraction"] == 0.0


def test_remeasure_preserves_composite_pattern_extractor_rejects(tmp_path):
    """Frozen inventories store compile_reason only — empty pattern must not flip encodable."""
    mod = _load_script()
    records = [
        {
            "regex_id": "comp-1",
            "site": "rule.yaml:1",
            "pattern": "",
            "flags": "",
            "dialect": "py_re",
            "call_kind": "search",
            "encodable": False,
            "compile_reason": "composite-pattern",
        },
        {
            "regex_id": "ok-1",
            "site": "x.py:1",
            "pattern": "a+",
            "flags": "",
            "dialect": "py_re",
            "call_kind": "search",
            "encodable": True,
            "compile_reason": None,
        },
    ]
    inv = _write_inventory(tmp_path, records)
    mod.OUT = tmp_path
    report = mod.remeasure("semgrep_rules", inventory=inv, dry_run=True)
    assert report["sample_size"] == 2
    assert report["encodable"] == 1
    assert report["fraction"] == 0.5
    assert report["reasons"].get("composite-pattern") == 1
    assert report["remeasure"]["flips"]["now_encodable"] == 0
