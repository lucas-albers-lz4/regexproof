"""The autonomous run recorder persists exact site/question accounting."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from regexproof.mine.autonomous_work import load_rows

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "record_autonomous_run", ROOT / "scripts" / "record-autonomous-run.py"
)
assert SPEC is not None and SPEC.loader is not None
CLI = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLI)


def _args(log: Path, work_items: Path) -> list[str]:
    return [
        "--run-id", "run-with-identities",
        "--agent", "codex",
        "--model", "gpt-6",
        "--cohort-id", "test-cohort",
        "--manifest-digest", "a" * 64,
        "--repo-id", "example/demo",
        "--repository-url", "https://github.com/example/demo",
        "--source-pin", "b" * 40,
        "--wave-id", "wave-1",
        "--started-at", "2026-10-15T10:00:00Z",
        "--completed-at", "2026-10-15T10:00:02Z",
        "--reviewed-sites", "1",
        "--proof-questions-attempted", "1",
        "--work-items", str(work_items),
        "--log", str(log),
    ]


def test_recorder_writes_v3_identity_row(tmp_path, monkeypatch, capsys):
    log = tmp_path / "autonomous.jsonl"
    work_items = tmp_path / "work-items.json"
    work_items.write_text(json.dumps([{
        "site": "src/guard.py:1:pattern",
        "reviewed": True,
        "question_ids": ["q-no-semicolon"],
    }]), encoding="utf-8")
    monkeypatch.setattr(CLI, "LOG_PATH", log)

    assert CLI.main(_args(log, work_items)) == 0
    capsys.readouterr()
    row = load_rows(log)[0]
    assert row["schema_version"] == "3"
    assert row["work_items"] == [{
        "site": "src/guard.py:1:pattern",
        "reviewed": True,
        "question_ids": ["q-no-semicolon"],
    }]


def test_recorder_rejects_missing_work_items_for_attempted_question(tmp_path, monkeypatch):
    log = tmp_path / "autonomous.jsonl"
    work_items = tmp_path / "work-items.json"
    work_items.write_text("[]\n", encoding="utf-8")
    monkeypatch.setattr(CLI, "LOG_PATH", log)
    args = _args(log, work_items)
    args.remove("--work-items")
    args.remove(str(work_items))

    assert CLI.main(args) == 2
    assert not log.exists()
