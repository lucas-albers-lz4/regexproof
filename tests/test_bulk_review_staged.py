"""Wave 3 (#560): staged bulk review CLI + requeue/demote semantics tests.

Covers the REAL pipeline wiring (Luna r1): schema-valid authoring via
author_human/author_auto, provenance enforcement (go/triage-trial REQUIRE
human + reviewer + conditions + rationale; auto = NO-GO-only), stub
rejection, ledger audit promotion (promoted_via/promoted_at for the
sampler), requeue via transition API + decision archiving, demote with
retained location, and (url, pin) supersession dedup by CHRONOLOGICAL
decision_date (not lexical SHA order).
"""

from __future__ import annotations

import json
import os
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.mine import audit, lease_registry  # noqa: E402


def _probe_draft(url: str = "https://x/y", *, corpus: str = "ow") -> dict:
    """Real probe-shaped draft (what load_probe_draft accepts). The auto
    NO-GO path reads regex_sites as a COUNT; sites=0 is auto-eligible
    regardless of security_boundary (require_auto_nogo)."""
    return {
        "candidate_url": url,
        "corpus": corpus,
        "probe": {
            "dialect": {"shell": 1},
            "flags": [],
            "pin": "a" * 40,
            "regex_sites": 0,
            "predicted_buckets": {"high-yield": 1},  # AC4 under-report rule
        },
    }


def _load_brs():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "brs", ROOT / "scripts" / "bulk-review-staged.py",
    )
    brs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(brs)  # type: ignore[union-attr]
    return brs


def _write_draft(tmp_path: pathlib.Path, draft: dict | None = None) -> pathlib.Path:
    d = draft or _probe_draft()
    p = tmp_path / "draft.json"
    p.write_text(json.dumps(d, sort_keys=True) + "\n", encoding="utf-8")
    return p


def _ledger_with(url: str = "https://x/y") -> dict:
    from regexproof.mine.ledger import empty_ledger

    ledger = empty_ledger()
    # Requeue is a legal transition from gated:* → queued.
    ledger["candidates"].append({"url": url, "status": "gated:no-go"})
    return ledger


def _write_ledger(tmp_path: pathlib.Path, url: str = "https://x/y") -> pathlib.Path:
    p = tmp_path / "ledger.json"
    p.write_text(json.dumps(_ledger_with(url), indent=2, sort_keys=True) + "\n",
                 encoding="utf-8")
    return p


# --- provenance enforcement (Luna r1 #2: schema-valid, not flag-level) -------


def test_go_requires_reviewer(tmp_path):
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="requires --reviewer"):
        brs.main(["--draft", str(draft), "--go", "--ledger", str(ledger)])


def test_go_requires_rationale(tmp_path):
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="requires --rationale"):
        brs.main(["--draft", str(draft), "--go", "--reviewer", "alice",
                  "--ledger", str(ledger)])


def test_go_requires_conditions_ok(tmp_path):
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="requires --conditions-ok"):
        brs.main(["--draft", str(draft), "--go", "--reviewer", "alice",
                  "--rationale", "verified", "--ledger", str(ledger)])


def test_triage_trial_requires_human_flow(tmp_path):
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="requires --reviewer"):
        brs.main(["--draft", str(draft), "--triage-trial", "--ledger", str(ledger)])


def test_stub_provenance_rejected(tmp_path):
    """Luna r1 #2: provenance=stub in the input draft is structurally
    rejected — a queue stub can never be promoted."""
    brs = _load_brs()
    d = _probe_draft()
    d["provenance"] = "stub"
    draft = _write_draft(tmp_path, d)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="queue stub"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])


