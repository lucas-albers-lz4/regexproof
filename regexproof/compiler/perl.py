"""Perl encodable-subset compiler + system-perl helper gate (Wave 3 / #113)."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import (
    CompileResult,
    Unencodable,
    add_compiler_meta,
)
from regexproof.compiler.fold import python_fold_closure
from regexproof.compiler.lower import lower, space_codes_from_chars
from regexproof.compiler.perl_strip import strip_perl_transparent
from regexproof.compiler.reject_markers import PERL_REJECT_MARKERS, unicode_prop_unencodable
from regexproof.compiler.simple_parse import parse_pattern

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "perl" / "match.py"
DEFAULT_MAX_LENGTH = 256
HELPER_TIMEOUT_S = 30
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
    prop = unicode_prop_unencodable(pattern)
    if prop:
        return prop
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


def _classify_perl_helper_error(error: str) -> str:
    """Map perl stderr to a named reject bucket (never leave bare parse-error)."""
    e = (error or "").lower()
    if not e.strip():
        return "malformed-pattern"
    if "invalid [] range" in e or "false [] range" in e:
        return "bad-range"
    if "unescaped left brace" in e:
        return "unescaped-brace"
    if "unmatched (" in e or "unmatched )" in e or "unexpected ')'" in e:
        return "unmatched-paren"
    if "unmatched [" in e:
        return "unmatched-bracket"
    if "reference to nonexistent group" in e or "invalid reference to group" in e:
        return "backref"
    if "group name must start" in e or "sequence (?<" in e:
        return "named-group"
    if "eval-group" in e or "(*{" in e:
        return "code-embed"
    if "posix syntax" in e:
        return "posix-class"
    if "mutually exclusive" in e or "may not appear" in e or "maximum of twice" in e:
        return "flag-conflict"
    if "useless (?" in e:
        return "useless-flag"
    if "incomplete expression within '(?[ ])'" in e:
        return "extended-charclass"
    if "unknown verb" in e or "unknown '(*" in e or "'{#' is an unknown bound" in e:
        return "verb-construct"
    if "nested quantifiers" in e or "quantifier follows nothing" in e:
        return "bad-quantifier"
    if "\\o{}" in e or "octal" in e or "non-octal" in e:
        return "bad-octal"
    if "\\x{}" in e or "non-hex" in e or "\\x{...}" in e:
        return "bad-hex"
    if "empty \\b{}" in e or "empty \\B{}" in e:
        return "bad-boundary"
    if "sequence (?" in e or "in '(?...)" in e:
        return "inline-flag"
    if (
        "unexpected character" in e
        or "unexpected binary operator" in e
        or "unexpected '('" in e
        or "operand with no preceding" in e
    ):
        return "malformed-pattern"
    return "malformed-pattern"


def _helper_parse(pattern: str) -> dict:
    # argv cannot carry NUL; reject before spawn (Wave-3 P5 perl t/re).
    if "\x00" in pattern:
        return {"ok": False, "unencodable_reason": "embedded-nul"}
    try:
        proc = subprocess.run(
            [sys.executable, str(HELPER), "parse", pattern],
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout"}
    except ValueError:
        # Defense in depth: e.g. unexpected argv encoding failures.
        return {"ok": False, "unencodable_reason": "embedded-nul"}
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
        if "\x00" in pattern:
            raise Unencodable("embedded-nul")
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
            if ureason == "timeout":
                raise Unencodable("timeout")
            if ureason in (
                "perl-helper-unavailable",
                "perl-version-mismatch",
            ) or gate.get("helper") == "none":
                raise Unencodable("helper-unavailable")
            if ureason == "parse-error":
                ureason = _classify_perl_helper_error(str(gate.get("error") or ""))
            raise Unencodable(ureason or "malformed-pattern")
        ast = parse_pattern(rewritten)

        def fold_fn(ch):
            return python_fold_closure(ch, ascii_only=True)

        fold = fold_fn if "i" in flags else None
        # ``s`` (dotall): ``.`` matches newline — empty terminator set.
        terminators = frozenset() if "s" in flags else PERL_TERMINATORS
        mirror, meta = lower(
            ast,
            fold=fold,
            case_fold=fold_fn,
            dot_terminators=terminators,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in _PERL_SPACE_CHARS]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=True,
            call_kind=call_kind,
            allow_ascii_word_boundary=True,
            space_codes=space_codes_from_chars(_PERL_SPACE_CHARS),
        )
        # C1 (luna re-gate 7): respect a lowering-level mirror_exact verdict
        # (mixed \b alternations set False) — the entry defaults True.
        add_compiler_meta(meta, mirror_exact=bool(meta.get("mirror_exact", True)))
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="perl",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
            meta=meta,
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
    try:
        proc = subprocess.run(
            [sys.executable, str(HELPER), "match", "a+", ""],
            input="aaa",
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return False
    return proc.returncode == 0
