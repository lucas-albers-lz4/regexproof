#!/usr/bin/env python3
"""Wave 1 (#557): offline eval of score-v1.5 vs score-v1 per the P0 frozen protocol.

Consumes AND VALIDATES the Phase 0 freeze artifact (fails closed on snapshot
hash mismatch). Runs the stratified 50/50 split with the freeze's seed,
scores the untouched test half exactly once with BOTH allocators, and
records the flip decision per the predeclared rule:

    flip iff bootstrap BCa difference-distribution CI (v1.5 - v1) excludes 0,
    one-sided, AUC-only, no OR alternative.

precision@K is exact Clopper-Pearson, DESCRIPTIVE only. v2 is a label
reproduction reference, never validation.

Usage: ``python3 scripts/eval-score-v15.py`` (run from the repo root).
Writes ``properties/generated/score_v15_flip_decision.json``.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"

FREEZE_PATH = GEN / "phase0_freeze.json"
BASELINE_PATH = GEN / "escape_baseline.json"
FLIP_OUT = GEN / "score_v15_flip_decision.json"

POSITIVE = {"go", "triage-trial"}


def load_freeze() -> dict:
    if not FREEZE_PATH.is_file():
        raise SystemExit(f"FATAL: {FREEZE_PATH} missing — run build-phase0-freeze.py")
    return json.loads(FREEZE_PATH.read_text(encoding="utf-8"))


def validate_freeze_snapshot(freeze: dict) -> None:
    """Fail closed on snapshot hash mismatch: the eval's population must be
    the SAME committed population the freeze pinned — including the (url,
    pin) supersession dedup (#560 Wave 3: the freeze counts only the
    latest pin per url)."""
    import hashlib
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bpf", ROOT / "scripts" / "build-phase0-freeze.py",
    )
    bpf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bpf)  # type: ignore[union-attr]
    rows = bpf.load_decision_population(gen=GEN)
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda r: r["file"]):
        h.update(r["file"].encode("utf-8"))
        h.update(b"\x00")
        h.update(json.dumps(r["payload"], sort_keys=True).encode("utf-8"))
        h.update(b"\n")
    if h.hexdigest() != freeze["dataset"]["snapshot_sha256"]:
        raise SystemExit(
            "FATAL: freeze snapshot hash mismatch — the eval population "
            "differs from the Phase 0 frozen population. Regenerate the "
            "freeze first."
        )
    # The frozen score-v1.5 overlay must match the implementation — a drift
    # in the weights would silently change what the eval measures.
    import hashlib

    from regexproof.mine.score import _TREE_OVERLAY_WEIGHTS

    pinned = freeze.get("eval", {}).get("score_v15_overlay")
    if not pinned:
        raise SystemExit(
            "FATAL: freeze has no score_v15_overlay definition — regenerate "
            "build-phase0-freeze.py output (the eval cannot verify the model)."
        )
    canonical = json.dumps(_TREE_OVERLAY_WEIGHTS, sort_keys=True).encode("utf-8")
    impl_hash = hashlib.sha256(canonical).hexdigest()
    if impl_hash != pinned["sha256"]:
        raise SystemExit(
            "FATAL: score-v1.5 overlay hash mismatch — the implementation "
            "drifted from the frozen weights. Re-freeze or fix the weights."
        )
    # The freeze's recorded weight map must itself hash to the anchor — a
    # hand-edited weights map (with a copied sha) would otherwise pass.
    pinned_map = pinned.get("weights")
    if not isinstance(pinned_map, dict):
        raise SystemExit("FATAL: freeze score_v15_overlay.weights is missing")
    pinned_hash = hashlib.sha256(
        json.dumps(pinned_map, sort_keys=True).encode("utf-8")
    ).hexdigest()
    if pinned_hash != pinned["sha256"]:
        raise SystemExit(
            "FATAL: freeze score_v15_overlay.weights does not match its "
            "recorded sha256 — the freeze artifact is inconsistent."
        )


def join_rows(freeze: dict) -> list[dict]:
    """Join decision labels with ledger features by normalized URL. The
    decision population is the SAME deduped one the freeze pinned (#560
    Wave 3: (url, pin) supersession — only the latest pin per url counts
    for eval/escape counters)."""
    import importlib.util
    from regexproof.mine.exclusions import normalize_repo_url
    from regexproof.mine.tree import _repo_slug

    ledger = json.loads((GEN / "candidate-ledger.json").read_text(encoding="utf-8"))
    by_url: dict[str, dict] = {}
    for cand in ledger.get("candidates") or []:
        url = normalize_repo_url(str(cand.get("url") or ""))
        if url:
            by_url[url] = cand

    # Tree features: committed artifact keyed slug -> {pin -> TreeProbeResult}.
    tree_artifact: dict = {}
    tree_path = GEN / "mine-tree-features.json"
    if tree_path.is_file():
        tree_artifact = json.loads(tree_path.read_text(encoding="utf-8")).get(
            "entries", {}
        )

    rows = []
    spec = importlib.util.spec_from_file_location(
        "bpf", ROOT / "scripts" / "build-phase0-freeze.py",
    )
    bpf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bpf)  # type: ignore[union-attr]
    for f in bpf.load_decision_population(gen=GEN):
        d = f["payload"]
        status = str(d.get("status") or d.get("decision") or "")
        url = str(d.get("candidate_url") or "")
        label = 1 if status in POSITIVE else 0
        led = by_url.get(normalize_repo_url(url), {})
        # Tree feature from the committed artifact: slug -> pin -> result.
        # Pin precedence MUST match the tree builder (build-gate-labels.py):
        # a decision's probe.pin_probed is the decision-time probed pin
        # (E3), then corpus_pin, then probe.pin. The ledger's mined
        # pin_probed is NEVER substituted (E3 data absent).
        tree_feature = None
        probe = d.get("probe") if isinstance(d.get("probe"), dict) else {}
        pin = str(
            probe.get("pin_probed")
            or d.get("corpus_pin")
            or probe.get("pin")
            or ""
        )
        slug = _repo_slug(url)
        if slug and pin:
            entry = tree_artifact.get(slug, {})
            if isinstance(entry, dict):
                tree_feature = entry.get(pin)
        sites_raw = probe.get("regex_sites")
        row = {
            "url": url,
            "label": label,
            "status": status,
            "stars": led.get("stars") or 0,
            "pushed_date": led.get("pushed_date") or "",
            "source_query": led.get("source_query") or "",
            "capped": bool(led.get("capped")),
            "pin": pin,
            "tree_feature": tree_feature
            if isinstance(tree_feature, dict)
            else None,
        }
        if type(sites_raw) is int:
            row["regex_sites"] = sites_raw
        rows.append(row)
    return rows


def stratified_split(rows: list[dict], seed: int) -> tuple[list[dict], list[dict]]:
    """Stratified 50/50 split per the freeze protocol: THREE status strata
    (go / triage-trial / no-go), then collapse to binary labels only for AUC.
    Preserves the label mix by construction."""
    import random

    rng = random.Random(seed)
    by_status: dict[str, list[dict]] = {}
    for r in rows:
        by_status.setdefault(r["status"], []).append(r)
    train: list[dict] = []
    test: list[dict] = []
    for status, group in sorted(by_status.items()):
        rng.shuffle(group)
        half = len(group) // 2
        train.extend(group[:half])
        test.extend(group[half:])
    rng.shuffle(train)
    rng.shuffle(test)
    return train, test


def score_rows(rows: list[dict], allocator: str, *, today=None) -> list[float]:
    from regexproof.mine.score import candidate_score

    scores = []
    for r in rows:
        cand = {
            "url": r["url"],
            "stars": r["stars"],
            "pushed_date": r["pushed_date"],
            "source_query": r["source_query"],
            "capped": r["capped"],
        }
        tree_feature = None
        if allocator == "score-v1.5":
            # Tree signals from the committed mine-tree-features artifact
            # (the walk already ran at gate time; keyed slug -> pin).
            tree_feature = r.get("tree_feature")
        total, _ = candidate_score(
            cand, today=today, allocator=allocator, tree_feature=tree_feature
        )
        scores.append(total)
    return scores


def _auc_delta_ci(
    v1_scores: list[float],
    v15_scores: list[float],
    labels: list[int],
    *,
    seed: int,
    n_boot: int = 10000,
    method: str = "bca",
) -> tuple[float, float, str]:
    """Seeded bootstrap CI for AUC(v1.5) - AUC(v1) — the flip-rule statistic.

    Resamples the PAIRED (v1, v1.5, label) rows, computes both AUCs on each
    resample, and collects the delta distribution. ``method='bca'`` applies
    the bias-corrected-and-accelerated adjustment (jackknife over leave-one-
    out paired rows); ``method='percentile'`` is the declared fallback.
    Returns ``(lo, hi, method_used)`` — the flip rule fires only when the
    whole interval sits above 0 (one-sided IMPROVEMENT)."""
    import random

    from regexproof.mine.score_v2 import auc
    from regexproof.stats.intervals import _inv_normal, _normal_cdf

    rng = random.Random(seed)
    n = len(v1_scores)
    assert n == len(v15_scores) == len(labels)
    pairs = list(zip(v1_scores, v15_scores, labels))

    def delta_of(idx: list[int]) -> float:
        s1 = [pairs[i][0] for i in idx]
        s15 = [pairs[i][1] for i in idx]
        lab = [pairs[i][2] for i in idx]
        a1 = auc(s1, lab)
        a15 = auc(s15, lab)
        if a1 != a1 or a15 != a15:  # nan guard (single-class resample)
            return float("nan")
        return a15 - a1

    deltas: list[float] = []
    for _ in range(n_boot):
        idx = [rng.randrange(n) for _ in range(n)]
        d = delta_of(idx)
        if d == d:
            deltas.append(d)
    deltas.sort()
    if not deltas:
        # Every resample was single-class — the statistic is undefined on
        # this population; never index an empty list. The eval treats this
        # as "no evidence" (no flip) rather than crashing.
        return (0.0, 0.0, "undefined-single-class")

    def endpoint(p: float) -> float:
        return deltas[max(0, math.floor(p * len(deltas)) - 1)]

    method_used = method
    if method == "bca" and len(deltas) >= 100:
        # Jackknife over leave-one-out paired rows for the acceleration a.
        jack = [
            delta_of([j for j in range(n) if j != i]) for i in range(n)
        ]
        finite = [j for j in jack if j == j]
        if len(finite) >= 3:
            mean_j = sum(finite) / len(finite)
            num = sum((mean_j - j) ** 3 for j in finite)
            den = sum((mean_j - j) ** 2 for j in finite)
            accel = num / (6.0 * den**1.5) if den else 0.0
            observed = delta_of(list(range(n)))
            frac = sum(1.0 for d in deltas if d < observed) / len(deltas)
            if 0.0 < frac < 1.0:
                z0 = _inv_normal(frac)
                za = abs(_inv_normal(0.025))
                a1 = z0 + (z0 + za) / (1.0 - accel * (z0 + za))
                a2 = z0 + (z0 - za) / (1.0 - accel * (z0 - za))
                p1 = _normal_cdf(a1)
                p2 = _normal_cdf(a2)
                lo = deltas[max(0, math.floor(min(p1, p2) * len(deltas)) - 1)]
                hi = deltas[min(len(deltas) - 1, math.ceil(max(p1, p2) * len(deltas)) - 1)]
                return (lo, hi, method_used)
        # BCa undefined (no finite acceleration / z0) → declared fallback.
        method_used = "percentile-fallback"
    return (endpoint(0.025), endpoint(0.975), method_used)


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        type=pathlib.Path,
        default=FLIP_OUT,
        help="Output path for the flip decision (default: "
        "properties/generated/score_v15_flip_decision.json). Tests pass a "
        "tmp path so the committed artifact is never mutated.",
    )
    args = ap.parse_args(argv)
    out_path = args.out
    sys.path.insert(0, str(ROOT))
    freeze = load_freeze()
    validate_freeze_snapshot(freeze)

    from regexproof.mine.score_v2 import auc
    from regexproof.stats.intervals import clopper_pearson

    rows = join_rows(freeze)
    n = len(rows)
    pos = sum(1 for r in rows if r["label"])
    if n != freeze["dataset"]["n"]:
        raise SystemExit(
            f"FATAL: joined population n={n} != freeze n={freeze['dataset']['n']}"
        )

    split = freeze["split"]
    seed = int(split["seed"])
    _train, test = stratified_split(rows, seed)
    labels = [r["label"] for r in test]

    # Frozen eval date: the recency features must NOT use the wall clock.
    # The freeze's escape baseline records computed_at — the artifact clock.
    from datetime import date

    eval_date = date.fromisoformat(str(freeze["escape_baseline"]["computed_at"]))

    v1_scores = score_rows(test, "score-v1", today=eval_date)
    v15_scores = score_rows(test, "score-v1.5", today=eval_date)

    auc_v1 = auc(v1_scores, labels)
    auc_v15 = auc(v15_scores, labels)
    # Flip rule: bootstrap DIFFERENCE-DISTRIBUTION CI on AUC. Resample the
    # paired (v1, v1.5) score rows (not the score differences — AUC is
    # computed per resample), collect the AUC delta distribution, and take
    # the seeded percentile CI. One-sided IMPROVEMENT: flip only when the
    # whole CI sits above 0 (a significantly WORSE v1.5 must never flip).
    lo_ci, hi_ci, ci_method = _auc_delta_ci(v1_scores, v15_scores, labels, seed=seed)
    # precision@K descriptive only (K=30 frozen).
    k = int(freeze["eval"]["k_frozen"])
    top_v15 = sorted(range(len(test)), key=lambda i: v15_scores[i], reverse=True)[:k]
    top_v1 = sorted(range(len(test)), key=lambda i: v1_scores[i], reverse=True)[:k]
    top_pos = sum(labels[i] for i in top_v15)
    top_pos_v1 = sum(labels[i] for i in top_v1)
    cp = clopper_pearson(top_pos, k)
    cp_v1 = clopper_pearson(top_pos_v1, k)
    # Cap-raise calibration note: v1.5 overlay changes scores; record the
    # observed delta so the cap logic is calibrated, not silently re-raised.
    mean_delta = round(
        sum(a - b for a, b in zip(v15_scores, v1_scores)) / len(v1_scores), 4
    ) if v1_scores else 0.0

    flips = bool(lo_ci > 0)  # one-sided IMPROVEMENT only — CI above 0
    decision = {
        "schema_version": "1",
        "eval": {
            "population_n": n,
            "positive": pos,
            "split": {"seed": seed, "ratio": split["ratio"]},
            "test_n": len(test),
            "auc_v1": round(auc_v1, 6),
            "auc_v15": round(auc_v15, 6),
            "auc_delta_v15_minus_v1": round(auc_v15 - auc_v1, 6),
            "bootstrap_ci_95_delta": [round(lo_ci, 6), round(hi_ci, 6)],
            "bootstrap_method": ci_method,
            "precision_at_k": {"k": k, "positive_in_top_k": top_pos, "clopper_pearson_95": [round(cp[0], 6), round(cp[1], 6)]},
            "precision_at_k_v1": {"k": k, "positive_in_top_k": top_pos_v1, "clopper_pearson_95": [round(cp_v1[0], 6), round(cp_v1[1], 6)]},
            "mean_score_delta": mean_delta,
            "cap_raise_calibration_note": "overlay shifts scores by "
            f"{mean_delta} on average; any cap raise must be recalibrated, "
            "never applied silently",
        },
        "flip_rule": "bootstrap BCa difference CI (v1.5 - v1) excludes 0, "
        "one-sided, AUC-only, no OR alternative",
        "flip_to_v15": flips,
        "action": (
            "record offline AUC flip to score-v1.5; live drain unchanged"
            if flips
            else "keep score-v1 (offline AUC and live drain)"
        ),
        "note": "v2 comparison is label reproduction only, never validation",
        "live_drain": "score-v1 (rank-mine-candidates.py / docs/MINE-SETUP.md)",
        "designed_mismatch": (
            (
                "Eval already flipped to v1.5 (flip_to_v15). Live drain is still "
                "v1. AUC is a global-health statistic; the operational flip of "
                "the probe stream is a separate, currently unowned decision. A "
                "firing escape while v1.5 sits unflipped on live drain is a "
                "designed outcome. No second top-K flip rule (freeze is AUC-only)."
            )
            if flips
            else (
                "Eval kept score-v1 (flip_to_v15 false). Live drain is also "
                "v1; there is no drain mismatch. No second top-K flip rule "
                "(freeze is AUC-only)."
            )
        ),
    }
    out_path.write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n")
    print(f"eval: n={n} pos={pos} test={len(test)}")
    print(f"  auc_v1={auc_v1:.4f} auc_v15={auc_v15:.4f} delta={auc_v15 - auc_v1:+.4f}")
    print(f"  bootstrap95_delta=[{lo_ci:.4f}, {hi_ci:.4f}] -> flip={flips}")
    print(f"  precision@{k} v1.5={top_pos}/{k} CP95=[{cp[0]:.4f}, {cp[1]:.4f}] (descriptive)")
    print(f"  precision@{k} v1={top_pos_v1}/{k} CP95=[{cp_v1[0]:.4f}, {cp_v1[1]:.4f}] (descriptive)")
    print(f"  wrote {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
