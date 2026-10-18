"""CLI integration for pinned conversion-queue state transitions."""

from __future__ import annotations

import importlib.util
import json
import pathlib
import subprocess

from regexproof.contract_adoption import build_adoption_record
from regexproof.mine import conversion_queue as cq
from regexproof.mine.corpus_lock import wave_abort, wave_close, wave_open

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "conversion_queue_transition",
    ROOT / "scripts" / "conversion-queue-transition.py",
)
assert SPEC is not None and SPEC.loader is not None
CLI = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLI)
PIN = "a" * 40
URL = "https://github.com/example/project"
SITE = "src/guard.py:1:0"


def _git(*args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True,
        timeout=10,
    ).stdout.strip()


def _fixture(tmp_path, *, count=1):
    source = tmp_path / "source"
    (source / "src").mkdir(parents=True)
    source_file = source / "src" / "guard.py"
    source_file.write_text("def validate_name(value): return value\n")
    _git("init", "-q", cwd=source)
    _git("config", "user.email", "test@example.com", cwd=source)
    _git("config", "user.name", "Test", cwd=source)
    _git("add", "src/guard.py", cwd=source)
    _git("commit", "-q", "-m", "fixture", cwd=source)
    pin = _git("rev-parse", "HEAD", cwd=source)
    queue_dir = tmp_path / "queue"
    ranked = [
        {
            "site": SITE if i == 1 else f"src/guard.py:{i}:0",
            "corpus": "sample",
            "pin": pin,
            "idiom_bucket": "input-guard",
            "provenance": "stub",
        }
        for i in range(1, count + 1)
    ]
    cq.emit(
        "sample", wave_id="sample-w1", generation=0, ranked=ranked,
        root=queue_dir, clock_iso="2026-10-15T00:00:00Z",
    )
    events = tmp_path / "events.jsonl"
    wave_open("sample", "sample-w1", log=events)
    decision = tmp_path / "decision.json"
    decision.write_text(json.dumps({
        "schema_version": "1", "corpus": "sample", "decision": "go",
        "corpus_pin": pin, "candidate_url": URL,
    }) + "\n")
    ledger = tmp_path / "conversion-ledger.json"
    ledger.write_text(json.dumps({"schema_version": "1", "per_wave": []}) + "\n")
    return source, pin, queue_dir, events, decision, ledger


def _claim_args(queue_dir, events, decision, ledger, site=SITE):
    return [
        "claim", "--cluster", "sample", "--site", site,
        "--gate-decision", str(decision), "--conversion-ledger", str(ledger),
        "--queue-dir", str(queue_dir), "--events-log", str(events),
    ]


def _agent_contract(source, pin):
    contract = {
        "schema_version": "1",
        "site": SITE,
        "guarantee": "The accepted value cannot contain a shell separator.",
        "input_source": "untrusted request field",
        "trust": "untrusted-input",
        "declared_domain": "ASCII values accepted by validate_name",
        "provenance": "agent_derived",
    }
    contract["adoption"] = build_adoption_record(
        contract,
        repository_url=URL,
        pin=pin,
        checkout=source,
        source_file="src/guard.py",
        evidence=[
            f"{URL}/blob/{pin}/src/guard.py",
            "caller: request value reaches validate_name",
        ],
        rationale="Pinned source and caller establish the boundary.",
        author="luna-agent",
        reviewer="independent-review-pass",
        same_model=True,
        approved_on="2026-10-15",
    )
    return contract


def test_cli_claim_binds_pin_gate_and_conversion_ledger_snapshot(tmp_path, capsys):
    _, pin, queue_dir, events, decision, ledger = _fixture(tmp_path)
    assert CLI.main(_claim_args(queue_dir, events, decision, ledger)) == 0
    claimed = cq.load_queue("sample", root=queue_dir)["candidate_sites"][0]
    assert claimed["status"] == "claimed"
    snapshot = claimed["ledger_state_at_claim"]
    assert snapshot["n"] == 0
    assert len(snapshot["conversion_ledger_sha256"]) == 64
    assert len(snapshot["gate_decision_sha256"]) == 64
    assert snapshot["source_pin"] == pin
    assert snapshot["repository_url"] == URL
    assert json.loads(capsys.readouterr().out)["status"] == "claimed"


