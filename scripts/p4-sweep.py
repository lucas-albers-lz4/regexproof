#!/usr/bin/env python3
"""Phase 4 corpus sweep (P4, #220): classify every stock-unknown property
into the four explicit buckets and publish the report + versioned manifest.

Run: python scripts/p4-sweep.py            (NOODLER must point at the pinned
                                            binary for a full sweep)
     NOODLER=/path/to/z3-noodler python scripts/p4-sweep.py
The absent-binary environment is recorded honestly (still-unknown), never
silently skipped.

REPRODUCIBILITY (luna r1 on #234):
- the COMMITTED manifest is consumed and verified (repo-relative paths +
  commit == HEAD) before anything runs;
- the stock-unknown inventory is DERIVED from the committed Phase-1 matrix
  (rows with stock=unknown), and the sweep asserts coverage of exactly that
  set — a newly added stock-unknown class fails the assertion;
- the U9 decision artifact (u9-decision.md) is consumed, not re-decided;
- a non-empty unexplained-triage list FAILS the run (exit 1).

Outputs (committed):
  sweep/harness-backends/p4/corpus-manifest.json  (commit + repo-relative paths + sha256)
  sweep/harness-backends/p4/sweep.json            (per-property evidence)
  sweep/harness-backends/p4/sweep-report.md       (the published report)
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import (Concat, Contains, InRe, Length, Range, Re, Star, String,  # noqa: E402
                StringVal, Union)

from regexproof.harness import core  # noqa: E402
from regexproof.harness.sweep import (build_manifest, classify,  # noqa: E402
                                      corpus_commit, d10_decision,
                                      divergence_rate, metric8,
                                      render_report, triage_audit,
                                      u9_publication, verify_manifest)

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "sweep" / "harness-backends" / "p4"
MATRIX_JSON = HERE / "sweep" / "harness-backends" / "p1-baseline" / "matrix.json"
U9_DECISION = HERE / "sweep" / "harness-backends" / "p1-baseline" / "u9-decision.md"


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


def derive_stock_unknown_inventory() -> list[str]:
    """Derive the stock-unknown inventory from the COMMITTED Phase-1 matrix
    (rows with stock == 'unknown') — the sweep covers exactly this set."""
    rows = json.loads(MATRIX_JSON.read_text())
    names = [r["property"] for r in rows if r.get("stock") == "unknown"]
    return sorted(names)


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
    commit = corpus_commit(HERE, corpus_files())
    print(f"corpus commit: {commit}")

    # 1) CONSUME the committed manifest: verify against disk + corpus-commit
    #    match (the corpus commit is stable — the sweep does not modify the
    #    corpus, so committing the refreshed manifest does NOT invalidate it).
    committed = OUT / "corpus-manifest.json"
    if committed.is_file():
        cm = json.loads(committed.read_text())
        problems = verify_manifest(cm, HERE)
        if problems:
            print("committed manifest problems:\n - " + "\n - ".join(problems),
                  file=sys.stderr)
            return 1
        if cm.get("commit") != commit:
            print(f"committed manifest pins {cm.get('commit')} but the corpus "
                  f"commit is {commit} — re-run to refresh", file=sys.stderr)
            return 1
    manifest = build_manifest(commit, corpus_files(), HERE)

    # 2) DERIVE the inventory from the committed matrix + assert coverage
    inventory = derive_stock_unknown_inventory()
    fns = stock_unknown_fns()
    missing = [n for n in inventory if n not in fns]
    extra = [n for n in fns if n not in inventory]
    if missing or extra:
        print(f"inventory mismatch — matrix: {inventory}, sweep: "
              f"{sorted(fns)} (missing={missing} extra={extra})",
              file=sys.stderr)
        return 1

    # 3) run + classify
    records = []
    for name in inventory:
        fn, expect_unsat = fns[name]
        entry = {
            "fn": fn, "domain": "ascii", "expect_unsat": expect_unsat,
            "timeout_ms": 30000, "ground_truth": None, "kind": "property",
            "family": name.split("-")[0], "input_domain": "ascii",
            "call_kind": None, "backend": "noodler", "route": "mirror",
        }
        result = core.run_one(name, entry)
        c = classify(result)
        rec = {
            "name": name,
            "result": result,
            "classification": c.to_record(),
            "cross_check_reason": result.get("cross_check_reason"),
            "triage": None,  # no disagreements on the measured set
        }
        records.append(rec)
        print(f"{name:18s} -> {c.bucket:22s} "
              f"(noodler={c.noodler_verdict} "
              f"cvc5={rec['cross_check_reason'] or c.cross_check_verdict or '-'})")

    m8 = metric8([r["result"] for r in records])
    d10 = divergence_rate([r["result"] for r in records])
    d10dec = d10_decision(d10)
    audit = triage_audit(records, manifest, HERE)
    # U9 evidence derived from the COMMITTED Phase-1 pilot artifact (the six
    # fwlive patterns + their mirror comparisons — never hardcoded)
    pilot = json.loads(
        (HERE / "sweep" / "harness-backends" / "p1-baseline" /
         "ecma-pilot.json").read_text()
    )
    mirror_divergences = sum(
        len(p.get("real_vs_mirror") or []) for p in pilot
    )
    evidence = {
        "divergence": d10,
        "d10_decision": d10dec["decision"],
        "fwlive_patterns": [p.get("pattern") for p in pilot],
        "fwlive_pattern_count": len(pilot),
        "pilot_mirror_divergences": mirror_divergences,
        "measured_matrix_rows": len(json.loads(MATRIX_JSON.read_text())),
    }
    # The reopen trigger is an EXPLICIT input (`--reopen-trigger`): the sweep
    # is not a pattern-discovery tool (D14/Phase 5 is); a NEW fwlive pattern
    # lacking a standard-encoding mirror is detected there and passed here.
    u9 = u9_publication(U9_DECISION,
                        reopen_trigger_hit="--reopen-trigger" in sys.argv,
                        evidence=evidence)
    report = render_report(manifest, records, m8, d10, d10dec, audit, u9)

    # 4) S14 enforcement: any unexplained disagreement FAILS the sweep
    if audit["unexplained"]:
        print(f"UNEXPLAINED DISAGREEMENTS: {audit['unexplained']} — sweep "
              "FAILS (S14)", file=sys.stderr)
        return 1

    (OUT / "corpus-manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    (OUT / "sweep.json").write_text(json.dumps(records, indent=1, default=str) + "\n")
    (OUT / "sweep-report.md").write_text(report)
    print(f"\nwrote {OUT}/sweep-report.md (+ manifest, + sweep.json)")
    print(f"buckets: {[r['classification']['bucket'] for r in records]}")
    print(f"D10: {d10dec['decision']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
