"""Intent-vs-actual detectors (usage + intent mismatches) — mechanical only."""

from __future__ import annotations

import re
from typing import Any

# Identifier/comment keywords → characters that should be excluded if the name
# claims that validation. Mechanical table — no NLP.
INTENT_TABLE: dict[str, frozenset[str]] = {
    "email": frozenset("\n\r\t "),
    "isemail": frozenset("\n\r\t "),
    "url": frozenset("\n\r\t "),
    "isurl": frozenset("\n\r\t "),
    "hostname": frozenset("\n\r\t@/"),
    "ishostname": frozenset("\n\r\t@/"),
    "ascii": frozenset(),  # checked via high-bit separately if needed
}


def _corpus_slug(rec: dict[str, Any]) -> str:
    """Prefer short pilot corpus name; fall back to extractor repo slug."""
    if rec.get("corpus_slug"):
        return str(rec["corpus_slug"])
    if rec.get("corpus") and "/" not in str(rec["corpus"]):
        return str(rec["corpus"])
    return str(rec.get("repo") or rec.get("corpus") or "")


def _keyword_hit(hay: str, key: str) -> bool:
    """Whole-token match only — avoids `url` inside `curl-auth-header`."""
    # Split camelCase then tokenize on non-alnum so isHostname → hostname.
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", hay)
    tokens = re.findall(r"[a-z0-9]+", spaced.lower())
    return key.lower() in tokens


