"""Shape-5 batch admission and search/pad SAT gate (#477)."""

from __future__ import annotations

import json

from regexproof.rule_diff.batch_shape5 import (
    _PAD_GATE_MODEL_CAP,
    admit_shape5_for_batch,
    filter_batch_pairs,
    run_batch_shape5_pairs,
)
from regexproof.rule_diff.search_replay import search_pad_confirms_gap


def test_sibling_family_not_admitted():
    pair = {
        "pair_kind": "sibling_family",
        "provenance": "sibling_family",
        "family_contract": {"R1": "a", "R2": "b", "provenance": "cross_engine"},
    }
    assert admit_shape5_for_batch(pair) is False


def test_version_diff_requires_family_contract():
    pair = {
        "pair_kind": "version_diff",
        "provenance": "version_diff",
        "family_contract": {"R1": "old", "R2": "new", "provenance": "version_diff"},
    }
    assert admit_shape5_for_batch(pair) is True
    pair["family_contract"] = {}
    assert admit_shape5_for_batch(pair) is False


def test_filter_drops_gitleaks_independent_spec():
    pairs = [
        {"provenance": "independent-spec", "family_contract": {"R1": "a", "R2": "b", "provenance": "human"}},
        {
            "provenance": "cross_engine",
            "family_contract": {"R1": "pcre", "R2": "re2", "provenance": "cross_engine"},
        },
    ]
    out = filter_batch_pairs(pairs)
    assert len(out) == 1
    assert out[0]["provenance"] == "cross_engine"


def test_search_pad_confirms_unanchored_gap():
    assert search_pad_confirms_gap(r"^keep-alive", r"keep-alive", "keep-alive")
    assert not search_pad_confirms_gap(r"keep-alive", r"keep-alive", "keep-alive")


def _toy_pair(pair_id: str, r1: str, r2: str, *, pair_kind: str = "version_diff") -> dict:
    return {
        "pair_id": pair_id,
        "pair_kind": pair_kind,
        "provenance": pair_kind,
        "family_contract": {"R1": r1, "R2": r2, "provenance": pair_kind},
        "max_len": 4,
        "r1": {"pattern": r1, "flags": "", "dialect": "py_re"},
        "r2": {"pattern": r2, "flags": "", "dialect": "py_re"},
    }


def test_run_executes_sat_gate_and_skips_independent_spec():
    rows = run_batch_shape5_pairs(
        [
            _toy_pair("toy-sat", "a", "a|b"),
            _toy_pair("toy-unsat", "a|b", "a"),
            {
                **_toy_pair("toy-gitleaks", "a", "a|b", pair_kind="independent-spec"),
                "provenance": "independent-spec",
            },
        ],
        timeout_ms=8000,
    )
    assert {r["pair_id"] for r in rows} == {"toy-sat", "toy-unsat"}
    by_id = {r["pair_id"]: r for r in rows}
    assert by_id["toy-sat"]["result"] == "sat"
    assert by_id["toy-sat"]["search_pad_gate"] is True
    assert by_id["toy-sat"]["ground_truth_status"] == "reproduced"
    assert by_id["toy-sat"]["witness"]["s"]
    assert by_id["toy-unsat"]["result"] == "unsat"


def test_sat_fullmatch_only_when_pad_gate_rejects(monkeypatch):
    monkeypatch.setattr(
        "regexproof.rule_diff.batch_shape5.gate_sat_witness",
        lambda pair, witness: False,
    )
    rows = run_batch_shape5_pairs([_toy_pair("toy-fm", "a", "a|b")], timeout_ms=8000)
    assert len(rows) == 1
    assert rows[0]["result"] == "sat_fullmatch_only"
    assert rows[0]["search_pad_gate"] is False
    assert rows[0]["ground_truth_status"] == "fullmatch-only-not-search-gap"


def test_pad_gate_model_cap_exceeds_five():
    assert _PAD_GATE_MODEL_CAP > 5


def test_compile_bound_is_pattern_length_not_witness_max_len():
    long_a = "a" * 20
    pair = _toy_pair("long-pat", long_a, long_a + "|b")
    assert pair["max_len"] == 4
    rows = run_batch_shape5_pairs([pair], timeout_ms=8000)
    assert len(rows) == 1
    assert rows[0]["result"] != "skipped_unencodable"
    assert rows[0]["result"] == "sat"


def test_write_batch_shape5_strips_nondeterministic_witness(tmp_path):
    from regexproof.batch.runner import _write_batch_shape5_artifact

    rows = [
        {
            "pair_id": "a",
            "result": "sat",
            "ground_truth_status": "reproduced",
            "witness": {"s": "volatile"},
        }
    ]
    summary = {"executed": 1, "sat_search_gap": 1}
    _write_batch_shape5_artifact("demo", tmp_path, rows=rows, summary=summary)
    data = json.loads((tmp_path / "demo_batch_shape5.json").read_text(encoding="utf-8"))
    assert data["rows"][0]["witness"] is None
    assert data["rows"][0]["witness_present"] is True
    # In-memory row still has the witness for callers that GT'd already.
    assert rows[0]["witness"] == {"s": "volatile"}


def test_timeout_gate_fails_batch(tmp_path, monkeypatch):
    import pytest

    from regexproof.batch.runner import _run_and_record_shape5

    monkeypatch.setattr(
        "regexproof.rule_diff.batch_shape5.run_batch_shape5_pairs",
        lambda pairs, timeout_ms=30000: [{"pair_id": "hung", "result": "timeout"}],
    )
    with pytest.raises(SystemExit, match="timeout gate"):
        _run_and_record_shape5(
            "gitleaks",
            [_toy_pair("hung", "a", "a|b")],
            tmp_path,
            admitted=1,
            dropped=0,
            note="test",
        )


def test_require_ground_truth_fails_sat_without_gt(tmp_path, monkeypatch):
    import pytest

    from regexproof.batch.runner import _run_and_record_shape5

    monkeypatch.setattr(
        "regexproof.rule_diff.batch_shape5.run_batch_shape5_pairs",
        lambda pairs, timeout_ms=30000: [
            {
                "pair_id": "gap",
                "result": "sat",
                "search_pad_gate": True,
                "ground_truth_status": None,
            }
        ],
    )
    with pytest.raises(SystemExit, match="require-ground-truth"):
        _run_and_record_shape5(
            "coreruleset",
            [_toy_pair("gap", "a", "a|b")],
            tmp_path,
            admitted=1,
            dropped=0,
            note="test",
            require_ground_truth=True,
        )
