"""False-UNSAT detection: seeded under-approximating mirror must fail fuzz."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_underapprox_mirror_fails_differential_fuzz():
    """Mirror Re('a') under-approximates grep '^[ab]$' — must mismatch."""
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "differential-fuzz.py"),
            "--mirror-expr",
            "Re('a')",
            "--alphabet",
            "ab",
            "--mutations",
            "x",
            "--runs",
            "5",
            "--exhaust-max-len",
            "1",
            "--seed",
            "1",
            "--real-argv",
            "grep",
            "-qE",
            "^[ab]$",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 1, proc.stdout + proc.stderr
    assert "MISMATCH" in proc.stdout
