"""PCRE encodable-subset compiler + PCRE2 CLI helper gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.fold import python_fold_closure
from regexproof.compiler.lower import lower
from regexproof.compiler.simple_parse import parse_pattern

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "pcre2" / "match.py"
DEFAULT_MAX_LENGTH = 256
PCRE_TERMINATORS = frozenset(["\n"])


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
        # Strip atomic groups / possessive — language-transparent for membership.
        stripped = (
            pattern.replace("(?>", "(?:")
            .replace("++", "+")
            .replace("*+", "*")
            .replace("?+", "?")
        )
        gate = _helper_parse(stripped)
        if gate.get("ok") is False:
            raise Unencodable(gate.get("unencodable_reason") or "parse-error")
        for marker, reason in (
            ("\\R", "r-escape"),
            ("\\X", "x-escape"),
            ("\\C", "c-escape"),
        ):
            if marker in pattern:
                raise Unencodable(reason)
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
    gate = _helper_parse("a+")
    if not gate.get("ok"):
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