def detect_usage_mismatches(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Anchored pattern used via search/test (or match when full-string implied)."""
    findings: list[dict[str, Any]] = []
    for rec in records:
        pattern = rec.get("pattern") or ""
        call_kind = rec.get("call_kind") or ""
        anchored = pattern.startswith("^") or pattern.endswith("$")
        if not anchored:
            continue
        if call_kind in ("search", "test"):
            findings.append(
                {
                    "schema_version": "1",
                    "regex_id": rec["regex_id"],
                    "kind": "usage_mismatch",
                    "corpus": _corpus_slug(rec),
                    "result": "finding",
                    "site": rec.get("site") or "",
                    "pattern": pattern,
                    "shape": None,
                    "disclosure": None,
                    "detail": {
                        "call_kind": call_kind,
                        "reason": "anchored pattern consumed via search/test",
                    },
                }
            )
        elif call_kind == "match" and pattern.startswith("^") and pattern.endswith("$"):
            findings.append(
                {
                    "schema_version": "1",
                    "regex_id": rec["regex_id"],
                    "kind": "usage_mismatch",
                    "corpus": _corpus_slug(rec),
                    "result": "finding",
                    "site": rec.get("site") or "",
                    "pattern": pattern,
                    "shape": None,
                    "disclosure": None,
                    "detail": {
                        "call_kind": call_kind,
                        "reason": "full-anchored pattern via match (fullmatch likely intended)",
                    },
                }
            )
    findings.sort(key=lambda f: f["regex_id"])
    return findings


def _class_has_whitespace_shorthand(content: str) -> bool:
    """True when a character-class body contains a REAL whitespace shorthand
    (``\\s`` — backslash not itself escaped) that covers SPACE. ``\\S`` is the
    NON-whitespace class and ``\\t`` is tab only: neither excludes space inside
    a negated class nor admits it inside a positive one. ``\\\\s`` inside a
    class is a literal backslash + s, which does NOT exclude whitespace."""
    i = 0
    n = len(content)
    while i < n:
        if content[i] != "\\":
            i += 1
            continue
        if i + 1 >= n:
            return False
        if content[i + 1] == "\\":
            i += 2  # escaped backslash: the next char is a literal
            continue
        if content[i + 1] == "s":
            return True
        i += 2
    return False


def _pattern_admits_space(pattern: str) -> bool:
    """True when the pattern can match a literal space (email/hostname context).

    Class-aware: ``\\s`` inside a NEGATED class excludes whitespace (no fire);
    ``\\\\s`` (escaped backslash + s) inside any class is literal backslash + s
    and does NOT exclude space (fire); ``\\S`` is the non-whitespace class (a
    negated class containing it still admits space — fire); a positive class
    admits space iff it holds a real ``\\s`` or a literal space; a negated class
    admits space unless it excludes it; ``\\s`` outside any class admits space.
    A ``]`` immediately after ``[``/``[^`` is a literal class char, not the
    terminator.
    """
    i = 0
    n = len(pattern)
    while i < n:
        ch = pattern[i]
        if ch == "[" and i + 1 < n:
            j = i + 1
            negated = pattern[j] == "^"
            if negated:
                j += 1
            content = ""
            if j < n and pattern[j] == "]":
                content = "]"
                j += 1
            while j < n:
                if pattern[j] == "\\" and j + 1 < n:
                    content += pattern[j : j + 2]
                    j += 2
                elif pattern[j] == "]":
                    break
                else:
                    content += pattern[j]
                    j += 1
            if j < n:  # closing ] found
                if negated:
                    if not _class_has_whitespace_shorthand(content) and " " not in content:
                        return True
                else:
                    if _class_has_whitespace_shorthand(content) or " " in content:
                        return True
                i = j + 1
                continue
            # unterminated '[' — treat as literal
            i += 1
            continue
        if ch == "\\" and i + 1 < n:
            if pattern[i + 1] == "s":
                return True
            i += 2  # any other escape (incl. \\\\ -> literal backslash)
            continue
        if ch == " ":
            return True
        i += 1
    return False


def detect_intent_mismatches(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Name/comment claims a validation the language does not enforce."""
    findings: list[dict[str, Any]] = []
    for rec in records:
        hay = " ".join(
            [
                str(rec.get("context_snippet") or ""),
                str(rec.get("file") or ""),
                str(rec.get("site") or ""),
                str(rec.get("name") or ""),
            ]
        )
        pattern = rec.get("pattern") or ""
        for key, excluded in INTENT_TABLE.items():
            if not _keyword_hit(hay, key):
                continue
            # If pattern clearly admits an excluded char via `.` or missing negation
            for ch in excluded:
                if ch == "\n" and (".*" in pattern or "[\\s\\S]" in pattern or r"[\s\S]" in pattern):
                    findings.append(_intent_finding(rec, key, ch))
                    break
                if ch == "@" and "@" in pattern and "hostname" in key:
                    # hostname pattern that includes @ literally is suspicious
                    findings.append(_intent_finding(rec, key, ch))
                    break
                if ch == " " and key in (
                    "email",
                    "isemail",
                    "hostname",
                    "ishostname",
                ):
                    # whitespace class in email/hostname claim (class-aware;
                    # no cheap pre-filter — _pattern_admits_space is precise and
                    # cheap, and a pre-filter would miss e.g. [^\S@] which admits
                    # whitespace without any literal space or \s signal)
                    if _pattern_admits_space(pattern):
                        findings.append(_intent_finding(rec, key, ch))
                        break
    # Deduplicate by regex_id+keyword
    uniq: dict[str, dict[str, Any]] = {}
    for f in findings:
        uniq[f"{f['regex_id']}:{f['detail']['keyword']}"] = f
    return sorted(uniq.values(), key=lambda f: (f["regex_id"], f["detail"]["keyword"]))


def _intent_finding(rec: dict[str, Any], keyword: str, bad_char: str) -> dict[str, Any]:
    return {
        "schema_version": "1",
        "regex_id": rec["regex_id"],
        "kind": "intent_mismatch",
        "corpus": _corpus_slug(rec),
        "result": "finding",
        "site": rec.get("site") or "",
        "pattern": rec.get("pattern") or "",
        "shape": None,
        "disclosure": None,
        "detail": {
            "keyword": keyword,
            "admitted_char": repr(bad_char),
            "reason": "name/comment claims validation but pattern admits excluded char",
        },
    }
