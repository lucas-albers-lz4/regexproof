#!/usr/bin/env python3
"""Phase 4: three shape-5 rule_diff families with declared pair semantics.

Families:
  1. gitleaks↔trufflehog cross-scanner (fixture pairs, same detector intent)
  2. IDS old↔new signature evolution (fixture adjacent)
  3. CRS adjacent-tag (fold #44 — existing crs_rule_diff artifacts)

Writes ``properties/generated/phase4_rule_diff_families.json`` (+ markdown).
"""

from __future__ import annotations

import hashlib
import json
import platform
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.rule_diff.encode import shape5_constraints  # noqa: E402

OUT = ROOT / "properties" / "generated"
TIMEOUT_MS = 10000


def _fp() -> str:
    h = hashlib.sha256()
    for p in sorted((ROOT / "regexproof" / "compiler").rglob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


def _run_gap(r1: str, r2: str, *, dialect: str, flags: str = "") -> dict:
    c1 = compile_pattern(r1, flags, dialect, "search", max_length=48)
    c2 = compile_pattern(r2, flags, dialect, "search", max_length=48)
    if not (c1.encodable and c2.encodable):
        return {
            "result": "skipped",
            "reason": f"unencodable r1={c1.unencodable_reason} r2={c2.unencodable_reason}",
        }
    constraints, bad, s = shape5_constraints(
        c1.mirror, c2.mirror, min_len=1, max_len=32
    )
    solver = z3.Solver()
    solver.set("timeout", TIMEOUT_MS)
    for c in constraints:
        solver.add(c)
    solver.add(bad)
    t0 = time.perf_counter()
    check = solver.check()
    wall = int((time.perf_counter() - t0) * 1000)
    if check == z3.sat:
        model = solver.model()
        witness = str(model[s]).strip('"')
        return {"result": "sat", "witness": witness, "wall_ms": wall}
    if check == z3.unsat:
        return {"result": "unsat", "witness": None, "wall_ms": wall}
    return {"result": "timeout", "witness": None, "wall_ms": wall}


def _gt_python(r1: str, r2: str, witness: str) -> dict:
    return {
        "engine": "python.re",
        "r1_match": bool(re.search(r1, witness)),
        "r2_match": bool(re.search(r2, witness)),
        "status": (
            "reproduced"
            if (not re.search(r1, witness)) and re.search(r2, witness)
            else "failed"
        ),
        "witness_redacted": f"<redacted len={len(witness)}>",
    }


def family_gitleaks_trufflehog() -> dict:
    r1 = r"AKIA[0-9A-Z]{16}"
    r2 = r"(?:AKIA|ASIA)[0-9A-Z]{16}"
    gap = _run_gap(r1, r2, dialect="re2")
    gt = None
    if gap.get("result") == "sat" and gap.get("witness"):
        gt = _gt_python(r1, r2, gap["witness"])
    return {
        "family": "gitleaks-trufflehog-cross-scanner",
        "pair_kind": "cross_scanner",
        "r1_provenance": "gitleaks-like AWS key prefix (fixture)",
        "r2_provenance": "trufflehog-like widened AWS key prefixes (fixture)",
        "mapping_rationale": "same detector intent: cloud access-key id shape",
        "dialect": "re2",
        "call_kind": "search",
        "domain": "len(s)∈[1,32] ascii",
        "ground_truth_engine": "python.re",
        "mutation_guard": "narrow-R2 / widen-R1 registered in rule-diff-pilot style",
        "gap": {k: v for k, v in gap.items() if k != "witness"},
        "ground_truth": gt,
    }


def family_ids_evolution() -> dict:
    r1 = r"^GET\s+/"
    r2 = r"^(?:GET|POST)\s+/"
    gap = _run_gap(r1, r2, dialect="pcre")
    gt = None
    if gap.get("result") == "sat" and gap.get("witness"):
        gt = _gt_python(r1, r2, gap["witness"])
    return {
        "family": "ids-sig-evolution",
        "pair_kind": "version_diff",
        "r1_provenance": "IDS sample older GET-only HTTP method gate",
        "r2_provenance": "IDS sample newer GET|POST method gate",
        "mapping_rationale": "same sid family / adjacent signature revision",
        "dialect": "pcre",
        "call_kind": "search",
        "domain": "len(s)∈[1,32]",
        "ground_truth_engine": "python.re (pcre2 when helper present)",
        "mutation_guard": "required in harness registration",
        "gap": {k: v for k, v in gap.items() if k != "witness"},
        "ground_truth": gt,
    }


def family_crs_fold_44() -> dict:
    report_path = OUT / "crs_rule_diff_report.json"
    triage = ROOT / "properties" / "triage" / "coreruleset_rule_diff.ndjson"
    existing = None
    if report_path.is_file():
        existing = json.loads(report_path.read_text(encoding="utf-8"))
    return {
        "family": "crs-adjacent-tag",
        "pair_kind": "version_diff+sibling_family",
        "r1_provenance": "coreruleset older tag (rule-derived R1 per crs_pairs)",
        "r2_provenance": "coreruleset newer tag",
        "mapping_rationale": "fold issue #44 private_first SAT gaps; see SECURITY.md",
        "dialect": "pcre",
        "call_kind": "search/fullmatch-mirror",
        "domain": "len(s)∈[1,96]",
        "ground_truth_engine": "helpers/pcre2",
        "mutation_guard": "crs_rule_diff_pilot mutation guards",
        "issue_44_fold": "retain private_first; do not auto-publish upstream",
        "artifact": str(report_path.relative_to(ROOT)) if report_path.is_file() else None,
        "triage": str(triage.relative_to(ROOT)) if triage.is_file() else None,
        "existing_report_summary": {
            "admitted_pairs": (existing or {}).get("admitted_pairs"),
            "path": str(report_path.relative_to(ROOT)) if report_path.is_file() else None,
        },
    }


def main() -> int:
    families = [
        family_gitleaks_trufflehog(),
        family_ids_evolution(),
        family_crs_fold_44(),
    ]
    report = {
        "schema_version": "1",
        "phase": 4,
        "compiler_fingerprint": _fp(),
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "phase3_artifacts_required": [
            "phase3_delta_table.json",
            "phase3_decision_matrix.json",
            "gitleaks_residual_abc.json",
        ],
        "families": families,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "phase4_rule_diff_families.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [
        "# Phase 4 rule_diff families",
        "",
        "| Family | Kind | Gap result | Ground truth |",
        "|---|---|---|---|",
    ]
    for f in families:
        gap = f.get("gap") or {}
        gt = f.get("ground_truth") or {}
        lines.append(
            f"| {f['family']} | {f['pair_kind']} | {gap.get('result', 'n/a')} | "
            f"{gt.get('status', f.get('issue_44_fold', 'see artifact'))} |"
        )
    (OUT / "phase4_rule_diff_families.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(families)} families → properties/generated/phase4_rule_diff_families.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
