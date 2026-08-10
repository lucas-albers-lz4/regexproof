"""Foundation tests for mining ledger (P2 B0–B1)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.mine.ledger import (
    empty_ledger,
    load_ledger,
    save_ledger,
    set_crash_before_replace,
)
from regexproof.mine.transition import TransitionError, transition_candidate

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "properties" / "generated" / "candidate-ledger.json"


def _sample_candidate(**overrides):
    base = {
        "url": "https://github.com/example/corpus",
        "default_branch": "main",
        "pin": "abc123def456",
        "pushed_date": "2026-08-01",
        "stars": 10,
        "source_query": "filename:gitleaks.toml",
        "first_seen": "2026-08-09T00:00:00Z",
        "status": "mined",
    }
    base.update(overrides)
    return base


def test_committed_scaffold_shape():
    """Committed ledger is schema v1; may be empty or hold live mine admits."""
    data = json.loads(SCAFFOLD.read_text(encoding="utf-8"))
    assert data["schema_version"] == "1"
    assert isinstance(data["candidates"], list)
    required = {
        "url",
        "default_branch",
        "pin",
        "pushed_date",
        "stars",
        "source_query",
        "first_seen",
        "status",
    }
    for cand in data["candidates"]:
        assert required.issubset(cand.keys())
        assert cand["status"] in {"mined", "queued"}
        assert isinstance(cand["url"], str) and cand["url"]
        assert isinstance(cand["stars"], int)


def test_save_load_round_trip(tmp_path: Path):
    path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"].append(_sample_candidate())
    save_ledger(path, ledger)
    loaded = load_ledger(path)
    assert loaded["candidates"][0]["url"] == "https://github.com/example/corpus"
    assert loaded["candidates"][0]["pin"] == "abc123def456"


def test_crash_before_replace_leaves_prior_intact(tmp_path: Path):
    path = tmp_path / "candidate-ledger.json"
    prior = empty_ledger()
    prior["candidates"].append(_sample_candidate(url="https://github.com/example/prior"))
    save_ledger(path, prior)
    prior_bytes = path.read_bytes()

    def boom() -> None:
        raise RuntimeError("simulated crash")

    set_crash_before_replace(boom)
    try:
        new = empty_ledger()
        new["candidates"].append(_sample_candidate(url="https://github.com/example/new"))
        with pytest.raises(RuntimeError, match="simulated crash"):
            save_ledger(path, new)
        assert path.read_bytes() == prior_bytes
    finally:
        set_crash_before_replace(None)


def test_transition_requeue_preserves_audit_and_fields(tmp_path: Path):
    path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    cand = _sample_candidate(status="mined")
    cand["audit"] = {"auto_filed": True, "template_fired": "below-scale"}
    ledger["candidates"].append(cand)
    save_ledger(path, ledger)

    out = transition_candidate(
        path,
        cand["url"],
        to="queued",
        reason="audit-sampler-fail",
    )
    assert out["status"] == "queued"
    assert out["pin"] == cand["pin"]
    assert out["stars"] == cand["stars"]
    assert out["audit"]["auto_filed"] is True
    assert out["audit"]["template_fired"] == "below-scale"
    assert out["audit"]["transitions"][-1]["to"] == "queued"

    reloaded = load_ledger(path)
    assert reloaded["candidates"][0]["status"] == "queued"
    assert reloaded["candidates"][0]["audit"]["auto_filed"] is True


def test_transition_rejects_illegal_and_missing(tmp_path: Path):
    path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"].append(_sample_candidate(status="queued"))
    save_ledger(path, ledger)

    with pytest.raises(TransitionError, match="not in ledger"):
        transition_candidate(path, "https://github.com/missing/repo", to="queued")

    with pytest.raises(TransitionError, match="not P2-owned"):
        transition_candidate(
            path,
            "https://github.com/example/corpus",
            to="auto-filed",
        )
