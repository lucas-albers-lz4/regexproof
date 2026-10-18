"""Tests for deterministic, pre-outcome candidate allocation."""

from __future__ import annotations

import hashlib
import json

import pytest

from regexproof.mine.conversion_allocation import (
    AllocationError,
    allocate_candidates,
    validate_population,
    verify_classification_binding,
    verify_inventory_binding,
)

PIN = "4b53dc7629ca3bc88bf5467db481ad2af7130711"
SEED = hashlib.sha256(b"frozen before outcomes").hexdigest()


def _candidate(index: int, idiom_class: str) -> dict:
    return {
        "regex_id": f"{index:032x}",
        "site": f"scripts/tool-{index}.sh:10:2",
        "inventory_site": f"batch/corpora/mycelium/rules/scripts/tool-{index}.sh:10:2",
        "source_file": f"scripts/tool-{index}.sh",
        "source_sha256": hashlib.sha256(f"source-{index}".encode()).hexdigest(),
        "idiom_bucket": "scripts-bootstrap",
        "pattern": "^[a-z]+$",
        "flags": "",
        "dialect": "posix-shell",
        "call_kind": "search",
        "trust_class": "config",
        "encodable": True,
        "idiom_key": f"safe-token-{idiom_class}",
        "idiom_class": idiom_class,
        "classification_evidence": f"pre-outcome classification for {index}",
        "prior_question_ids": [],
    }


def _population() -> dict:
    candidates = []
    candidates.extend(_candidate(i, "productive") for i in range(20))
    candidates.extend(_candidate(i + 20, "novel_idiom") for i in range(5))
    candidates.extend(_candidate(i + 25, "unclassified") for i in range(5))
    return {
        "schema_version": "1",
        "population_id": "fixture-p4-pre-outcome",
        "cluster": "mycelium",
        "repository_url": "https://github.com/mycelium0/mycelium",
        "source_pin": PIN,
        "idiom_bucket": "scripts-bootstrap",
        "product_engine": "fixture POSIX shell",
        "frozen_at": "2026-10-15T00:00:00Z",
        "inventory_sha256": hashlib.sha256(b"inventory").hexdigest(),
        "classification_sha256": hashlib.sha256(b"classification").hexdigest(),
        "outcome_ledger_sha256": hashlib.sha256(b"ledger snapshot").hexdigest(),
        "selection_seed_sha256": hashlib.sha256(SEED.encode()).hexdigest(),
        "question_history_sha256": hashlib.sha256(b"frozen history index").hexdigest(),
        "candidates": candidates,
    }


def test_population_precondition_rejects_duplicates_and_asked_sites():
    population = _population()
    population["candidates"].append(dict(population["candidates"][0]))
    with pytest.raises(AllocationError, match="duplicate candidate identity"):
        validate_population(population)

    population = _population()
    population["candidates"][0]["prior_question_ids"] = ["question-1"]
    with pytest.raises(AllocationError, match="expected to be empty"):
        validate_population(population)


def test_fifteen_site_mix_is_10_productive_3_novel_2_uniform():
    allocation = allocate_candidates(_population(), seed=SEED)

    assert allocation["nominal_quotas"] == {
        "productive": 10,
        "novel_idiom": 3,
        "unbiased": 2,
    }
    assert allocation["actual_selection_counts"] == {
        "productive": 10,
        "novel_idiom": 3,
        "unbiased": 2,
        "unbiased_reallocation": 0,
    }
    assert len(allocation["selected_candidates"]) == 15
    assert len({row["regex_id"] for row in allocation["selected_candidates"]}) == 15


def test_selection_is_independent_of_population_row_order():
    population = _population()
    forward = allocate_candidates(population, seed=SEED)
    population["candidates"].reverse()
    reverse = allocate_candidates(population, seed=SEED)

    assert [r["regex_id"] for r in forward["selected_candidates"]] == [
        r["regex_id"] for r in reverse["selected_candidates"]
    ]
    assert [r["selection_mode"] for r in forward["selected_candidates"]] == [
        r["selection_mode"] for r in reverse["selected_candidates"]
    ]


