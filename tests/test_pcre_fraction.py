"""PCRE encodable-fraction measurement report (Phase 1)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.compiler.pcre import compile_pcre

REPORT = Path(__file__).resolve().parents[1] / "properties" / "generated" / "pcre_encodable_fraction.json"

SAMPLE = [
    r"^[a-z]+$",
    r"\d+",
    r"(a|b)+",
    r"foo(?:bar)?",
    r"a{2,4}",
    r"(?=x)y",
    r"(a)\1",
    r"(?(1)a|b)",
    r"a\Kb",
    r"\bword\b",
    r"^https?://\S+$",
    r"[A-Z]{3}\d{2}",
    r"(?>atomic)",
    r"a++",
    r"[\w.-]+@[\w.-]+",
    r"password\s*=\s*\S+",
    r"(?i)admin",
    r"x|y|z",
    r"^$",
    r"a" * 300,
]


def test_pcre_encodable_fraction_report():
    rows = []
    encodable = 0
    for pat in SAMPLE:
        r = compile_pcre(pat, call_kind="search")
        rows.append(
            {
                "pattern": pat[:80],
                "encodable": r.encodable,
                "reason": r.unencodable_reason,
            }
        )
        if r.encodable:
            encodable += 1
    fraction = encodable / len(SAMPLE)
    report = {
        "schema_version": "1",
        "dialect": "pcre",
        "sample_size": len(SAMPLE),
        "encodable": encodable,
        "fraction": fraction,
        "rows": rows,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    assert REPORT.is_file()
    assert 0 <= fraction <= 1
