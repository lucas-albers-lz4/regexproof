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

Path = pathlib.Path

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


def load_decision_population(gen: Path | None = None) -> list[dict]:
    files = sorted((gen if gen is not None else GEN).glob("*_gate_decision.json"))
    rows = []
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise SystemExit(
                f"error: {f.name}: unreadable/invalid decision file — the "
                f"frozen population must not silently shrink: {exc}"
            )
        status = str(d.get("status") or d.get("decision") or "")
        if not status:
            raise SystemExit(
                f"error: {f.name}: decision file has neither 'status' nor "
                "'decision' — a population row cannot be silently dropped"
            )
        # Canonical pin: real artifacts carry corpus_pin (top-level) and
        # probe.pin (nested); the eval's join_rows uses the same precedence
        # (Luna r1 #4 — reading top-level pin/probed_pin yields EMPTY pins).
        probe = d.get("probe") if isinstance(d.get("probe"), dict) else {}
        pin = str(d.get("corpus_pin") or probe.get("pin") or "")
        # Chronological recency: decision_date (Luna r1 #5 — lexical SHA
        # order is wrong: a newer commit can have a smaller SHA).
        recency = str(d.get("decision_date") or d.get("updated_at") or "")
        rows.append(
            {
                "file": f.name,
                "url": d.get("candidate_url"),
                "pin": pin,
                "recency": recency,
                "status": status,
                "payload": d,  # full contents — hashed verbatim (canonical JSON)
            }
        )
    # (url, pin) supersession dedup (#560 Wave 3): when a candidate is
    # requeued and re-decided, only the LATEST decision counts for
    # eval/escape counters. "Latest" = the recorded decision_date
    # (chronological), NOT lexical pin order (Luna r1 #5); ties break
    # deterministically by the last file in sort order. URL-less rows are
    # never superseded.
    by_url: dict[str, dict] = {}
    url_less = [r for r in rows if not str(r.get("url") or "")]
    for r in rows:
        url = str(r.get("url") or "")
        if not url:
            continue
        prev = by_url.get(url)
        if prev is not None and (not r["recency"] or not prev["recency"]):
            # CodeRabbit #573: fail CLOSED when the ordering value is absent
            # for a dedup-eligible pair — a silent tie could pick the wrong
            # decision as "latest".
            raise SystemExit(
                f"error: {r['file']}/{prev['file']}: same url {url} but no "
                "decision_date/updated_at to order by — cannot supersede"
            )
        if prev is None or r["recency"] >= prev["recency"]:
            by_url[url] = r
    keep_ids = {id(r) for r in by_url.values()} | {id(r) for r in url_less}
    return [r for r in rows if id(r) in keep_ids]


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


def _score_v15_overlay_definition() -> dict:
    """Pin the score-v1.5 overlay (weights + hash) in the freeze artifact.

    The weights are FROZEN in ``regexproof.mine.score._TREE_OVERLAY_WEIGHTS``
    (#550 Phase 1 / Item II); the freeze records them and a SHA-256 so Wave
    1's offline eval can fail closed if the implementation drifts."""
    import hashlib

    from regexproof.mine.score import _TREE_OVERLAY_WEIGHTS

    canonical = json.dumps(_TREE_OVERLAY_WEIGHTS, sort_keys=True).encode("utf-8")
    return {
        "weights": {k: v for k, v in sorted(_TREE_OVERLAY_WEIGHTS.items())},
        "sha256": hashlib.sha256(canonical).hexdigest(),
        "source": "regexproof.mine.score._TREE_OVERLAY_WEIGHTS",
    }


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
            "excludes 0, one-sided IMPROVEMENT only (lo > 0), AUC-only, "
            "no OR alternative",
            "missing_values": "median imputation from TRAIN split only",
            "tie_breaking": "stable: (regex_id, site) lexicographic",
            "score_v15_overlay": _score_v15_overlay_definition(),
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
            "runtime_versions": "python >= 3.10 (pyproject requires-python); "
            "z3-solver==5.0.0 pinned. Literal interpreter versions are NOT "
            "embedded: they differ across the CI matrix and would break "
            "byte-stable regeneration.",
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
        "test_revision": {
            "date": "2026-08-24",
            "from": "statsmodels.stats.proportion.proportions_ztest with "
            "Wilson continuity-corrected SE (#550 REV-6 named impl)",
            "via": "stdlib null-SE z-test without continuity correction "
            "(Phase 0 / waves, intervals.py before PR #583)",
            "to": "stdlib one-proportion z-test with 1/(2n) continuity "
            "correction toward the null (PR #583)",
            "implementation": "regexproof.stats.intervals.two_proportion_test",
            "effect": "k=3/n=50 vs baseline 121/874: uncorrected just above 0.05 "
            "(p~=0.0541); corrected does not (p~=0.0806). Pinned in "
            "tests/test_intervals.py.",
            "rationale": "Match the predeclared #550 continuity-corrected "
            "oracle. statsmodels' two-proportion wrapper has no "
            "correction parameter -- the corrected oracle is this "
            "stdlib function. Future method changes append here "
            "instead of each operator re-deriving one.",
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
