"""JS/TS extractor — regex literal + new RegExp.

``extract_js`` is the legacy regex-based scan (validatorjs / fixtures).
``extract_js_precise`` is a tokenizing scan that skips comments/strings and
only accepts ``/…/`` where a regex literal is grammatically allowed — used by
Wave-3 ecma frontier corpora (DOMPurify / isemail / email-addresses).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_LITERAL = re.compile(r"/(?P<pat>(?:\\.|[^/\\])+)/(?P<flags>[dgimsuvy]*)")
_NEW_REGEXP = re.compile(
    r"new\s+RegExp\s*\(\s*(?P<arg>[^)]+)\s*\)",
    re.MULTILINE,
)

_FLAGS = frozenset("dgimsuvy")
_REGEX_PREV = frozenset({"sof", "op", "kw", "lp", "colon", "comma", "return"})


def extract_js(source: str, *, repo: str, file: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in _LITERAL.finditer(source):
        flags = m.group("flags")
        reason = None
        call_kind = "search"
        if any(f in flags for f in "gy"):
            reason = "stateful"
        elif "u" in flags or "v" in flags:
            reason = f"{ 'u' if 'u' in flags else 'v' }-flag"
        # Heuristic consuming call on same line
        line_start = source.rfind("\n", 0, m.start()) + 1
        line_end = source.find("\n", m.end())
        if line_end < 0:
            line_end = len(source)
        line = source[line_start:line_end]
        if ".exec(" in line:
            call_kind = "exec"
        elif ".test(" in line:
            call_kind = "search"
        elif ".replace(" in line:
            call_kind = "substitution"
        line_no = source.count("\n", 0, m.start()) + 1
        col = m.start() - line_start
        out.append(
            make_record(
                repo=repo,
                pattern=m.group("pat"),
                flags="".join(c for c in "dgimsuvy" if c in flags),
                dialect="ecma",
                call_kind=call_kind,
                file=file,
                line=line_no,
                column=col,
                context_snippet=line.strip()[:500],
                unencodable_reason=reason,
            )
        )
    for m in _NEW_REGEXP.finditer(source):
        arg = m.group("arg").strip()
        line_no = source.count("\n", 0, m.start()) + 1
        col = m.start() - (source.rfind("\n", 0, m.start()) + 1)
        if (arg.startswith("'") and arg.endswith("'")) or (
            arg.startswith('"') and arg.endswith('"')
        ) or (arg.startswith("`") and arg.endswith("`") and "${" not in arg):
            pattern = arg[1:-1]
            reason = None
        else:
            pattern = ""
            reason = "composite-pattern"
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect="ecma",
                call_kind="search",
                file=file,
                line=line_no,
                column=col,
                context_snippet=m.group(0)[:500],
                unencodable_reason=reason,
            )
        )
    return out


def extract_js_precise(source: str, *, repo: str, file: str) -> list[dict[str, Any]]:
    """Tokenizing JS/TS regex-literal extractor (comment/string-aware).

    Deterministic left-to-right scan. Division vs regex disambiguated by the
    previous token class (after ``=``, ``(``, ``return``, ``:``, ``,``, …).
    Also collects string-literal ``new RegExp(...)`` sites.
    """
    literals = _scan_regex_literals(source)
    out: list[dict[str, Any]] = []
    for start, pattern, flags in literals:
        line_start = source.rfind("\n", 0, start) + 1
        line_end = source.find("\n", start)
        if line_end < 0:
            line_end = len(source)
        line = source[line_start:line_end]
        line_no = source.count("\n", 0, start) + 1
        col = start - line_start
        reason = None
        call_kind = "search"
        if any(f in flags for f in "gy"):
            reason = "stateful"
        elif "u" in flags or "v" in flags:
            reason = "u-flag" if "u" in flags else "v-flag"
        # Prefer call on the same line; also peek at a short window after.
        window = source[max(0, start - 80) : min(len(source), start + len(pattern) + 40)]
        if ".exec(" in line or ".exec(" in window:
            call_kind = "exec"
        elif ".test(" in line or "regExpTest(" in line or ".test(" in window:
            call_kind = "search"
        elif ".replace(" in line or ".replace(" in window:
            call_kind = "substitution"
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags="".join(c for c in "dgimsuvy" if c in flags),
                dialect="ecma",
                call_kind=call_kind,
                file=file,
                line=line_no,
                column=col,
                context_snippet=line.strip()[:500],
                unencodable_reason=reason,
            )
        )
    # new RegExp("...") — reuse legacy scanner (composite → unencodable).
    for m in _NEW_REGEXP.finditer(source):
        arg = m.group("arg").strip()
        line_no = source.count("\n", 0, m.start()) + 1
        col = m.start() - (source.rfind("\n", 0, m.start()) + 1)
        if (arg.startswith("'") and arg.endswith("'")) or (
            arg.startswith('"') and arg.endswith('"')
        ) or (arg.startswith("`") and arg.endswith("`") and "${" not in arg):
            pattern = arg[1:-1]
            reason = None
        else:
            pattern = ""
            reason = "composite-pattern"
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect="ecma",
                call_kind="search",
                file=file,
                line=line_no,
                column=col,
                context_snippet=m.group(0)[:500],
                unencodable_reason=reason,
            )
        )
    out.sort(key=lambda r: (r["line"], r["column"], r["regex_id"]))
    return out


def _scan_regex_literals(source: str) -> list[tuple[int, str, str]]:
    """Return ``(start_offset, pattern, flags)`` for each regex literal."""
    results: list[tuple[int, str, str]] = []
    i = 0
    n = len(source)
    prev = "sof"

    while i < n:
        ch = source[i]
        if ch in " \t\r":
            i += 1
            continue
        if ch == "\n":
            i += 1
            continue
        if source.startswith("//", i):
            while i < n and source[i] != "\n":
                i += 1
            continue
        if source.startswith("/*", i):
            j = source.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        if ch in "\"'`":
            i = _skip_string(source, i)
            prev = "val"
            continue
        if ch == "/":
            if prev in _REGEX_PREV:
                start = i
                lit = _try_parse_regex(source, i)
                if lit is not None:
                    pattern, flags, end = lit
                    results.append((start, pattern, flags))
                    i = end
                    prev = "val"
                    continue
            i += 1
            prev = "op"
            continue
        if ch.isalpha() or ch in "_$":
            j = i + 1
            while j < n and (source[j].isalnum() or source[j] in "_$"):
                j += 1
            word = source[i:j]
            i = j
            if word == "return":
                prev = "return"
            elif word in (
                "case",
                "throw",
                "typeof",
                "delete",
                "void",
                "new",
                "in",
                "of",
                "instanceof",
                "await",
                "yield",
            ):
                prev = "kw"
            else:
                prev = "id"
            continue
        if ch.isdigit():
            while i < n and (source[i].isalnum() or source[i] in "._"):
                i += 1
            prev = "val"
            continue
        if ch in "([{":
            prev = "lp"
            i += 1
            continue
        if ch in ")]}":
            prev = "val"
            i += 1
            continue
        if ch == ",":
            prev = "comma"
            i += 1
            continue
        if ch == ":":
            prev = "colon"
            i += 1
            continue
        if ch == ";":
            prev = "sof"
            i += 1
            continue
        if source.startswith("=>", i):
            i += 2
            prev = "op"
            continue
        if ch in "=!<>+-*%&|^~?":
            i += 1
            prev = "op"
            continue
        if ch == ".":
            i += 1
            prev = "dot"
            continue
        i += 1
        prev = "op"
    return results


def _skip_string(source: str, i: int) -> int:
    q = source[i]
    n = len(source)
    i += 1
    while i < n:
        c = source[i]
        if c == "\\":
            i += 2
            continue
        if q == "`" and source.startswith("${", i):
            i += 2
            depth = 1
            while i < n and depth:
                if source[i] == "{":
                    depth += 1
                elif source[i] == "}":
                    depth -= 1
                i += 1
            continue
        if c == q:
            return i + 1
        i += 1
    return n


def _try_parse_regex(source: str, i: int) -> tuple[str, str, int] | None:
    """Parse ``/pattern/flags`` starting at ``i``. Return None if not a regex."""
    n = len(source)
    if i >= n or source[i] != "/":
        return None
    i += 1
    pat: list[str] = []
    while i < n:
        c = source[i]
        if c == "\\":
            pat.append(c)
            if i + 1 < n:
                pat.append(source[i + 1])
                i += 2
                continue
            return None
        if c == "/":
            i += 1
            flags = ""
            while i < n and source[i] in _FLAGS:
                flags += source[i]
                i += 1
            return "".join(pat), flags, i
        if c == "\n":
            return None
        if c == "[":
            pat.append(c)
            i += 1
            while i < n and source[i] != "]":
                if source[i] == "\\" and i + 1 < n:
                    pat.append(source[i])
                    pat.append(source[i + 1])
                    i += 2
                    continue
                if source[i] == "\n":
                    return None
                pat.append(source[i])
                i += 1
            if i >= n or source[i] != "]":
                return None
            pat.append("]")
            i += 1
            continue
        pat.append(c)
        i += 1
    return None
