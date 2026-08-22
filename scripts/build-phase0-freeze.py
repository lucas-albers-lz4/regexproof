#!/usr/bin/env python3
"""Build the Phase 0 freeze + escape-baseline artifacts (#555 Wave P0).

Outputs (both committed, drift-checked in CI):

- ``properties/generated/phase0_freeze.json`` — the frozen eval protocol:
  dataset snapshot hash, split seed, labels, dedup rules, feature defs,
  score weights, missing-value rules, split algorithm, tie-breaking,
  K=30 frozen, stratified bootstrap units, BCa impl + fallback, confidence
  convention, software/runtime versions, and the committed escape baseline.
- ``properties/generated/escape_baseline.json`` — probe-lifecycle population,
  survivor count, Wilson CI, sample size, date, query, and the FULL
  predeclared escape protocol (H0/H1/test/floor/block-direction).

The dataset snapshot is the committed ``*_gate_decision.json`` population
(n=853); its content hash is computed over the sorted file contents so the
freeze is reproducible on a fresh clone without extra artifacts.

Usage: ``python3 scripts/build-phase0-freeze.py`` (run from the repo root).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"

FREEZE_OUT = GEN / "phase0_freeze.json"
BASELINE_OUT = GEN / "escape_baseline.json"

SPLIT_SEED = 20260822
SPLIT_RATIO = 0.5
K_FROZEN = 30
CONFIDENCE = 0.95
BOOTSTRAP_B = 10000
SIGNIFICANCE = 0.05
WINDOW_DAYS = 7
N_FLOOR = 50

POSITIVE_STATUSES = ("go", "triage-trial")


def load_decision_population() -> list[dict]:
    files = sorted(GEN.glob("*_gate_decision.json"))
    rows = []
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        status = str(d.get("status") or d.get("decision") or "")
        if not status:
            continue
        rows.append(
            {
                "file": f.name,
                "url": d.get("candidate_url"),
                "status": status,
                "payload": d,  # full contents — hashed verbatim (canonical JSON)
            }
        )
    return rows


def snapshot_hash(rows: list[dict]) -> str:
    """Content hash over the FULL canonical JSON of every decision file.

    Hashes each committed decision file's raw parsed contents (filename
    framing + canonical JSON bytes), so ANY mutation — status, url, pin,
    rationale, probe, conditions — changes the hash. This is the
    reproducibility claim the freeze artifact makes."""
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda r: r["file"]):
        h.update(r["file"].encode("utf-8"))
        h.update(b"\x00")
        h.update(json.dumps(r["payload"], sort_keys=True).encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def main() -> int:
    rows = load_decision_population()
    n = len(rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    pos = sum(counts.get(s, 0) for s in POSITIVE_STATUSES)
    rate = pos / n if n else 0.0


    sys.path.insert(0, str(ROOT))
    from regexproof.stats.intervals import wilson_ci

    lo, hi = wilson_ci(pos, n, CONFIDENCE)

    freeze = {
        "schema_version": "1",
        "dataset": {
            "source": "properties/generated/*_gate_decision.json",
            "n": n,
            "positive_statuses": list(POSITIVE_STATUSES),
            "positive_count": pos,
            "positive_rate": round(rate, 6),
            "status_counts": counts,
            "snapshot_sha256": snapshot_hash(rows),
            "snapshot_note": "Committed decision files; archived *.audit-failed.json "
            "excluded by suffix (structural (url,pin) supersession dedup).",
        },
        "split": {
            "algorithm": "stratified_50_50",
            "seed": SPLIT_SEED,
            "ratio": SPLIT_RATIO,
            "strata": ["go", "triage-trial", "no-go"],
            "rule": "train-only imputation + K selection; test-half evaluated "
            "exactly once (AUC flip metric).",
        },
        "eval": {
            "k_frozen": K_FROZEN,
            "k_note": "Frozen a priori — no K search anywhere in Phase 0 code paths.",
            "auc": "bootstrap BCa, B=10000, 95%, percentile fallback",
            "precision_at_k": "exact Clopper-Pearson, descriptive only",
            "flip_rule": "bootstrap difference-distribution CI (v1.5 - v1) "
            "excludes 0, one-sided, AUC-only, no OR alternative",
            "missing_values": "median imputation from TRAIN split only",
            "tie_breaking": "stable: (regex_id, site) lexicographic",
        },
        "escape_baseline": {
            "value": round(rate, 6),
            "n": n,
            "positive_count": pos,
            "wilson_ci_95": [round(lo, 6), round(hi, 6)],
            "computed_at": "2026-08-22",
            "note": "Fixed constant for the shared-gate one-sided z-test; "
            "never re-derived from a live window.",
        },
        "protocol": {
            "escape_test": "one-sided z-test of window rate vs fixed baseline; "
            "null SE = sqrt(b0*(1-b0)/n); fires when p < 0.05",
            "significance": SIGNIFICANCE,
            "n_floor": N_FLOOR,
            "window_days": WINDOW_DAYS,
            "two_windows_rule": "n < floor requires two consecutive 7-day windows",
            "fire_blocks": "#550 Phase 2 scale (shared gate; no low-yield unlock)",
        },
        "determinism": {
            "intervals_library": "regexproof/stats/intervals.py (stdlib, seeded)",
            "bootstrap_seed": SPLIT_SEED,
            "runtime_versions": {
                "python": sys.version.split()[0],
            },
        },
    }

    baseline = {
        "schema_version": "1",
        "population": "probe-lifecycle: all probe outcomes counted (committed "
        "gate-decision artifacts, n=%d)" % n,
        "n": n,
        "survivors": pos,
        "survivor_rate": round(rate, 6),
        "wilson_ci_95": [round(lo, 6), round(hi, 6)],
        "sample_size_note": "n=%d committed decision files; ledger lag "
        "(candidate-ledger rows) is documented sync drift, never a second "
        "population." % n,
        "computed_at": "2026-08-22",
        "query": "properties/generated/*_gate_decision.json with "
        "status in {go, triage-trial}",
        "test": {
            "h0": "window_rate >= baseline",
            "h1": "window_rate < baseline (one-sided, smaller)",
            "implementation": "regexproof.stats.intervals.two_proportion_test",
            "significance": SIGNIFICANCE,
            "n_floor": N_FLOOR,
            "two_windows_rule": "n < floor requires two consecutive 7-day windows",
            "fire_action": "BLOCKS #550 Phase 2 scale; no low-yield unlock",
        },
    }

    FREEZE_OUT.write_text(json.dumps(freeze, indent=2, sort_keys=True) + "\n")
    BASELINE_OUT.write_text(json.dumps(baseline, indent=2, sort_keys=True) + "\n")
    # External whole-file hash anchor (tamper-evident). Regenerated here so CI
    # can drift-check it alongside the artifacts.
    anchor = FREEZE_OUT.with_name(FREEZE_OUT.name + ".sha256")
    anchor.write_text(
        hashlib.sha256(FREEZE_OUT.read_bytes()).hexdigest() + "\n"
    )
    print(f"phase0_freeze.json: n={n} pos={pos} rate={rate:.4f} "
          f"wilson95=[{lo:.4f}, {hi:.4f}]")
    print(f"escape_baseline.json + {anchor.name}: written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
