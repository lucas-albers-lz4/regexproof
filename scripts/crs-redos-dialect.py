#!/usr/bin/env python3
"""Phase 3: CRS unencodable-feature triage + uncapped ReDoS report.

Usage:
  python scripts/crs-redos-dialect.py --rules batch/corpora/coreruleset/rules
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.batch.compile_records import compile_records
from regexproof.batch.extract import extract_corpus  # noqa: E402
from regexproof.redos.runner import analyze_record  # noqa: E402

OUT = ROOT / "properties" / "generated"

# Routing policy for compiler reject reasons (P3).
ROUTING = {
    "pattern-too-long": {
        "route": "policy",
        "note": (
            "Capacity cap (>256 chars), not a language limit. Policy: keep cap for "
            "interactive Z3 queries; triage long patterns to ReDoS-only / manual review. "
            "See TRAPS #21."
        ),
    },
    "word-boundary": {
        "route": "triage",
        "note": "Genuine stock-Z3 limit (gate-3 \\b direction); ASCII domain declared for CRS.",
    },
    "negated-class": {
        "route": "prove",
        "note": (
            "Encoded via BMP/ASCII range complement (TRAPS #1/#10) when members are "
            "literals/ranges/ASCII shorthands; residual Unicode-word cases still reject."
        ),
    },
    "inline-flag": {
        "route": "prove",
        "note": (
            "Scoped (?i:...) encoded for PCRE/RE2; mid-pattern (?i), (?-i:...), "
            "scoped m/s/x, and ECMA remain rejects."
        ),
    },
    "m-flag": {
        "route": "triage",
        "note": "Multiline ^/$ — rewrite or LOOKBEHIND_REWRITE; never ASCII-approx (TRAPS #22).",
    },
    "u-flag": {
        "route": "triage",
        "note": "ECMA Unicode mode — stock Z3 limit; do not silent-approx (TRAPS #22).",
    },
    "v-flag": {
        "route": "triage",
        "note": "ECMA Unicode-sets mode — stock Z3 limit (TRAPS #22).",
    },
    "stateful": {
        "route": "triage",
        "note": "ECMA g/y/d — lastIndex / indices metadata, not language membership (TRAPS #22).",
    },
    "bad-range": {
        "route": "prove",
        "note": "\\x{} / hex ranges — mostly fixed; residual bad escapes still reject.",
    },
    "parse-error": {
        "route": "prove",
        "note": "Often lazy quantifiers / hex escapes — language-transparent strip candidates.",
    },
    "lookaround": {"route": "triage", "note": "Not expressible in stock Z3."},
    "backref": {"route": "triage", "note": "Not expressible in stock Z3."},
    "negated-unsupported": {
        "route": "triage",
        "note": (
            "ModSecurity !@rx / selector negation — reject before compile "
            "(docs/NEGATION.md); never silent-positive or Z3 Complement()."
        ),
    },
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--rules",
        type=Path,
        default=ROOT / "batch" / "corpora" / "coreruleset" / "rules",
    )
    ap.add_argument("--with-redos", action="store_true", default=True)
    ap.add_argument("--skip-redos", action="store_true")
    args = ap.parse_args(argv)

    if not args.rules.is_dir():
        print(f"FAIL: rules dir missing: {args.rules}", file=sys.stderr)
        return 2

    # Reuse corpus extract via temporary CORPUS path — call extract_modsec path.
    from regexproof.batch.manifests import CORPUS_MANIFESTS

    meta = dict(CORPUS_MANIFESTS["coreruleset"])
    meta["path"] = args.rules
    records = extract_corpus("coreruleset", meta)
    compiled = compile_records(records, lift_inline=True, corpus_slug="coreruleset")
    rows = [pair[0] for pair in compiled]
    compiled.clear()  # C1 fold (luna re-gate 5): release the Z3 ASTs
    rx_only = [c for c in rows if not c.get("selector")]

    reasons = Counter((c.get("compile_reason") or "ok") for c in rx_only)
    triage_rows = []
    for reason, count in sorted(reasons.items(), key=lambda kv: (-kv[1], kv[0])):
        if reason == "ok":
            route = {"route": "prove", "note": "encodable — Z3 property / rule_diff / ReDoS"}
        else:
            route = ROUTING.get(
                reason, {"route": "triage", "note": "unclassified reject — inspect"}
            )
        triage_rows.append(
            {
                "reason": reason,
                "count": count,
                "route": route["route"],
                "note": route["note"],
            }
        )

    pattern_too_long_policy = ROUTING["pattern-too-long"]

    # Noodler probe re-confirmation
    noodler_path = ROOT / "tests" / "fixtures" / "noodler_probe.json"
    noodler = json.loads(noodler_path.read_text(encoding="utf-8"))
    available = False
    error = None
    try:
        import z3

        available = hasattr(z3, "re") and hasattr(z3.re, "from_ecma2020")
        if not available:
            available = hasattr(z3, "from_ecma2020")
    except Exception as exc:  # noqa: BLE001
        error = str(exc)
    noodler_status = {
        "fixture": str(noodler_path.relative_to(ROOT)),
        "available": bool(available),
        "prior_available": noodler.get("available"),
        "error": error or noodler.get("error"),
        "triage_fallback": True,
        "note": "CRS @rx has zero lookarounds; probe is confirmatory",
        "changed": bool(available) != bool(noodler.get("available")),
    }

    redos_rows = []
    if args.with_redos and not args.skip_redos:
        for rec in rows:
            if not rec.get("encodable"):
                continue
            for f in analyze_record(rec, triage=False):
                redos_rows.append(
                    {
                        "regex_id": f.get("regex_id"),
                        "rule_id": rec.get("rule_id"),
                        "site": f.get("site"),
                        "result": f.get("result"),
                        "tool": f.get("tool"),
                        "tool_version": f.get("tool_version"),
                        "severity": f.get("severity"),
                        "pattern": (f.get("pattern") or "")[:120],
                    }
                )

    report = {
        "schema_version": "1",
        "pilot": "coreruleset-redos-dialect",
        "rx_count": len(rx_only),
        "encodable": sum(1 for c in rx_only if c.get("encodable")),
        "unencodable_triage": triage_rows,
        "pattern_too_long_policy": pattern_too_long_policy,
        "noodler_probe": noodler_status,
        "redos": {
            "uncapped": True,
            "count": len(redos_rows),
            "by_result": dict(Counter(r["result"] for r in redos_rows)),
            "rows": redos_rows,
        },
        "engine_versions": {"python": platform.python_version()},
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "crs_unencodable_triage.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "unencodable_triage": triage_rows,
                "pattern_too_long_policy": pattern_too_long_policy,
                "noodler_probe": noodler_status,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (OUT / "crs_redos_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    md = [
        "# CRS ReDoS + dialect triage",
        "",
        f"- @rx sites: {len(rx_only)}",
        f"- encodable: {report['encodable']}",
        f"- ReDoS findings (uncapped): {len(redos_rows)}",
        f"- Noodler available: {noodler_status['available']} (changed={noodler_status['changed']})",
        "",
        "## Unencodable routing",
        "",
        "| reason | count | route | note |",
        "|---|---:|---|---|",
    ]
    for row in triage_rows:
        md.append(
            f"| `{row['reason']}` | {row['count']} | {row['route']} | {row['note']} |"
        )
    md.extend(
        [
            "",
            "## Pattern-too-long policy",
            "",
            pattern_too_long_policy["note"],
            "",
            "## ReDoS PASS/FAIL rows (sample)",
            "",
            "| regex_id | result | tool |",
            "|---|---|---|",
        ]
    )
    for row in redos_rows[:50]:
        md.append(f"| `{row['regex_id']}` | {row['result']} | {row['tool']} |")
    if len(redos_rows) > 50:
        md.append(f"| … | ({len(redos_rows) - 50} more) | |")
    (OUT / "crs_redos_dialect.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    if noodler_status["changed"]:
        print("WARN: Noodler availability changed vs fixture — reassessment needed")
    print(
        f"crs redos/dialect: encodable={report['encodable']}/{len(rx_only)} "
        f"redos={len(redos_rows)} noodler={noodler_status['available']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
