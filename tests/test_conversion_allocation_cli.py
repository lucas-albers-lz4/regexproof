"""CLI-level source and registry binding for conversion candidate allocation."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from argparse import Namespace
from pathlib import Path

import pytest

from regexproof.contract_adoption import build_adoption_record
from regexproof.mine.conversion_bucket_registry import (
    append_registration,
    build_registration,
    load_registry,
)
from regexproof.mine.question_history import build_question_history_index

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "allocate_conversion_candidates",
    ROOT / "scripts" / "allocate-conversion-candidates.py",
)
assert SPEC is not None and SPEC.loader is not None
CLI = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLI)


def _git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True,
        timeout=10,
    ).stdout.strip()


def _fixture(tmp_path: Path, monkeypatch, *, sample_size: int = 1) -> Namespace:
    monkeypatch.setattr(CLI, "ROOT", tmp_path)
    cluster = "demo-cluster"
    bucket = "request-boundary"
    repository_url = "https://github.com/example/demo"
    checkout = tmp_path / "checkout"
    (checkout / "src").mkdir(parents=True)
    source_path = checkout / "src" / "guard.py"
    source_path.write_text(
        "PATTERN = r'^[a-z]+$'\ndef accepts(value): return ';' not in value\n",
        encoding="utf-8",
    )
    _git(checkout, "init", "-q")
    _git(checkout, "config", "user.email", "test@example.com")
    _git(checkout, "config", "user.name", "Test")
    _git(checkout, "add", "src/guard.py")
    _git(checkout, "commit", "-q", "-m", "fixture")
    pin = _git(checkout, "rev-parse", "HEAD")
    site = "src/guard.py:1:pattern"
    contract_site = "src/guard.py:2:accepts"
    inventory_site = "batch/corpora/demo-cluster/rules/src/guard.py:1:pattern"
    source_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()

    contract = {
        "schema_version": "1",
        "site": contract_site,
        "guarantee": "Accepted request values contain no semicolon.",
        "input_source": "untrusted request value",
        "trust": "untrusted-input",
        "declared_domain": "ASCII request values",
        "provenance": "agent_derived",
    }
    contract["adoption"] = build_adoption_record(
        contract,
        repository_url=repository_url,
        pin=pin,
        checkout=checkout,
        source_file="src/guard.py",
        evidence=[f"{repository_url}/blob/{pin}/src/guard.py", "caller: request value"],
        rationale="The pinned source is the request validation boundary.",
        author="test-author",
        reviewer="test-reviewer",
        same_model=True,
        approved_on="2026-10-15",
    )
    registration = build_registration(
        cluster=cluster,
        bucket=bucket,
        repository_url=repository_url,
        pin=pin,
        checkout=checkout,
        product_engine="CPython re",
        trust_map={"untrusted-input": "request value from an external caller"},
        source_sites=[contract_site, site],
        question_family="request-boundary-validator",
        max_candidates=1,
        registered_on="2026-10-15",
        rationale="One pinned request boundary defines this fixture slice.",
        contract=contract,
        author="test-author",
        reviewer="test-reviewer",
        same_model=True,
    )
    registry_path = tmp_path / "bucket-registry.json"
    append_registration(registration, registry_path)
    registry = load_registry(registry_path)
    registry_digest = hashlib.sha256(
        json.dumps(registry, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    gate_path = tmp_path / "gate.json"
    gate_path.write_text(json.dumps({
        "decision": "go",
        "corpus": cluster,
        "corpus_pin": pin,
        "candidate_url": repository_url,
    }), encoding="utf-8")
    schedule_path = tmp_path / "schedule.json"
    schedule_path.write_text(json.dumps({
        "bucket_registry_digest": registry_digest,
        "selections": [{
            "cluster": cluster,
            "selected_bucket": bucket,
            "selection_basis": "named-next-unused",
        }],
    }), encoding="utf-8")

    inventory_row = {
        "regex_id": "1" * 32,
        "site": inventory_site,
        "pattern": "^[a-z]+$",
        "flags": "",
        "dialect": "python",
        "call_kind": "fullmatch",
        "encodable": True,
        "corpus": cluster,
    }
    inventory_raw = (json.dumps(inventory_row, sort_keys=True) + "\n").encode()
    inventory_path = tmp_path / "inventory.ndjson"
    inventory_path.write_bytes(inventory_raw)
    ledger_raw = b'{"schema_version":"1","upstream_rows":[]}\n'
    ledger_path = tmp_path / "conversion-ledger.json"
    ledger_path.write_bytes(ledger_raw)
    classification = {
        "schema_version": "1",
        "population_id": "demo-population-1",
        "source_pin": pin,
        "outcome_ledger_sha256": hashlib.sha256(ledger_raw).hexdigest(),
        "classifications": [{
            "regex_id": inventory_row["regex_id"],
            "idiom_key": "request-token-allowlist",
            "idiom_class": "novel_idiom",
            "evidence": "Synthetic fixture: empty ledger contains no prior idiom key.",
        }],
    }
    classification_raw = (json.dumps(classification, sort_keys=True) + "\n").encode()
    classification_path = tmp_path / "classification.json"
    classification_path.write_bytes(classification_raw)

    history = build_question_history_index(tmp_path)
    history_raw = (
        json.dumps(history, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode()
    history_path = tmp_path / "question-history-index.json"
    history_path.write_bytes(history_raw)

    population = {
        "schema_version": "1",
        "population_id": "demo-population-1",
        "cluster": cluster,
        "repository_url": repository_url,
        "source_pin": pin,
        "idiom_bucket": bucket,
        "product_engine": "CPython re",
        "frozen_at": "2026-10-15T00:00:00Z",
        "inventory_sha256": hashlib.sha256(inventory_raw).hexdigest(),
        "classification_sha256": hashlib.sha256(classification_raw).hexdigest(),
        "outcome_ledger_sha256": hashlib.sha256(ledger_raw).hexdigest(),
        "question_history_sha256": hashlib.sha256(history_raw).hexdigest(),
        "selection_seed_sha256": hashlib.sha256(
            hashlib.sha256(b"frozen before outcomes").hexdigest().encode()
        ).hexdigest(),
        "candidates": [{
            "regex_id": inventory_row["regex_id"],
            "site": site,
            "inventory_site": inventory_site,
            "source_file": "src/guard.py",
            "source_sha256": source_sha,
            "idiom_bucket": bucket,
            "pattern": inventory_row["pattern"],
            "flags": inventory_row["flags"],
            "dialect": inventory_row["dialect"],
            "call_kind": inventory_row["call_kind"],
            "trust_class": "untrusted-input",
            "encodable": True,
            "idiom_key": "request-token-allowlist",
            "idiom_class": "novel_idiom",
            "classification_evidence": "Synthetic fixture: empty ledger contains no prior idiom key.",
            "prior_question_ids": [],
        }],
    }
    population_path = tmp_path / "population.json"
    population_path.write_text(json.dumps(population), encoding="utf-8")
    return Namespace(
        population=population_path,
        gate_decision=gate_path,
        schedule=schedule_path,
        bucket_registry=registry_path,
        checkout=checkout,
        inventory_file=inventory_path,
        classification_file=classification_path,
        conversion_ledger=ledger_path,
        question_history_index=history_path,
        selection_seed=hashlib.sha256(b"frozen before outcomes").hexdigest(),
        sample_size=sample_size,
        events_log=tmp_path / "events.jsonl",
        output=tmp_path / "allocation.json",
    )


def test_allocator_cli_rechecks_joined_inputs_and_clean_pinned_source(tmp_path, monkeypatch):
    args = _fixture(tmp_path, monkeypatch)

    result = CLI.build_allocation(args)

    assert result["sample_size_selected"] == 1
    assert result["actual_selection_counts"]["novel_idiom"] == 1
    assert result["inventory_rows_reverified"] == 1
    assert result["classifications_reverified"] == 1
    assert result["question_history_sites_reverified"] == 1
    assert result["question_history_sources_reverified"] == 0
    assert result["source_files_reverified"] == 1
    assert result["scheduler_selection_basis"] == "named-next-unused"
    assert result["wave_opened"] is False


def test_allocator_cli_enforces_registration_cap_before_selection(tmp_path, monkeypatch):
    args = _fixture(tmp_path, monkeypatch, sample_size=2)

    with pytest.raises(CLI.AllocationInputError, match="exceeds registered candidate cap"):
        CLI.build_allocation(args)
