"""Historical fraction provenance must survive aggregate projections."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_SCRIPT = ROOT / "scripts" / "build-cross-corpus-matrix.py"


def test_cross_corpus_matrix_propagates_historical_fraction_status(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("cross_corpus_matrix", MATRIX_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    monkeypatch.setattr(module, "CORPORA", ["aidevops"])
    monkeypatch.setattr(module, "OUT", tmp_path)
    (tmp_path / "aidevops_encodable_fraction.json").write_text(
        json.dumps(
            {
                "scope": "full_corpus",
                "decision": "go",
                "fraction": 0.9013,
                "encodable": 10212,
                "sample_size": 11330,
                "complete_run": True,
                "measurement_status": "historical_pre_615_shell_extractor",
                "measurement_note": "rerun before current use",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    assert module.main() == 0
    report = json.loads((tmp_path / "cross_corpus_matrix.json").read_text())
    row = report["corpora"][0]
    assert row["measurement_status"] == "historical_pre_615_shell_extractor"
    assert row["measurement_note"] == "rerun before current use"
    assert "historical_pre_615_shell_extractor" in (
        tmp_path / "cross_corpus_matrix.md"
    ).read_text()
