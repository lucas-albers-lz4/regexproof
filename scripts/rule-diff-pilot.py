#!/usr/bin/env python3
"""Phase 3 shape-5 pilot: discover pairs, run rule_diff, emit report + markdown.

Usage:
  python scripts/rule-diff-pilot.py
  python scripts/rule-diff-pilot.py --require-ground-truth
  python scripts/rule-diff-pilot.py --family RD-github-oauth-token --require-ground-truth

FAILED ground-truth on auto pairs is recorded as FAILED and, without
--require-ground-truth, continues. With --require-ground-truth (CI), a
FAILED or missing ground-truth on any SAT gap is a hard failure.

--family restricts registration/run to one admitted-pair family (Phase 6
property-subset gate). Floor checks are skipped in family mode.
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

from regexproof.compiler.re2 import replay_argv  # noqa: E402
from regexproof.extractors.rule_file import extract_rule_file  # noqa: E402
from regexproof.rule_diff.pairs import (  # noqa: E402
    MIN_ADMITTED_PAIRS,
    _min_literal_span,
    discover_pairs,
    write_jsonl,
)
from regexproof.rule_diff.specs import (  # noqa: E402
    gitleaks_rule_patterns,
    load_canonical_specs,
    reject_rule_derived_r1,
)
from regexproof.schemas import (  # noqa: E402
    admitted_pair_schema,
    rule_diff_report_schema,
)
from regexproof.rule_diff.pilot_runner import (  # noqa: E402
    Shape5PairConfig,
    load_harness,
    register_shape5_pair,
)
from regexproof.rule_diff.timeout_gate import (  # noqa: E402
    fail_message,
    timeout_gate,
)

TOML = ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml"
SPECS = ROOT / "pilots" / "gitleaks" / "canonical_specs" / "catalog.json"
OUT = ROOT / "properties" / "generated"
TIMEOUT_MS = 15000
# Named exceptions only — empty means zero timeouts required (#186).
TIMEOUT_ALLOWLIST: frozenset[str] = frozenset()


def _length_bounds(pattern: str) -> tuple[int, int]:
    """Pin a tight length window for Z3 (fullmatch-style gap queries).

    Span estimate can over-count groups/alternation; keep slack below the floor.
    """
    span = _min_literal_span(pattern)
    if span <= 0:
        return 1, 48
    lo = max(1, span - 12)
    hi = min(96, span + 8)
    if lo > hi:
        lo, hi = 1, min(96, max(span, 48))
    return lo, hi


def _load_harness():
    return load_harness()


def _go_re2(pattern: str, flags: str, s: str) -> bool:
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

    go = "unknown"
    try:
        go = subprocess.check_output(["go", "version"], text=True, shell=False).strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    return {
        "python": platform.python_version(),
        "z3": z3.get_version_string(),
        "go": go,
    }


def _emit_extractor_jsonl() -> Path:
    source = TOML.read_text(encoding="utf-8")
    recs = extract_rule_file(
        source,
        repo="gitleaks/gitleaks",
        file="pilots/gitleaks/config/gitleaks.toml",
        dialect="re2",
    )
    path = OUT / "gitleaks_extractor.jsonl"
    write_jsonl(path, recs)
    return path


def _register_pair(harness, pair: dict, *, require_gt: bool) -> None:
    def gt(p: dict, w: dict) -> bool:
        s = w.get("s")
        if not isinstance(s, str):
            return False
        return _go_re2(p["r2"]["pattern"], p["r2"]["flags"], s) and not _go_re2(
            p["r1"]["pattern"], p["r1"]["flags"], s
        )

    def domain_fn(p: dict, lo: int, hi: int) -> str:
        return (
            f"len(s) in [{lo},{hi}]; dialect=re2; solver_call_kind=fullmatch; "
            f"site_call_kind={p['call_kind']}"
        )

    register_shape5_pair(
        harness,
        pair,
        cfg=Shape5PairConfig(
            dialect_r1=pair["r1"]["dialect"],
            dialect_r2=pair["r2"]["dialect"],
            timeout_ms=TIMEOUT_MS,
            length_bounds=_length_bounds,
            ground_truth=gt,
            domain_fn=domain_fn,
        ),
    )
    _ = require_gt


def _redact_witness(witness: object) -> object:
    """Avoid committing solver strings that match secret scanners (token-shaped).

    Idempotent: already-redacted placeholders are left unchanged.
    """
    if witness is None:
        return None
    if isinstance(witness, dict):
        out = {}
        for k, v in witness.items():
            if isinstance(v, str) and v.startswith("<redacted"):
                out[k] = v
            elif isinstance(v, str) and len(v) >= 8:
                out[k] = f"<redacted len={len(v)}>"
            else:
                out[k] = v
        return out
    if isinstance(witness, str) and witness.startswith("<redacted"):
        return witness
    return "<redacted>"


def _write_markdown(report: dict, pairs: list[dict]) -> None:
    lines = [
        "---",
        "schema_version: \"1\"",
        "pilot: gitleaks",
        f"admitted_pairs: {report['admitted_pairs']}",
        f"timeout_rate: {report['timeout_rate']}",
        "shape: 5",
        "---",
        "",
        "# gitleaks shape-5 rule_diff (encodable subset)",
        "",
    ]
    by_id = {p["pair_id"]: p for p in pairs}
    for res in sorted(report["results"], key=lambda r: r["pair_id"]):
        if res.get("kind") != "rule_diff":
            continue
        pair = by_id.get(res["pair_id"], {})
        r2 = pair.get("r2", {})
        lines.extend(
            [
                f"## {res['pair_id']}",
                "",
                f"- regex_id: `{res['regex_id']}`",
                f"- result: `{res['result']}`",
                f"- ground_truth_status: `{res['ground_truth_status']}`",
                f"- domain: {res['declared_domain']}",
                f"- wall_ms: {res['wall_ms']}",
                "",
                "### Pattern",
                "",
                f"- R1: `{pair.get('r1', {}).get('pattern', '')}`",
                f"- R2: `{r2.get('pattern', '')}`",
                "",
                "### Context",
                "",
                f"- site: `{r2.get('site', '')}`",
                f"- rule_id: `{r2.get('rule_id', '')}`",
                "",
                "### Witness",
                "",
                f"```json\n{json.dumps(res.get('witness'), sort_keys=True)}\n```",
                "",
                "### Ground-truth",
                "",
                f"{res['ground_truth_status']}",
                "",
            ]
        )
    (OUT / "gitleaks.md").write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--require-ground-truth", action="store_true")
    ap.add_argument(
        "--require-domain",
        action="store_true",
        help="accepted for CLI parity with the proof job. INERT for this "
        "pilot: check_domain_coverage covers kind=property and "
        "counterexample_finder only, and this registry is rule_diff gaps + "
        "mutation guards — see the check_domain_coverage(require=...) call "
        "in main().",
    )
    ap.add_argument(
        "--family",
        default=None,
        help="Run only this admitted-pair family (Phase 6 subset)",
    )
    args = ap.parse_args(argv)

    OUT.mkdir(parents=True, exist_ok=True)
    _emit_extractor_jsonl()

    specs = load_canonical_specs(SPECS)
    violations = reject_rule_derived_r1(specs, rule_patterns=gitleaks_rule_patterns(TOML))
    if violations:
        print("FAIL independent-spec integrity:")
        for v in violations:
            print(" ", v)
        return 1

    discovered = discover_pairs(toml_path=TOML, specs_path=SPECS, file=str(TOML.relative_to(ROOT)))
    if args.family:
        admitted = [p for p in discovered["admitted_pairs"] if p["family"] == args.family]
        if not admitted:
            print(f"FAIL unknown or non-admitted rule_diff family: {args.family}")
            print(
                "known:",
                ", ".join(sorted({p['family'] for p in discovered['admitted_pairs']})),
            )
            return 1
        discovered = {
            **discovered,
            "admitted_pairs": admitted,
            "admitted_count": len(admitted),
            "floor_ok": True,
        }
    else:
        write_jsonl(OUT / "gitleaks_admitted_pairs.jsonl", discovered["admitted_pairs"])
        write_jsonl(OUT / "gitleaks_dropped_pairs.jsonl", discovered["dropped_pairs"])
        (OUT / "gitleaks_pair_discovery.json").write_text(
            json.dumps(
                {
                    k: discovered[k]
                    for k in (
                        "schema_version",
                        "admitted_count",
                        "dropped_count",
                        "min_admitted_pairs",
                        "max_len",
                        "floor_ok",
                    )
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        if not discovered["floor_ok"]:
            print(
                f"FAIL admitted_pairs floor: {discovered['admitted_count']} < {MIN_ADMITTED_PAIRS}"
            )
            return 1

    for pair in discovered["admitted_pairs"]:
        jsonschema.validate(pair, admitted_pair_schema())

    harness = _load_harness()
    # Clear any leftover registry from import side effects
    harness.REGISTRY.clear()

    for pair in discovered["admitted_pairs"]:
        _register_pair(harness, pair, require_gt=args.require_ground_truth)
        if args.require_ground_truth:
            gap_name = f"{pair['family']}-gap"
            if harness.REGISTRY[gap_name].get("ground_truth") is None:
                print(f"FAIL --require-ground-truth: {gap_name} has no callback")
                return 1

    cov = harness.check_mutation_coverage()
    if cov:
        print("FAIL mutation coverage:", cov)
        return 1

    # P1 (#425): --require-domain is accepted for CLI parity with the proof
    # job, but the check is INERT here — check_domain_coverage covers
    # kind=property and counterexample_finder only, and this registry holds
    # rule_diff gaps + mutation guards (nothing to check). Wired anyway so a
    # future property-kind addition to this pilot cannot silently skip the
    # domain gate.
    if harness.check_domain_coverage(require=args.require_domain):
        print("FAIL --require-domain: a registered property declares no input_domain",
              file=sys.stderr)
        return 1

    results = []
    gt_failed = 0
    gap_names = [n for n, e in harness.REGISTRY.items() if e["kind"] == "rule_diff"]
    pair_by_family = {p["family"]: p for p in discovered["admitted_pairs"]}

    for name in sorted(harness.REGISTRY):
        entry = harness.REGISTRY[name]
        t0 = time.perf_counter()
        # GT is enforced below when --require-ground-truth; harness flag stays
        # False so we can record FAILED status before deciding exit code.
        res = harness.run_one(name, entry, require_ground_truth=False)
        wall = (time.perf_counter() - t0) * 1000
        family = entry["family"]
        pair = pair_by_family.get(family, {})
        gt_status = "N/A"
        if res.get("result") == "timeout":
            outcome = "timeout"
            ok = False
        elif res.get("result") == "sat" and entry["kind"] == "rule_diff":
            outcome = "sat"
            if args.require_ground_truth and entry.get("ground_truth") is None:
                print(f"FAIL --require-ground-truth but no callback: {name}")
                return 1
            if entry.get("ground_truth") and res.get("witness") is not None:
                try:
                    gt_ok = bool(entry["ground_truth"](res["witness"]))
                    gt_status = "PASS" if gt_ok else "FAILED"
                except Exception:
                    gt_status = "FAILED"
            elif args.require_ground_truth:
                print(f"FAIL --require-ground-truth missing witness for SAT: {name}")
                return 1
            if gt_status == "FAILED":
                gt_failed += 1
            # SAT gap is a finding, not a harness failure.
            ok = True
        elif res.get("result") == "unsat":
            outcome = "unsat"
            gt_status = "N/A"
            # UNSAT = no gap in declared bound (valid).
            ok = True if entry["kind"] == "rule_diff" else res.get("ok", False)
        else:
            outcome = res.get("result") or "not_proven_bounded"
            ok = res.get("ok", False)

        results.append(
            {
                "name": name,
                "regex_id": pair.get("regex_id_r2") or "",
                "pair_id": pair.get("pair_id") or family,
                "file": (pair.get("r2") or {}).get("site"),
                "line": None,
                "pattern": (pair.get("r2") or {}).get("pattern") or "",
                "shape": 5,
                "result": outcome if outcome != "unknown" else "not_proven_bounded",
                "declared_domain": entry["domain"],
                "ground_truth_status": gt_status,
                "wall_ms": round(wall, 3),
                "schema_version": "1",
                "family": family,
                "kind": entry["kind"],
                "ok": ok,
                "witness": _redact_witness(res.get("witness")),
            }
        )

    admitted = discovered["admitted_count"]
    # timeouts counted only on rule_diff base props (results list includes guards)
    rule_diff_rows = [r for r in results if r.get("kind") == "rule_diff"]
    timeout_gate_ok, timeouts, timeout_rate, bad_timeouts = timeout_gate(
        rule_diff_rows,
        allowlist=TIMEOUT_ALLOWLIST,
    )

    report = {
        "schema_version": "1",
        "pilot": "gitleaks",
        "admitted_pairs": admitted,
        "timeouts": timeouts,
        "timeout_rate": timeout_rate,
        "floor_ok": True,
        "timeout_gate_ok": timeout_gate_ok,
        "engine_versions": _engine_versions(),
        "results": results,
        "mutation_coverage_ok": True,
        "gap_properties": len(gap_names),
    }
    if args.family:
        # Subset mode: do not clobber the full Phase-3 report artifacts.
        out_subset = OUT / f"gitleaks_rule_diff_subset_{args.family}.json"
        jsonschema.validate(report, rule_diff_report_schema())
        out_subset.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        jsonschema.validate(report, rule_diff_report_schema())
        (OUT / "gitleaks_rule_diff_report.json").write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        _write_markdown(report, discovered["admitted_pairs"])

    print(
        f"admitted={admitted} timeouts={timeouts} timeout_rate={timeout_rate:.3f} "
        f"gate_ok={timeout_gate_ok}"
    )
    if not timeout_gate_ok:
        print(fail_message(bad_timeouts, timeouts))
        return 1

    # Mutation guards must pass (ok)
    for r in results:
        if r["kind"] == "mutation_guard" and not r["ok"]:
            # timeout on guard counts against soft fail — treat as failure
            if r["result"] == "timeout":
                print(f"FAIL mutation guard timeout: {r['name']}")
                return 1
            print(f"FAIL mutation guard: {r['name']} result={r['result']}")
            return 1

    if args.require_ground_truth and gt_failed:
        print(
            f"FAIL --require-ground-truth: {gt_failed} SAT gap(s) with "
            "ground_truth_status=FAILED"
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
