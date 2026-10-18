"""Autonomous run metrics stay separate from human stopwatch measurements."""

from __future__ import annotations

import copy

import pytest

from regexproof.mine.autonomous_work import (
    AutonomousWorkError,
    append_run,
    load_rows,
    summarize,
)
from regexproof.mine.question_history import (
    QuestionHistoryError,
    build_question_history_index,
    check_candidates_new,
)


def _row():
    return {
        "schema_version": "1",
        "measurement_id": "run-1",
        "policy_version": "autonomous-contracts-v1",
        "run_id": "forge-helper-wave",
        "agent": "codex",
        "model": "gpt-6.1-sol",
        "cohort_id": "20-r2",
        "manifest_digest": "a" * 64,
        "repo_id": "Agenticstiger/forge-cli",
        "repository_url": "https://github.com/Agenticstiger/forge-cli",
        "source_pin": "e" * 40,
        "wave_id": "forge-cli-helper-image",
        "started_at": "2026-10-13T10:00:00Z",
        "completed_at": "2026-10-13T10:01:30Z",
        "elapsed_seconds": 90,
        "reviewed_sites": 1,
        "contracts_adopted": 1,
        "proof_questions_attempted": 1,
        "decided_faithful_questions": 1,
        "unsat_guarantees": 1,
        "sat_candidates": 0,
        "replayed_witnesses": 0,
        "reachable_violations": 0,
        "security_impact_confirmed": 0,
        "local_runnable_gates": 1,
        "consumer_adopted_gates": 0,
        "mutation_checks_passed": 1,
        "differential_cases": 5680,
        "third_party_reports_sent": 0,
        "maintainer_confirmations": 0,
        "third_party_fixes": 0,
        "human_interventions": 0,
        "input_tokens": None,
        "output_tokens": None,
        "cost_usd": None,
        "human_active_minutes": None,
        "recorded_at": "2026-10-13T10:02:00Z",
    }


def _row_v3():
    row = _row()
    row.update({
        "schema_version": "3",
        "elapsed_basis": "wall_clock",
        "work_items": [{
            "site": "src/guard.py:1:pattern",
            "reviewed": True,
            "question_ids": ["request-token-no-semicolon"],
        }],
    })
    return row


