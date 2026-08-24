"""Wave 7 (#576): probe_success_rate vs escape-window survivor."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import pytest

from regexproof.mine import batch_state
from regexproof.mine.escape_window import escape_window

PIN_A = "a" * 40
PIN_B = "b" * 40
NOW = dt.datetime(2026, 8, 24, 12, 0, tzinfo=dt.timezone.utc)


def _state(tmp_path: Path) -> Path:
    p = tmp_path / "state.json"
    batch_state.begin_item("d1", "https://x/y", PIN_A, at="2026-08-24T11:00:00+00:00", path=p)
    batch_state.record_outcome(
        "d1", "https://x/y", PIN_A, "ok",
        extra={"cache_hit": False, "clone_ms": 10, "completed_at": "2026-08-24T11:00:05+00:00"},
        path=p,
    )
    batch_state.begin_item("d1", "https://x/z", PIN_B, at="2026-08-24T11:01:00+00:00", path=p)
    batch_state.record_outcome(
        "d1", "https://x/z", PIN_B, "clone_timeout",
        extra={"cache_hit": False, "clone_ms": 300000, "completed_at": "2026-08-24T11:06:00+00:00"},
        path=p,
    )
    return p


def _baseline(tmp_path: Path) -> Path:
    path = tmp_path / "escape_baseline.json"
    path.write_text(
        json.dumps({"survivor_rate": 0.143365, "n": 844, "survivors": 121}) + "\n",
        encoding="utf-8",
    )
    return path


def _decision(gen: Path, url: str, pin: str, decision: str) -> None:
    stem = url.rsplit("/", 1)[-1]
    payload = {
        "candidate_url": url,
        "corpus_pin": pin,
        "decision": decision,
        "decision_date": "2026-08-24",
    }
    (gen / f"{stem}_gate_decision.json").write_text(
        json.dumps(payload) + "\n", encoding="utf-8"
    )


def test_empty_state_does_not_use_gate_files_as_denominator(tmp_path: Path):
    """n=0 even when gate files exist — never a gate-only window."""
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    result = escape_window(
        state_path=tmp_path / "missing-state.json",
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    assert result["n_window"] == 0
    assert result["k_window"] == 0
    assert result["rate"] is None
    assert result["fires"] is None


def test_window_joins_admitted_decisions_over_probes(tmp_path: Path):
    state = _state(tmp_path)
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    _decision(gen, "https://x/z", PIN_B, "no-go")
    result = escape_window(
        state_path=state,
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    # Both probes count (ok + clone_timeout). Only the GO is a survivor.
    assert result["n_window"] == 2
    assert result["k_window"] == 1
    assert result["rate"] == 0.5
    assert result["fires"] is False  # 1/2 is above the 14.3% baseline


def test_incomplete_rows_are_excluded(tmp_path: Path):
    p = tmp_path / "state.json"
    batch_state.begin_item("d1", "https://x/y", PIN_A, at="2026-08-24T11:00:00+00:00", path=p)
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    result = escape_window(
        state_path=p,
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    assert result["n_window"] == 0
    assert result["rate"] is None


def test_unreadable_gate_decision_fails_closed(tmp_path: Path):
    state = _state(tmp_path)
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    (gen / "broken_gate_decision.json").write_text("{not json", encoding="utf-8")
    with pytest.raises(SystemExit, match="unreadable/invalid"):
        escape_window(
            state_path=state,
            gen=gen,
            baseline_path=_baseline(tmp_path),
            now=NOW,
        )


def test_duplicate_url_pin_keeps_newer_decision(tmp_path: Path):
    state = _state(tmp_path)
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "no-go")
    newer = {
        "candidate_url": "https://x/y",
        "corpus_pin": PIN_A,
        "decision": "go",
        "decision_date": "2026-08-24",
        "updated_at": "2026-08-24T11:00:00+00:00",
    }
    (gen / "y_newer_gate_decision.json").write_text(
        json.dumps(newer) + "\n", encoding="utf-8"
    )
    # older file used decision_date 2026-08-24 without time — parse as midnight.
    # Give the first file an older date.
    older = json.loads((gen / "y_gate_decision.json").read_text(encoding="utf-8"))
    older["decision_date"] = "2026-08-23"
    (gen / "y_gate_decision.json").write_text(json.dumps(older) + "\n", encoding="utf-8")
    result = escape_window(
        state_path=state,
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    assert result["k_window"] == 1


def test_duplicate_url_pin_equal_recency_keeps_last_sorted_file(tmp_path: Path):
    """Freeze supersession: equal recency → last sorted path wins."""
    state = _state(tmp_path)
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    (gen / "zzz_y_dup_gate_decision.json").write_text(
        json.dumps({
            "candidate_url": "https://x/y",
            "corpus_pin": PIN_A,
            "decision": "no-go",
            "decision_date": "2026-08-24",
        }) + "\n",
        encoding="utf-8",
    )
    result = escape_window(
        state_path=state,
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    # y_dup sorts after y_gate_decision → no-go wins → k_window 0 for y.
    assert result["k_window"] == 0


def test_indexes_committed_gate_decisions():
    """Default checkout must not abort on real equal-recency aliases (#584 Luna)."""
    from regexproof.mine.escape_window import _index_decisions

    indexed = _index_decisions(Path("properties/generated"))
    assert len(indexed) > 100


def test_rows_outside_window_are_excluded(tmp_path: Path):
    p = tmp_path / "state.json"
    batch_state.begin_item("d1", "https://x/y", PIN_A, at="2026-08-01T00:00:00+00:00", path=p)
    batch_state.record_outcome(
        "d1", "https://x/y", PIN_A, "ok",
        extra={"completed_at": "2026-08-01T00:00:01+00:00"},
        path=p,
    )
    gen = tmp_path / "gen"
    gen.mkdir()
    _decision(gen, "https://x/y", PIN_A, "go")
    result = escape_window(
        state_path=p,
        gen=gen,
        baseline_path=_baseline(tmp_path),
        now=NOW,
    )
    assert result["n_window"] == 0
