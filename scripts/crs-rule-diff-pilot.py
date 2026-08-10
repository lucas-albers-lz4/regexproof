#!/usr/bin/env python3
"""CRS shape-5 rule_diff pilot (dogfooding wave Phase 2).

Usage:
  python scripts/crs-rule-diff-pilot.py \\
    --older-rules /path/to/coreruleset-v4.27.0/rules \\
    --newer-rules /path/to/coreruleset-v4.28.0/rules \\
    --require-ground-truth

CRS adapter: R1 for version-diff pairs is rule-derived (prior tag). See
regexproof.rule_diff.crs_pairs module docstring — do not apply
reject_rule_derived_r1 here.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


import jsonschema  # noqa: E402

from regexproof.compiler.pcre import replay_argv  # noqa: E402
from regexproof.rule_diff.crs_pairs import discover_crs_pairs  # noqa: E402
from regexproof.rule_diff.pairs import _min_literal_span, write_jsonl  # noqa: E402
from regexproof.schemas import admitted_pair_schema, rule_diff_report_schema  # noqa: E402
from regexproof.rule_diff.pilot_runner import (  # noqa: E402
    Shape5PairConfig,
    load_harness,
    register_shape5_pair,
)
from regexproof.rule_diff.timeout_gate import fail_message, timeout_gate  # noqa: E402

OUT = ROOT / "properties" / "generated"
TRIAGE = ROOT / "properties" / "triage"
TIMEOUT_MS = 15000


def _length_bounds(pattern: str) -> tuple[int, int]:
    span = _min_literal_span(pattern)
    if span <= 0:
        return 1, 48
    # Optional prefixes (e.g. `(?:json\.)?`) inflate span; keep a low floor so
    # short witnesses like `json.cfsid` remain in-bounds.
    lo = 1
    hi = min(96, max(span + 8, 32))
    return lo, hi


def _load_harness():
    return load_harness()


def _pcre2(pattern: str, flags: str, s: str) -> bool:
    proc = subprocess.run(
        replay_argv(pattern, flags),
        input=s,
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0


def _engine_versions() -> dict:
    import z3

    return {
        "python": platform.python_version(),
        "z3": z3.get_version_string(),
        "pcre2_helper": str(ROOT / "helpers" / "pcre2" / "match.py"),
    }


def _register_pair(harness, pair: dict) -> None:
    def gt(p: dict, w: dict) -> bool:
        s = w.get("s")
        if not isinstance(s, str):
            return False
        s = s.replace("\x00", "")
        return _pcre2(p["r2"]["pattern"], p["r2"]["flags"], s) and not _pcre2(
            p["r1"]["pattern"], p["r1"]["flags"], s
        )

    def domain_fn(p: dict, lo: int, hi: int) -> str:
        return (
            f"len(s) in [{lo},{hi}]; dialect=pcre; solver_call_kind=fullmatch; "
            f"adapter={p.get('adapter')}; direction={p.get('direction_label') or p.get('direction')}"
        )

    register_shape5_pair(
        harness,
        pair,
        cfg=Shape5PairConfig(
            dialect_r1="pcre",
            dialect_r2="pcre",
            timeout_ms=TIMEOUT_MS,
            length_bounds=_length_bounds,
            ground_truth=gt,
            domain_fn=domain_fn,
        ),
    )



def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--older-rules", type=Path, required=True)
    ap.add_argument("--newer-rules", type=Path, required=True)
    ap.add_argument("--older-tag", default="v4.27.0")
    ap.add_argument("--newer-tag", default="v4.28.0")
    ap.add_argument("--family", default=None, help="run one admitted family only")
    ap.add_argument("--require-ground-truth", action="store_true")
    ap.add_argument("--max-pairs", type=int, default=0, help="0 = all admitted")
    args = ap.parse_args(argv)

    OUT.mkdir(parents=True, exist_ok=True)
    TRIAGE.mkdir(parents=True, exist_ok=True)

    discovered = discover_crs_pairs(
        older_rules=args.older_rules,
        newer_rules=args.newer_rules,
        older_tag=args.older_tag,
        newer_tag=args.newer_tag,
    )
    admitted = discovered["admitted"]
    if args.family:
        admitted = [p for p in admitted if p["family"] == args.family]
    if args.max_pairs:
        # Prefer version_diff pairs first (known SAT surface), then siblings.
        admitted = sorted(
            admitted, key=lambda p: 0 if p.get("pair_kind") == "version_diff" else 1
        )[: args.max_pairs]

    for p in admitted:
        jsonschema.validate(p, admitted_pair_schema())

    write_jsonl(OUT / "crs_admitted_pairs.jsonl", admitted)
    (OUT / "crs_pair_discovery.json").write_text(
        json.dumps(
            {
                k: discovered[k]
                for k in discovered
                if k not in ("admitted", "dropped", "min_literal_span_hint")
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    harness = _load_harness()
    harness.REGISTRY.clear()
    for pair in admitted:
        _register_pair(harness, pair)

    rows = []
    gt_failed = 0
    sat_gaps = 0
    for name, entry in list(harness.REGISTRY.items()):
        res = harness.run_one(name, entry, require_ground_truth=False)
        # Reinterpret rule_diff: SAT = gap finding (ok), UNSAT = no gap in bound (ok)
        if entry.get("kind") == "rule_diff":
            if res.get("result") == "sat":
                sat_gaps += 1
                res["ok"] = True
                res["classification"] = "gap"
                if entry.get("ground_truth") and res.get("witness") is not None:
                    try:
                        gt_ok = bool(entry["ground_truth"](res["witness"]))
                    except Exception as exc:  # noqa: BLE001
                        gt_ok = False
                        res["ground_truth_error"] = str(exc)
                    res["ground_truth_status"] = "reproduced" if gt_ok else "failed"
                    if not gt_ok:
                        gt_failed += 1
                        res["ok"] = False
                elif args.require_ground_truth:
                    res["ground_truth_status"] = "refused-no-callback"
                    gt_failed += 1
                    res["ok"] = False
                else:
                    res["ground_truth_status"] = None
            elif res.get("result") == "unsat":
                res["ok"] = True
                res["classification"] = "no_gap_in_bound"
                res["ground_truth_status"] = None
            else:
                res["ok"] = False
                res["classification"] = res.get("result")
        elif entry.get("kind") == "mutation_guard":
            # harness.run_one already sets ok from expect_unsat
            res["ground_truth_status"] = (
                "mutation-guard-sat-expected"
                if res.get("result") == "sat" and not entry.get("expect_unsat")
                else res.get("ground_truth")
            )
        rows.append(
            {
                "name": name,
                "family": entry.get("family"),
                "kind": entry.get("kind"),
                "result": res.get("result"),
                "ok": res.get("ok"),
                "witness": res.get("witness"),
                "ground_truth_status": res.get("ground_truth_status"),
                "wall_ms": res.get("wall_ms"),
                "domain": entry.get("domain"),
                "classification": res.get("classification"),
                "engine_versions": _engine_versions(),
            }
        )

    if args.require_ground_truth and gt_failed:
        print(f"FAIL --require-ground-truth: {gt_failed} SAT gap(s) failed replay")
        # still write artifacts for triage

    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "corpus": "coreruleset",
        "older_tag": args.older_tag,
        "newer_tag": args.newer_tag,
        "admitted_pairs": len(admitted),
        "sat_gaps": sat_gaps,
        "gt_failed": gt_failed,
        "timeouts": sum(1 for r in rows if r.get("result") == "timeout"),
        "timeout_rate": (
            sum(1 for r in rows if r.get("result") == "timeout") / len(rows)
            if rows
            else 0.0
        ),
        "engine_versions": _engine_versions(),
        "results": [
            {
                "schema_version": "1",
                "regex_id": r["name"],
                "pair_id": r.get("family") or r["name"],
                "shape": 5,
                "result": r["result"]
                if r["result"] in ("sat", "unsat", "timeout")
                else "not_proven_bounded",
                "declared_domain": "ascii",
                "ground_truth_status": {
                    "reproduced": "PASS",
                    "failed": "FAILED",
                    "mutation-guard-sat-expected": "N/A",
                    None: "N/A",
                }.get(r.get("ground_truth_status"), "SKIPPED"),
                "wall_ms": r.get("wall_ms") or 0,
                "family": r.get("family"),
                "kind": r.get("kind"),
                "witness": r.get("witness"),
                "classification": r.get("classification"),
            }
            for r in rows
            if r.get("kind") == "rule_diff"
        ],
        "rows": rows,
    }
    jsonschema.validate(report, rule_diff_report_schema())
    (OUT / "crs_rule_diff_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )

    # Triage NDJSON (facts for P5)
    triage_path = TRIAGE / "coreruleset_rule_diff.ndjson"
    with triage_path.open("w", encoding="utf-8") as fh:
        for r in rows:
            if r.get("kind") != "rule_diff":
                continue
            cls = "artifact"
            if r.get("result") == "sat" and r.get("ground_truth_status") == "reproduced":
                cls = "bypass" if "sibling" in (r.get("family") or "") else "divergence"
            fh.write(
                json.dumps(
                    {
                        "schema_version": "1",
                        "regex_id": r["name"],
                        "kind": "rule_diff",
                        "corpus": "coreruleset",
                        "result": r["result"],
                        "witness": r.get("witness"),
                        "ground_truth_status": r.get("ground_truth_status"),
                        "wall_ms": r.get("wall_ms"),
                        "domain": r.get("domain"),
                        "family": r.get("family"),
                        "disclosure": "private_first",
                        "classification": cls,
                        "engine_versions": r.get("engine_versions"),
                    },
                    sort_keys=True,
                    default=str,
                )
                + "\n"
            )

    md_lines = [
        "# CRS rule_diff report",
        "",
        f"- older: `{args.older_tag}`",
        f"- newer: `{args.newer_tag}`",
        f"- admitted pairs run: {len(admitted)}",
        f"- SAT gaps: {sat_gaps}",
        f"- GT failures: {gt_failed}",
        "",
        "| name | kind | result | gt | classification |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        md_lines.append(
            f"| `{r['name']}` | {r['kind']} | {r['result']} | "
            f"{r.get('ground_truth_status')} | {r.get('classification') or ''} |"
        )
    (OUT / "crs_rule_diff.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(
        f"crs rule_diff: admitted={len(admitted)} sat_gaps={sat_gaps} "
        f"gt_failed={gt_failed}"
    )
    gate_ok, n_timeout, _rate, bad = timeout_gate(
        [r for r in rows if r.get("kind") == "rule_diff"]
    )
    if not gate_ok:
        print(fail_message(bad, n_timeout))
        return 1
    if args.require_ground_truth and gt_failed:
        return 1
    if sat_gaps < 1:
        print("FAIL: need ≥1 verified SAT gap")
        return 1
    # Ensure at least one reproduced GT when flag set
    if args.require_ground_truth:
        reproduced = sum(
            1
            for r in rows
            if r.get("kind") == "rule_diff"
            and r.get("result") == "sat"
            and r.get("ground_truth_status") == "reproduced"
        )
        if reproduced < 1:
            print("FAIL: no PCRE2-reproduced SAT gap")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