def test_scorecard_separates_useful_gate_bug_and_external_outcomes(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    append_run(_row(), log)
    report = summarize(log)
    assert report["counts"]["local_runnable_gates"] == 1
    assert report["counts"]["unsat_guarantees"] == 1
    assert report["counts"]["sat_candidates"] == 0
    assert report["counts"]["third_party_reports_sent"] == 0
    assert report["schema_version"] == "2"
    assert report["resource_totals"]["input_tokens"] is None
    assert report["resource_totals"]["cost_usd"] is None
    assert report["resource_totals"]["human_active_minutes"] is None
    assert report["rates"]["contracts_per_agent_hour"] == 40
    assert report["rates"]["third_party_confirmation_per_report_sent"] is None
    assert report["track_order"] == [
        "useful_proofs_and_gates", "bug_discovery", "external_outcomes"
    ]


def test_scorecard_can_filter_off_cohort_calibration_from_campaign(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    campaign = _row()
    off_cohort = _row()
    off_cohort.update({
        "measurement_id": "run-2",
        "run_id": "off-cohort-gate",
        "cohort_id": "off-cohort-mycelium-current-pin",
        "local_runnable_gates": 2,
    })
    append_run(campaign, log)
    append_run(off_cohort, log)

    report = summarize(log, cohort_ids={"20-r2"})
    assert report["run_count"] == 1
    assert report["cohort_filter"] == ["20-r2"]
    assert report["counts"]["local_runnable_gates"] == 1

    all_rows = summarize(log)
    assert all_rows["run_count"] == 2
    assert all_rows["cohort_filter"] is None
    assert all_rows["counts"]["local_runnable_gates"] == 3


def test_phase_sum_timing_accepts_subsecond_runs_and_keeps_basis_visible(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    row = _row()
    row.update({
        "schema_version": "2",
        "elapsed_basis": "phase_sum",
        "started_at": "2026-10-15T10:00:00Z",
        "completed_at": "2026-10-15T10:00:00Z",
        "elapsed_seconds": 0.55,
    })
    append_run(row, log)
    report = summarize(log)
    assert report["resource_totals"]["elapsed_seconds"] == 0.55
    assert report["resource_totals"]["elapsed_seconds_by_basis"] == {
        "wall_clock": 0,
        "phase_sum": 0.55,
    }

    invalid = _row()
    invalid.update({
        "schema_version": "2",
        "elapsed_basis": "unknown",
        "started_at": "2026-10-15T10:00:00Z",
        "completed_at": "2026-10-15T10:00:00Z",
        "elapsed_seconds": 0.55,
    })
    with pytest.raises(AutonomousWorkError, match="elapsed_basis"):
        append_run(invalid, tmp_path / "invalid.jsonl")


def test_invalid_outcome_chain_and_duplicate_measurement_fail_closed(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    bad = _row()
    bad["reachable_violations"] = 1
    with pytest.raises(AutonomousWorkError, match="cannot exceed replayed_witnesses"):
        append_run(bad, log)
    append_run(_row(), log)
    with pytest.raises(AutonomousWorkError, match="already exists"):
        append_run(_row(), log)
    loaded = load_rows(log)
    assert len(loaded) == 1


def test_run_id_cannot_double_count_a_retry_or_resume(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    append_run(_row(), log)
    repeated = _row()
    repeated["measurement_id"] = "new-measurement-id"
    repeated["local_runnable_gates"] = 0
    repeated["mutation_checks_passed"] = 0
    repeated["differential_cases"] = 0
    with pytest.raises(AutonomousWorkError, match="run_id already exists"):
        append_run(repeated, log)


def test_human_intervention_clock_is_explicit_and_validated(tmp_path):
    log = tmp_path / "autonomous.jsonl"
    row = _row()
    row["human_interventions"] = 1
    row["human_active_minutes"] = 2.5
    append_run(row, log)
    assert summarize(log)["resource_totals"]["human_active_minutes"] == "2.5"

    invalid = copy.deepcopy(row)
    invalid["measurement_id"] = "run-2"
    invalid["human_interventions"] = 0
    with pytest.raises(AutonomousWorkError, match="requires a human intervention"):
        append_run(invalid, log)


def test_v3_run_work_items_bind_reviewed_sites_and_attempted_questions(tmp_path):
    log = tmp_path / "properties/generated/autonomous_work.jsonl"
    append_run(_row_v3(), log)
    loaded = load_rows(log)
    assert loaded[0]["work_items"][0]["question_ids"] == ["request-token-no-semicolon"]

    index = build_question_history_index(tmp_path)
    assert index["audit"]["asked_site_count"] == 1
    assert index["audit"]["reserved_site_count"] == 1
    assert index["audit"]["unbound_record_count"] == 0
    population = {
        "cluster": "forge-cli",
        "repository_url": "https://github.com/Agenticstiger/forge-cli",
        "source_pin": "e" * 40,
        "candidates": [{"site": "src/guard.py:1:pattern"}],
    }
    with pytest.raises(QuestionHistoryError, match="already asked"):
        check_candidates_new(population, index)


def test_v3_run_requires_exact_site_and_question_accounting(tmp_path):
    row = _row_v3()
    row["work_items"] = []
    row["reviewed_sites"] = 0
    with pytest.raises(AutonomousWorkError, match="question count differs"):
        append_run(row, tmp_path / "autonomous.jsonl")

    row = _row_v3()
    row["work_items"][0]["reviewed"] = False
    with pytest.raises(AutonomousWorkError, match="reviewed count differs"):
        append_run(row, tmp_path / "autonomous.jsonl")
