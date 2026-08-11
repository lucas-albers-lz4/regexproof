#!/usr/bin/env python3
"""Phase 4 corpus sweep (P4, #220): classify every stock-unknown property
into the four explicit buckets and publish the report + versioned manifest.

Run: python scripts/p4-sweep.py            (NOODLER must point at the pinned
                                            binary for a full sweep)
     NOODLER=/path/to/z3-noodler python scripts/p4-sweep.py
The absent-binary environment is recorded honestly (still-unknown), never
silently skipped.

Outputs (committed):
  sweep/harness-backends/p4/corpus-manifest.json  (commit + paths + sha256)
  sweep/harness-backends/p4/sweep.json            (per-property evidence)
  sweep/harness-backends/p4/sweep-report.md       (the published report)
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import (Concat, Contains, InRe, Length, Range, Re, Solver, Star,
                String, StringVal, Union)  # noqa: E402

from regexproof.harness import core  # noqa: E402
from regexproof.harness.sweep import (BUCKETS, build_manifest, classify,
                                      divergence_rate, metric8, render_report,
                                      triage_audit, u9_publication,
                                      verify_manifest)  # noqa: E402

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "sweep" / "harness-backends" / "p4"


def stock_unknown_fns():
    """The two documented seq-timeout classes (fact 17 — same definitions as
    the Phase-1 matrix build_extra; NOT in the harness registry)."""
    def p2_len64():
        a = String("a")
        ACTOR_CLS = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"),
                          Re("."), Re("_"), Re("@"), Re("-"))
        wl_re = Concat(ACTOR_CLS, Star(ACTOR_CLS))
        return [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 64], \
            Contains(a, StringVal(" "))

    def p4_monolithic():
        v = String("v")
        ESCAPE_SAFE = Union(Range("\x20", "\x21"), Range("\x23", "\x5b"),
                            Range("\x5d", "\x7e"))
        ESCAPE_ESC = Union(Re("\\\\"), Re('\\"'), Re("\\t"), Re("\\r"),
                           Re("\\n"))
        ESCAPE_TOKENS = Union(ESCAPE_SAFE, ESCAPE_ESC)
        return [InRe(v, Star(ESCAPE_TOKENS)), Length(v) >= 1], \
            Contains(v, StringVal("\t"))

    return {
        "P2-len64": (p2_len64, True),        # expect_unsat
        "P4-monolithic": (p4_monolithic, True),
    }


def corpus_files() -> list[Path]:
    base = HERE / "sweep" / "harness-backends" / "p1-baseline"
    names = ["matrix.json", "MATRIX.md", "PIN.md", "TRIAGE.md",
             "p-gate-table.md", "blocker-probe.md", "r5-cost.md",
             "u9-decision.md"]
    return [base / n for n in names]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # Use the cvc5 wheel when a venv is present (the cross-check leg is real);
    # the worker inherits PYTHONPATH.
    cvc5_sp = Path("/tmp/cvc5venv/lib/python3.13/site-packages")
    if cvc5_sp.is_dir():
        os.environ["PYTHONPATH"] = str(cvc5_sp)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=HERE, capture_output=True, text=True
    ).stdout.strip()
    manifest = build_manifest(commit, corpus_files())
    problems = verify_manifest(manifest)
    if problems:
        print("manifest problems:\n - " + "\n - ".join(problems), file=sys.stderr)
        return 1

    records = []
    for name, (fn, expect_unsat) in sorted(stock_unknown_fns().items()):
        entry = {
            "fn": fn, "domain": "ascii", "expect_unsat": expect_unsat,
            "timeout_ms": 30000, "ground_truth": None, "kind": "property",
            "family": name.split("-")[0], "input_domain": "ascii",
            "call_kind": None, "backend": "noodler",
        }
        result = core.run_one(name, entry)
        c = classify(result)
        rec = {
            "name": name,
            "result": result,
            "classification": c.to_record(),
            "cross_check_reason": result.get("cross_check_reason"),
        }
        records.append(rec)
        print(f"{name:18s} -> {c.bucket:22s} "
              f"(noodler={c.noodler_verdict} "
              f"cvc5={rec['cross_check_reason'] or c.cross_check_verdict or '-'})")

    m8 = metric8([r["result"] for r in records])
    d10 = divergence_rate([r["result"] for r in records])
    audit = triage_audit(records, manifest)
    evidence = {
        "divergence_rate": d10,
        "matrix_measured": {
            "P2-len64": "noodler unsat 17.4ms, cvc5 unsat 12.2ms (agree)",
            "P4-monolithic": "noodler unsat 19.3ms, cvc5 unknown 30s (cvc5 abstain)",
        },
        "all_six_fwlive_patterns_mirror_expressible": True,
    }
    u9 = u9_publication(reopen_trigger_hit=False, evidence=evidence)
    report = render_report(manifest, records, m8, d10, audit, u9)

    (OUT / "corpus-manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    (OUT / "sweep.json").write_text(json.dumps(records, indent=1, default=str) + "\n")
    (OUT / "sweep-report.md").write_text(report)
    print(f"\nwrote {OUT}/sweep-report.md (+ manifest, + sweep.json)")
    print(f"buckets: {[r['classification']['bucket'] for r in records]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
