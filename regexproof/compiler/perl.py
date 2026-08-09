"""Perl encodable-subset compiler + system-perl helper gate (Wave 3 / #113)."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.fold import python_fold_closure
from regexproof.compiler.lower import lower, space_codes_from_chars
from regexproof.compiler.perl_strip import strip_perl_transparent
from regexproof.compiler.reject_markers import PERL_REJECT_MARKERS
from regexproof.compiler.simple_parse import parse_pattern

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "perl" / "match.py"
DEFAULT_MAX_LENGTH = 256
PERL_TERMINATORS = frozenset(["\n"])
_PERL_SPACE_CHARS = " \t\n\r\f\v"

# Full ``[[:name:]]`` class → ASCII equivalent (before parse).
_POSIX_CLASS_REWRITES: tuple[tuple[str, str], ...] = (
    ("[[:alpha:]]", "[a-zA-Z]"),
    ("[[:digit:]]", "[0-9]"),
    ("[[:alnum:]]", "[a-zA-Z0-9]"),
    ("[[:space:]]", "[ \t\n\r\f\v]"),
    ("[[:blank:]]", "[ \t]"),
    ("[[:upper:]]", "[A-Z]"),
    ("[[:lower:]]", "[a-z]"),
    ("[[:xdigit:]]", "[0-9A-Fa-f]"),
)


def _local_reject(pattern: str) -> str | None:
    for marker, reason in PERL_REJECT_MARKERS:
        if marker in pattern:
            return reason
    if re.search(r"(?<!\\)\\[1-9]", pattern):
        return "backref"
    return None


def _rewrite_posix_classes(pattern: str) -> str:
    out = pattern
    for src, dst in _POSIX_CLASS_REWRITES:
        out = out.replace(src, dst)
    return out


def _residual_posix_in_class(pattern: str) -> bool:
    """True if ``[:`` remains inside a character class after rewrites."""
    i = 0
    in_class = False
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            i += 2
            continue
        if not in_class and ch == "[":
            in_class = True
            i += 1
            continue
        if in_class and ch == "]":
            in_class = False
            i += 1
            continue
        if in_class and pattern.startswith("[:", i):
            return True
        i += 1
    return False


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


def compile_perl(
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
        stripped = strip_perl_transparent(pattern)
        rewritten = _rewrite_posix_classes(stripped)
        if _residual_posix_in_class(rewritten):
            raise Unencodable("posix-class")
        gate = _helper_parse(rewritten)
        if gate.get("ok") is False:
            ureason = gate.get("unencodable_reason")
            # Only hard-reject on real parse failures; helper absence is optional.
            if ureason not in (
                None,
                "perl-helper-unavailable",
                "perl-version-mismatch",
            ):
                raise Unencodable(ureason or "parse-error")
        ast = parse_pattern(rewritten)
        fold_fn = lambda ch: python_fold_closure(ch, ascii_only=True)
        fold = fold_fn if "i" in flags else None
        mirror, _meta = lower(
            ast,
            fold=fold,
            case_fold=fold_fn,
            dot_terminators=PERL_TERMINATORS,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in _PERL_SPACE_CHARS]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=True,
            call_kind=call_kind,
            allow_ascii_word_boundary=True,
            space_codes=space_codes_from_chars(_PERL_SPACE_CHARS),
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="perl",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="perl",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def replay_argv(pattern: str, flags: str) -> list[str]:
    return [sys.executable, str(HELPER), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    """True only when system perl helper is present and pins."""
    gate = _helper_parse("a+")
    if not gate.get("ok"):
        return False
    if gate.get("helper") != "perl":
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
