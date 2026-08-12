"""Corpus admission gate enforcement (regexproof/batch/runner.check_admission_gates)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.batch.runner import CORPUS_MANIFESTS, check_admission_gates
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"


def _decision(decision: str, *, security_boundary: bool = False, **overrides) -> dict:
    base = {
        "schema_version": "1",
        "corpus": "probe-corpus",
        "candidate_url": "https://github.com/example/probe-corpus",
        "decision": decision,
        "probe": {
            "regex_sites": 10,
            "dialect": {"py": 10},
            "flags": {},
            "predicted_buckets": {},
        },
        "conditions": [
            {"id": "new-surface", "met": False, "evidence": "x"},
            {"id": "security-boundary", "met": security_boundary, "evidence": "x"},
            {"id": "large-under-saturated", "met": False, "evidence": "x"},
        ],
        "rationale": "test",
    }
    base.update(overrides)
    return base


def _write(out_dir: Path, name: str, data: dict) -> Path:
    p = out_dir / f"{name}_gate_decision.json"
    p.write_text(json.dumps(data, indent=1), encoding="utf-8")
    return p


def _enforced_corpora() -> list[str]:
    return [
        name
        for name, meta in CORPUS_MANIFESTS.items()
        if meta.get("corpus_type") not in ("testdata", "inventory_only")
    ]


def test_every_enforced_corpus_has_a_committed_decision(tmp_path):
    """Backfill invariant: no rule corpus lacks an admission record.

    Existence + schema validity, not decision value: a no-go corpus (for
    example semgrep_rules, re-measured only from frozen inventories) still
    has a decision — the run-time gate blocks batch runs of it.
    """
    schema = gate_decision_schema()
    for name in _enforced_corpora():
        committed = GENERATED / f"{name}_gate_decision.json"
        assert committed.exists(), (
            f"{name} lacks a committed gate decision; run the admission probe "
            "and commit properties/generated/<name>_gate_decision.json"
        )
        data = json.loads(committed.read_text(encoding="utf-8"))
        __import__("jsonschema").validate(instance=data, schema=schema)
    # Sandbox copy for the enforcement check itself.
    for name in _enforced_corpora():
        committed = GENERATED / f"{name}_gate_decision.json"
        (tmp_path / committed.name).write_bytes(committed.read_bytes())
    # Enforcement sees only runnable corpora: drop the no-go ones.
    runnable = [
        name
        for name in _enforced_corpora()
        if json.loads((tmp_path / f"{name}_gate_decision.json").read_text()).get(
            "decision"
        )
        in ("go", "triage-trial")
    ]
    assert check_admission_gates(runnable, out_dir=tmp_path) == []


def test_committed_decisions_validate_against_schema():
    schema = gate_decision_schema()
    for name in _enforced_corpora():
        p = GENERATED / f"{name}_gate_decision.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        # jsonschema raises on violation
        __import__("jsonschema").validate(instance=data, schema=schema)


def test_missing_decision_is_a_violation(tmp_path):
    violations = check_admission_gates(["gitleaks"], out_dir=tmp_path)
    assert len(violations) == 1
    assert "gitleaks" in violations[0]
    assert "missing" in violations[0]


def test_no_go_decision_is_a_violation(tmp_path):
    _write(tmp_path, "gitleaks", _decision("no-go"))
    violations = check_admission_gates(["gitleaks"], out_dir=tmp_path)
    assert len(violations) == 1
    assert "go or triage-trial required" in violations[0]


def test_schema_invalid_decision_is_a_violation(tmp_path):
    _write(tmp_path, "gitleaks", _decision("go", conditions=[]))
    violations = check_admission_gates(["gitleaks"], out_dir=tmp_path)
    assert len(violations) == 1
    assert "fails schema" in violations[0]


def test_triage_trial_passes(tmp_path):
    _write(
        tmp_path,
        "gitleaks",
        _decision(
            "triage-trial",
            security_boundary=True,
            decision_basis="escape_hatch",
            escape_hatch_applied=True,
        ),
    )
    assert check_admission_gates(["gitleaks"], out_dir=tmp_path) == []


def test_go_requires_basis_when_no_conditions_met(tmp_path):
    """Schema cross-constraint: decision=go with 0/3 conditions met needs a basis."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    bad = _decision("go")  # all conditions met=False, no decision_basis
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)
    # grandfathered basis makes it valid (with provenance)
    good = _decision(
        "go",
        decision_basis="grandfathered",
        related={"backfilled": True, "repo": "example/probe-corpus"},
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_no_go_with_conditions_met_is_invalid():
    """decision=no-go while an admission condition is met is a contradiction."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    bad = _decision(
        "no-go",
        conditions=[
            {"id": "new-surface", "met": False, "evidence": "x"},
            {"id": "security-boundary", "met": True, "evidence": "x"},
            {"id": "large-under-saturated", "met": False, "evidence": "x"},
        ],
    )
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)


def test_probe_requires_regex_sites_for_fresh_decision():
    """A non-grandfathered decision must carry at least one regex site."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    # decision=go via conditions, but probe.regex_sites=0 -> invalid
    bad = _decision(
        "go",
        decision_basis="admission_conditions",
        conditions=[
            {"id": "new-surface", "met": False, "evidence": "x"},
            {"id": "security-boundary", "met": True, "evidence": "x"},
            {"id": "large-under-saturated", "met": False, "evidence": "x"},
        ],
        probe={
            "regex_sites": 0,
            "dialect": {"py": 10},
            "flags": {},
            "predicted_buckets": {},
        },
    )
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)
    # grandfathered exempts the probe evidence minimum (with provenance)
    good = _decision(
        "go", decision_basis="grandfathered",
        related={"backfilled": True, "repo": "example/probe-corpus"},
        probe={
            "regex_sites": 0,
            "dialect": {"py": 10},
            "flags": {},
            "predicted_buckets": {},
        },
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_grandfathered_requires_backfill_provenance():
    """A fresh probe cannot claim grandfathered: related.backfilled=true required."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    # no provenance -> invalid
    bad = _decision("go", decision_basis="grandfathered")
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)
    # with provenance -> valid
    good = _decision(
        "go",
        decision_basis="grandfathered",
        related={"backfilled": True, "repo": "example/probe-corpus"},
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_escape_hatch_requires_security_boundary():
    """escape_hatch basis requires security-boundary met + escape_hatch_applied."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    # non-security corpus claiming the hatch -> invalid
    bad = _decision("go", decision_basis="escape_hatch", escape_hatch_applied=True)
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)
    # security-boundary met + applied -> valid
    good = _decision(
        "go",
        security_boundary=True,
        decision_basis="escape_hatch",
        escape_hatch_applied=True,
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_triage_trial_requires_security_boundary():
    """triage-trial is the security-boundary findings trial; non-security triage is invalid."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    bad = _decision("triage-trial", decision_basis="escape_hatch", escape_hatch_applied=True)
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=bad, schema=schema)
    good = _decision(
        "triage-trial",
        security_boundary=True,
        decision_basis="escape_hatch",
        escape_hatch_applied=True,
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_no_go_exempt_from_probe_evidence_minimum():
    """NO-GO with zero regex sites is valid: no regex surface is itself the rejection."""
    schema = gate_decision_schema()
    good = _decision(
        "no-go",
        probe={
            "regex_sites": 0,
            "dialect": {"shell": 0},
            "flags": {},
            "predicted_buckets": {},
        },
    )
    __import__("jsonschema").validate(instance=good, schema=schema)


def test_conditions_ids_are_unique():
    """Three copies of the same condition id must not validate."""
    from jsonschema import ValidationError

    schema = gate_decision_schema()
    dup = _decision("go")
    dup["conditions"] = [
        {"id": "security-boundary", "met": True, "evidence": "x"},
        {"id": "security-boundary", "met": True, "evidence": "x"},
        {"id": "security-boundary", "met": True, "evidence": "x"},
    ]
    dup["decision_basis"] = "admission_conditions"
    with pytest.raises(ValidationError):
        __import__("jsonschema").validate(instance=dup, schema=schema)


def test_unreadable_decision_is_a_violation(tmp_path):
    """The unreadable/JSONDecodeError branch is exercised (MCR finding m2)."""
    (tmp_path / "gitleaks_gate_decision.json").write_text("{not json!!", encoding="utf-8")
    violations = check_admission_gates(["gitleaks"], out_dir=tmp_path)
    assert len(violations) == 1
    assert "unreadable" in violations[0]


def test_testdata_corpora_are_exempt(tmp_path):
    # A testdata corpus in the manifest needs no decision artifact.
    assert check_admission_gates(["re2_testdata"], out_dir=tmp_path) == []


def test_unknown_corpus_is_a_violation(tmp_path):
    violations = check_admission_gates(["not-a-corpus"], out_dir=tmp_path)
    assert len(violations) == 1
    assert "not in CORPUS_MANIFESTS" in violations[0]


def test_run_batch_rejects_missing_decision(tmp_path):
    """The gate fires through run_batch: no artifact -> SystemExit before work."""
    from regexproof.batch.runner import run_batch

    with pytest.raises(SystemExit) as exc:
        run_batch(["gitleaks"], out_dir=tmp_path)
    assert "admission gate failed" in str(exc.value)


def test_security_tool_manifests_are_in_disclose_set():
    """Every security_tool corpus must get private_first via SECURITY_TOOL_CORPORA.

    ReDoS tagging uses meta["security_tool"]; property/usage findings use the
    frozenset. Partial wiring would under-disclose on one path.
    """
    from regexproof.batch.disclose import SECURITY_TOOL_CORPORA

    flagged = sorted(
        name
        for name, meta in CORPUS_MANIFESTS.items()
        if meta.get("security_tool")
    )
    missing = [n for n in flagged if n not in SECURITY_TOOL_CORPORA]
    assert missing == [], (
        "manifest security_tool=True but missing from SECURITY_TOOL_CORPORA: "
        + ", ".join(missing)
    )
    # Reverse: disclose-set members that are manifests must also flag security_tool.
    unflagged = sorted(
        n
        for n in SECURITY_TOOL_CORPORA
        if n in CORPUS_MANIFESTS and not CORPUS_MANIFESTS[n].get("security_tool")
    )
    assert unflagged == [], (
        "SECURITY_TOOL_CORPORA member lacks manifest security_tool=True: "
        + ", ".join(unflagged)
    )
