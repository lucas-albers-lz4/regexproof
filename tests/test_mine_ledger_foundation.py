"""Foundation tests for mining ledger (P2 B0–B1)."""

from __future__ import annotations

import importlib.util
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
        assert cand["status"] in {"mined", "queued", "gated:go", "gated:no-go", "gated:triage-trial"}
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


def test_sync_through_api_persists_gated_status(tmp_path: Path):
    """sync_gate_decisions applies transitions; final persisted state shows gated:*."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "mine_cli", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()

    ledger = empty_ledger()
    ledger["candidates"].append(
        _sample_candidate(
            url="https://github.com/acme/target-repo",
            status="mined",
        )
    )
    save_ledger(ledger_path, ledger)

    # Write a gate decision file
    (gen / "target-repo_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "target-repo",
                "candidate_url": "https://github.com/acme/target-repo",
                "decision": "no-go",
            }
        ),
        encoding="utf-8",
    )

    synced = mod.sync_gate_decisions(ledger_path, gen)
    assert synced == 1

    # The FINAL persisted state must carry gated:no-go
    final = load_ledger(ledger_path)
    cand = final["candidates"][0]
    assert cand["status"] == "gated:no-go"
    assert cand["audit"]["transitions"][-1]["to"] == "gated:no-go"


def test_main_sequence_reload_after_sync_prevents_stale_save(tmp_path: Path):
    """Red/green for the stale-save regression (luna re-gate 2).

    main() previously loaded the ledger BEFORE sync_gate_decisions(), then
    saved that pre-sync object AFTER the sync — overwriting the transitions.
    The fix reloads from disk after the sync. Prove both directions.
    """
    spec = importlib.util.spec_from_file_location(
        "mine_corpus_candidates", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sync_gate_decisions = mod.sync_gate_decisions
    sync_and_reload = mod.sync_and_reload

    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    ledger["candidates"].append(
        _sample_candidate(
            url="https://github.com/acme/stale-save",
            status="mined",
        )
    )
    save_ledger(ledger_path, ledger)
    (gen / "stale-save_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "stale-save",
                "candidate_url": "https://github.com/acme/stale-save",
                "decision": "no-go",
            }
        ),
        encoding="utf-8",
    )

    # BUGGY sequence: load -> sync -> save the PRE-SYNC object (what main()
    # did before the fold). The persisted status must NOT be gated — this is
    # the red direction; if it were gated, the test would not discriminate.
    pre = load_ledger(ledger_path)
    sync_gate_decisions(ledger_path, gen)
    save_ledger(ledger_path, pre)  # stale overwrite
    stale = load_ledger(ledger_path)
    assert stale["candidates"][0]["status"] != "gated:no-go"

    # FIXED path: the shared helper main() uses — sync + RELOAD from disk.
    synced, fresh = sync_and_reload(ledger_path, gen)
    assert synced == 1
    save_ledger(ledger_path, fresh)
    final = load_ledger(ledger_path)
    assert final["candidates"][0]["status"] == "gated:no-go"


def test_audit_requeue_archives_gate_and_new_decision_applies(tmp_path: Path):
    """P7 fold (luna re-gate 5): the audit requeue ARCHIVES the decision file
    (reset) — the read-only sync cannot reapply the old decision, rank sees
    no gate file, and a NEW decision written after recovery applies normally.
    """
    spec = importlib.util.spec_from_file_location(
        "mine_cli2", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    from regexproof.mine.audit import run_audit_sampler

    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    cand = _sample_candidate(
        url="https://github.com/acme/recovered",
        status="gated:no-go",
    )
    cand["audit"] = {
        "transitions": [
            {"to": "gated:no-go", "reason": "sync:recovered_gate_decision"},
        ],
        "auto_filed": True,
        "auto_filed_at": "2026-08-05T00:00:00Z",  # ISO week 2026-W32
    }
    ledger["candidates"].append(cand)
    save_ledger(ledger_path, ledger)
    (gen / "recovered_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "recovered",
                "candidate_url": "https://github.com/acme/recovered",
                "decision": "no-go",
            }
        ),
        encoding="utf-8",
    )

    # 1. Audit failure requeues + archives the decision file. The archive
    #    matches by candidate_url (the file name uses a SANITIZED corpus slug,
    #    not the URL segment — luna re-gate 6).
    out = run_audit_sampler(
        ledger_path, week="2026-W32", fail_urls={"https://github.com/acme/recovered"},
        generated_dir=gen,
    )
    assert out["failed_urls"] == ["https://github.com/acme/recovered"]
    assert not (gen / "recovered_gate_decision.json").exists()
    assert (gen / "recovered_gate_decision.audit-failed.json").exists()
    assert load_ledger(ledger_path)["candidates"][0]["status"] == "queued"

    # 2. Sync with no file: nothing to reapply.
    assert mod.sync_gate_decisions(ledger_path, gen) == 0
    assert load_ledger(ledger_path)["candidates"][0]["status"] == "queued"

    # 3. A NEW decision file (post-recovery re-evaluation) applies normally.
    (gen / "recovered_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "recovered",
                "candidate_url": "https://github.com/acme/recovered",
                "decision": "go",
            }
        ),
        encoding="utf-8",
    )
    # Diagnostic preconditions (CI-only divergence hunt — the sync returned 0
    # on the runner while passing locally):
    assert sorted(p.name for p in gen.glob("*_gate_decision.json")) == [
        "recovered_gate_decision.json"
    ]
    led2 = load_ledger(ledger_path)
    assert mod.find_candidate(led2, "https://github.com/acme/recovered") is not None
    assert led2["candidates"][0]["status"] == "queued"
    # Surface the swallowed TransitionError (CI-only divergence):
    try:
        mod.set_status(
            ledger_path, "https://github.com/acme/recovered", decision="go",
            reason="diag",
        )
    except Exception as exc:  # noqa: BLE001
        raise AssertionError(f"set_status raised in CI: {exc!r}") from exc
    # Revert the diagnostic transition so the sync still sees "queued".
    from regexproof.mine.transition import transition_candidate

    transition_candidate(
        ledger_path, "https://github.com/acme/recovered", to="queued",
        reason="diag-revert",
    )
    # Decisive spy: does the sync's loop even reach set_status?
    calls: list[tuple] = []
    fc_calls: list[str] = []
    led_views: list[dict] = []
    orig_ss = mod.set_status
    orig_fc = mod.find_candidate
    orig_ll = mod.load_ledger

    def _spy(*a, **k):
        calls.append((a, k))
        return orig_ss(*a, **k)

    def _fc_spy(led, url):
        fc_calls.append(str(url))
        return orig_fc(led, url)

    def _ll_spy(path):
        led = orig_ll(path)
        led_views.append(led)
        return led

    mod.set_status = _spy
    mod.find_candidate = _fc_spy
    mod.load_ledger = _ll_spy
    try:
        result = mod.sync_gate_decisions(ledger_path, gen)
    finally:
        mod.set_status = orig_ss
        mod.find_candidate = orig_fc
        mod.load_ledger = orig_ll
    assert fc_calls == ["https://github.com/acme/recovered"], fc_calls
    assert calls, f"sync never reached set_status; result={result} fc={fc_calls}"
    assert result == 1, f"sync returned {result} after {len(calls)} set_status calls"
    assert load_ledger(ledger_path)["candidates"][0]["status"] == "gated:go"


def test_archive_matches_by_candidate_url_not_slug(tmp_path: Path):
    """P7 fold (luna re-gate 6): the archive locates the decision file by its
    candidate_url field — the file name is derived from a SANITIZED corpus
    slug, which is not the URL's last path segment."""
    from regexproof.mine.audit import _archive_gate_decision

    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "sanitized_slug_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "sanitized-slug",
                "candidate_url": "https://github.com/acme/recovered",
                "decision": "no-go",
            }
        ),
        encoding="utf-8",
    )
    _archive_gate_decision(gen, "https://github.com/acme/recovered")
    assert not (gen / "sanitized_slug_gate_decision.json").exists()
    assert (gen / "sanitized_slug_gate_decision.audit-failed.json").exists()
    # A different candidate's file is untouched.
    (gen / "other_gate_decision.json").write_text(
        json.dumps({"schema_version": "1", "corpus": "other",
                    "candidate_url": "https://github.com/acme/other",
                    "decision": "go"}),
        encoding="utf-8",
    )
    _archive_gate_decision(gen, "https://github.com/acme/recovered")
    assert (gen / "other_gate_decision.json").exists()
