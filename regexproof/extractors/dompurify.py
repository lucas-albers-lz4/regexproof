"""DOMPurify TS regex extractor (Wave 3 / #115).

Wraps ``extract_js_precise`` and enriches ``seal(/…/)`` sites with the
exported sanitizer-check name (``IS_ALLOWED_URI``, ``IS_SCRIPT_OR_DATA``, …).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.js_babel import (
    _skip_string,
    _try_parse_regex,
    extract_js_precise,
)

_SEAL_NAME = re.compile(
    r"(?:export\s+)?const\s+(?P<name>[A-Z][A-Z0-9_]*)\s*=\s*seal\s*\(",
    re.MULTILINE,
)
_SEAL_CALL = re.compile(r"\bseal\s*\(", re.MULTILINE)


def extract_dompurify(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract ecma regex literals from a DOMPurify TS/JS source unit."""
    recs = extract_js_precise(source, repo=repo, file=file)
    seal_spans = _seal_name_spans(source)
    anon_spans = _anon_seal_spans(source, named_starts={s for s, _, _ in seal_spans})
    for rec in recs:
        offset = _approx_offset(source, rec["line"], rec["column"])
        name = _seal_name_for_offset(seal_spans, offset)
        if name:
            rec["rule_name"] = name
            snippet = rec.get("context_snippet") or ""
            if name not in snippet:
                rec["context_snippet"] = f"seal:{name}; {snippet}"[:500]
            # Sanitizer-boundary markers used by triage / disclosure.
            if name in ("IS_ALLOWED_URI", "IS_SCRIPT_OR_DATA"):
                rec["sanitizer_check"] = name
        elif _offset_in_spans(anon_spans, offset):
            snippet = rec.get("context_snippet") or ""
            if not snippet.startswith("seal:"):
                rec["context_snippet"] = f"seal:(anon); {snippet}"[:500]
    return recs


def _seal_name_spans(source: str) -> list[tuple[int, int, str]]:
    """``(open_paren, close_paren, NAME)`` for each ``const NAME = seal(``."""
    spans: list[tuple[int, int, str]] = []
    for m in _SEAL_NAME.finditer(source):
        open_paren = m.end() - 1  # points at '('
        close = _match_paren(source, open_paren)
        if close is None:
            continue
        spans.append((open_paren, close, m.group("name")))
    return spans


def _anon_seal_spans(
    source: str, *, named_starts: set[int]
) -> list[tuple[int, int]]:
    """``seal(`` calls that are not ``const NAME = seal(`` bindings."""
    spans: list[tuple[int, int]] = []
    for m in _SEAL_CALL.finditer(source):
        open_paren = m.end() - 1
        if open_paren in named_starts:
            continue
        # Skip Object.seal( — word boundary already; require not preceded by '.'
        if open_paren > 0 and source[m.start() - 1 : m.start()] == ".":
            continue
        close = _match_paren(source, open_paren)
        if close is not None:
            spans.append((open_paren, close))
    return spans


def _seal_name_for_offset(
    spans: list[tuple[int, int, str]], offset: int
) -> str | None:
    """Attach a name only when the regex offset sits inside that seal(...) call."""
    for open_paren, close, name in spans:
        if open_paren < offset < close:
            return name
    return None


def _offset_in_spans(spans: list[tuple[int, int]], offset: int) -> bool:
    return any(a < offset < b for a, b in spans)


def _match_paren(source: str, open_paren: int) -> int | None:
    """Return index of matching ``)`` for ``(`` at ``open_paren``, or None.

    Skips string literals and regex literals so nested ``(`` inside patterns
    do not confuse the depth count.
    """
    if open_paren >= len(source) or source[open_paren] != "(":
        return None
    depth = 0
    i = open_paren
    n = len(source)
    while i < n:
        ch = source[i]
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
            continue
        if ch == "/":
            # Regex literal inside seal(...) args (the common DOMPurify form).
            lit = _try_parse_regex(source, i)
            if lit is not None:
                i = lit[2]
                continue
        if ch == "(":
            depth += 1
            i += 1
            continue
        if ch == ")":
            depth -= 1
            if depth == 0:
                return i
            i += 1
            continue
        i += 1
    return None


def _approx_offset(source: str, line: int, column: int) -> int:
    lines = source.splitlines(keepends=True)
    if line < 1 or line > len(lines):
        return 0
    return sum(len(lines[i]) for i in range(line - 1)) + column
