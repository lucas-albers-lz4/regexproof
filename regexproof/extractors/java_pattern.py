"""Extract Java ``Pattern.compile("…")`` string literals as pcre-approx records.

Inventory dialect on the probe path remains ``java`` (count-only). Graduation
compiles the encodable subset as ``pcre`` with an explicit java→pcre
approximation (Wave 4 / #133). See ``sweep/corpus-wave4/java-features.md``.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.compiler.reject_markers import PCRE_REJECT_MARKERS
from regexproof.extractors.record import make_record

# Same surface as admission.walk.count_java_pattern_compile (single-line strings).
_JAVA_PATTERN_COMPILE = re.compile(
    r"Pattern\s*\.\s*compile\s*\(\s*\"((?:\\.|[^\"\\])*)\"",
    re.MULTILINE,
)

APPROXIMATION = "java→pcre"


def java_reject_reason(pattern: str) -> str | None:
    """Return unencodable reason for A1B / pcre-approx graduation, or None."""
    for needle, reason in PCRE_REJECT_MARKERS:
        if needle in pattern:
            return reason
    if r"\p{" in pattern or r"\P{" in pattern:
        return "unicode-property"
    if r"\Q" in pattern or r"\E" in pattern:
        # Quote escapes are not faithfully lowered in the pcre ASCII mirror.
        return "quote"
    if pattern.count("(") != pattern.count(")"):
        return "parse-error"
    return None


def _unescape_java_string(raw: str) -> str:
    try:
        return bytes(raw, "utf-8").decode("unicode_escape")
    except UnicodeDecodeError:
        return raw


def extract_java_pattern(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    """Extract Pattern.compile string literals as pcre records (+ approx note)."""
    out: list[dict[str, Any]] = []
    for m in _JAVA_PATTERN_COMPILE.finditer(source):
        line = source.count("\n", 0, m.start()) + 1
        col = m.start() - (source.rfind("\n", 0, m.start()) + 1)
        pattern = _unescape_java_string(m.group(1))
        flags = ""
        # Promote leading (?i) to flags for the pcre ASCII fold path.
        if pattern.startswith("(?i)"):
            flags = "i"
            body = pattern[4:]
        else:
            body = pattern
        reason = java_reject_reason(pattern)
        rec = make_record(
            repo=repo,
            pattern=body if not reason else pattern,
            flags=flags if not reason else "",
            dialect=dialect,
            call_kind="search",
            file=file,
            line=line,
            column=col,
            context_snippet=f"approximation:{APPROXIMATION}",
            unencodable_reason=reason,
        )
        rec["approximation"] = APPROXIMATION
        rec["source_dialect"] = "java"
        out.append(rec)
    return out
