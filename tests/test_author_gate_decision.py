"""P3 author-gate-decision tests (#132 ACs)."""

from __future__ import annotations

import importlib.util
import json
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from regexproof.admission.author import (
    AuthorError,
    assemble_decision,
    author_auto,
    author_human,
    emit_decision_text,
    load_probe_draft,
)
from regexproof.admission.auto_nogo import AutoNoGoError, auto_nogo_eligible, require_auto_nogo
from regexproof.admission.templates import TemplateError, render_rationale
from regexproof.mine.audit import mark_auto_filed, run_audit_sampler, sample_size
from regexproof.mine.ledger import empty_ledger, load_ledger, save_ledger
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "admission"
WTFORMS_DRAFT = FIXTURES / "probe_draft_wtforms_shaped.json"
WTFORMS_GOLDEN = FIXTURES / "wtforms_shaped_gate_decision.json"


def _cli():
    spec = importlib.util.spec_from_file_location(
        "author_cli", ROOT / "scripts" / "author-gate-decision.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _validate(decision: dict) -> None:
    import jsonschema

    jsonschema.validate(instance=decision, schema=gate_decision_schema())


def _draft_with(**probe_overrides) -> dict:
    draft = load_probe_draft(WTFORMS_DRAFT)
    draft = json.loads(json.dumps(draft))  # deep copy
    draft["probe"].update(probe_overrides)
    return draft


def test_human_go_with_met_condition_schema_valid():
    draft = load_probe_draft(WTFORMS_DRAFT)
    # AC4: a go with new-surface carries NON-EMPTY predicted_buckets (the
    # under-report rule is enforced at the tool since P3); a realistic
    # go-new-surface draft has shell/construct evidence.
    draft["probe"]["predicted_buckets"] = {"posix-class": 3, "inline-flag": 1}
    dec = author_human(
        draft,
        decision="go",
        rationale="New surface at scale.",
        met={"new-surface"},
        evidence={"new-surface": "First-seen construct class X."},
        decision_date=date(2026, 8, 9),
    )
    assert dec["decision"] == "go"
    _validate(dec)


def test_go_new_surface_empty_buckets_refused():
    """AC4 under-report rule (P3): go + new-surface + EMPTY
    predicted_buckets is refused at the tool — enforcement, not review."""
    draft = load_probe_draft(WTFORMS_DRAFT)
    draft["probe"]["predicted_buckets"] = {}
    with pytest.raises(AuthorError, match="predicted_buckets"):
        author_human(
            draft,
            decision="go",
            rationale="New surface at scale.",
            met={"new-surface"},
            evidence={"new-surface": "First-seen construct class X."},
            decision_date=date(2026, 8, 9),
        )


def test_go_new_surface_empty_buckets_refused_at_assemble():
    """Cumulative finding #9 (defense-in-depth): the AC4 rule lives in the
    SHARED builder — a DIRECT assemble_decision call (bypassing the CLI
    authoring path) also fails closed."""
    draft = load_probe_draft(WTFORMS_DRAFT)
    draft["probe"]["predicted_buckets"] = {}
    with pytest.raises(AuthorError, match="predicted_buckets"):
        assemble_decision(
            draft,
            decision="go",
            rationale="New surface at scale.",
            conditions=[
                {"id": "new-surface", "met": True, "evidence": "X."},
                {"id": "security-boundary", "met": False, "evidence": "-"},
                {"id": "large-under-saturated", "met": False, "evidence": "-"},
            ],
        )


def test_refuse_decision_without_rationale():
    draft = load_probe_draft(WTFORMS_DRAFT)
    with pytest.raises(AuthorError, match="rationale"):
        author_human(draft, decision="no-go", rationale="")


def test_refuse_go_zero_met_without_decision_basis():
    draft = load_probe_draft(WTFORMS_DRAFT)
    with pytest.raises(AuthorError, match="decision_basis"):
        author_human(
            draft,
            decision="go",
            rationale="nope",
            met=set(),
        )


def test_repo_moved_template_human_only():
    draft = load_probe_draft(WTFORMS_DRAFT)
    related = {"moved_to": "https://github.com/example/successor"}
    dec = author_human(
        draft,
        decision="no-go",
        template="repo-moved",
        related=related,
        decision_date=date(2026, 8, 9),
    )
    assert dec["decision"] == "no-go"
    assert all(not c["met"] for c in dec["conditions"])
    assert "moved" in dec["rationale"].lower() or "superseded" in dec["rationale"].lower()
    _validate(dec)

    with pytest.raises(TemplateError, match="related"):
        author_human(draft, decision="no-go", template="repo-moved")

    # Auto path never emits repo-moved
    auto = author_auto(draft, decision_date=date(2026, 8, 9))
    assert "repo-moved" not in auto["rationale"]
    assert "Below admission scale" in auto["rationale"]


def test_auto_standard_wtforms_and_ledger_audit(tmp_path: Path):
    draft = load_probe_draft(WTFORMS_DRAFT)
    assert auto_nogo_eligible(draft["probe"])
    dec = author_auto(draft, decision_date=date(2026, 8, 9))
    assert dec["decision"] == "no-go"
    assert "Below admission scale" in dec["rationale"]
    _validate(dec)

    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"].append(
        {
            "url": draft["candidate_url"],
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 1,
            "source_query": "q",
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        }
    )
    save_ledger(ledger_path, ledger)
    mark_auto_filed(
        ledger_path,
        draft["candidate_url"],
        template_fired="below-scale",
        clock=lambda: datetime(2026, 8, 9, tzinfo=timezone.utc),
    )
    reloaded = load_ledger(ledger_path)
    audit = reloaded["candidates"][0]["audit"]
    assert audit["auto_filed"] is True
    assert audit["template_fired"] == "below-scale"


