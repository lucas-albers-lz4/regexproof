"""Source-pinned registration is additive, duplicate-safe, and schedulable."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.contract_adoption import build_adoption_record
from regexproof.mine.conversion_bucket_registry import (
    BucketRegistryError,
    append_registration,
    build_registration,
    load_registry,
)

ROOT = Path(__file__).resolve().parents[1]


def _source_repo(tmp_path):
    checkout = tmp_path / "source"
    (checkout / "src").mkdir(parents=True)
    source = checkout / "src" / "guard.py"
    source.write_text("def accepts(value): return ';' not in value\n")
    for args in (
        ("git", "init", "-q"),
        ("git", "config", "user.email", "test@example.com"),
        ("git", "config", "user.name", "Test"),
        ("git", "add", "src/guard.py"),
        ("git", "commit", "-q", "-m", "fixture"),
    ):
        subprocess.run(args, cwd=checkout, check=True)
    pin = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=checkout, check=True,
        capture_output=True, text=True,
    ).stdout.strip()
    return checkout, pin


def _registration(
    checkout, pin, *, cluster="demo-cluster", bucket="new-boundary",
    qualified_site=False,
):
    url = "https://github.com/example/demo"
    site = "src/guard.py:1:accepts"
    if qualified_site:
        site = f"example/demo@{pin}:{site}"
    contract = {
        "schema_version": "1", "site": site,
        "guarantee": "Accepted request values contain no semicolon.",
        "input_source": "untrusted query value", "trust": "untrusted-input",
        "declared_domain": "ASCII request values", "provenance": "agent_derived",
    }
    contract["adoption"] = build_adoption_record(
        contract,
        repository_url=url,
        pin=pin,
        checkout=checkout,
        source_file="src/guard.py",
        evidence=[f"{url}/blob/{pin}/src/guard.py", "caller: accepts(query.value)"],
        rationale="The caller and pinned validator define the request boundary.",
        author="agent-author", reviewer="agent-reviewer", same_model=True,
        approved_on="2026-10-13",
    )
    return build_registration(
        cluster=cluster, bucket=bucket, repository_url=url, pin=pin,
        checkout=checkout, product_engine="CPython re",
        trust_map={"untrusted-input": "query value from an external request"},
        source_sites=[site], question_family="request-allowlist-guard",
        max_candidates=8, registered_on="2026-10-13",
        rationale="A pinned product boundary and representative adopted contract support this idiom.",
        contract=contract, author="agent-author", reviewer="agent-reviewer",
        same_model=True,
    )


def test_registered_bucket_is_selected_for_go_cluster(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    entry = _registration(checkout, pin)
    registry_path = tmp_path / "registry.json"
    append_registration(entry, registry_path)
    assert load_registry(registry_path)["entries"] == [entry]

    decisions = tmp_path / "decisions"
    decisions.mkdir()
    (decisions / "demo-cluster_gate_decision.json").write_text(json.dumps({
        "corpus": "demo-cluster", "decision": "go", "corpus_pin": pin,
    }))
    spec = __import__("importlib.util").util.spec_from_file_location(
        "conversion_scheduler", ROOT / "scripts" / "conversion-scheduler.py"
    )
    scheduler = __import__("importlib.util").util.module_from_spec(spec)
    spec.loader.exec_module(scheduler)
    report = scheduler.build_schedule(
        [], queues_dir=tmp_path / "queues", gate_decisions_dir=decisions,
        dispositions_path=tmp_path / "dispositions.jsonl",
        bucket_registry_path=registry_path,
    )
    assert report["selections"][0]["selected_bucket"] == "new-boundary"
    assert report["registered_bucket_count"] == 1
    assert report["registered_bucket_rejections"] == []


def test_repository_qualified_site_resolves_to_checkout_relative_source(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    entry = _registration(checkout, pin, qualified_site=True)

    assert entry["source_sites"] == [f"example/demo@{pin}:src/guard.py:1:accepts"]
    assert entry["source_files"][0]["path"] == "src/guard.py"


def test_repository_qualified_site_rejects_mismatched_pin(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    other_pin = "a" * 40 if pin != "a" * 40 else "b" * 40
    site = f"example/demo@{other_pin}:src/guard.py:1:accepts"
    url = "https://github.com/example/demo"
    contract = {
        "schema_version": "1", "site": site,
        "guarantee": "Accepted request values contain no semicolon.",
        "input_source": "untrusted query value", "trust": "untrusted-input",
        "declared_domain": "ASCII request values", "provenance": "agent_derived",
    }
    contract["adoption"] = build_adoption_record(
        contract, repository_url=url, pin=pin, checkout=checkout,
        source_file="src/guard.py",
        evidence=[f"{url}/blob/{pin}/src/guard.py", "caller: accepts(query.value)"],
        rationale="The caller and pinned validator define the request boundary.",
        author="agent-author", reviewer="agent-reviewer", same_model=True,
        approved_on="2026-10-13",
    )
    with pytest.raises(BucketRegistryError, match="site repository or pin"):
        build_registration(
            cluster="demo-cluster", bucket="new-boundary",
            repository_url=url, pin=pin,
            checkout=checkout, product_engine="CPython re",
            trust_map={"untrusted-input": "query value from an external request"},
            source_sites=[site], question_family="request-allowlist-guard",
            max_candidates=8, registered_on="2026-10-13",
            rationale="A pinned product boundary and representative adopted contract support this idiom.",
            contract=contract,
            author="agent-author", reviewer="agent-reviewer", same_model=True,
        )


def test_registered_bucket_is_blocked_after_go_pin_changes(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    entry = _registration(checkout, pin)
    registry_path = tmp_path / "registry.json"
    append_registration(entry, registry_path)

    decisions = tmp_path / "decisions"
    decisions.mkdir()
    other_pin = "a" * 40 if pin != "a" * 40 else "b" * 40
    (decisions / "demo-cluster_gate_decision.json").write_text(json.dumps({
        "corpus": "demo-cluster", "decision": "go", "corpus_pin": other_pin,
    }))
    spec = __import__("importlib.util").util.spec_from_file_location(
        "conversion_scheduler", ROOT / "scripts" / "conversion-scheduler.py"
    )
    scheduler = __import__("importlib.util").util.module_from_spec(spec)
    spec.loader.exec_module(scheduler)
    report = scheduler.build_schedule(
        [], queues_dir=tmp_path / "queues", gate_decisions_dir=decisions,
        dispositions_path=tmp_path / "dispositions.jsonl",
        bucket_registry_path=registry_path,
    )
    assert report["selections"][0]["selected_bucket"] is None
    assert report["selections"][0]["selection_basis"] == "registered-pin-mismatch"
    assert report["registered_bucket_rejections"] == [{
        "cluster": "demo-cluster", "bucket": "new-boundary",
        "reason": "current-go-pin-missing-or-mismatched",
    }]


def test_stopped_cluster_and_duplicate_family_are_rejected(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    with pytest.raises(BucketRegistryError, match="stopped"):
        _registration(checkout, pin, cluster="openwrt_packages")

    registry_path = tmp_path / "registry.json"
    append_registration(_registration(checkout, pin), registry_path)
    duplicate = _registration(checkout, pin, bucket="renamed-same-family")
    with pytest.raises(BucketRegistryError, match="duplicate question family"):
        append_registration(duplicate, registry_path)


def test_cli_requires_go_decision_and_verifies_source_pin(tmp_path):
    checkout, pin = _source_repo(tmp_path)
    decision = tmp_path / "gate.json"
    decision.write_text(json.dumps({
        "corpus": "demo-cluster", "decision": "triage-trial", "corpus_pin": pin,
    }))
    contract = _registration(checkout, pin)
    contract_path = tmp_path / "contract.json"
    # `build_registration` is also the strict validator used by the CLI; the
    # test exercises the Go-status guard before a registry write.
    contract_path.write_text(json.dumps({
        "schema_version": "1", "site": contract["contract_site"],
    }))
    command = [
        sys.executable, str(ROOT / "scripts" / "register-conversion-bucket.py"),
        "--cluster", "demo-cluster", "--bucket", "new-boundary",
        "--repository-url", "https://github.com/example/demo", "--pin", pin,
        "--checkout", str(checkout), "--gate-decision", str(decision),
        "--product-engine", "CPython re", "--trust-map", "untrusted-input=query",
        "--source-site", "src/guard.py:1:accepts", "--question-family", "query-guard",
        "--max-candidates", "8", "--registered-on", "2026-10-13",
        "--rationale", "source-backed family", "--contract", str(contract_path),
        "--author", "a", "--reviewer", "b", "--same-model",
        "--registry", str(tmp_path / "registry.json"),
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 2
    assert "gated:go" in result.stderr
    assert not (tmp_path / "registry.json").exists()
