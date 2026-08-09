#!/usr/bin/env python3
"""Phase 3: build gitleaks residual (a/b/c) + delta + decision matrix.

Baselines (issue #51): gitleaks 18.5% (221 rules, 101 lazy parse-errors);
CRS ~38.4%; current artifacts are the \"after\" numbers.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "properties" / "generated"

# (a) cleared by Phase-2 toolkit fixes; (b) engine limit; (c) policy.
_CLASS = {
    "ok": "encodable",
    "lazy-quantifier": "a",  # historical bucket — strip landed in #45
    "inline-flag": "b",  # residual scoped / global flags not lifted for dialect
    "word-boundary": "b",
    "negated-shorthand": "b",
    "pattern-too-long": "c",
    "lookaround": "b",
    "backref": "b",
    "m-flag": "b",
    "u-flag": "b",
    "internal-anchor": "b",
    "composite-pattern": "b",
    "per-alternative-anchor": "b",
    "unicode-not-literal": "b",
    "unsupported:POSSESSIVE_REPEAT": "b",
    "parse-error:PatternError": "b",
    "unclosed-class": "b",
    "unclosed-group": "b",
    "unsupported-syntax": "b",
    "negated-class": "a",  # #45 lift when applicable
    "bad-range": "b",
}


def _load_fraction(name: str) -> dict:
    return json.loads((OUT / f"{name}_encodable_fraction.json").read_text(encoding="utf-8"))


def gitleaks_residual() -> dict:
    inv = OUT / "gitleaks-inventory.ndjson"
    rows = []
    if inv.is_file():
        for line in inv.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    else:
        # Fall back to reasons histogram only.
        frac = _load_fraction("gitleaks")
        for reason, n in (frac.get("reasons") or {}).items():
            for i in range(int(n)):
                rows.append(
                    {
                        "regex_id": f"synthetic:{reason}:{i}",
                        "compile_reason": reason if reason != "ok" else "ok",
                        "encodable": reason == "ok",
                    }
                )

    classified = []
    buckets = Counter()
    for r in rows:
        reason = r.get("compile_reason") or ("ok" if r.get("encodable") else "unknown")
        if r.get("encodable"):
            cls = "encodable"
        else:
            cls = _CLASS.get(reason, "b")
        buckets[cls] += 1
        classified.append(
            {
                "regex_id": r.get("regex_id"),
                "compile_reason": reason,
                "class": cls,
            }
        )
    unexplained = [c for c in classified if c["class"] not in ("a", "b", "c", "encodable")]
    report = {
        "schema_version": "1",
        "superseded": True,
        "superseded_by": (
            "gitleaks_encodable_fraction.json + trailing_alt_dollar_p3_delta.md "
            "+ trailing_alt_dollar_p4_drift.md (wave #81)"
        ),
        "corpus": "gitleaks",
        "baseline_fraction": 0.185,
        "baseline_note": "issue #51: 221 rules, 101 lazy parse-errors",
        "current": _load_fraction("gitleaks"),
        "class_counts": dict(buckets),
        "unexplained": len(unexplained),
        "records": classified,
        "non_lazy_fix_evidence": {
            "crs_before": 0.384,
            "crs_after": _load_fraction("coreruleset").get("fraction"),
            "note": (
                "CRS lift 38.4%→64.8% includes hex soundness + negated-class/"
                "scoped-flag work beyond lazy-strip; gitleaks residual is mostly "
                "word-boundary (b) after lazy cleared."
            ),
        },
    }
    (OUT / "gitleaks_residual_abc.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def hermes_delta() -> dict:
    """Record hermes-agent before/after from dogfooding + frozen sample IDs."""
    sample = ROOT / "batch" / "corpora" / "hermes_agent" / "sample" / "sites.jsonl"
    frozen_ids: list[str] = []
    if sample.is_file():
        for line in sample.read_text(encoding="utf-8").splitlines():
            if line.strip():
                frozen_ids.append(json.loads(line)["regex_id"])
    report = {
        "schema_version": "1",
        "corpus": "hermes_agent",
        "sites_approx": 1100,
        "baseline_note": "dogfooding wave: case flags, Unicode classes, dynamic compiles",
        "before": {
            "encodable_fraction_approx": 0.42,
            "known_gaps": ["case-flag", "unicode-class", "dynamic-compile", "lookbehind"],
        },
        "after": {
            "encodable_fraction_approx": 0.55,
            "fixes_applied": ["lazy-strip", "scoped-(?i:)", "hex-soundness"],
            "remaining_gaps": ["unicode-class", "dynamic-compile", "variable-width-lookbehind"],
        },
        "frozen_regex_ids_sample": frozen_ids,
        "decision": "go-with-gaps",
        "decision_rule": "re-measure full tree when hermes pin is materialized; sample IDs frozen here",
    }
    (OUT / "hermes_agent_delta.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def decision_matrix() -> dict:
    matrix = json.loads((OUT / "cross_corpus_matrix.json").read_text(encoding="utf-8"))
    decisions = []
    for row in matrix.get("corpora") or []:
        name = row["corpus"]
        dec = row.get("decision")
        frac = row.get("fraction")
        redecision = {
            "corpus": name,
            "decision": dec,
            "fraction": frac,
            "rule": "go iff encodable/sample_size >= 0.30 (inventory_only exempt)",
        }
        if dec == "no-go":
            redecision["phase3_redecision"] = (
                "remain no-go; primary residual is engine-limit (word-boundary / "
                "composite-pattern / internal-anchor) — not a silent skip"
            )
            redecision["next"] = "Phase-2 backlog or dialect rewrite; do not raise pattern-too-long cap"
        elif dec == "go":
            redecision["phase3_redecision"] = "confirm go"
        elif dec == "inventory_only":
            redecision["phase3_redecision"] = "no fraction gate"
        decisions.append(redecision)
    report = {
        "schema_version": "1",
        "superseded": True,
        "superseded_by": (
            "cross_corpus_matrix.json + *_encodable_fraction.json "
            "(PR #80/#89/#90); see phase3_decision_matrix.md"
        ),
        "phase": 3,
        "decisions": decisions,
        "gitleaks_target_met": (_load_fraction("gitleaks").get("fraction") or 0) >= 0.60,
    }
    (OUT / "phase3_decision_matrix.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md = [
        "# Phase 3 decision matrix — SUPERSEDED",
        "",
        "> **Superseded** by `cross_corpus_matrix.md` and each "
        "`*_encodable_fraction.json` (PR #80/#89/#90). Rows below are "
        "historical regenerations only.",
        "",
        "| Corpus | Decision | Fraction | Phase-3 note |",
        "|---|---|---|---|",
    ]
    for d in decisions:
        md.append(
            f"| {d['corpus']} | {d['decision']} | {d.get('fraction')} | "
            f"{d.get('phase3_redecision', d.get('rule'))} |"
        )
    (OUT / "phase3_decision_matrix.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return report


def delta_table() -> dict:
    report = {
        "schema_version": "1",
        "phase": 3,
        "rows": [
            {
                "corpus": "gitleaks",
                "before_fraction": 0.185,
                "after_fraction": _load_fraction("gitleaks").get("fraction"),
                "delta": round(
                    (_load_fraction("gitleaks").get("fraction") or 0) - 0.185, 4
                ),
                "non_lazy_contributor": "CRS/hex+scoped-flag evidence; gitleaks lift dominated by lazy-strip",
            },
            {
                "corpus": "coreruleset",
                "before_fraction": 0.384,
                "after_fraction": _load_fraction("coreruleset").get("fraction"),
                "delta": round(
                    (_load_fraction("coreruleset").get("fraction") or 0) - 0.384, 4
                ),
                "non_lazy_contributor": "hex soundness + negated-class / scoped-flag",
            },
            {
                "corpus": "validatorjs",
                "before_fraction": None,
                "after_fraction": _load_fraction("validatorjs").get("fraction"),
                "delta": None,
                "non_lazy_contributor": "see validatorjs_encodable_fraction.json",
            },
            {
                "corpus": "trufflehog",
                "before_fraction": None,
                "after_fraction": _load_fraction("trufflehog").get("fraction"),
                "decision": "no-go",
            },
            {
                "corpus": "semgrep_rules",
                "before_fraction": None,
                "after_fraction": _load_fraction("semgrep_rules").get("fraction"),
                "decision": "no-go",
            },
            {
                "corpus": "ids_rules",
                "before_fraction": None,
                "after_fraction": _load_fraction("ids_rules").get("fraction"),
                "decision": "go",
            },
        ],
    }
    (OUT / "phase3_delta_table.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def _is_superseded(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        return bool(json.loads(path.read_text(encoding="utf-8")).get("superseded"))
    except json.JSONDecodeError:
        return False


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # Wave #81 / P5: phase-3 decision artifacts are historical. Do not clobber
    # SUPERSEDED stubs or the hand-maintained phase3_decision_matrix.md.
    guarded = [
        OUT / "gitleaks_residual_abc.json",
        OUT / "phase3_decision_matrix.json",
        OUT / "phase3_decision_matrix.md",
    ]
    if any(_is_superseded(p) if p.suffix == ".json" else p.is_file() for p in guarded):
        print(
            "NOTE: phase3 decision artifacts are superseded "
            "(see cross_corpus_matrix.md / *_encodable_fraction.json). "
            "Refusing to overwrite — clear superseded=true to force regen.",
            file=sys.stderr,
        )
        return 0
    g = gitleaks_residual()
    h = hermes_delta()
    d = delta_table()
    m = decision_matrix()
    print(
        f"gitleaks residual unexplained={g['unexplained']} "
        f"target_met={m['gitleaks_target_met']} hermes_ids={len(h['frozen_regex_ids_sample'])} "
        f"delta_rows={len(d['rows'])}"
    )
    return 0 if g["unexplained"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
