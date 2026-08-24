"""Wave 5 (#574): hashed rank manifest + auto-NO-GO fold into batch-probe."""

from __future__ import annotations

import json
import pathlib

import pytest

from regexproof.admission.author import load_probe_draft
from regexproof.mine import batch_manifest, batch_nogo, batch_state
from regexproof.mine.ledger import empty_ledger, save_ledger

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "admission"
PIN = "a" * 40
URL = "https://github.com/wtforms/wtforms"


def _ledger(tmp_path, url=URL):
    p = tmp_path / "ledger.json"
    led = empty_ledger()
    led["candidates"].append({"url": url, "status": "mined", "pin": PIN})
    save_ledger(p, led)
    return p


def test_walk_repo_invokes_heartbeat(tmp_path):
    from regexproof.admission.walk import walk_repo

    for i in range(4):
        (tmp_path / f"f{i}.py").write_text("x = 1\n")
    hits = {"n": 0}
    walk_repo(tmp_path, heartbeat=lambda: hits.__setitem__("n", hits["n"] + 1), heartbeat_every=2)
    assert hits["n"] >= 1


def test_items_prefer_pin_probed_over_mined():
    probed = "b" * 40
    mined = "c" * 40
    items = batch_manifest.items_from_rank_ndjson(
        json.dumps({"url": URL, "pin": mined, "pin_probed": probed, "score": 1})
    )
    assert items[0]["pin"] == probed
    items = batch_manifest.items_from_rank_ndjson(
        json.dumps({"url": URL, "pin": PIN, "score": 1.0, "allocator": "score-v1"})
    )
    assert items[0]["corpus"] == "wtforms"
    assert items[0]["pin"] == PIN
    d1 = batch_manifest.items_digest(items)
    d2 = batch_manifest.items_digest(items)
    assert d1 == d2
    with pytest.raises(SystemExit, match="40-char hex"):
        batch_manifest.items_from_rank_ndjson(
            json.dumps({"url": URL, "pin": "short", "score": 1})
        )


