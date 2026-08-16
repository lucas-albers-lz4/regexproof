"""Admission fork/duplicate detection (#481)."""

from __future__ import annotations

from datetime import date

from regexproof.admission.author import author_auto
from regexproof.admission.forks import fork_duplicate_reason, normalize_github_repo
from tests.test_author_gate_decision import _draft_with, _validate


def test_cpython_fork_is_duplicate():
    meta = {
        "fork": True,
        "full_name": "zrsx/cpython",
        "parent": {"full_name": "python/cpython"},
    }
    reason = fork_duplicate_reason(meta, go_repos={"python/cpython"})
    assert reason is not None
    assert "cpython" in reason.lower() or "interpreter" in reason.lower()


def test_non_fork_not_duplicate():
    meta = {"fork": False, "full_name": "acme/app"}
    assert fork_duplicate_reason(meta, go_repos={"python/cpython"}) is None


def test_author_auto_nogo_duplicate_fork_even_when_large(tmp_path):
    draft = _draft_with(
        regex_sites=5000,
        security_boundary="unknown",
        fork=True,
        full_name="someone/cpython",
        parent_full_name="python/cpython",
    )
    go = tmp_path / "python_cpython_gate_decision.json"
    go.write_text(
        '{"schema_version":"1","corpus":"cpython","candidate_url":'
        '"https://github.com/python/cpython","decision":"go"}',
        encoding="utf-8",
    )
    dec = author_auto(draft, decision_date=date(2026, 8, 15), generated_dir=tmp_path)
    assert dec["decision"] == "no-go"
    assert "Duplicate-class fork" in dec["rationale"]
    _validate(dec)


def test_author_auto_nogo_from_candidate_url_alone(tmp_path):
    draft = _draft_with(regex_sites=5000, security_boundary="unknown")
    draft["candidate_url"] = "https://github.com/zrsx/cpython"
    dec = author_auto(draft, decision_date=date(2026, 8, 15), generated_dir=tmp_path)
    assert dec["decision"] == "no-go"
    assert "Duplicate-class fork" in dec["rationale"]
    _validate(dec)


def test_normalize_github_repo():
    assert normalize_github_repo("https://github.com/Python/CPython") == "python/cpython"
