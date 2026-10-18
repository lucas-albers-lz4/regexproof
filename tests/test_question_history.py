"""Tests for the fail-closed index of asked and reserved conversion sites."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.mine.question_history import (
    QuestionHistoryError,
    build_question_history_index,
    check_candidates_new,
    verify_index_current,
)

PIN = "4b53dc7629ca3bc88bf5467db481ad2af7130711"
REPO = "https://github.com/example/demo"


def _population(*sites: str) -> dict:
    return {
        "cluster": "demo",
        "repository_url": REPO,
        "source_pin": PIN,
        "candidates": [{"site": site} for site in sites],
    }


def _write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value) + "\n", encoding="utf-8")


def test_history_index_blocks_asked_and_reserved_sites_but_allows_new_site(tmp_path):
    _write_json(
        tmp_path / "properties/generated/demo_conversion.ndjson",
        {
            "site": f"example/demo@{PIN}:src/asked.py:1:pattern",
            "result": "SAT",
            "name": "question-asked",
            "corpus": "demo",
        },
    )
    _write_json(
        tmp_path / "properties/calibration/run/roster-v2.json",
        {
            "identities": [{
                "site": "src/reserved.py:2:pattern",
                "question_id": "question-reserved",
                "cluster": "demo",
                "repo_id": "example/demo",
                "pin": PIN,
            }]
        },
    )
    index = build_question_history_index(tmp_path)

    assert index["audit"]["asked_site_count"] == 1
    assert index["audit"]["reserved_site_count"] == 1
    assert check_candidates_new(_population("src/new.py:3:pattern"), index) == 1
    with pytest.raises(QuestionHistoryError, match="already asked"):
        check_candidates_new(_population("src/asked.py:1:pattern"), index)
    with pytest.raises(QuestionHistoryError, match="already reserved"):
        check_candidates_new(_population("src/reserved.py:2:pattern"), index)


def test_history_index_matches_the_inventory_site_alias(tmp_path):
    path = tmp_path / "properties/generated/demo_conversion.ndjson"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps({
            "site": "legacy/path/alias.py:4:pattern",
            "inventory_site": "batch/corpora/demo/rules/src/alias.py:4:pattern",
            "result": "UNSAT",
            "name": "question-alias",
            "corpus": "demo",
        }) + "\n",
        encoding="utf-8",
    )
    index = build_question_history_index(tmp_path)
    population = _population("src/alias.py:4:pattern")
    population["candidates"][0]["inventory_site"] = (
        "batch/corpora/demo/rules/src/alias.py:4:pattern"
    )

    with pytest.raises(QuestionHistoryError, match="already asked"):
        check_candidates_new(population, index)


def test_history_index_matches_regex_id_when_source_columns_use_aliases(tmp_path):
    regex_id = "a" * 32
    _write_json(
        tmp_path / "properties/generated/demo_conversion.ndjson",
        {
            "site": "src/alias.py:4:pattern-name",
            "regex_id": regex_id,
            "result": "UNSAT",
            "name": "question-column-alias",
            "corpus": "demo",
            "url": REPO,
            "source_pin": PIN,
        },
    )
    index = build_question_history_index(tmp_path)
    population = _population("src/alias.py:4:column-17")
    population["candidates"][0]["regex_id"] = regex_id

    with pytest.raises(QuestionHistoryError, match="already asked"):
        check_candidates_new(population, index)


def test_history_index_matches_source_line_pattern_aliases(tmp_path):
    _write_json(
        tmp_path / "properties/generated/demo_conversion.ndjson",
        {
            "site": "src/line.py:7:legacy-token",
            "pattern": "^[a-z]+$",
            "flags": "i",
            "call_kind": "search",
            "result": "UNSAT",
            "name": "question-line-alias",
            "corpus": "demo",
            "url": REPO,
            "source_pin": PIN,
        },
    )
    index = build_question_history_index(tmp_path)

    duplicate = _population("src/line.py:7:column-22")
    duplicate["candidates"][0].update({
        "pattern": "^[a-z]+$", "flags": "i", "call_kind": "search",
    })
    with pytest.raises(QuestionHistoryError, match="already asked"):
        check_candidates_new(duplicate, index)

    distinct = _population("src/line.py:7:column-41")
    distinct["candidates"][0].update({
        "pattern": "^[0-9]+$", "flags": "", "call_kind": "fullmatch",
    })
    assert check_candidates_new(distinct, index) == 1


def test_contract_artifacts_and_frozen_shortlists_reserve_sites(tmp_path):
    _write_json(
        tmp_path / "properties/calibration/run/contracts.json",
        [{
            "site": f"example/demo@{PIN}:src/contract.py:1:guard",
            "adoption": {"source_url": REPO, "source_pin": PIN},
        }],
    )
    _write_json(
        tmp_path / "properties/calibration/run/shortlist.json",
        {
            "corpus": "demo",
            "keep": [{
                "site": "batch/corpora/demo/rules/src/shortlisted.py:2:pattern",
                "regex_id": "1" * 32,
            }],
        },
    )
    index = build_question_history_index(tmp_path)

    with pytest.raises(QuestionHistoryError, match="already reserved"):
        check_candidates_new(
            _population("src/contract.py:1:guard"), index
        )
    shortlist_candidate = _population("src/shortlisted.py:2:pattern")
    shortlist_candidate["candidates"][0]["inventory_site"] = (
        "batch/corpora/demo/rules/src/shortlisted.py:2:pattern"
    )
    with pytest.raises(QuestionHistoryError, match="already reserved"):
        check_candidates_new(shortlist_candidate, index)


def test_aggregate_autonomous_measurement_is_unresolved_history(tmp_path):
    path = tmp_path / "properties/generated/autonomous_work.jsonl"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({
        "run_id": "aggregate-run-1",
        "repository_url": REPO,
        "source_pin": PIN,
        "proof_questions_attempted": 1,
        "reviewed_sites": 0,
    }) + "\n", encoding="utf-8")
    index = build_question_history_index(tmp_path)

    assert index["audit"]["unbound_record_count"] == 1
    with pytest.raises(QuestionHistoryError, match="unresolved prior history"):
        check_candidates_new(_population("src/unmapped.py:1:pattern"), index)


def test_history_index_rejects_unbound_question_for_same_cluster(tmp_path):
    path = tmp_path / "properties/generated/demo_conversion.ndjson"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps({"name": "question-unknown-site", "result": "SAT", "corpus": "demo"})
        + "\n",
        encoding="utf-8",
    )
    index = build_question_history_index(tmp_path)

    assert index["audit"]["unbound_record_count"] == 1
    with pytest.raises(QuestionHistoryError, match="unresolved prior history"):
        check_candidates_new(_population("src/possibly-asked.py:1:pattern"), index)


@pytest.mark.parametrize("change", ["modify", "add"])
def test_history_index_is_invalidated_by_changed_or_new_history(tmp_path, change):
    source = tmp_path / "properties/generated/demo_conversion.ndjson"
    source.parent.mkdir(parents=True)
    source.write_text("", encoding="utf-8")
    index = build_question_history_index(tmp_path)
    if change == "modify":
        source.write_text("{}\n", encoding="utf-8")
    else:
        (source.parent / "other_conversion.ndjson").write_text("", encoding="utf-8")

    with pytest.raises(QuestionHistoryError, match="stale"):
        verify_index_current(tmp_path, index)
