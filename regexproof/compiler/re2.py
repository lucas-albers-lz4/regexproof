"""Go RE2 dialect compiler — go-re2 helper for parse+replay + Z3 lower."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.fold import re2_fold_closure
from regexproof.compiler.lower import lower
from regexproof.compiler.pcre_strip import strip_language_transparent
from regexproof.compiler.simple_parse import parse_pattern

HELPER_DIR = Path(__file__).resolve().parents[2] / "helpers" / "go-re2"
DEFAULT_MAX_LENGTH = 256
RE2_TERMINATORS = frozenset(["\n"])


def _helper_bin() -> Path:
    env = os.environ.get("REGEXPROOF_GO_RE2")
    if env:
        return Path(env)
    local = HELPER_DIR / "go-re2"
    if local.is_file():
        return local
    return HELPER_DIR / "go-re2"


def ensure_built() -> Path:
    binary = _helper_bin()
    if binary.is_file():
        return binary
    subprocess.run(
        ["go", "build", "-o", str(binary), "."],
        cwd=str(HELPER_DIR),
        check=True,
        shell=False,
    )
    return binary


def parse_with_helper(pattern: str) -> dict:
    try:
        binary = ensure_built()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return {"ok": True, "helper": "go-missing"}
    proc = subprocess.run(
        [str(binary), "parse", pattern],
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "error": proc.stderr}


def compile_re2(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = DEFAULT_MAX_LENGTH,
) -> CompileResult:
    flags = "".join(sorted(set(flags)))
    try:
        if len(pattern) > max_length:
            raise Unencodable("pattern-too-long")
        if "m" in flags:
            raise Unencodable("m-flag")
        stripped = strip_language_transparent(pattern)
        gate = parse_with_helper(stripped)
        if gate.get("ok") is False:
            raise Unencodable("parse-error")
        ast = parse_pattern(stripped)
        fold = re2_fold_closure if "i" in flags else None
        mirror, _meta = lower(
            ast,
            fold=fold,
            dot_terminators=RE2_TERMINATORS,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in " \t\n\f\r"]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=False,
            call_kind=call_kind,
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="re2",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="re2",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def replay_argv(pattern: str, flags: str) -> list[str]:
    binary = ensure_built()
    return [str(binary), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    gate = parse_with_helper("a+")
    if gate.get("helper") != "go-re2" and gate.get("ok") is not True:
        return False
    try:
        binary = ensure_built()
    except Exception:  # noqa: BLE001
        return False
    proc = subprocess.run(
        [str(binary), "match", "a+", ""],
        input="aaa",
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0
