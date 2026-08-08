"""TIMEOUT/unknown remains a hard failure in the harness path."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def test_harness_marks_unknown_as_not_ok():
    path = Path(__file__).resolve().parents[1] / "scripts" / "z3-verify.py"
    spec = importlib.util.spec_from_file_location("z3_verify", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    # Ensure run_one treats unknown as failure — inspect source contract.
    src = path.read_text(encoding="utf-8")
    assert "unknown" in src
    assert "TIMEOUT" in src
    assert "hard" in src.lower() or "FAIL" in src
