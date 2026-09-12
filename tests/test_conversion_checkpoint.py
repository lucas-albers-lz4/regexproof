"""Tests for the strict frozen-cohort conversion checkpoint."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from regexproof.mine.cohort_manifest import build_manifest
from regexproof.mine.conversion_checkpoint import (
    ConversionCheckpointError,
    build_report,
    dumps_report,
    load_checkpoint,
    wilson_interval,
)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "conversion-checkpoint.py"


def _cohort():
    return build_manifest(
        {
            "candidates": [
                {
                    "repo_id": "owner/repo",
                    "url": "https://github.com/owner/repo",
                    "pin": "a" * 40,
                    "dialect_family": "py_re",
                    "boundary_family": "validator",
                    "score": 1.0,
                    "sites": 20,
                    "fork": False,
                    "duplicate_of": None,
                    "partial": False,
                }
            ]
        },
        "cohort-1",
        1,
    )


def _contract(**overrides):
    value = {
        "schema_version": "1",
        "site": "src/validator.py:0:1",
        "guarantee": "accepted input cannot contain a shell separator",
        "input_source": "untrusted HTTP username",
        "trust": "untrusted-input",
        "declared_domain": "ASCII username alphabet",
        "provenance": "human",
    }
    value.update(overrides)
    return value


def _disposition(status="wont_file", *, filed_at=None, **overrides):
    value = {
        "status": status,
        "filed_at": filed_at,
        "resolved_at": None,
        "approval_escape": None,
        "approval_ref": None,
        "reason_code": None,
        "backfilled": False,
        "disposition_date": None,
    }
    value.update(overrides)
    return value


def _row(
    index: int,
    *,
    result="sat",
    gt="reproduced",
    status="wont_file",
    filed_at=None,
    contract=None,
    kind="property",
    synthesized=False,
):
    site = f"src/validator.py:{index}:1"
    contract_value = _contract() if contract is None else dict(contract)
    contract_value["site"] = site
    canonical = {
        "schema_version": "1",
        "site": site,
        "contract": contract_value,
        "domain": "accepted username alphabet",
        "kind": kind,
        "synthesized": synthesized,
        "result": result,
        "ground_truth_status": gt,
        "name": f"question-{index}",
    }
    return {
        "repo_id": "owner/repo",
        "url": "https://github.com/owner/repo",
        "pin": "a" * 40,
        "schema_version": "1",
        "site": site,
        "question_id": f"question-{index}",
        "kind": kind,
        "synthesized": synthesized,
        "result": result,
        "domain": "accepted username alphabet",
        "contract": contract_value,
        "ground_truth_status": gt,
        "disposition": _disposition(status, filed_at=filed_at),
        "canonical": canonical,
    }


def _checkpoint(*rows):
    cohort = _cohort()
    return {
        "schema_version": "1",
        "cohort_id": cohort["cohort_id"],
        "manifest_digest": cohort["manifest_digest"],
        "cohort": cohort,
        "expected_rows": [
            {
                "repo_id": row["repo_id"],
                "url": row["url"],
                "pin": row["pin"],
                "site": row["site"],
                "question_id": row["question_id"],
            }
            for row in rows
        ],
        "rows": list(rows),
    }


def test_funnel_counts_preserve_filing_and_disposition_distinctions():
    report = build_report(
        _checkpoint(
            _row(0, gt="PASS", status="fixed_upstream", filed_at="2026-09-01"),
            _row(1, status="private_first", filed_at="2026-09-02"),
            _row(2, gt="PASS", status="filed", filed_at="2026-09-03"),
            _row(3, status="wont_file"),
            _row(4, gt="PASS", status="false_positive"),
            _row(5, result="unsat", gt="not_applicable"),
            _row(6, gt="PASS", status="filed", filed_at="2026-09-12"),
            _row(7, gt="PASS", status="filed_plan", filed_at="2026-09-12"),
        )
    )
    assert report["counts"] == {
        "asked": 8,
        "sat": 7,
        "ground_truthed": 7,
        "filed": 4,
        "private_first": 1,
        "accepted": 1,
    }
    assert report["disposition_breakdown"] == {
        "false_positive": 1,
        "filed": 2,
        "fixed_upstream": 1,
        "filed_plan": 1,
        "private_first": 1,
        "wont_file": 2,
    }
    assert report["filing_interpretation"]["private_first_is_filed"] is True
    assert report["filing_interpretation"]["accepted_is_not_third_party_remediation"]
    assert report["idiom_interpretation"]["product_conversion_checkpoint_is_not_compiler_saturation"]


def test_strict_schema_and_exclusions_fail_closed():
    bad_rows = [
        (_row(0, result="gap"), "result must be 'sat' or 'unsat'"),
        (_row(0, status="filed", gt="not_run"), "filing status requires"),
        (_row(0, result="unsat", gt="reproduced"), "not_applicable"),
        (_row(0, status="unknown"), "status .* unknown"),
        (_row(0, kind="rule_diff"), "kind must be"),
        (_row(0, synthesized=True), "synthesized must be false"),
        (_row(0, contract=_contract(provenance="agent")), "provenance must be 'human'"),
    ]
    for row, message in bad_rows:
        with pytest.raises(ConversionCheckpointError, match=message):
            build_report(_checkpoint(row))

    missing_contract = _row(0)
    del missing_contract["contract"]
    with pytest.raises(ConversionCheckpointError, match="contract"):
        build_report(_checkpoint(missing_contract))


def test_duplicate_identity_tampering_and_unknown_repo_fail_closed():
    with pytest.raises(ConversionCheckpointError, match="duplicates expected stable"):
        build_report(_checkpoint(_row(0), _row(0)))

    tampered = _checkpoint(_row(0))
    tampered["manifest_digest"] = "b" * 64
    with pytest.raises(ConversionCheckpointError, match="does not match"):
        build_report(tampered)

    outside = _row(0)
    outside["repo_id"] = "other/repo"
    with pytest.raises(ConversionCheckpointError, match="outside"):
        build_report(_checkpoint(outside))


def test_duplicate_keys_and_nonfinite_numbers_are_rejected(tmp_path: Path):
    path = tmp_path / "checkpoint.json"
    valid = json.dumps(_checkpoint(_row(0)))
    path.write_text(valid.replace('"rows":', '"rows":', 1).replace(
        '"schema_version": "1"', '"schema_version": "1", "schema_version": "1"', 1
    ), encoding="utf-8")
    with pytest.raises(ConversionCheckpointError, match="duplicate JSON key"):
        load_checkpoint(path)

    path.write_text(valid.replace('"score": 1.0', '"score": NaN'), encoding="utf-8")
    with pytest.raises(ConversionCheckpointError, match="non-finite"):
        load_checkpoint(path)


def test_wilson_interval_and_target_widths_are_deterministic():
    lower, upper = wilson_interval(5, 50)
    assert round(lower, 12) == 0.043475764904
    assert round(upper, 12) == 0.213602314488
    report = build_report(_checkpoint(_row(0)))
    targets = report["intervals"]["targets"]
    assert targets["50"] == {"max_width": "0.267109713863", "successes_at_max_width": 25}
    assert targets["100"] == {"max_width": "0.192336939417", "successes_at_max_width": 50}
    assert dumps_report(report) == dumps_report(build_report(_checkpoint(_row(0))))


def test_cli_is_read_only_and_returns_json(tmp_path: Path, capsys):
    spec = importlib.util.spec_from_file_location("conversion_checkpoint", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = tmp_path / "checkpoint.json"
    source_text = json.dumps(_checkpoint(_row(0)), indent=2) + "\n"
    source.write_text(source_text, encoding="utf-8")
    assert module.main([str(source)]) == 0
    assert json.loads(capsys.readouterr().out)["counts"]["asked"] == 1
    assert source.read_text(encoding="utf-8") == source_text

    source.write_text(json.dumps({"schema_version": "bad"}), encoding="utf-8")
    assert module.main([str(source)]) == 2
    assert "conversion-checkpoint: error:" in capsys.readouterr().err
