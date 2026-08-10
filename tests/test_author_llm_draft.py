"""P3b --llm-draft classify-then-template tests (#134)."""

from __future__ import annotations

import importlib.util
import json
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from regexproof.admission.author import emit_decision_text, load_probe_draft
from regexproof.admission.auto_nogo import auto_nogo_eligible
from regexproof.admission.llm_client import RetryingClassifier, StaticClassifier
from regexproof.admission.llm_draft import author_llm_draft
from regexproof.mine.ledger import empty_ledger, load_ledger, save_ledger
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "admission"
WTFORMS_DRAFT = FIXTURES / "probe_draft_wtforms_shaped.json"


def _cli():
    spec = importlib.util.spec_from_file_location(
        "author_cli_llm", ROOT / "scripts" / "author-gate-decision.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _validate(decision: dict) -> None:
    import jsonschema

    jsonschema.validate(instance=decision, schema=gate_decision_schema())


def _draft_with(**probe_overrides) -> dict:
    draft = json.loads(WTFORMS_DRAFT.read_text(encoding="utf-8"))
    draft["probe"].update(probe_overrides)
    return draft


def _ledger_with(url: str, tmp_path: Path) -> Path:
    path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"].append(
        {
            "url": url,
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 1,
            "source_query": "q",
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        }
    )
    save_ledger(path, ledger)
    return path


def test_below_scale_schema_valid():
    draft = load_probe_draft(WTFORMS_DRAFT)
    assert auto_nogo_eligible(draft["probe"])
    out = author_llm_draft(
        draft, StaticClassifier("below-scale"), decision_date=date(2026, 8, 9)
    )
    assert not out.needs_human_review
    assert out.decision is not None
    assert out.decision["decision"] == "no-go"
    assert out.template_fired == "below-scale"
    _validate(out.decision)


def test_four_classes_repo_moved_and_disallowed_go_classes():
    draft = load_probe_draft(WTFORMS_DRAFT)
    # Auto-eligible: new-surface / security-boundary → human review
    for label in ("new-surface", "security-boundary"):
        out = author_llm_draft(draft, StaticClassifier(label))
        assert out.needs_human_review
        assert out.decision is None

    # repo-moved without related → human review
    out = author_llm_draft(draft, StaticClassifier("repo-moved"))
    assert out.needs_human_review

    # Outside auto class + below-scale still writes no-go
    big = _draft_with(regex_sites=500, security_boundary="deterministic-true")
    assert not auto_nogo_eligible(big["probe"])
    out = author_llm_draft(
        big, StaticClassifier("below-scale"), decision_date=date(2026, 8, 9)
    )
    assert out.decision is not None
    _validate(out.decision)

    # Outside auto class + new-surface → human (LLM never approves)
    out = author_llm_draft(big, StaticClassifier("new-surface"))
    assert out.needs_human_review
    assert out.decision is None


def test_garbage_needs_human_review():
    draft = load_probe_draft(WTFORMS_DRAFT)
    out = author_llm_draft(draft, StaticClassifier("not-a-real-class"))
    assert out.needs_human_review
    assert out.decision is None


def test_retry_then_human_review():
    sleeps: list[float] = []
    inner = StaticClassifier(None, fail_times=99, error="down")
    clf = RetryingClassifier(inner, sleep_fn=lambda s: sleeps.append(s), backoff_s=60.0)
    draft = load_probe_draft(WTFORMS_DRAFT)
    out = author_llm_draft(draft, clf)
    assert out.needs_human_review
    assert len(sleeps) == 1
    assert sleeps[0] == 60.0
    assert inner.calls == 2


def test_retry_recovers():
    inner = StaticClassifier("below-scale", fail_times=1)
    clf = RetryingClassifier(inner, sleep_fn=lambda _s: None)
    draft = load_probe_draft(WTFORMS_DRAFT)
    out = author_llm_draft(draft, clf, decision_date=date(2026, 8, 9))
    assert out.decision is not None
    assert inner.calls == 2


def test_llm_never_sets_auto_filed(tmp_path: Path):
    draft = load_probe_draft(WTFORMS_DRAFT)
    ledger = _ledger_with(draft["candidate_url"], tmp_path)
    mod = _cli()
    out = tmp_path / "dec.json"
    rc = mod.main(
        [
            str(WTFORMS_DRAFT),
            "--llm-draft",
            "--classify-label",
            "below-scale",
            "-o",
            str(out),
            "--allow-outside-generated",
            "--ledger",
            str(ledger),
            "--now",
            "2026-08-09",
        ]
    )
    assert rc == 0
    assert out.is_file()
    data = load_ledger(ledger)
    audit = data["candidates"][0]["audit"]
    assert audit.get("auto_filed") is False
    assert audit["template_fired"] == "below-scale"
    assert audit["model_calls"]


def test_cli_garbage_exit_and_human_review(tmp_path: Path):
    draft = load_probe_draft(WTFORMS_DRAFT)
    ledger = _ledger_with(draft["candidate_url"], tmp_path)
    mod = _cli()
    out = tmp_path / "should-not-exist.json"
    rc = mod.main(
        [
            str(WTFORMS_DRAFT),
            "--llm-draft",
            "--classify-label",
            "garbage",
            "-o",
            str(out),
            "--ledger",
            str(ledger),
        ]
    )
    assert rc == 1
    assert not out.exists()
    audit = load_ledger(ledger)["candidates"][0]["audit"]
    assert audit["needs_human_review"] is True


def test_boundary_true_cannot_auto_file_via_llm(tmp_path: Path):
    """LLM path never calls mark_auto_filed even on deterministic-true."""
    draft = _draft_with(regex_sites=50, security_boundary="deterministic-true")
    path = tmp_path / "draft.json"
    path.write_text(json.dumps(draft), encoding="utf-8")
    ledger = _ledger_with(draft["candidate_url"], tmp_path)
    mod = _cli()
    out = tmp_path / "dec.json"
    # below-scale outside auto class still writes no-go draft, but not auto_filed
    rc = mod.main(
        [
            str(path),
            "--llm-draft",
            "--classify-label",
            "below-scale",
            "-o",
            str(out),
            "--allow-outside-generated",
            "--ledger",
            str(ledger),
            "--now",
            "2026-08-09",
        ]
    )
    assert rc == 0
    audit = load_ledger(ledger)["candidates"][0]["audit"]
    assert audit.get("auto_filed") is False


def test_byte_identical_clock():
    draft = load_probe_draft(WTFORMS_DRAFT)
    a = author_llm_draft(
        draft, StaticClassifier("below-scale"), decision_date=date(2026, 8, 9)
    )
    b = author_llm_draft(
        draft, StaticClassifier("below-scale"), decision_date=date(2026, 8, 9)
    )
    assert emit_decision_text(a.decision) == emit_decision_text(b.decision)


def test_absolute_output_path(tmp_path: Path):
    mod = _cli()
    out = tmp_path / "nested" / "dec.json"
    # Outside properties/generated requires an explicit opt-out (#176).
    rc_denied = mod.main(
        [
            str(WTFORMS_DRAFT.resolve()),
            "--llm-draft",
            "--classify-label",
            "below-scale",
            "-o",
            str(out),
            "--now",
            "2026-08-09",
        ]
    )
    assert rc_denied == 1
    assert not out.exists()
    rc = mod.main(
        [
            str(WTFORMS_DRAFT.resolve()),
            "--llm-draft",
            "--classify-label",
            "below-scale",
            "-o",
            str(out),
            "--allow-outside-generated",
            "--now",
            "2026-08-09",
        ]
    )
    assert rc == 0
    assert out.resolve() == out
