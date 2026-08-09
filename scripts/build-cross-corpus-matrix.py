#!/usr/bin/env python3
"""Build cross-corpus encodable-fraction matrix for Phase 1 / wave rollups.

Reads ``properties/generated/*_encodable_fraction.json`` and writes
``properties/generated/cross_corpus_matrix.json`` (+ markdown).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "properties" / "generated"

# Stable rollup order: phase-1 pilots → wave-2 → wave-3 → sample testdata.
CORPORA = [
    "gitleaks",
    "validatorjs",
    "coreruleset",
    "trufflehog",
    "detect-secrets",
    "ids_rules",
    "semgrep_rules",
    "yara_rules",
    # Wave-3 rule / library corpora
    "spamassassin",
    "noseyparker",
    "shhgit",
    "dompurify",
    "isemail",
    "email_addresses",
    # Wave-3 full-suite testdata
    "perl_tre",
    "go_regexp_tests",
    "v8_mjsunit",
    # Sample / inventory
    "pcre2_testdata",
    "re2_testdata",
    "cpython_re",
    "busybox",
    "test262",
    "rust_regex",
]

WAVE = "corpus-wave3"
NOTE = "Rollup after Corpus Wave 3 (#117)."


def main() -> int:
    rows = []
    for name in CORPORA:
        path = OUT / f"{name}_encodable_fraction.json"
        if not path.is_file():
            inv = OUT / f"{name}_inventory_only.json"
            if inv.is_file():
                d = json.loads(inv.read_text(encoding="utf-8"))
                rows.append(
                    {
                        "corpus": name,
                        "scope": d.get("scope", "inventory_only"),
                        "decision": "inventory_only",
                        "fraction": None,
                        "encodable": d.get("extracted"),
                        "sample_size": d.get("extracted"),
                        "unclassified_parse_errors": 0,
                        "complete_run": d.get("complete_run"),
                        "corpus_pin": d.get("corpus_pin"),
                        "reasons": d.get("reasons") or {},
                    }
                )
            continue
        d = json.loads(path.read_text(encoding="utf-8"))
        rows.append(
            {
                "corpus": name,
                "scope": d.get("scope"),
                "decision": d.get("decision"),
                "fraction": d.get("fraction"),
                "encodable": d.get("encodable"),
                "sample_size": d.get("sample_size"),
                "unclassified_parse_errors": d.get("unclassified_parse_errors", 0),
                "reasons": d.get("reasons"),
                "corpus_pin": d.get("corpus_pin"),
                "complete_run": d.get("complete_run"),
            }
        )
    report = {
        "schema_version": "1",
        "wave": WAVE,
        "note": NOTE,
        "corpora": rows,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cross_corpus_matrix.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [
        "# Cross-corpus encodable matrix",
        "",
        NOTE,
        "",
        "| Corpus | Decision | Fraction | Encodable | Size | scope | parse-error |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['corpus']} | {r.get('decision')} | {r.get('fraction')} | "
            f"{r.get('encodable')} | {r.get('sample_size')} | "
            f"{r.get('scope')} | {r.get('unclassified_parse_errors')} |"
        )
    (OUT / "cross_corpus_matrix.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(rows)} rows → properties/generated/cross_corpus_matrix.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
