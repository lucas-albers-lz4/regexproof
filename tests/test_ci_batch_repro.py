from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "ci-batch-repro.py"


def _module():
    spec = importlib.util.spec_from_file_location("ci_batch_repro", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_reproducibility_fingerprint_round_trip_and_compare(tmp_path):
    repro = _module()
    generated = tmp_path / "generated"
    triage = tmp_path / "triage"
    generated.mkdir()
    triage.mkdir()
    (generated / "result.json").write_text('{"ok": true}\n', encoding="utf-8")
    (triage / "result.ndjson").write_text('{"regex_id": "one"}\n', encoding="utf-8")

    fingerprint = repro._fingerprint(generated)
    left = tmp_path / "left.json"
    right = tmp_path / "right.json"
    repro._write_fingerprint(left, fingerprint)
    repro._write_fingerprint(right, fingerprint)

    assert repro._read_fingerprint(left) == fingerprint
    assert repro._compare_fingerprints(left, right) == 0

    (generated / "result.json").write_text('{"ok": false}\n', encoding="utf-8")
    repro._write_fingerprint(right, repro._fingerprint(generated))
    assert repro._compare_fingerprints(left, right) == 1
