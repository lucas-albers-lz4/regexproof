"""Tests for the CI corpus-fan-out aggregation contract."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from regexproof.batch import runner


ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "ci-batch-aggregate.py"


def _summary(corpus: str) -> dict:
    return {
        "schema_version": "1",
        "corpus": corpus,
        "corpus_type": "rule_corpus" if corpus != "validatorjs" else "validator",
        "extracted": 1,
        "encodable": 1,
        "triage": 0,
        "findings": 0,
        "inventory_questions": 0,
        "join_regex_ids": 0,
        "engine": {"python": "3.13.15"},
        "redos_findings": 0,
        "redos_incomplete": False,
        "complete_run": True,
        "cache": {"hits": 0, "misses": 1, "entries": 1, "hit_rate": 0.0},
        "cache_hit_rate": 0.0,
    }


def test_aggregate_rejects_missing_worker_summary(tmp_path: Path, monkeypatch):
    for name in runner.PILOT_CORPORA:
        (tmp_path / f"{name}_gate_decision.json").write_text(
            (ROOT / "properties" / "generated" / f"{name}_gate_decision.json").read_text(),
            encoding="utf-8",
        )
    monkeypatch.setattr(runner, "check_corpus_coverage", lambda: [])
    monkeypatch.setattr(runner, "check_admission_gates", lambda *args, **kwargs: [])

    with pytest.raises(SystemExit, match="fan-out artifact missing"):
        runner.aggregate_batch(runner.PILOT_CORPORA, out_dir=tmp_path)


def test_aggregate_writes_complete_contract(tmp_path: Path, monkeypatch):
    for name in runner.PILOT_CORPORA:
        (tmp_path / f"{name}_gate_decision.json").write_text(
            (ROOT / "properties" / "generated" / f"{name}_gate_decision.json").read_text(),
            encoding="utf-8",
        )
        (tmp_path / f"{name}_batch_summary.json").write_text(
            json.dumps(_summary(name)) + "\n", encoding="utf-8"
        )
        (tmp_path / f"{name}.ndjson").write_text("\n", encoding="utf-8")
    (tmp_path / "gitleaks_batch_shape5.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "gitleaks",
                "rows": [],
                "summary": {
                    "executed": 0,
                    "sat_fullmatch_only": 0,
                    "sat_search_gap": 0,
                    "skipped": 0,
                    "timeout": 0,
                    "timeout_gate_ok": True,
                    "timeout_rate": 0.0,
                    "unsat": 0,
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(runner, "check_corpus_coverage", lambda: [])
    monkeypatch.setattr(runner, "check_admission_gates", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        runner,
        "measure_coreruleset",
        lambda out_dir: {"decision": "skipped", "fraction": None, "scope": "not-measured"},
    )

    result = runner.aggregate_batch(runner.PILOT_CORPORA, out_dir=tmp_path)

    assert set(result["corpora"]) == set(runner.PILOT_CORPORA)
    assert (tmp_path / "batch_summary.json").is_file()
    assert (tmp_path / "batch_pair_counts.json").is_file()
    assert (tmp_path / "batch_repro.sha256").is_file()
    aggregate = json.loads((tmp_path / "batch_summary.json").read_text())
    assert aggregate["cache_hit_rate"] == 0.0
    assert aggregate["pair_counts"]["gitleaks"]["batch_shape5"] == 0


def test_aggregate_script_has_cli_entrypoint():
    spec = importlib.util.spec_from_file_location("ci_batch_aggregate", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(SystemExit) as exc:
        module.main(["--help"])
    assert exc.value.code == 0
