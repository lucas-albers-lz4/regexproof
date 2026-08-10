#!/usr/bin/env python3
"""Coraza (go-re2) ↔ ModSecurity (pcre2) cross-engine rule_diff pilot.

Usage:
  python scripts/cross-engine-rule-diff-pilot.py --require-ground-truth
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


import jsonschema  # noqa: E402
from z3 import Concat, Re, Star  # noqa: E402

from regexproof.batch.disclose import tag_disclosure  # noqa: E402
from regexproof.batch.report import write_ndjson  # noqa: E402
from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.pcre import replay_argv as pcre_replay  # noqa: E402
from regexproof.compiler.re2 import ensure_built, replay_argv as re2_replay  # noqa: E402
from regexproof.rule_diff.cross_engine import (  # noqa: E402
    discover_cross_engine_pairs,
    load_crs_rx_records,
    preflight_crs,
)
from regexproof.rule_diff.encode import shape5_constraints  # noqa: E402
from regexproof.rule_diff.pairs import _min_literal_span  # noqa: E402
from regexproof.schemas import rule_diff_report_schema  # noqa: E402
from regexproof.rule_diff.timeout_gate import fail_message, timeout_gate  # noqa: E402

OUT = ROOT / "properties" / "generated"
TRIAGE = ROOT / "properties" / "triage"
TIMEOUT_MS = 15000
DEFAULT_RULES = ROOT / "batch" / "corpora" / "coreruleset" / "rules"


def _length_bounds(pattern: str) -> tuple[int, int]:
    span = _min_literal_span(pattern)
    lo = 1
    hi = min(64, max(span + 8, 24))
    return lo, hi


def _load_harness():
    import regexproof.harness as harness
    return harness


def _rel_cmd(argv: list[str]) -> list[str]:
    out: list[str] = []
    for a in argv:
        try:
            p = Path(a)
            if p.is_absolute():
                out.append(str(p.resolve().relative_to(ROOT)))
                continue
        except (OSError, ValueError):
            pass
        out.append(a)
    return out


def _match(argv: list[str], s: str) -> tuple[bool, dict[str, Any]]:
    proc = subprocess.run(
        argv,
        input=s,
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0, {
        "cmd": _rel_cmd(argv),
        "returncode": proc.returncode,
        "stdout": (proc.stdout or "")[:200],
        "stderr": (proc.stderr or "")[:200],
    }


def _engine_versions() -> dict[str, Any]:
    import z3

    go = "unknown"
    try:
        go = subprocess.check_output(["go", "version"], text=True, shell=False).strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    go_helper = ensure_built()
    try:
        go_rel = str(Path(go_helper).resolve().relative_to(ROOT))
    except ValueError:
        go_rel = str(go_helper)
    return {
        "python": platform.python_version(),
        "z3": z3.get_version_string(),
        "go": go,
        "pcre2_helper": "helpers/pcre2/match.py",
        "go_re2_helper": go_rel,
    }


def _per_engine_gt(pattern: str, flags: str, witness: str) -> dict[str, Any]:
    """Ground-truth on BOTH engines for a gap witness (pcre match, re2 miss)."""
    pcre_ok, pcre_meta = _match(pcre_replay(pattern, flags), witness)
    re2_ok, re2_meta = _match(re2_replay(pattern, flags), witness)
    # Gap claim: pcre accepts ∧ re2 rejects
    pcre_status = "PASS" if pcre_ok else "FAILED"
    re2_status = "PASS" if (not re2_ok) else "FAILED"
    overall = "PASS" if (pcre_ok and not re2_ok) else "FAILED"
    return {
        "status": overall,
        "pcre2": {
            "status": pcre_status,
            "version": "pcre2-helper",
            "cmd": pcre_meta["cmd"],
            "matched": pcre_ok,
            "replay": pcre_meta,
        },
        "go_re2": {
            "status": re2_status,
            "version": "go-re2-helper",
            "cmd": re2_meta["cmd"],
            "matched": re2_ok,
            "replay": re2_meta,
        },
    }


def _register_pair(harness, pair: dict) -> None:
    prop = harness.prop
    family = pair["family"]
    r1 = pair["r1"]
    r2 = pair["r2"]
    lo, hi = _length_bounds(r2["pattern"])
    r1_c = compile_pattern(
        r1["pattern"], r1["flags"], "re2", "fullmatch", max_length=256
    )
    r2_c = compile_pattern(
        r2["pattern"], r2["flags"], "pcre", "fullmatch", max_length=256
    )
    assert r1_c.encodable and r2_c.encodable

    def gt(w: dict) -> bool:
        s = w.get("s")
        if not isinstance(s, str):
            return False
        s = s.replace("\x00", "")
        evidence = _per_engine_gt(r2["pattern"], r2["flags"], s)
        return evidence["status"] == "PASS"

    domain = (
        f"len(s) in [{lo},{hi}]; R1=re2(Coraza) R2=pcre(ModSec); "
        f"solver_call_kind=fullmatch; adapter={pair.get('adapter')}"
    )

    @prop(
        f"{family}-gap",
        domain,
        expect_unsat=True,
        timeout_ms=TIMEOUT_MS,
        ground_truth=gt,
        kind="rule_diff",
        family=family,
        input_domain="ascii",
        call_kind=pair["call_kind"],
    )
    def _gap():
        constraints, bad, _s = shape5_constraints(
            r1_c.mirror, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    @prop(
        f"{family}-control",
        domain,
        expect_unsat=True,
        timeout_ms=TIMEOUT_MS,
        kind="mutation_guard",
        family=family,
        input_domain="ascii",
        call_kind=pair["call_kind"],
    )
    def _control():
        constraints, bad, _s = shape5_constraints(
            r2_c.mirror, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    narrow_r1 = Concat(Re("\x01"), Star(Re("\x01")))

    @prop(
        f"{family}-widen-R1",
        domain,
        expect_unsat=False,
        timeout_ms=TIMEOUT_MS,
        kind="mutation_guard",
        family=family,
        input_domain="ascii",
        call_kind=pair["call_kind"],
    )
    def _widen_r1():
        constraints, bad, _s = shape5_constraints(
            narrow_r1, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    # Stash patterns for post-run per-engine evidence attachment.
    pair["_compiled"] = {"pattern": r2["pattern"], "flags": r2["flags"]}
    _ = (_gap, _control, _widen_r1)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    ap.add_argument("--require-ground-truth", action="store_true")
    ap.add_argument("--max-pairs", type=int, default=24)
    ap.add_argument("--max-classify", type=int, default=300)
    ap.add_argument("--solve-limit", type=int, default=12)
    args = ap.parse_args(argv)

    ensure_built()
    pre = preflight_crs(args.rules)
    records = load_crs_rx_records(args.rules)
    discovered = discover_cross_engine_pairs(
        records,
        max_pairs=args.max_pairs,
        max_classify=args.max_classify,
    )
    pairs = discovered["admitted_pairs"][: args.solve_limit]

    harness = _load_harness()
    # Fresh registry for this pilot run
    harness.REGISTRY.clear()
    for pair in pairs:
        _register_pair(harness, pair)

    results: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []
    class_counts = dict(discovered["class_counts"])
    class_counts.setdefault("gap", 0)
    class_counts.setdefault("no-gap", 0)
    pair_by_family = {p["family"]: p for p in pairs}

    for name, entry in sorted(harness.REGISTRY.items()):
        if entry["kind"] != "rule_diff":
            continue
        res = harness.run_one(name, entry, require_ground_truth=False)
        if res.get("result") == "sat":
            res["ok"] = True
            res["classification"] = "gap"
        elif res.get("result") == "unsat":
            res["ok"] = True
            res["classification"] = "no-gap"
        pair_id = entry["family"]
        outcome = res.get("classification") or res.get("result")
        if outcome == "gap":
            class_counts["gap"] = class_counts.get("gap", 0) + 1
        elif outcome == "no-gap":
            class_counts["no-gap"] = class_counts.get("no-gap", 0) + 1
        eng_gt = None
        gt_status = "N/A"
        if res.get("result") == "sat" and isinstance(res.get("witness"), dict):
            meta = pair_by_family.get(pair_id, {}).get("_compiled") or {}
            s = res["witness"].get("s")
            if isinstance(s, str) and meta.get("pattern") is not None:
                eng_gt = _per_engine_gt(meta["pattern"], meta.get("flags") or "", s)
                gt_status = eng_gt["status"]
                if args.require_ground_truth and gt_status != "PASS":
                    res["ok"] = False
        row = {
            "regex_id": name,
            "pair_id": pair_id,
            "shape": 5,
            "result": res.get("result"),
            "declared_domain": entry.get("domain") or "",
            "ground_truth_status": gt_status,
            "ground_truth": eng_gt,
            "wall_ms": res.get("wall_ms"),
            "schema_version": "1",
            "family": entry["family"],
            "kind": "rule_diff",
            "result_class": outcome,
            "ok": res.get("ok"),
            "witness": res.get("witness"),
        }
        results.append(row)
        if outcome == "gap":
            findings.append(
                {
                    "schema_version": "1",
                    "regex_id": name,
                    "kind": "rule_diff",
                    "corpus": "coreruleset",
                    "result": "gap",
                    "site": pair_id,
                    "pattern": pair_id,
                    "shape": 5,
                    "ground_truth_status": gt_status,
                    "ground_truth": eng_gt,
                    "detail": {
                        "result_class": "gap",
                        "engines": ["go_re2", "pcre2"],
                        "adapter": "crs_cross_engine_coraza_modsec",
                    },
                }
            )

    # Run mutation guards for coverage (first family)
    mut_ok = True
    if pairs:
        fam = pairs[0]["family"]
        for suffix, expect_sat in (("-control", False), ("-widen-R1", True)):
            name = f"{fam}{suffix}"
            entry = harness.REGISTRY.get(name)
            if not entry:
                continue
            res = harness.run_one(name, entry, require_ground_truth=False)
            if expect_sat and res.get("result") != "sat":
                mut_ok = False
            if (not expect_sat) and res.get("result") == "sat":
                mut_ok = False

    findings = tag_disclosure(findings, corpus="coreruleset")
    timeout_gate_ok, n_timeout, timeout_rate, bad_timeouts = timeout_gate(results)
    report = {
        "schema_version": "1",
        "pilot": "crs_cross_engine_coraza_modsec",
        "admitted_pairs": len(pairs),
        "timeouts": n_timeout,
        "timeout_rate": timeout_rate,
        "floor_ok": len(pairs) >= 1,
        "timeout_gate_ok": timeout_gate_ok,
        "engine_versions": _engine_versions(),
        "preflight": pre,
        "class_counts": class_counts,
        "classified_patterns": discovered["classified"],
        "mutation_guard_ok": mut_ok,
        "findings": len(findings),
        "disclosure": "private_first" if findings else None,
        "results": results,
        "family_contract": {
            "R1": "go-re2 (Coraza engine semantics)",
            "R2": "pcre2 (ModSecurity / CRS native)",
            "provenance": "same CRS rule text @ 55b09f5",
            "dialect_parity": "fullmatch mirrors; site call_kind=search",
            "ground_truth": "per-engine pcre2 + go_re2 replay",
            "mutation_guards": ["control", "widen-R1"],
        },
    }
    OUT.mkdir(parents=True, exist_ok=True)
    TRIAGE.mkdir(parents=True, exist_ok=True)
    report_path = OUT / "crs_cross_engine_rule_diff_report.json"
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    jsonschema.validate(report, rule_diff_report_schema())
    findings_path = OUT / "crs_cross_engine_findings.ndjson"
    write_ndjson(findings_path, findings)
    md = [
        "# CRS cross-engine rule_diff (Coraza↔ModSecurity)",
        "",
        f"- pin: `{pre['head']}`",
        f"- classified: {discovered['classified']}",
        f"- class_counts: `{json.dumps(class_counts, sort_keys=True)}`",
        f"- solved pairs: {len(pairs)}",
        f"- gaps/findings: {len(findings)} (disclosure=private_first)",
        f"- mutation_guard_ok: {mut_ok}",
        "",
        "## Family contract",
        "",
        "```json",
        json.dumps(report["family_contract"], indent=2),
        "```",
        "",
    ]
    (OUT / "crs_cross_engine_rule_diff.md").write_text(
        "\n".join(md) + "\n", encoding="utf-8"
    )
    print(f"wrote {report_path.relative_to(ROOT)}")
    print(f"class_counts={class_counts} findings={len(findings)} mut_ok={mut_ok}")
    if args.require_ground_truth:
        for r in results:
            if r.get("result_class") == "gap":
                gt = r.get("ground_truth") or {}
                if gt.get("status") != "PASS":
                    print("FAIL: gap without dual-engine ground truth", file=sys.stderr)
                    return 1
                if not (
                    isinstance(gt.get("pcre2"), dict)
                    and isinstance(gt.get("go_re2"), dict)
                ):
                    print("FAIL: missing per-engine ground_truth", file=sys.stderr)
                    return 1
    if not mut_ok:
        print("FAIL: mutation guard", file=sys.stderr)
        return 1
    if not timeout_gate_ok:
        print(fail_message(bad_timeouts, n_timeout), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
