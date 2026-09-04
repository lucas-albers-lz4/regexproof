"""Wave 1 (#557): score-v1.5 offline eval — freeze validation + determinism.

The eval must fail closed when the committed population diverges from the
Phase 0 freeze snapshot, and the flip decision must be byte-stable (same
seed + same data ⇒ same decision)."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"
FLIP_OUT = GEN / "score_v15_flip_decision.json"


def test_flip_decision_exists_and_is_shape_checked():
    assert FLIP_OUT.is_file(), "eval must produce the flip decision artifact"
    d = json.loads(FLIP_OUT.read_text(encoding="utf-8"))
    assert d["schema_version"] == "1"
    assert d["eval"]["population_n"] == 875
    assert d["eval"]["split"]["ratio"] == 0.5
    assert d["flip_rule"].startswith("bootstrap BCa difference CI")
    # Freeze-eval golden: current population flips offline to v1.5; live drain stays v1.
    assert d["flip_to_v15"] is True
    assert d["action"] == (
        "record offline AUC flip to score-v1.5; live drain unchanged"
    )
    mismatch = d["designed_mismatch"].lower()
    assert "live drain is still" in mismatch
    assert "auc is a global-health statistic" in mismatch
    assert "operational flip of the probe stream" in mismatch
    assert "no second top-k flip" in mismatch
    assert d["live_drain"] == (
        "score-v1 (rank-mine-candidates.py / docs/MINE-SETUP.md)"
    )
    # precision@K is descriptive only; freeze-eval golden counts.
    assert d["eval"]["precision_at_k"]["k"] == 30
    assert d["eval"]["precision_at_k_v1"]["k"] == 30
    assert d["eval"]["precision_at_k"]["positive_in_top_k"] == 12
    assert d["eval"]["precision_at_k_v1"]["positive_in_top_k"] == 8
    assert d["eval"]["precision_at_k"]["clopper_pearson_95"] == [0.226558, 0.593965]
    assert d["eval"]["precision_at_k_v1"]["clopper_pearson_95"] == [0.122795, 0.458894]
    for name in ("precision_at_k", "precision_at_k_v1"):
        lo, hi = d["eval"][name]["clopper_pearson_95"]
        assert 0 <= lo <= hi <= 1
    assert "cap_raise_calibration_note" in d["eval"]


def test_flip_decision_deterministic(tmp_path: Path):
    """Same seed + same data ⇒ byte-identical decision (golden discipline).

    Writes to a tmp path via --out — the committed artifact is never
    mutated by the test. Bounded by a timeout (10k bootstrap iterations)."""
    out = tmp_path / "flip.json"
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "eval-score-v15.py"), "--out", str(out)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r.returncode == 0, r.stderr
    first = out.read_bytes()
    r2 = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "eval-score-v15.py"), "--out", str(out)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r2.returncode == 0, r2.stderr
    assert out.read_bytes() == first, "flip decision drifts on re-run"
    # The committed artifact is untouched by this test.
    assert (GEN / "score_v15_flip_decision.json").is_file()


def test_eval_fails_closed_on_freeze_mismatch(tmp_path: Path):
    """A decision-file mutation must abort the eval (snapshot hash check)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "eval_v15", ROOT / "scripts" / "eval-score-v15.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Isolate the test's decision file in tmp_path — never write into the
    # real generated dir.
    setattr(mod, "GEN", tmp_path)
    (tmp_path / "_zz_mut_gate_decision.json").write_text(
        json.dumps({"candidate_url": "https://x/y", "decision": "go"})
        + "\n",
        encoding="utf-8",
    )
    freeze = mod.load_freeze()
    with pytest.raises(SystemExit, match="snapshot hash mismatch"):
        mod.validate_freeze_snapshot(freeze)


def test_join_pin_precedence_matches_tree_builder(tmp_path: Path):
    """probe.pin_probed (the decision-time E3 pin) must win over the ledger's
    mined pin — a distinct probed pin must join against the probed pin's tree
    entry, not silently fall back (Luna r2 fold)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "eval_v15b", ROOT / "scripts" / "eval-score-v15.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Isolate all writes in tmp_path (mirrors the real GEN layout).
    setattr(mod, "GEN", tmp_path)
    (tmp_path / "candidate-ledger.json").write_text(
        json.dumps({"candidates": []}), encoding="utf-8"
    )
    (tmp_path / "mine-tree-features.json").write_text(
        json.dumps({"schema_version": "1", "entries": {}}), encoding="utf-8"
    )
    # Decision with probe.pin_probed = probed-pin; ledger has a DIFFERENT
    # mined pin. The join must use probe.pin_probed.
    (tmp_path / "_zz_pin_gate_decision.json").write_text(
        json.dumps(
            {
                "candidate_url": "https://github.com/zztest/probe-pin-repo",
                "decision": "go",
                "corpus_pin": "mined-pin",
                "probe": {"pin_probed": "probed-pin", "pin": "probe-pin"},
            }
        )
        + "\n",
        encoding="utf-8",
    )
    # Tree artifact has BOTH pins; only the probed pin resolves.
    artifact = {
        "schema_version": "1",
        "entries": {
            "zztest/probe-pin-repo": {
                "probed-pin": {
                    "complete": True,
                    "truncated": False,
                    "security_boundary": "deterministic-true",
                    "regex_file_type_counts": {".yara": 3},
                    "path_count": 10,
                }
            }
        },
    }
    (tmp_path / "mine-tree-features.json").write_text(
        json.dumps(artifact), encoding="utf-8"
    )
    rows = mod.join_rows(mod.load_freeze())
    row = next(r for r in rows if "probe-pin-repo" in r["url"])
    assert row["pin"] == "probed-pin", f"pin={row['pin']!r}"
    assert row["tree_feature"] is not None, "tree feature must resolve"
    assert row["tree_feature"]["path_count"] == 10
