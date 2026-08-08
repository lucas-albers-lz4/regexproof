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
                    "corpus": rec.get("repo") or rec.get("corpus") or "",
                    "result": "finding",
                    "site": rec.get("site") or "",
                    "pattern": pattern,
                    "shape": None,
                    "ground_truth_status": "N/A",
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
                    "corpus": rec.get("repo") or rec.get("corpus") or "",
                    "result": "finding",
                    "site": rec.get("site") or "",
                    "pattern": pattern,
                    "shape": None,
                    "ground_truth_status": "N/A",
                    "disclosure": None,
                    "detail": {
                        "call_kind": call_kind,
                        "reason": "full-anchored pattern via match (fullmatch likely intended)",
                    },
                }
            )
    findings.sort(key=lambda f: f["regex_id"])
    return findings


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
        ).lower()
        pattern = rec.get("pattern") or ""
        for key, excluded in INTENT_TABLE.items():
            if key not in hay.replace("_", "").replace("-", ""):
                # also allow isEmail-style camel
                if not re.search(rf"\b{re.escape(key)}\b", hay, re.I):
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
                if ch == " " and (" " in pattern or r"\s" in pattern) and key in (
                    "email",
                    "isemail",
                    "hostname",
                    "ishostname",
                ):
                    # whitespace class in email/hostname claim
                    if r"\s" in pattern or "[ ]" in pattern:
                        findings.append(_intent_finding(rec, key, ch))
                        break
    # Deduplicate by regex_id+keyword
    uniq: dict[str, dict[str, Any]] = {}
    for f in findings:
        uniq[f"{f['regex_id']}:{f['detail']['keyword']}"] = f
    return sorted(uniq.values(), key=lambda f: f["regex_id"])


def _intent_finding(rec: dict[str, Any], keyword: str, bad_char: str) -> dict[str, Any]:
    return {
        "schema_version": "1",
        "regex_id": rec["regex_id"],
        "kind": "intent_mismatch",
        "corpus": rec.get("repo") or rec.get("corpus") or "",
        "result": "finding",
        "site": rec.get("site") or "",
        "pattern": rec.get("pattern") or "",
        "shape": None,
        "ground_truth_status": "N/A",
        "disclosure": None,
        "detail": {
            "keyword": keyword,
            "admitted_char": repr(bad_char),
            "reason": "name/comment claims validation but pattern admits excluded char",
        },
    }
