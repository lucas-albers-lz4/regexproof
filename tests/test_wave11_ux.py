"""Wave 11 (#580): operator UX — gitignore, pipeline-status, probe CLI, ready-to-file."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from regexproof.mine.pipeline_status import render_status, render_weekly, snapshot
from regexproof.probe.cli import main as probe_main

ROOT = Path(__file__).resolve().parents[1]


def _empty_stores(tmp_path: Path) -> tuple[Path, Path, Path]:
    ledger = tmp_path / "ledger.json"
    queue = tmp_path / "queue.json"
    conv = tmp_path / "conv.json"
    ledger.write_text(json.dumps({"candidates": []}) + "\n", encoding="utf-8")
    queue.write_text(json.dumps({"items": []}) + "\n", encoding="utf-8")
    conv.write_text(
        json.dumps({"starvation": {}, "per_wave": []}) + "\n", encoding="utf-8"
    )
    return ledger, queue, conv


def test_staged_probes_gitignored_and_walker_guard_stays():
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "properties/staged_probes/" in gi
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "ci-check-probe-walkers.py" in ci
    daily = (ROOT / ".github" / "workflows" / "daily-mine.yml").read_text(
        encoding="utf-8"
    )
    assert "pipeline-status.py --weekly" in daily
    assert (ROOT / "docs" / "PIPELINE.md").is_file()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "docs/PIPELINE.md" in readme
    assert "pipeline-status.py" in readme


def test_pipeline_status_snapshot(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "conversion-ledger.json").write_text(
        json.dumps(
            {
                "starvation": {
                    "mine_queue_pressure": 0.5,
                    "mine_queue_len": 50,
                    "mine_queue_cap": 100,
                    "backlog_weeks": 4.0,
                    "demand_open_gated_go_no_closed_wave": 8,
                    "admission_per_week": 2,
                },
                "per_wave": [
                    {
                        "wave_id": "w1",
                        "idiom_bucket": "demo",
                        "properties_asked": 5,
                        "properties_sat": 1,
                        "sat_ground_truthed": 1,
                        "filed": 0,
                        "accepted": 0,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (gen / "candidate-ledger.json").write_text(
        json.dumps(
            {
                "candidates": [
                    {
                        "first_seen": "2026-08-20T12:00:00Z",
                        "audit": {"needs_human_review": True},
                    },
                    {
                        "first_seen": "2026-08-20T13:00:00Z",
                        "audit": {"needs_human_review": False},
                    },
                    {
                        "first_seen": "2026-08-19T01:00:00Z",
                        "audit": {"needs_human_review": False},
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    (gen / "mine-queue.json").write_text(
        json.dumps({"items": [{}] * 50}), encoding="utf-8"
    )
    (gen / "demo_gate_decision.json").write_text(
        json.dumps(
            {
                "decision": "no-go",
                "decision_basis": "admission_conditions",
                "conditions": [
                    {"id": "below-scale", "met": False},
                    {"id": "new-surface", "met": True},
                ],
            }
        ),
        encoding="utf-8",
    )
    (gen / "escape_baseline.json").write_text(
        json.dumps({"survivor_rate": 0.14}), encoding="utf-8"
    )
    state = tmp_path / "state.json"
    snap = snapshot(
        generated=gen,
        state_path=state,
        ledger_path=gen / "candidate-ledger.json",
        queue_path=gen / "mine-queue.json",
        conversion_ledger=gen / "conversion-ledger.json",
        baseline_path=gen / "escape_baseline.json",
    )
    assert snap["latest_mine_day_drain"] == {"date": "2026-08-20", "admitted": 2}
    assert snap["queue_pressure"] == 0.5
    assert snap["backlog_weeks"] == 4.0
    assert snap["needs_human_backlog"] == 1
    assert snap["nogo_dominant"] == "below-scale"
    assert snap["hops"][0]["wave_id"] == "w1"
    text = render_status(snap)
    assert "latest mine-day drain: 2" in text
    assert "backlog weeks: 4.0" in text
    weekly = render_weekly(snap)
    assert "What changed this week" in weekly
    assert "below-scale=1" in weekly


def test_injected_missing_state_does_not_use_default(tmp_path: Path, monkeypatch):
    seen: dict = {}

    def fake_escape(**kwargs):
        seen.update(kwargs)
        return {
            "n_window": 0,
            "k_window": 0,
            "rate": None,
            "baseline": 0.14,
            "fires": None,
        }

    monkeypatch.setattr(
        "regexproof.mine.pipeline_status.escape_window.escape_window",
        fake_escape,
    )
    missing = tmp_path / "absent-state.json"
    baseline = tmp_path / "absent-baseline.json"
    ledger, queue, conv = _empty_stores(tmp_path)
    snapshot(
        generated=tmp_path,
        state_path=missing,
        ledger_path=ledger,
        queue_path=queue,
        conversion_ledger=conv,
        baseline_path=baseline,
    )
    assert seen["state_path"] == missing
    assert seen["baseline_path"] == baseline


def test_corrupt_gate_decision_fails_closed(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "bad_gate_decision.json").write_text("{not json", encoding="utf-8")
    (gen / "escape_baseline.json").write_text(
        json.dumps({"survivor_rate": 0.14}), encoding="utf-8"
    )
    ledger, queue, conv = _empty_stores(tmp_path)
    with pytest.raises(SystemExit, match="unreadable/invalid"):
        snapshot(
            generated=gen,
            state_path=tmp_path / "state.json",
            ledger_path=ledger,
            queue_path=queue,
            conversion_ledger=conv,
            baseline_path=gen / "escape_baseline.json",
        )


def test_missing_baseline_fails_closed(tmp_path: Path):
    ledger, queue, conv = _empty_stores(tmp_path)
    with pytest.raises(OSError):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=ledger,
            queue_path=queue,
            conversion_ledger=conv,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_missing_conversion_ledger_fails_closed(tmp_path: Path):
    ledger, queue, _conv = _empty_stores(tmp_path)
    missing = tmp_path / "absent-conv.json"
    with pytest.raises(SystemExit, match="missing"):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=ledger,
            queue_path=queue,
            conversion_ledger=missing,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_schema_empty_object_fails_closed(tmp_path: Path):
    ledger, queue, _conv = _empty_stores(tmp_path)
    bad = tmp_path / "bad-conv.json"
    bad.write_text("{}\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="missing object field"):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=ledger,
            queue_path=queue,
            conversion_ledger=bad,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_malformed_ledger_fails_closed(tmp_path: Path):
    _ledger, queue, conv = _empty_stores(tmp_path)
    bad = tmp_path / "ledger.json"
    bad.write_text("{not json", encoding="utf-8")
    with pytest.raises(SystemExit, match="unreadable/invalid"):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=bad,
            queue_path=queue,
            conversion_ledger=conv,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_non_file_ledger_fails_closed(tmp_path: Path):
    _ledger, queue, conv = _empty_stores(tmp_path)
    d = tmp_path / "ledger-dir"
    d.mkdir()
    with pytest.raises(SystemExit, match="not a regular file"):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=d,
            queue_path=queue,
            conversion_ledger=conv,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_invalid_utf8_ledger_fails_closed(tmp_path: Path):
    _ledger, queue, conv = _empty_stores(tmp_path)
    bad = tmp_path / "ledger.json"
    bad.write_bytes(b"\xff\xfe{")
    with pytest.raises(SystemExit, match="unreadable/invalid"):
        snapshot(
            generated=tmp_path,
            state_path=tmp_path / "state.json",
            ledger_path=bad,
            queue_path=queue,
            conversion_ledger=conv,
            baseline_path=tmp_path / "no-baseline.json",
        )


def test_probe_cli_help():
    assert probe_main(["--help"]) == 0
    assert probe_main(["--single", "--help"]) == 0


def test_probe_cli_forwards_args_before_mode(monkeypatch):
    seen: dict = {}

    class _Fake:
        @staticmethod
        def main(argv):
            seen["argv"] = list(argv)
            seen["env"] = os.environ.get("REGEXPROOF_PROBE_CANONICAL")
            return 0

    monkeypatch.setattr(
        "regexproof.probe.cli._load_script", lambda _name: _Fake()
    )
    assert (
        probe_main(["--url", "https://example.com/r", "--pin", "abc", "--batch"])
        == 0
    )
    assert seen["argv"] == ["--url", "https://example.com/r", "--pin", "abc"]
    assert seen["env"] == "1"
    assert "REGEXPROOF_PROBE_CANONICAL" not in os.environ


def test_probe_cli_rejects_both_modes(capsys):
    with pytest.raises(SystemExit) as excinfo:
        probe_main(["--single", "--batch"])
    assert excinfo.value.code == 2
    assert "mutually exclusive" in capsys.readouterr().err


def test_probe_cli_prints_string_systemexit(monkeypatch, capsys):
    class _Fake:
        @staticmethod
        def main(_argv):
            raise SystemExit("batch_state: corrupt — fail closed")

    monkeypatch.setattr(
        "regexproof.probe.cli._load_script", lambda _name: _Fake()
    )
    assert probe_main(["--batch", "--url", "u", "--pin", "p"]) == 1
    assert "corrupt — fail closed" in capsys.readouterr().err


def test_z3_verify_help():
    from regexproof.harness.cli import main

    assert main(["--help"]) == 0
