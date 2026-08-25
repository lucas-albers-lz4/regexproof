#!/usr/bin/env python3
"""Wave 9 (#578): offline skip-class surrogate on the frozen train half.

Fit on train only; AUC and skip-rate are measured **once** on the test half.
Does not mutate ``phase0_freeze.json``. Does not roll out score-v2 or change
the live drain allocator.

Usage: ``python3 scripts/eval-ranking-surrogate.py``
Writes ``properties/generated/ranking_surrogate.json``.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"
OUT = GEN / "ranking_surrogate.json"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _round_floats(obj):
    if isinstance(obj, float):
        return round(obj, 6)
    if isinstance(obj, dict):
        return {k: _round_floats(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(v) for v in obj]
    return obj


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=pathlib.Path, default=OUT)
    args = ap.parse_args(argv)

    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "eval_score_v15", ROOT / "scripts" / "eval-score-v15.py"
    )
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)  # type: ignore[union-attr]

    from regexproof.mine.surrogate import (
        DEFAULT_FIT_DATE,
        PREDECLARED_THRESHOLD,
        SKIP_SITE_CAP,
        evaluate_skip_rate,
        fit_surrogate,
        skip_class_label,
    )

    freeze = ev.load_freeze()
    ev.validate_freeze_snapshot(freeze)
    rows = ev.join_rows(freeze)
    split = freeze["split"]
    seed = int(split["seed"])
    train, test = ev.stratified_split(rows, seed)
    y_train = [skip_class_label(r["status"], r.get("regex_sites")) for r in train]
    y_test = [skip_class_label(r["status"], r.get("regex_sites")) for r in test]
    model = fit_surrogate(train, y_train, today=DEFAULT_FIT_DATE)
    metrics = evaluate_skip_rate(
        test, y_test, model, threshold=PREDECLARED_THRESHOLD, today=DEFAULT_FIT_DATE
    )
    skip_pop = sum(1 for r in rows if skip_class_label(r["status"], r.get("regex_sites")))
    art = {
        "schema_version": "1",
        "wave": 9,
        "issue": "#578",
        "live_rollout": False,
        "live_drain": "score-v1 (rank-mine-candidates.py / docs/MINE-SETUP.md)",
        "do_not_roll_out_score_v2": True,
        "hard_reject": False,
        "label": {
            "name": "le50_site_nogo",
            "rule": f"status==no-go and regex_sites<={SKIP_SITE_CAP}",
            "site_cap": SKIP_SITE_CAP,
            "population_skip_n": skip_pop,
            "population_n": len(rows),
            "population_skip_frac": round(skip_pop / len(rows), 6) if rows else 0.0,
        },
        "split": {"seed": seed, "ratio": split["ratio"], "train_n": len(train), "test_n": len(test)},
        "features": {
            "set": "preprobe_v1_tree_slug",
            "excludes": ["probe.regex_sites", "walked boundary as a fitted target leak"],
            "note": (
                "Tree summaries are GitHub tree-API features, not the clone "
                "walk. Walked regex_sites is the label only."
            ),
        },
        "fit": {
            "half": "train",
            "today": DEFAULT_FIT_DATE,
            **_round_floats(model),
        },
        "test_once": metrics,
        "freeze_snapshot_sha256": freeze["dataset"]["snapshot_sha256"],
        "not_conversion_wont_file": True,
    }
    text = json.dumps(art, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    out = args.out.expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    from regexproof.io_atomic import atomic_write_text

    atomic_write_text(out, text)
    print(
        f"wrote {out} test_auc={metrics['auc']} skip_rate={metrics['skip_rate']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
