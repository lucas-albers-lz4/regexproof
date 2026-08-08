"""Argv-based engine adapters for differential fuzz / ground-truth replay.

Phase-1 gate: never use shell=True when scanning untrusted patterns/repos.
"""

from __future__ import annotations

import ast
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path


def real_accepts_argv(argv: Sequence[str], s: str, timeout: float = 10.0) -> bool:
    """Run argv with `s` on stdin; exit 0 = accept. Always shell=False."""
    if not argv:
        raise ValueError("argv must be non-empty")
    if isinstance(argv, str):
        raise TypeError(
            "argv must be a sequence of strings, not a shell string — "
            "pass a list (e.g. ['grep', '-qE', pattern])"
        )
    try:
        proc = subprocess.run(
            list(argv),
            input=s,
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(
            f"    TIMEOUT running real impl on {s!r} — treat as mismatch",
            file=sys.stderr,
        )
        return False
    return proc.returncode == 0


def reject_shell_subprocess_usage(paths: Sequence[Path] | None = None) -> list[str]:
    """Static check: fail if any scanned file passes shell=True to subprocess.

    Returns a list of violation messages (empty = clean).
    """
    if paths is None:
        root = Path(__file__).resolve().parents[2]
        paths = [
            root / "regexproof" / "fuzz",
            root / "regexproof" / "redos",
            root / "helpers" / "redos",
            root / "scripts" / "differential-fuzz.py",
        ]
    violations: list[str] = []
    for path in paths:
        if path.is_dir():
            files = sorted(path.rglob("*.py"))
        else:
            files = [path]
        for file in files:
            if not file.is_file():
                continue
            source = file.read_text(encoding="utf-8")
            try:
                tree = ast.parse(source, filename=str(file))
            except SyntaxError as exc:
                violations.append(f"{file}: syntax error: {exc}")
                continue
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                name = None
                if isinstance(func, ast.Attribute) and func.attr in {
                    "run",
                    "Popen",
                    "call",
                    "check_call",
                    "check_output",
                }:
                    name = func.attr
                elif isinstance(func, ast.Name) and func.id in {
                    "run",
                    "Popen",
                    "call",
                    "check_call",
                    "check_output",
                }:
                    name = func.id
                if name is None:
                    continue
                for kw in node.keywords:
                    if kw.arg != "shell":
                        continue
                    if isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        violations.append(
                            f"{file}:{node.lineno}: subprocess.{name}(..., shell=True) forbidden"
                        )
    return violations