def test_selection_seed_must_match_the_frozen_population_commitment():
    with pytest.raises(AllocationError, match="does not match the frozen population commitment"):
        allocate_candidates(_population(), seed=hashlib.sha256(b"changed after outcomes").hexdigest())


def test_unbiased_arm_draws_from_the_complete_population():
    population = _population()
    result = allocate_candidates(population, seed=SEED)
    expected = sorted(
        population["candidates"],
        key=lambda row: (
            hashlib.sha256(f"{SEED}\0unbiased\0{row['regex_id']}".encode()).hexdigest(),
            row["regex_id"],
        ),
    )[:2]
    actual = [
        row["regex_id"]
        for row in result["selected_candidates"]
        if row["selection_mode"] == "unbiased"
    ]
    assert set(actual) == {row["regex_id"] for row in expected}


def test_empty_targeted_arm_reallocates_slots_and_reports_the_actual_mix():
    population = _population()
    population["candidates"] = [
        _candidate(0, "productive"),
        *(_candidate(i, "novel_idiom") for i in range(1, 6)),
        *(_candidate(i, "unclassified") for i in range(6, 15)),
    ]
    result = allocate_candidates(population, seed=SEED, sample_size=10)

    assert result["sample_size_selected"] == 10
    assert result["actual_selection_counts"]["productive"] <= 1
    assert sum(result["actual_selection_counts"].values()) == 10
    assert result["unbiased_reallocation_count"] >= 0
    assert len({row["regex_id"] for row in result["selected_candidates"]}) == 10


def test_inventory_rows_are_joined_by_id_and_all_semantic_fields():
    population = _population()
    inventory = "\n".join(
        json.dumps({
            "regex_id": row["regex_id"],
            "site": row["inventory_site"],
            "pattern": row["pattern"],
            "flags": row["flags"],
            "dialect": row["dialect"],
            "call_kind": row["call_kind"],
            "encodable": row["encodable"],
            "corpus": population["cluster"],
        })
        for row in population["candidates"]
    )
    assert verify_inventory_binding(population, inventory) == 30

    altered = json.loads(inventory.splitlines()[0])
    altered["pattern"] = "^.*$"
    with pytest.raises(AllocationError, match="differs from its frozen inventory row"):
        verify_inventory_binding(population, json.dumps(altered))

    duplicate = inventory + "\n" + inventory.splitlines()[0]
    with pytest.raises(AllocationError, match="duplicate regex_id"):
        verify_inventory_binding(population, duplicate)

    duplicate_field = inventory.splitlines()[0].replace(
        '"pattern": "^[a-z]+$"', '"pattern": "^[a-z]+$", "pattern": ".*"'
    )
    with pytest.raises(AllocationError, match="duplicate JSON key"):
        verify_inventory_binding(population, duplicate_field)


def test_classification_rows_are_complete_unique_and_bound_to_the_ledger():
    population = _population()
    classification = {
        "schema_version": "1",
        "population_id": population["population_id"],
        "source_pin": population["source_pin"],
        "outcome_ledger_sha256": population["outcome_ledger_sha256"],
        "classifications": [
            {
                "regex_id": row["regex_id"],
                "idiom_key": row["idiom_key"],
                "idiom_class": row["idiom_class"],
                "evidence": row["classification_evidence"],
            }
            for row in population["candidates"]
        ],
    }
    assert verify_classification_binding(population, classification) == 30

    classification["classifications"].pop()
    with pytest.raises(AllocationError, match="omits candidates"):
        verify_classification_binding(population, classification)

    classification["classifications"].append(classification["classifications"][0])
    with pytest.raises(AllocationError, match="unknown or duplicate regex_id"):
        verify_classification_binding(population, classification)

    classification = {
        "schema_version": "1",
        "population_id": population["population_id"],
        "source_pin": population["source_pin"],
        "outcome_ledger_sha256": "0" * 64,
        "classifications": [],
    }
    with pytest.raises(AllocationError, match="does not bind this population and ledger"):
        verify_classification_binding(population, classification)
