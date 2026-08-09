"""Pregate mirror-fidelity gate smoke + Wave-2 surface checks."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "sweep" / "corpus-wave2" / "fixtures"


def test_mirror_fidelity_gate_script_ok():
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "mirror-fidelity-gate.py"),
            "--max-per-corpus",
            "2",
            "--runs",
            "10",
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    report = json.loads(
        (ROOT / "properties" / "generated" / "mirror_fidelity_gate.json").read_text(
            encoding="utf-8"
        )
    )
    assert report["ok"] is True
    assert report["surfaces_ok"] is True
    assert report["wrong_wide_caught"] is True
    assert set(report["surfaces"]) == {
        "yara",
        "semgrep",
        "pcre2",
        "re2",
        "cpython",
        "busybox",
        "test262",
        "rule_diff",
    }
    assert report["checked_ok"] >= 1
    if report.get("pcre2_helper"):
        assert report.get("pcre_checked_ok", 0) >= 1


def test_mirror_fidelity_fail_closed_missing_fixture():
    """Removing one fixture must fail the gate (fail-closed)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "mirror_fidelity_gate",
        ROOT / "scripts" / "mirror-fidelity-gate.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    missing = FIXTURES / "yara.json"
    backup = missing.read_text(encoding="utf-8")
    missing.unlink()
    try:
        reports, ok = mod._run_surfaces()
        assert ok is False
        assert reports["yara"]["status"] == "absent"
    finally:
        missing.write_text(backup, encoding="utf-8")


def test_yara_helper_version_and_match():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "helpers" / "yara" / "match.py"), "version"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    meta = json.loads(proc.stdout)
    assert meta["ok"] is True
    assert "4." in meta.get("version", "")
