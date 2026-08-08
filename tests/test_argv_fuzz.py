"""Argv-only fuzz adapters + static shell=True rejection."""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.fuzz.adapters import real_accepts_argv, reject_shell_subprocess_usage
from regexproof.fuzz.job import pinned_alphabet


def test_real_accepts_argv_grep_metachar_pattern():
    """Metachar-containing pattern must not be shell-interpreted."""
    # Pattern has $ and quotes that would break under shell=True mishandling.
    argv = ["grep", "-qE", r"^[a-z0-9._-]+$"]
    assert real_accepts_argv(argv, "abc") is True
    assert real_accepts_argv(argv, "a;b") is False
    assert real_accepts_argv(argv, "ab|cd") is False


def test_real_accepts_argv_rejects_shell_string_type():
    with pytest.raises(TypeError):
        real_accepts_argv("grep -qE foo", "x")  # type: ignore[arg-type]


def test_no_shell_true_in_fuzz_paths():
    violations = reject_shell_subprocess_usage()
    assert violations == [], "\n".join(violations)


def test_pinned_alphabets_exist():
    for d in ("py_re", "ecma", "re2", "pcre"):
        assert pinned_alphabet(d)


def test_cli_rejects_real_cmd(tmp_path):
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        [
            sys.executable,
            str(root / "scripts" / "differential-fuzz.py"),
            "--mirror-expr",
            "Re('a')",
            "--real-cmd",
            "grep -qE a",
            "--alphabet",
            "a",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 2
    assert "forbidden" in proc.stderr.lower() or "FATAL" in proc.stderr
