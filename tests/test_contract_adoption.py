"""Source-pinned autonomous contract adoption policy tests."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.contract_adoption import (
    build_adoption_record,
    contract_is_adopted,
    valid_adoption_record,
    verify_adoption_source,
)
from regexproof.harness.contract import valid_product_contract

ROOT = Path(__file__).resolve().parents[1]


def _contract(site="src/guard.py:1:0"):
    return {
        "schema_version": "1",
        "site": site,
        "guarantee": "The accepted value cannot contain a shell separator.",
        "input_source": "untrusted request field",
        "trust": "untrusted-input",
        "declared_domain": "ASCII values accepted by validate_name",
        "provenance": "agent_derived",
    }


def _git(*args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def _checkout(tmp_path):
    root = tmp_path / "source"
    (root / "src").mkdir(parents=True)
    (root / "src" / "guard.py").write_text("def validate_name(value): return value\n")
    _git("init", "-q", cwd=root)
    _git("config", "user.email", "test@example.com", cwd=root)
    _git("config", "user.name", "Test", cwd=root)
    _git("add", "src/guard.py", cwd=root)
    _git("commit", "-q", "-m", "fixture", cwd=root)
    return root, _git("rev-parse", "HEAD", cwd=root)


def _build(root, pin, contract=None):
    url = "https://github.com/example/project"
    path = "src/guard.py"
    return build_adoption_record(
        contract or _contract(),
        repository_url=url,
        pin=pin,
        checkout=root,
        source_file=path,
        evidence=[f"{url}/blob/{pin}/{path}", "caller: validate_name is used for request input"],
        rationale="The source and caller establish the accepted input boundary.",
        author="luna-agent",
        reviewer="independent-review-pass",
        same_model=True,
        approved_on="2026-10-13",
    )


def test_adoption_binds_exact_commit_source_and_contract(tmp_path):
    root, pin = _checkout(tmp_path)
    contract = _contract()
    record = _build(root, pin, contract)
    adopted = {**contract, "adoption": record}
    assert valid_adoption_record(record, adopted)
    assert valid_product_contract(adopted)
    assert contract_is_adopted(adopted)
    assert verify_adoption_source(adopted, root)

    edited_contract = {**adopted, "guarantee": "a different guarantee"}
    assert not valid_product_contract(edited_contract)

    stale = {**record, "source_pin": "b" * 40}
    assert not valid_adoption_record(stale, adopted)


def test_source_verifier_rejects_dirty_or_wrong_pin_checkout(tmp_path):
    root, pin = _checkout(tmp_path)
    contract = _contract()
    contract["adoption"] = _build(root, pin, contract)
    other_root, _ = _checkout(tmp_path / "other")
    (other_root / "src" / "guard.py").write_text("# a different pin\n")
    _git("add", "src/guard.py", cwd=other_root)
    _git("commit", "-q", "-m", "different pin", cwd=other_root)
    with pytest.raises(ValueError, match="does not match contract pin"):
        verify_adoption_source(contract, other_root)

    (root / "src" / "guard.py").write_text("# modified after adoption\n")
    with pytest.raises(ValueError, match="working-tree bytes differ"):
        verify_adoption_source(contract, root)


def test_builder_rejects_wrong_pin_dirty_source_and_unsafe_paths(tmp_path):
    root, pin = _checkout(tmp_path)
    with pytest.raises(ValueError, match="does not match"):
        _build(root, "b" * 40)
    (root / "src" / "guard.py").write_text("# changed after commit\n")
    with pytest.raises(ValueError, match="differ from the pinned commit"):
        _build(root, pin)
    (root / "src" / "guard.py").write_text("def validate_name(value): return value\n")
    with pytest.raises(ValueError, match="safe checkout-relative"):
        build_adoption_record(
            _contract(), repository_url="https://github.com/example/project",
            pin=pin, checkout=root, source_file="../outside.py", evidence=[],
            rationale="rationale", author="a", reviewer="b", same_model=True,
            approved_on="2026-10-13",
        )


def test_historical_human_contract_does_not_need_adoption_and_draft_does_not_count():
    human = {**_contract(), "provenance": "human"}
    assert contract_is_adopted(human)
    assert not contract_is_adopted({**_contract(), "provenance": "agent_derived"})


def test_cli_writes_only_after_source_and_schema_validation(tmp_path):
    root, pin = _checkout(tmp_path)
    contract_path = tmp_path / "contract.json"
    contract_path.write_text(json.dumps(_contract(), indent=2) + "\n")
    command = [
        sys.executable, str(ROOT / "scripts" / "adopt-property-contract.py"),
        "--contract", str(contract_path),
        "--repository-url", "https://github.com/example/project",
        "--pin", pin, "--checkout", str(root), "--source-file", "src/guard.py",
        "--evidence", f"https://github.com/example/project/blob/{pin}/src/guard.py",
        "--evidence", "caller: request value reaches validate_name",
        "--rationale", "The pinned source and caller support the guarantee.",
        "--author", "luna-agent", "--reviewer", "review-pass",
        "--same-model", "--approved-on", "2026-10-13",
    ]
    completed = subprocess.run(command, capture_output=True, text=True)
    assert completed.returncode == 0, completed.stderr
    adopted = json.loads(contract_path.read_text())
    assert valid_product_contract(adopted)
    original = contract_path.read_text()

    command[command.index("--pin") + 1] = "c" * 40
    completed = subprocess.run(command, capture_output=True, text=True)
    assert completed.returncode == 2
    assert contract_path.read_text() == original
