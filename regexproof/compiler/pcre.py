"""PCRE encodable-subset compiler + PCRE2 CLI helper gate."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.fold import python_fold_closure
from regexproof.compiler.lower import lower
from regexproof.compiler.pcre_strip import strip_atomic_and_possessive
from regexproof.compiler.simple_parse import parse_pattern

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "pcre2" / "match.py"
DEFAULT_MAX_LENGTH = 256
PCRE_TERMINATORS = frozenset(["\n"])

_REJECT_MARKERS = (
    ("(?=", "lookaround"),
    ("(?!", "lookaround"),
    ("(?<=", "lookaround"),
    ("(?<!", "lookaround"),
    ("\\k<", "backref"),
    ("\\g<", "backref"),
    ("(?(", "conditional"),
    ("\\K", "reset"),
    ("\\G", "g-anchor"),
    ("\\R", "r-escape"),
    ("\\X", "x-escape"),
    ("\\C", "c-escape"),
)


def _local_reject(pattern: str) -> str | None:
    for marker, reason in _REJECT_MARKERS:
        if marker in pattern:
            return reason
    if re.search(r"(?<!\\)\\[1-9]", pattern):
        return "backref"
    return None


def _helper_parse(pattern: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(HELPER), "parse", pattern],
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "unencodable_reason": "parse-error"}


def compile_pcre(
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
        reason = _local_reject(pattern)
        if reason:
            raise Unencodable(reason)
        # Strip atomic/possessive outside char classes only (never mutate `[*+]`).
        stripped = strip_atomic_and_possessive(pattern)
        # Optional real-engine parse when available; never required for encode.
        gate = _helper_parse(stripped)
        if gate.get("ok") is False and gate.get("unencodable_reason") not in (
            None,
            "pcre2-helper-unavailable",
        ):
            # Real engine rejected the pattern.
            if gate.get("helper") in ("pcre2-bindings", "pcre2grep"):
                raise Unencodable(gate.get("unencodable_reason") or "parse-error")
        ast = parse_pattern(stripped)
        fold = (lambda ch: python_fold_closure(ch, ascii_only=True)) if "i" in flags else None
        mirror, _meta = lower(
            ast,
            fold=fold,
            dot_terminators=PCRE_TERMINATORS,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in " \t\n\r\f\v"]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=True,
            call_kind=call_kind,
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="pcre",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="pcre",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def replay_argv(pattern: str, flags: str) -> list[str]:
    return [sys.executable, str(HELPER), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    """True only when a real PCRE2 engine (bindings or pcre2grep) is used."""
    gate = _helper_parse("a+")
    if not gate.get("ok"):
        return False
    if gate.get("helper") not in ("pcre2-bindings", "pcre2grep"):
        return False
    proc = subprocess.run(
        [sys.executable, str(HELPER), "match", "a+", ""],
        input="aaa",
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0
