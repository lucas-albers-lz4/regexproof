"""Pregate mirror-fidelity gate smoke test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
    assert report["checked_ok"] >= 1
    # PCRE2 is optional in CI (ci/toolchain.toml status=n/a). When the helper
    # is present, the gate must have checked at least one PCRE row.
    if report.get("pcre2_helper"):
        assert report.get("pcre_checked_ok", 0) >= 1
