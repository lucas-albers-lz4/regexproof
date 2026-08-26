"""F5 (#553 close-out): emit-conversion-ndjson SHAPE fail-closed."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_emit_module():
    spec = importlib.util.spec_from_file_location(
        "emit_conversion_ndjson",
        ROOT / "scripts" / "emit-conversion-ndjson.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_entry() -> dict:
    return {
        "kind": "property",
        "domain": "test domain",
        "family": "OW-packages",
        "contract": {
            "guarantee": "no semicolon in accepted strings",
            "declared_domain": "test domain",
            "provenance": "human",
        },
    }


def test_row_from_run_missing_shape_aborts():
    mod = _load_emit_module()
    name = "OW-packages-not-in-shape-map"
    entry = _minimal_entry()
    result = {
        "result": "unsat",
        "domain": "test domain",
        "ground_truth": "verified",
    }
    with pytest.raises(SystemExit, match="missing SHAPE entry"):
        mod.row_from_run(name, entry, result, corpus="openwrt_packages")
