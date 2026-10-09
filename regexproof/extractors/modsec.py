"""ModSecurity SecRule extractor (OWASP CRS-style .conf rule files).

Extracts regex-bearing operators from ModSecurity rule files:

- ``@rx`` / ``!@rx`` — the primary regex surface (negated operator = inverted match)
- an omitted operator — ModSecurity defaults to ``@rx``
- variable-selector regexes (``!REQUEST_COOKIES:/^_pk_ref/``) — exclusion/exception
  selectors with a ``/regex/`` form

Non-regex operators (``@lt``, ``@eq``, ``@ge``, ``@pm``, ``@streq``, ...) are
counted via :func:`count_operators` but not extracted — they are not regex
language.

Extraction invariant (verified on CRS v4.28.0): ModSecurity operator strings are
double-quoted with ``\\"`` escapes inside the pattern. A naive ``"..."`` capture
truncates the pattern at the first quote (102 false parse-errors before this
module existed). See the regression tests.

SecRule directives frequently span multiple lines with trailing ``\\``; this
module joins continuations before matching so ``id:NNNN`` on a later line is
captured as ``rule_id``.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Iterator
from typing import Any

from regexproof.extractors.record import make_record

# Operator string: "((?:!)?@rx) <pattern>" with \" escapes allowed inside.
# Safe escaped-string idiom ([^"\\]*(?:\\.[^"\\]*)*) — linear-time; the
# naive (?:\\.|[^"\\])* alternation trips CodeQL py/redos.
_RX_OP = re.compile(r'"((?:!)?@rx)\s+([^"\\]*(?:\\.[^"\\]*)*)"')
# SecRule's operator is the first quoted argument after the variable list.
# When that argument is not an operator, ModSecurity interprets it as the
# pattern for its implicit default operator (@rx). Actions are optional in
# SecRule, so accept either a following action list or the end of the rule.
_RX_DEFAULT_OP = re.compile(
    r'^SecRule\b\s+[^"\n]+\s+"(?P<pattern>[^"\\]*(?:\\.[^"\\]*)*)"'
    r'(?=\s+(?:"|[A-Za-z_][A-Za-z0-9_-]*(?:\s*[:,=]|\s*$)|$)|$)',
    re.IGNORECASE,
)
# Variable-selector regexes: !REQUEST_COOKIES:/^_pk_ref/  (optional trailing flags)
# Linear-time idiom (CodeQL py/redos): [^/"\\]*(?:\\.[^/"\\]*)* unrolls the naive
# (?:\\.|[^/"])* alternation. The trailing \\? preserves exact language parity with
# the old pattern: its class [^/"] admitted a lone backslash before the closing
# delimiter (e.g. /a\/ extracts body "a\\"), which the bare idiom would drop.
# Differential-verified 0 diffs vs the old pattern (CRS v4.28.0 corpus + fuzz).
_RX_SELECTOR = re.compile(r'!(?:[A-Z_]+):(/[^/"\\]*(?:\\.[^/"\\]*)*\\?/[a-z]*|"[^"]*")')
# Any operator name (for counting; @rx is handled separately).
_RX_OPNAME = re.compile(r'"((?:!)?@[a-z_]+)')
_RULE_ID = re.compile(r"\bid:(\d+)\b")
_VARIABLE_SELECTOR = re.compile(r"^![A-Z_]+:")


def iter_secrule_blocks(source: str) -> Iterator[tuple[int, str]]:
    """Yield (start_line, joined_text) for each SecRule, joining ``\\`` continuations."""
    buf: list[str] = []
    start: int | None = None
    for i, line in enumerate(source.splitlines(), 1):
        s = line.rstrip()
        if not buf and not s.strip().startswith("SecRule"):
            continue
        if not buf:
            start = i
        buf.append(s)
        if s.endswith("\\"):
            continue
        joined = " ".join(x[:-1].rstrip() if x.endswith("\\") else x for x in buf)
        assert start is not None
        yield start, joined
        buf = []
        start = None


def extract_modsec(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract regex-bearing records from ModSecurity .conf source.

    One record per ``@rx``/``!@rx`` operator and per variable-selector regex.
    Non-regex operators are ignored (see :func:`count_operators`).
    """
    out: list[dict[str, Any]] = []
    for start_line, joined in iter_secrule_blocks(source):
        ls = joined.strip()
        if ls.startswith("#"):
            continue
        selector_source = ls
        m = _RX_OP.search(ls)
        if m:
            negated = m.group(1).startswith("!")
            pattern = m.group(2).strip()
            if not pattern:
                continue
            rec = make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect="pcre",
                call_kind="search",
                file=file,
                line=start_line,
                column=0,
                context_snippet=ls[:500],
            )
            rec["negated"] = negated
            mid = _RULE_ID.search(ls)
            if mid:
                rec["rule_id"] = mid.group(1)
            out.append(rec)
            continue
        default = _RX_DEFAULT_OP.search(ls)
        if default:
            pattern = default.group("pattern").strip()
            # Operator arguments begin with @ (or !@); they are not patterns
            # for the implicit operator. Variable-selector expressions are
            # handled separately below and must not be counted twice.
            if (
                not pattern.startswith(("@", "!@"))
                and _VARIABLE_SELECTOR.match(pattern) is None
            ):
                rec = make_record(
                    repo=repo,
                    pattern=pattern,
                    flags="",
                    dialect="pcre",
                    call_kind="search",
                    file=file,
                    line=start_line,
                    column=0,
                    context_snippet=ls[:500],
                )
                rec["operator_defaulted"] = True
                mid = _RULE_ID.search(ls)
                if mid:
                    rec["rule_id"] = mid.group(1)
                out.append(rec)
                # The selector lives in the variable list before the first
                # quoted argument; don't scan the pattern or actions for
                # selector-looking text.
                selector_source = ls[: default.start("pattern")]
        for sm in _RX_SELECTOR.finditer(selector_source):
            sel = sm.group(1)
            if not (sel.startswith("/") and len(sel) > 2):
                continue  # quoted selectors are literal strings, not regexes
            closing = sel.rfind("/")
            if closing <= 0:
                continue
            pattern = sel[1:closing]
            if not pattern:
                continue
            rec = make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect="pcre",
                call_kind="search",
                file=file,
                line=start_line,
                column=0,
                context_snippet=ls[:500],
            )
            rec["negated"] = True  # variable-selector regexes are exclusion selectors
            rec["selector"] = True
            mid = _RULE_ID.search(ls)
            if mid:
                rec["rule_id"] = mid.group(1)
            out.append(rec)
    return out


def count_operators(source: str) -> Counter[str]:
    """Count operator occurrences (including non-regex ones) per SecRule block."""
    counts: Counter[str] = Counter()
    for _start, joined in iter_secrule_blocks(source):
        ls = joined.strip()
        if ls.startswith("#"):
            continue
        m = _RX_OPNAME.search(ls)
        if m:
            counts[m.group(1)] += 1
    return counts
