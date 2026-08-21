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


def real_accepts_argv_bytes(
    argv: Sequence[str], data: bytes, timeout: float = 10.0
) -> bool:
    """Run argv with raw ``data`` on stdin (binary-safe). Always shell=False."""
    if not argv:
        raise ValueError("argv must be non-empty")
    if isinstance(argv, str):
        raise TypeError("argv must be a sequence of strings, not a shell string")
    try:
        proc = subprocess.run(
            list(argv),
            input=data,
            capture_output=True,
            text=False,
            shell=False,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(
            "    TIMEOUT running real impl on binary probe — treat as mismatch",
            file=sys.stderr,
        )
        return False
    return proc.returncode == 0


def real_accepts_perl(
    pattern: str, flags: str, s: str, *, timeout: float = 10.0
) -> bool:
    """Replay via ``helpers/perl/match.py`` (system perl; no Python re).

    Exit codes from the helper: 0 match, 1 no-match, 2 pattern compile
    failure, 3 unavailable/version. Compile failures raise (not treated as
    helper-unavailable).
    """
    root = Path(__file__).resolve().parents[2]
    helper = root / "helpers" / "perl" / "match.py"
    try:
        proc = subprocess.run(
            [sys.executable, str(helper), "match", pattern, flags or ""],
            input=s,
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return False
    if proc.returncode == 2:
        raise RuntimeError(
            f"perl-pattern-compile-failed: {(proc.stderr or '').strip()}"
        )
    if proc.returncode == 3:
        raise RuntimeError("perl-helper-unavailable")
    return proc.returncode == 0


def real_accepts_yara(
    rule_src: str, data: bytes, *, timeout: float = 10.0
) -> bool:
    """Write rule + sample to temp files; invoke ``yara`` (NUL-safe)."""
    import tempfile
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    helper = root / "helpers" / "yara" / "match.py"
    with tempfile.TemporaryDirectory(prefix="yara-replay-") as tmp:
        tdir = Path(tmp)
        rule_path = tdir / "rule.yar"
        sample_path = tdir / "sample.bin"
        rule_path.write_text(rule_src, encoding="utf-8")
        sample_path.write_bytes(data)
        try:
            proc = subprocess.run(
                [sys.executable, str(helper), "match", str(rule_path), str(sample_path)],
                capture_output=True,
                shell=False,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return False
        if proc.returncode == 2:
            raise RuntimeError("yara-rule-compile-failed")
        if proc.returncode == 3:
            raise RuntimeError("yara-helper-unavailable")
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


_SUBPROCESS_METHODS = frozenset({"run", "Popen", "call", "check_call", "check_output"})


def _subprocess_aliases(tree: ast.AST) -> tuple[set[str], set[str]]:
    """Return (module aliases, imported method names) for subprocess."""
    aliases: set[str] = set()
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "subprocess":
                    aliases.add(alias.asname or "subprocess")
        elif isinstance(node, ast.ImportFrom) and node.module == "subprocess":
            for alias in node.names:
                if alias.name in _SUBPROCESS_METHODS:
                    imported.add(alias.asname or alias.name)
    return aliases, imported


def _timeout_is_explicit_and_enabled(call: ast.Call) -> bool:
    for kw in call.keywords:
        if kw.arg != "timeout":
            continue
        if isinstance(kw.value, ast.Constant) and kw.value.value is None:
            return False
        return True
    return False


def _popen_timed_in_function(tree: ast.Module, call: ast.Call) -> bool:
    """True when a Popen constructor's result is waited on with a timeout in
    the same function. subprocess.Popen takes no ``timeout=`` kwarg — the
    bound lives on ``communicate()`` / ``wait()`` — so a constructor whose
    result is timed there is compliant (the harness Popen sites use exactly
    this pattern with a process-group kill on TimeoutExpired).

    Gate-review fold (#548): the timed wait must be on the SAME receiver as
    the Popen result (``p.communicate(timeout=...)``, not some other
    variable), and the check uses the INNERMOST enclosing function so a
    Popen nested in an inner def cannot be blessed by a timed wait in the
    outer scope.
    """
    def contains(outer: ast.AST, target: ast.AST) -> bool:
        return any(child is target for child in ast.walk(outer))

    enclosing = None
    for node in ast.walk(tree):
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and contains(node, call)
            and (enclosing is None or contains(enclosing, node))
        ):
            enclosing = node
    if enclosing is None:
        return False

    targets: set[str] = set()
    for node in ast.walk(enclosing):
        if isinstance(node, ast.Assign) and node.value is call:
            for t in node.targets:
                if isinstance(t, ast.Name):
                    targets.add(t.id)
                elif isinstance(t, ast.Tuple):
                    for elt in t.elts:
                        if isinstance(elt, ast.Name):
                            targets.add(elt.id)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)) and node.value is call:
            if isinstance(node.target, ast.Name):
                targets.add(node.target.id)
    if not targets:
        return False

    for node in ast.walk(enclosing):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if (
            isinstance(func, ast.Attribute)
            and func.attr in ("communicate", "wait")
            and isinstance(func.value, ast.Name)
            and func.value.id in targets
            and _timeout_is_explicit_and_enabled(node)
        ):
            return True
    return False


def reject_untimed_subprocess_usage(paths: Sequence[Path] | None = None) -> list[str]:
    """Static check: fail if subprocess calls omit an explicit timeout=.

    Scans the whole ``regexproof/`` package by default (#543; previously only
    compilers + helpers, leaving harness/, rule_diff/, mine/ uncovered).
    subprocess.Popen is exempt when its result is waited on with a timeout in
    the same function (``communicate(timeout=...)`` / ``wait(timeout=...)``).
    Returns a list of violation messages (empty = clean).
    """
    if paths is None:
        root = Path(__file__).resolve().parents[2]
        paths = [
            root / "regexproof",
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
            aliases, imported = _subprocess_aliases(tree)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                name = None
                if (
                    isinstance(func, ast.Attribute)
                    and isinstance(func.value, ast.Name)
                    and func.value.id in aliases
                    and func.attr in _SUBPROCESS_METHODS
                ):
                    name = func.attr
                elif isinstance(func, ast.Name) and func.id in imported:
                    name = func.id
                if name is None:
                    continue
                if (
                    name == "Popen"
                    and _popen_timed_in_function(tree, node)
                ):
                    continue
                if not _timeout_is_explicit_and_enabled(node):
                    violations.append(
                        f"{file}:{node.lineno}: subprocess.{name}(...) missing timeout="
                    )
    return violations