def test_cli_claim_rejects_stale_gate_pin_without_changing_queue(tmp_path):
    _, _, queue_dir, events, decision, ledger = _fixture(tmp_path)
    value = json.loads(decision.read_text())
    value["corpus_pin"] = "f" * 40
    decision.write_text(json.dumps(value) + "\n")
    assert CLI.main(_claim_args(queue_dir, events, decision, ledger)) == 2
    assert cq.load_queue("sample", root=queue_dir)["candidate_sites"][0]["status"] == "emitted"


def test_cli_contract_verifies_adoption_source_before_locked_transition(tmp_path):
    source, pin, queue_dir, events, decision, ledger = _fixture(tmp_path)
    assert CLI.main(_claim_args(queue_dir, events, decision, ledger)) == 0
    contract_path = tmp_path / "contract.json"
    contract_path.write_text(json.dumps(_agent_contract(source, pin)) + "\n")
    args = [
        "contract", "--cluster", "sample", "--site", SITE,
        "--contract", str(contract_path), "--checkout", str(source),
        "--queue-dir", str(queue_dir), "--events-log", str(events),
    ]
    assert CLI.main(args) == 0
    row = cq.load_queue("sample", root=queue_dir)["candidate_sites"][0]
    assert row["status"] == "contracted"
    assert row["provenance"] == "agent_derived"
    assert row["contract"]["adoption"]["source_pin"] == pin


def test_cli_contract_rejects_modified_source_checkout(tmp_path):
    source, pin, queue_dir, events, decision, ledger = _fixture(tmp_path)
    assert CLI.main(_claim_args(queue_dir, events, decision, ledger)) == 0
    contract_path = tmp_path / "contract.json"
    contract_path.write_text(json.dumps(_agent_contract(source, pin)) + "\n")
    (source / "src" / "guard.py").write_text("# changed after adoption\n")
    args = [
        "contract", "--cluster", "sample", "--site", SITE,
        "--contract", str(contract_path), "--checkout", str(source),
        "--queue-dir", str(queue_dir), "--events-log", str(events),
    ]
    assert CLI.main(args) == 2
    assert cq.load_queue("sample", root=queue_dir)["candidate_sites"][0]["status"] == "claimed"


def test_cli_skip_requires_active_wave_and_closes_only_after_disposition(tmp_path):
    _, _, queue_dir, events, _, _ = _fixture(tmp_path)
    args = [
        "skip", "--cluster", "sample", "--site", SITE,
        "--reason", "out_of_scope", "--note", "Source path ends in a diagnostic sink.",
        "--queue-dir", str(queue_dir), "--events-log", str(events),
    ]
    assert CLI.main(args) == 0
    q = cq.load_queue("sample", root=queue_dir)
    assert q["candidate_sites"][0]["status"] == "skipped_out_of_scope"
    assert cq.non_contracted_top15(q) == []
    generation = wave_close("sample", "sample-w1", queue_root=queue_dir, log=events)
    assert generation == 1


def test_cli_skip_refuses_after_wave_abort(tmp_path):
    _, _, queue_dir, events, _, _ = _fixture(tmp_path)
    wave_abort("sample", "sample-w1", reason="fixture abort", log=events)
    args = [
        "skip", "--cluster", "sample", "--site", SITE,
        "--reason", "out_of_scope", "--note", "Reviewed and out of scope.",
        "--queue-dir", str(queue_dir), "--events-log", str(events),
    ]
    assert CLI.main(args) == 2
    assert cq.load_queue("sample", root=queue_dir)["candidate_sites"][0]["status"] == "emitted"
