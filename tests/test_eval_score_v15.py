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
    assert d["eval"]["population_n"] == 853
    assert d["eval"]["split"]["ratio"] == 0.5
    assert d["flip_rule"].startswith("bootstrap BCa difference CI")
    assert d["action"] in (
        "flip live drain to score-v1.5",
        "keep score-v1",
    )
    # precision@K is descriptive only.
    assert d["eval"]["precision_at_k"]["k"] == 30
    assert "cap_raise_calibration_note" in d["eval"]


def test_flip_decision_deterministic():
    """Same seed + same data ⇒ byte-identical decision (golden discipline)."""
    before = FLIP_OUT.read_bytes()
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "eval-score-v15.py")],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    assert FLIP_OUT.read_bytes() == before, "flip decision drifts on re-run"


def test_eval_fails_closed_on_freeze_mismatch(tmp_path: Path):
    """A decision-file mutation must abort the eval (snapshot hash check)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "eval_v15", ROOT / "scripts" / "eval-score-v15.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    freeze = mod.load_freeze()
    (GEN / "_zz_mut_gate_decision.json").write_text(
        json.dumps({"candidate_url": "https://x/y", "decision": "go"})
        + "\n",
        encoding="utf-8",
    )
    try:
        with pytest.raises(SystemExit, match="snapshot hash mismatch"):
            mod.validate_freeze_snapshot(freeze)
    finally:
        (GEN / "_zz_mut_gate_decision.json").unlink()