def test_auto_zero_sites_unknown_boundary():
    draft = _draft_with(regex_sites=0, security_boundary="unknown", dialect={})
    require_auto_nogo(draft["probe"])
    dec = author_auto(draft, decision_date=date(2026, 8, 9))
    assert dec["decision"] == "no-go"
    assert "Below admission scale" in dec["rationale"]
    _validate(dec)


def test_auto_guards_true_and_nonzero_unknown():
    draft_true = _draft_with(regex_sites=50, security_boundary="deterministic-true")
    with pytest.raises(AutoNoGoError, match="deterministic-true"):
        author_auto(draft_true)

    draft_unk = _draft_with(regex_sites=50, security_boundary="unknown")
    with pytest.raises(AutoNoGoError, match="unknown"):
        author_auto(draft_unk)

    # go / triage-trial never produced by auto
    draft = load_probe_draft(WTFORMS_DRAFT)
    dec = author_auto(draft, decision_date=date(2026, 8, 9))
    assert dec["decision"] == "no-go"


def test_sample_size_formula():
    assert sample_size(0) == 0
    assert sample_size(3) == 3  # pop < 5 → all
    assert sample_size(5) == 5
    assert sample_size(40) == 5  # max(5, ceil(4))=5
    assert sample_size(100) == 10


def test_audit_sampler_fail_requeues(tmp_path: Path):
    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    urls = [
        "https://github.com/a/one",
        "https://github.com/a/two",
        "https://github.com/a/three",
    ]
    for u in urls:
        ledger["candidates"].append(
            {
                "url": u,
                "default_branch": "main",
                "pin": "p",
                "pushed_date": "2026-08-01",
                "stars": 1,
                "source_query": "q",
                "first_seen": "2026-08-09T00:00:00Z",
                "status": "mined",
                "audit": {
                    "auto_filed": True,
                    "template_fired": "below-scale",
                    "auto_filed_at": "2026-08-09T12:00:00Z",
                    "updated_at": "2026-08-09T12:00:00Z",
                },
            }
        )
    save_ledger(ledger_path, ledger)

    # ISO week of 2026-08-09
    result = run_audit_sampler(
        ledger_path,
        week="2026-W32",
        seed=1,
        fail_urls={urls[0]},
        clock=lambda: datetime(2026, 8, 10, tzinfo=timezone.utc),
    )
    assert result["population"] == 3
    assert result["sample_size"] == 3  # all reviewed when pop < 5
    assert urls[0] in result["failed_urls"]

    reloaded = load_ledger(ledger_path)
    failed = next(c for c in reloaded["candidates"] if c["url"] == urls[0])
    assert failed["status"] == "queued"
    assert failed["audit"]["re_evaluate"] is True
    assert failed["audit"]["auto_filed"] is True  # preserved
    assert failed["audit"]["transitions"][-1]["reason"] == "audit-sampler-fail"


def test_byte_identical_with_fixed_now():
    draft = load_probe_draft(WTFORMS_DRAFT)
    a = emit_decision_text(author_auto(draft, decision_date=date(2026, 8, 9)))
    b = emit_decision_text(author_auto(draft, decision_date=date(2026, 8, 9)))
    assert a == b


def test_wtforms_shaped_golden_byte_identical():
    draft = load_probe_draft(WTFORMS_DRAFT)
    got = emit_decision_text(author_auto(draft, decision_date=date(2026, 8, 9)))
    expected = WTFORMS_GOLDEN.read_text(encoding="utf-8")
    assert got == expected
    # Must not claim identity with historical pre-C6 artifact
    historical = (
        ROOT / "properties" / "generated" / "wtforms_gate_decision.json"
    ).read_text(encoding="utf-8")
    assert got != historical
    assert '"py_re"' in got
    assert '"py":' not in got.split("dialect")[1].split("}")[0]


def test_cli_absolute_paths_and_llm_draft(tmp_path: Path):
    mod = _cli()
    out = tmp_path / "nested" / "dec.json"
    rc = mod.main(
        [
            str(WTFORMS_DRAFT.resolve()),
            "--auto",
            "-o",
            str(out),
            "--allow-outside-generated",
            "--now",
            "2026-08-09",
        ]
    )
    assert rc == 0
    assert out.is_file()
    assert out.resolve() == out
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["decision"] == "no-go"

    # P3b: --llm-draft is live; garbage classify → human review (exit 1), not stub exit 2
    rc2 = mod.main(
        [str(WTFORMS_DRAFT), "--llm-draft", "--classify-label", "not-a-class"]
    )
    assert rc2 == 1


def test_cli_human_requires_decision(tmp_path: Path):
    mod = _cli()
    with pytest.raises(SystemExit):
        mod.main([str(WTFORMS_DRAFT), "--human", "--rationale", "x"])


def test_render_templates_cover_four_classes():
    probe = load_probe_draft(WTFORMS_DRAFT)["probe"]
    for name in ("new-surface", "security-boundary", "below-scale"):
        assert render_rationale(name, probe=probe)
    assert render_rationale(
        "repo-moved", probe=probe, related={"moved_to": "https://example.com/r"}
    )
