"""DOMPurify TS regex extractor (Wave 3 / #115).

Wraps ``extract_js_precise`` and enriches ``seal(/…/)`` sites with the
exported sanitizer-check name (``IS_ALLOWED_URI``, ``IS_SCRIPT_OR_DATA``, …).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.js_babel import extract_js_precise

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
    seal_names = _seal_name_map(source)
    for rec in recs:
        # Offset of the regex start ≈ line/col; match nearest preceding seal.
        offset = _approx_offset(source, rec["line"], rec["column"])
        name = _nearest_seal_name(seal_names, offset)
        if name:
            rec["rule_name"] = name
            snippet = rec.get("context_snippet") or ""
            if name not in snippet:
                rec["context_snippet"] = f"seal:{name}; {snippet}"[:500]
            # Sanitizer-boundary markers used by triage / disclosure.
            if name in ("IS_ALLOWED_URI", "IS_SCRIPT_OR_DATA"):
                rec["sanitizer_check"] = name
        elif _is_inside_seal(source, offset):
            snippet = rec.get("context_snippet") or ""
            if not snippet.startswith("seal:"):
                rec["context_snippet"] = f"seal:(anon); {snippet}"[:500]
    return recs


def _seal_name_map(source: str) -> list[tuple[int, str]]:
    """``(offset, NAME)`` for each ``const NAME = seal(`` binding."""
    return [(m.start(), m.group("name")) for m in _SEAL_NAME.finditer(source)]


def _nearest_seal_name(names: list[tuple[int, str]], offset: int) -> str | None:
    best: str | None = None
    best_pos = -1
    for pos, name in names:
        if pos <= offset and pos >= best_pos:
            # Only attach if the seal( is within a short window (same binding).
            if offset - pos < 400:
                best = name
                best_pos = pos
    return best


def _is_inside_seal(source: str, offset: int) -> bool:
    for m in _SEAL_CALL.finditer(source):
        if m.start() <= offset < m.start() + 400:
            # Look for closing ); after the regex — best-effort.
            return True
    return False


def _approx_offset(source: str, line: int, column: int) -> int:
    lines = source.splitlines(keepends=True)
    if line < 1 or line > len(lines):
        return 0
    return sum(len(lines[i]) for i in range(line - 1)) + column