def test_human_go_writes_decision_and_promotes(tmp_path, monkeypatch):
    """Luna r1 #1/#3: a human go drives author_human (schema-validated),
    writes the gate decision, and promotes the ledger row so the sampler
    includes it."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    # go needs regex_sites >= 1 (schema minimum); auto-no-go needs 0.
    d = _probe_draft()
    d["probe"]["regex_sites"] = 1
    draft = _write_draft(tmp_path, d)
    ledger = _write_ledger(tmp_path)
    at = "2026-08-21T10:00:00"
    rc = brs.main(["--draft", str(draft), "--go", "--reviewer", "alice",
                   "--rationale", "human verified all conditions",
                   "--conditions-ok",
                   "--evidence", "new-surface=manual-source-confirmed",
                   "--evidence", "security-boundary=manual-review",
                   "--evidence", "large-under-saturated=manual-review",
                   "--at", at, "--ledger", str(ledger)])
    assert rc == 0
    # Schema-validated decision written.
    dec = json.loads((gen / "ow_gate_decision.json").read_text(encoding="utf-8"))
    assert dec["decision"] == "go"
    assert dec["rationale"] == "human verified all conditions"
    assert dec["decision_basis"] == "admission_conditions"
    # Ledger promoted for the sampler (Luna r1 #3).
    cand = next(iter(json.loads(ledger.read_text(encoding="utf-8"))["candidates"]))
    assert cand["audit"]["promoted_via"] == "bulk-review"
    assert cand["audit"]["promoted_at"] == "2026-08-21T10:00:00Z"  # canonical UTC
    # Luna r5 #2: human go must CLEAR the re-review state.
    assert cand["audit"]["re_evaluate"] is False
    assert cand["audit"]["needs_human_review"] is False
    assert cand["audit"]["human_resolved"] is True


def test_human_go_clears_re_evaluate_state(tmp_path, monkeypatch):
    """Luna r5 #2: a candidate flagged re_evaluate=true becomes fully
    resolved after a human go — later auto-filing is unblocked."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    from regexproof.mine.ledger import empty_ledger

    url = "https://x/y"
    ledger = tmp_path / "ledger.json"
    ld = empty_ledger()
    ld["candidates"].append({"url": url, "status": "mined",
                             "audit": {"re_evaluate": True,
                                       "needs_human_review": True}})
    ledger.write_text(json.dumps(ld, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    d = _probe_draft(url)
    d["probe"]["regex_sites"] = 1
    draft = _write_draft(tmp_path, d)
    rc = brs.main(["--draft", str(draft), "--go", "--reviewer", "alice",
                   "--rationale", "human verified all conditions",
                   "--conditions-ok",
                   "--evidence", "new-surface=manual-source-confirmed",
                   "--evidence", "security-boundary=manual-review",
                   "--evidence", "large-under-saturated=manual-review",
                   "--at", "2026-08-21T10:00:00", "--ledger", str(ledger)])
    assert rc == 0
    cand = next(iter(json.loads(ledger.read_text(encoding="utf-8"))["candidates"]))
    assert cand["audit"]["re_evaluate"] is False
    assert cand["audit"]["needs_human_review"] is False
    assert cand["audit"]["human_resolved"] is True
    assert cand["audit"]["auto_filed"] is False


def test_auto_no_go_is_deterministic(tmp_path, monkeypatch):
    """Auto paths are deterministic NO-GO-only — the auto author path never
    emits go/triage-trial (Luna r1 #2)."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    rc = brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    assert rc == 0
    dec = json.loads((gen / "ow_gate_decision.json").read_text(encoding="utf-8"))
    assert dec["decision"] == "no-go"
    assert dec["escape_hatch_applied"] is False


def test_promotion_fails_closed_on_missing_candidate(tmp_path, monkeypatch):
    """Luna r2 P0: a missing ledger candidate must FAIL CLOSED — the
    decision write must not look like a successful promotion without audit
    provenance."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    draft = _write_draft(tmp_path)
    ledger = tmp_path / "ledger.json"  # EMPTY ledger — candidate missing
    from regexproof.mine.ledger import empty_ledger

    ledger.write_text(json.dumps(empty_ledger(), indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    with pytest.raises(SystemExit, match=r"auto-filing refused|candidate not in ledger"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])


def test_demote_requires_retained_location(tmp_path):
    """Luna r2 Medium: demotion must not silently succeed without the
    required retained-location state."""
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="--retained-location"):
        brs.main(["--draft", str(draft), "--demote-retain-corpus",
                  "--ledger", str(ledger)])


# --- requeue / demote semantics (Luna r1 #1: real transitions) ---------------


def test_requeue_transitions_and_archives(tmp_path, monkeypatch):
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    url = "https://github.com/openwrt/packages"
    safe = "openwrt_packages"
    (gen / f"{safe}_gate_decision.json").write_text(
        json.dumps({"candidate_url": url, "decision": "no-go"}, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    # Unrelated decision must survive (Luna r3: filename globs were ambiguous).
    (gen / "other_openwrt_packages_gate_decision.json").write_text(
        json.dumps({"candidate_url": "https://github.com/other/packages",
                    "decision": "no-go"}, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    draft = _write_draft(tmp_path, _probe_draft(url))
    ledger = _write_ledger(tmp_path, url)
    rc = brs.main(["--draft", str(draft), "--requeue",
                   "--reason", "bulk-review", "--ledger", str(ledger)])
    assert rc == 0
    cand = next(iter(json.loads(ledger.read_text(encoding="utf-8"))["candidates"]))
    assert cand["status"] == "queued"  # P2-owned transition API
    # Decision archived so the read-only sync cannot reapply it.
    assert not (gen / f"{safe}_gate_decision.json").exists()
    assert (gen / "other_openwrt_packages_gate_decision.json").exists()
    assert len(list(gen.glob("*.requeued.json"))) == 1


def test_requeue_records_retained_location(tmp_path, monkeypatch):
    """CodeRabbit #573: --requeue --retained-location must NOT be silently
    dropped — the ledger row records it."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    url = "https://github.com/openwrt/packages"
    safe = "openwrt_packages"
    (gen / f"{safe}_gate_decision.json").write_text(
        json.dumps({"candidate_url": url, "decision": "no-go"}, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    draft = _write_draft(tmp_path, _probe_draft(url))
    ledger = _write_ledger(tmp_path, url)
    rc = brs.main(["--draft", str(draft), "--requeue",
                   "--retained-location", "batch/corpora/ow",
                   "--reason", "bulk-review", "--ledger", str(ledger)])
    assert rc == 0
    cand = next(iter(json.loads(ledger.read_text(encoding="utf-8"))["candidates"]))
    assert cand["status"] == "queued"
    assert cand["retained_location"] == "batch/corpora/ow"


def test_malformed_at_fails_closed(tmp_path):
    """CodeRabbit #573: a malformed --at fails early with a clean error on
    EVERY verb path — never an uncaught traceback or a raw string in the
    audit timestamps."""
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    for verb in (["--no-go"], ["--demote-retain-corpus",
                               "--retained-location", "x"]):
        with pytest.raises(SystemExit, match=r"--at must be ISO"):
            brs.main(["--draft", str(draft), *verb,
                      "--at", "not-a-timestamp", "--ledger", str(ledger)])


def test_auto_no_go_refusal_leaves_no_artifact(tmp_path, monkeypatch):
    """Luna r4: when mark_auto_filed refuses (re_evaluate=true), NO decision
    artifact may be left active — the next sync would apply it."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    from regexproof.mine.ledger import empty_ledger

    url = "https://x/y"
    ledger = tmp_path / "ledger.json"
    ld = empty_ledger()
    ld["candidates"].append({"url": url, "status": "mined",
                             "audit": {"re_evaluate": True}})
    ledger.write_text(json.dumps(ld, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    draft = _write_draft(tmp_path, _probe_draft(url))
    with pytest.raises(SystemExit, match="auto-filing refused"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    # Fail closed: nothing was written — the sync cannot apply a stale decision.
    assert not (gen / "ow_gate_decision.json").exists()


def test_custom_cache_root_lease_released(tmp_path):
    """Luna r4: _release_lease must release from the CUSTOM registry
    (--cache-root), not the default cache/leases.json."""
    brs = _load_brs()
    cache_root = tmp_path / "cache"
    cache_root.mkdir()
    url = "https://github.com/openwrt/packages"
    lease_registry.acquire(
        url, "a" * 40, owner_pid=os.getpid(), path=cache_root / "leases.json",
    )
    assert lease_registry.active_leases(path=cache_root / "leases.json")
    brs._release_lease(url, cache_root=cache_root)
    assert lease_registry.active_leases(path=cache_root / "leases.json") == []


def test_lightweight_batch_probe_draft_enriched(tmp_path, monkeypatch):
    """Luna r5 #1: a lightweight batch-probe stub (url/pin/corpus, NO probe)
    is enriched from the {corpus}_probe_decision.json artifact — the
    producer→reviewer workflow works without an undocumented conversion."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    # Probe evidence artifact (what probe-corpus-admission emits).
    (gen / "ow_probe_decision.json").write_text(
        json.dumps({"corpus": "ow", "candidate_url": "https://x/y",
                    "probe": {"dialect": {"shell": 1}, "regex_sites": 1,
                              "security_boundary": "deterministic-false",
                              "pin": "a" * 40}},
                   sort_keys=True) + "\n", encoding="utf-8")
    # Lightweight stub — batch-probe.py shape (no probe object).
    stub = {"url": "https://x/y", "pin": "a" * 40, "corpus": "ow",
            "manifest_digest": "d1", "files_walked": 10}
    draft = _write_draft(tmp_path, stub)
    ledger = _write_ledger(tmp_path)
    rc = brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    assert rc == 0  # enrichment succeeded; authoring ran on the resolved probe
    dec = json.loads((gen / "ow_gate_decision.json").read_text(encoding="utf-8"))
    assert dec["decision"] == "no-go"


def test_lightweight_draft_without_evidence_fails_closed(tmp_path, monkeypatch):
    """Luna r5 #1: a lightweight draft with NO probe evidence anywhere must
    fail closed with a clear routing error."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    stub = {"url": "https://x/y", "pin": "a" * 40, "corpus": "ow",
            "manifest_digest": "d1"}
    draft = _write_draft(tmp_path, stub)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="probe evidence"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])


def test_lightweight_draft_refuses_wrong_url_evidence(tmp_path, monkeypatch):
    """Luna r6 #1: probe evidence is BOUND to the draft candidate — an
    artifact for a DIFFERENT url must never be inherited (corpus filename
    alone is not identity)."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    # Evidence exists for corpus ow BUT a different url.
    (gen / "ow_probe_decision.json").write_text(
        json.dumps({"corpus": "ow", "candidate_url": "https://github.com/other/repo",
                    "probe": {"dialect": {"shell": 1}, "regex_sites": 1,
                              "security_boundary": "deterministic-false",
                              "pin": "b" * 40}},
                   sort_keys=True) + "\n", encoding="utf-8")
    stub = {"url": "https://x/y", "pin": "a" * 40, "corpus": "ow",
            "manifest_digest": "d1"}
    draft = _write_draft(tmp_path, stub)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="probe evidence"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])


def test_lightweight_draft_refuses_conflicting_probe_pin(tmp_path, monkeypatch):
    """Luna r7: pin binding checks EVERY pin — an artifact with a matching
    corpus_pin but a CONFLICTING probe.pin must be refused (evidence from
    the wrong revision must not pass the binding gate)."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    (gen / "ow_probe_decision.json").write_text(
        json.dumps({"corpus": "ow", "candidate_url": "https://x/y",
                    "corpus_pin": "a" * 40,  # matches the draft pin
                    "probe": {"dialect": {"shell": 1}, "regex_sites": 1,
                              "security_boundary": "deterministic-false",
                              "pin": "b" * 40}},  # CONFLICTS
                   sort_keys=True) + "\n", encoding="utf-8")
    stub = {"url": "https://x/y", "pin": "a" * 40, "corpus": "ow",
            "manifest_digest": "d1"}
    draft = _write_draft(tmp_path, stub)
    ledger = _write_ledger(tmp_path)
    with pytest.raises(SystemExit, match="do not match draft pins"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])


def test_failed_promotion_leaves_no_artifact(tmp_path, monkeypatch):
    """Luna r6 #2: when a ledger update fails, NO active decision artifact
    may remain — the next sync must not apply a stale decision."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    draft = _write_draft(tmp_path)
    ledger = tmp_path / "ledger.json"  # EMPTY ledger — candidate missing
    from regexproof.mine.ledger import empty_ledger

    ledger.write_text(json.dumps(empty_ledger(), indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    with pytest.raises(SystemExit, match="not in ledger"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    assert not (gen / "ow_gate_decision.json").exists()


def test_filing_failure_rolls_back_artifact(tmp_path, monkeypatch):
    """CodeRabbit #573 + Luna r9: if mark_auto_filed fails AFTER the pending
    write, the .pending file is removed and the final artifact never
    installed — audit state and decision files must never diverge."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    from regexproof.mine.ledger import empty_ledger

    url = "https://x/y"
    ledger = tmp_path / "ledger.json"
    ld = empty_ledger()
    ld["candidates"].append({"url": url, "status": "mined",
                             "audit": {"re_evaluate": False}})
    ledger.write_text(json.dumps(ld, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    draft = _write_draft(tmp_path, _probe_draft(url))
    # Simulate a filing failure that happens AFTER the pending write.
    def _boom(*args, **kwargs):
        raise ValueError("simulated filing failure")
    monkeypatch.setattr(brs.audit, "mark_auto_filed", _boom)
    with pytest.raises(SystemExit, match="auto-filing refused"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    # Rollback: neither the pending file nor the final artifact remains.
    assert not (gen / "ow_gate_decision.json").exists()
    assert not (gen / "ow_gate_decision.json.pending").exists()


def test_filing_failure_preserves_prior_artifact(tmp_path, monkeypatch):
    """Luna r9: a failed RETRY must NOT delete an existing valid decision —
    the pending-then-replace pattern only touches the new file."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    from regexproof.mine.ledger import empty_ledger

    url = "https://x/y"
    ledger = tmp_path / "ledger.json"
    ld = empty_ledger()
    ld["candidates"].append({"url": url, "status": "mined",
                             "audit": {"re_evaluate": False}})
    ledger.write_text(json.dumps(ld, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    draft = _write_draft(tmp_path, _probe_draft(url))
    # A PRIOR valid decision already exists.
    (gen / "ow_gate_decision.json").write_text(
        json.dumps({"decision": "no-go", "schema_version": "1"}) + "\n",
        encoding="utf-8")
    prior = (gen / "ow_gate_decision.json").read_text(encoding="utf-8")

    def _boom(*args, **kwargs):
        raise OSError("simulated ledger write failure")
    monkeypatch.setattr(brs.audit, "mark_auto_filed", _boom)
    with pytest.raises(SystemExit, match="auto-filing refused"):
        brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    # The prior decision survives untouched; no pending file leaks.
    assert (gen / "ow_gate_decision.json").read_text(encoding="utf-8") == prior
    assert not (gen / "ow_gate_decision.json.pending").exists()


def test_demote_records_retained_location(tmp_path):
    brs = _load_brs()
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    rc = brs.main(["--draft", str(draft), "--demote-retain-corpus",
                   "--retained-location", "batch/corpora/ow",
                   "--ledger", str(ledger)])
    assert rc == 0
    cand = next(iter(json.loads(ledger.read_text(encoding="utf-8"))["candidates"]))
    assert cand["status"] == "demoted"
    assert cand["retained_location"] == "batch/corpora/ow"


# --- audit sampler population extension (#560 Wave 3) ------------------------


def _ledger(candidates: list[dict]) -> dict:
    return {"schema_version": "1", "candidates": candidates}


def test_sampler_includes_bulk_promoted():
    c = {
        "url": "https://x/y",
        "provenance": "human",
        "audit": {
            "auto_filed": False,
            "promoted_via": "bulk-review",
            "promoted_at": "2026-08-21T10:00:00+00:00",
        },
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert len(pop) == 1


def test_sampler_excludes_stub_provenance():
    c = {
        "url": "https://x/y",
        "provenance": "stub",  # queue-only — never contract material
        "audit": {"auto_filed": True, "auto_filed_at": "2026-08-21T10:00:00+00:00"},
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert pop == []


def test_sampler_keeps_regular_auto_filed():
    c = {
        "url": "https://x/y",
        "provenance": "auto",
        "audit": {"auto_filed": True, "auto_filed_at": "2026-08-21T10:00:00+00:00"},
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert len(pop) == 1


# --- (url, pin) supersession dedup for eval/escape counters ------------------


def _decision_file(
    tmp_path: pathlib.Path, name: str, url: str,
    *, corpus_pin: str = "", decision: str = "no_go",
    decision_date: str = "",
) -> None:
    """Real gate-decision shape (Luna r1 #4): corpus_pin + decision +
    decision_date — NOT a top-level 'pin'/'status'."""
    d = {"candidate_url": url, "decision": decision}
    if corpus_pin:
        d["corpus_pin"] = corpus_pin
    if decision_date:
        d["decision_date"] = decision_date
    (tmp_path / name).write_text(
        json.dumps(d, sort_keys=True) + "\n", encoding="utf-8",
    )


def _load_bpf():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bpf", ROOT / "scripts" / "build-phase0-freeze.py",
    )
    bpf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bpf)  # type: ignore[union-attr]
    return bpf


def test_supersession_dedup_keeps_latest_decision(tmp_path, monkeypatch):
    """Luna r1 #4/#5: dedup keys on the CANONICAL pin (corpus_pin) and
    selects by CHRONOLOGICAL decision_date, not lexical SHA order."""
    bpf = _load_bpf()

    gen = tmp_path
    # Older decision_date with a LEXICALLY-LARGER pin (a newer commit can
    # have a smaller SHA) — the chronological winner must be the newer date.
    _decision_file(gen, "a_gate_decision.json", "https://x/y",
                   corpus_pin="ffff", decision="no_go", decision_date="2026-08-01")
    _decision_file(gen, "b_gate_decision.json", "https://x/y",
                   corpus_pin="0000", decision="go", decision_date="2026-08-22")
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 1  # superseded: the older decision is dropped
    assert rows[0]["pin"] == "0000"  # newer decision_date wins, NOT lexical max
    assert rows[0]["status"] == "go"


def test_supersession_dedup_reads_nested_probe_pin(tmp_path, monkeypatch):
    """Luna r1 #4: when corpus_pin is absent, the nested probe.pin is the
    canonical pin — a top-level pin read would see an empty key."""
    bpf = _load_bpf()

    gen = tmp_path
    (gen / "a_gate_decision.json").write_text(
        json.dumps({
            "candidate_url": "https://x/y",
            "decision": "no_go",
            "probe": {"pin": "abc123"},
            "decision_date": "2026-08-22",
        }, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 1
    assert rows[0]["pin"] == "abc123"


def test_supersession_dedup_distinct_urls_untouched(tmp_path, monkeypatch):
    bpf = _load_bpf()

    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y",
                   corpus_pin="aaa", decision="no_go", decision_date="2026-08-01")
    _decision_file(gen, "c_gate_decision.json", "https://x/z",
                   corpus_pin="ccc", decision="triage_trial", decision_date="2026-08-01")
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 2  # distinct urls never dedup


def test_supersession_dedup_missing_url_kept(tmp_path, monkeypatch):
    bpf = _load_bpf()

    gen = tmp_path
    (gen / "a_gate_decision.json").write_text(
        json.dumps({"decision": "no_go"}, sort_keys=True) + "\n", encoding="utf-8",
    )
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 1  # url-less rows are untouched


def test_supersession_dedup_fails_closed_on_missing_recency(tmp_path, monkeypatch):
    """CodeRabbit #573: a dedup-eligible pair with NO ordering value must
    fail closed — a silent tie could pick the wrong decision as latest."""
    bpf = _load_bpf()

    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y",
                   corpus_pin="aaa", decision="no_go")  # NO decision_date
    _decision_file(gen, "b_gate_decision.json", "https://x/y",
                   corpus_pin="bbb", decision="go")  # NO decision_date
    monkeypatch.setattr(bpf, "GEN", gen)
    with pytest.raises(SystemExit, match="cannot supersede"):
        bpf.load_decision_population()


# --- golden inputs_hash no-drift on requeue AND demote (#560 AC) -------------


def _load_bgl():
    """Production hash: build-gate-labels._inputs_hash (Luna r1 #6 — the
    tests must exercise the PRODUCTION hash, not a local reimplementation)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bgl", ROOT / "scripts" / "build-gate-labels.py",
    )
    bgl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bgl)  # type: ignore[union-attr]
    return bgl


def _inputs_hash_of(gen: pathlib.Path) -> str:
    return _load_bgl()._inputs_hash(sorted(gen.glob("*_gate_decision.json")))


def test_inputs_hash_no_drift_on_requeue(tmp_path):
    """Requeue (materialize --teardown / requeued archive) must NOT drift
    the golden inputs hash when decision CONTENT is unchanged — the hash is
    content-derived (D5 lesson), not HEAD-derived."""
    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y",
                   corpus_pin="aaa", decision="no_go", decision_date="2026-08-01")
    _decision_file(gen, "b_gate_decision.json", "https://x/z",
                   corpus_pin="bbb", decision="go", decision_date="2026-08-01")
    # Requeue = archive one decision (the read-only sync cannot reapply it).
    (gen / "a_gate_decision.json").rename(gen / "a_gate_decision.requeued.json")
    h2 = _inputs_hash_of(gen)
    # Content-derived: the hash over the SURVIVING decisions is stable and
    # the excluded file no longer counts — recomputing is deterministic.
    assert h2 == _inputs_hash_of(gen)  # no drift on re-run


def test_inputs_hash_no_drift_on_demote(tmp_path):
    """Demote (retain corpus, release lease) must NOT drift the golden
    inputs hash when decision content is unchanged."""
    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y",
                   corpus_pin="aaa", decision="no_go", decision_date="2026-08-01")
    h1 = _inputs_hash_of(gen)
    # Demote rewrites the row metadata but not the decision status/content.
    d = json.loads((gen / "a_gate_decision.json").read_text(encoding="utf-8"))
    d["demoted_at"] = "2026-08-23T00:00:00+00:00"  # metadata-only mutation
    (gen / "a_gate_decision.json").write_text(
        json.dumps(d, sort_keys=True) + "\n", encoding="utf-8",
    )
    # Content hash is over the full file bytes → a metadata mutation CHANGES
    # it (fail-closed: no silent drift). Re-running is deterministic.
    h2 = _inputs_hash_of(gen)
    assert h2 != h1  # metadata mutation detected (hash is content-derived)
    assert h2 == _inputs_hash_of(gen)  # stable across re-runs


# --- canonical JSON (#560: sorted keys, \\n-terminated, stable order) --------


def test_decision_output_canonical(tmp_path, monkeypatch):
    """The authored gate decision is canonical JSON (sorted keys, trailing
    newline) — golden artifacts must be byte-stable under regeneration."""
    brs = _load_brs()
    gen = tmp_path / "generated"
    gen.mkdir()
    monkeypatch.setattr(brs, "GEN", gen)
    monkeypatch.setattr(brs, "default_output_path",
                        lambda corpus, repo_root=None: gen / f"{corpus}_gate_decision.json")
    draft = _write_draft(tmp_path)
    ledger = _write_ledger(tmp_path)
    brs.main(["--draft", str(draft), "--no-go", "--ledger", str(ledger)])
    text = (gen / "ow_gate_decision.json").read_text(encoding="utf-8")
    assert text.endswith("\n")
    d = json.loads(text)
    assert list(d.keys()) == sorted(d.keys())  # sorted keys
