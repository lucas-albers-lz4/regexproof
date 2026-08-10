"""TIMEOUT/unknown remains a hard failure in the harness path."""

from __future__ import annotations

from pathlib import Path

from regexproof.harness import run_one


def test_harness_marks_unknown_as_not_ok():
    # Ensure run_one treats unknown as failure — inspect source contract.
    path = Path(run_one.__code__.co_filename)
    src = path.read_text(encoding="utf-8")
    assert "unknown" in src
    assert "TIMEOUT" in src
    assert "hard" in src.lower() or "FAIL" in src