def test_load_and_verify_fails_closed_on_mutation(tmp_path):
    items = [{"url": URL, "pin": PIN, "corpus": "wtforms", "score": 1, "allocator": "score-v1"}]
    path = tmp_path / "manifest.json"
    doc = batch_manifest.write_manifest(items, allocator="score-v1", limit=1, path=path)
    loaded = batch_manifest.load_and_verify(path)
    assert loaded["digest"] == doc["digest"]
    mutated = json.loads(path.read_text(encoding="utf-8"))
    mutated["items"][0]["url"] = "https://github.com/evil/evil"
    path.write_text(json.dumps(mutated, indent=2) + "\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="digest mismatch"):
        batch_manifest.load_and_verify(path)


def test_fold_auto_nogo_below_scale(tmp_path):
    draft = load_probe_draft(FIXTURES / "probe_draft_wtforms_shaped.json")
    gen = tmp_path / "generated"
    gen.mkdir()
    outcome, decision, _note = batch_nogo.fold_auto_nogo(
        draft,
        generated_dir=gen,
        ledger_path=_ledger(tmp_path),
        repo_root=ROOT,
    )
    assert outcome == "auto_nogo"
    assert decision is not None and decision.is_file()
    body = json.loads(decision.read_text(encoding="utf-8"))
    assert body["decision"] == "no-go"


def test_fold_needs_human_ledger_failure_is_incomplete(tmp_path):
    draft = load_probe_draft(FIXTURES / "probe_draft_wtforms_shaped.json")
    draft = json.loads(json.dumps(draft))
    draft["probe"]["regex_sites"] = 250
    draft["probe"]["security_boundary"] = "unknown"
    missing = tmp_path / "empty-ledger.json"
    save_ledger(missing, empty_ledger())
    with pytest.raises(batch_nogo.IncompleteFoldError, match="needs_human ledger"):
        batch_nogo.fold_auto_nogo(
            draft,
            generated_dir=tmp_path / "generated",
            ledger_path=missing,
            repo_root=ROOT,
        )


def test_fold_needs_human_when_above_scale(tmp_path):
    draft = load_probe_draft(FIXTURES / "probe_draft_wtforms_shaped.json")
    draft = json.loads(json.dumps(draft))
    draft["probe"]["regex_sites"] = 250
    draft["probe"]["security_boundary"] = "unknown"
    outcome, decision, note = batch_nogo.fold_auto_nogo(
        draft,
        generated_dir=tmp_path / "generated",
        ledger_path=_ledger(tmp_path),
        repo_root=ROOT,
    )
    assert outcome == "needs_human"
    assert decision is None
    assert "auto-NO-GO refused" in note


def test_fold_re_evaluate_is_needs_human_not_incomplete(tmp_path):
    draft = load_probe_draft(FIXTURES / "probe_draft_wtforms_shaped.json")
    ledger = tmp_path / "ledger.json"
    led = empty_ledger()
    led["candidates"].append({
        "url": URL,
        "status": "mined",
        "pin": PIN,
        "audit": {"re_evaluate": True},
    })
    save_ledger(ledger, led)
    gen = tmp_path / "generated"
    gen.mkdir()
    outcome, decision, note = batch_nogo.fold_auto_nogo(
        draft,
        generated_dir=gen,
        ledger_path=ledger,
        repo_root=ROOT,
    )
    assert outcome == "needs_human"
    assert decision is None
    assert "re_evaluate" in note
    assert not list(gen.glob("*.pending"))
    assert not list(gen.glob("*_gate_decision.json"))


def test_fold_install_failure_does_not_complete(tmp_path, monkeypatch):
    draft = load_probe_draft(FIXTURES / "probe_draft_wtforms_shaped.json")
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = _ledger(tmp_path)

    def boom(_src, _dst):
        raise OSError("disk full")

    monkeypatch.setattr(batch_nogo.audit, "mark_auto_filed", lambda *a, **k: {})
    monkeypatch.setattr(batch_nogo.os, "replace", boom)
    with pytest.raises(batch_nogo.IncompleteFoldError, match="artifact install"):
        batch_nogo.fold_auto_nogo(
            draft,
            generated_dir=gen,
            ledger_path=ledger,
            repo_root=ROOT,
        )
    pending = list(gen.glob("*.pending"))
    assert pending, "pending journal must remain for resume"


def test_batch_run_forwards_ledger_to_rank(tmp_path, monkeypatch):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "batch_run", ROOT / "scripts" / "batch-run.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    captured: dict[str, list[str]] = {}

    def fake_rank(argv):
        captured["argv"] = list(argv)
        return json.dumps({"url": URL, "pin": PIN, "score": 1, "allocator": "score-v1"}) + "\n"

    monkeypatch.setattr(mod, "_rank_ndjson", fake_rank)
    ledger = tmp_path / "custom-ledger.json"
    man = tmp_path / "manifest.json"
    rc = mod.main([
        "--limit", "1",
        "--ledger", str(ledger),
        "--manifest", str(man),
        "--snapshot-only",
    ])
    assert rc == 0
    assert "--ledger" in captured["argv"]
    assert str(ledger) in captured["argv"]
    assert captured["argv"][captured["argv"].index("--status") + 1] == "mined"


def test_batch_run_snapshot_and_resume(tmp_path):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "batch_run", ROOT / "scripts" / "batch-run.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    ndjson = tmp_path / "rank.ndjson"
    ndjson.write_text(
        json.dumps({"url": URL, "pin": PIN, "score": 9, "allocator": "score-v1"}) + "\n",
        encoding="utf-8",
    )
    man = tmp_path / "manifest.json"
    state = tmp_path / "state.json"
    rc = mod.main([
        "--from-ndjson", str(ndjson),
        "--manifest", str(man),
        "--snapshot-only",
        "--replace-manifest",
        "--limit", "1",
    ])
    assert rc == 0
    doc = batch_manifest.load_and_verify(man)
    digest = doc["digest"]
    batch_state.begin_item(digest, URL, PIN, path=state)
    batch_state.record_outcome(digest, URL, PIN, "needs_human", path=state)
    rc = mod.main([
        "--manifest", str(man),
        "--state", str(state),
        "--snapshot-only",
    ])
    assert rc == 0
    rc = mod.main(["--manifest", str(man), "--state", str(state)])
    assert rc == 0
    proj = batch_state.projection(path=state)
    assert proj["probe_success_rate"] == 1.0
    assert proj["clone_ms_p95"] is None
