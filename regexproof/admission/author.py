"""Assemble schema-valid gate decisions from probe drafts (P3 / #132)."""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable

from regexproof.admission.auto_nogo import AutoNoGoError, require_auto_nogo
from regexproof.admission.serialize import dumps_pinned
from regexproof.admission.templates import (
    AUTO_ALLOWED_TEMPLATES,
    CONDITION_IDS,
    TEMPLATE_NAMES,
    TemplateError,
    default_unmet_evidence,
    render_rationale,
)
from regexproof.schemas import gate_decision_schema

Clock = Callable[[], date]


class AuthorError(ValueError):
    """Invalid human/auto authoring inputs."""


def default_clock() -> date:
    return datetime.now(timezone.utc).date()


def load_probe_draft(path: Path | str) -> dict[str, Any]:
    p = Path(path).expanduser().resolve()
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise AuthorError("probe draft must be a JSON object")
    if "probe" not in data:
        raise AuthorError("probe draft missing probe object")
    return data


def _probe_subset(probe: dict[str, Any]) -> dict[str, Any]:
    """Gate-decision probe object (schema-required keys + useful extras).

    E3: carries the dual-pin set so gate evidence can cite the probed pin
    and stale-pin detection is preserved through authoring. ``pin`` retains
    its prior meaning (the SHA walked / corpus_pin); ``pin_probed`` is the
    default-branch HEAD resolved at clone time; ``pin_mined`` is the SHA the
    ledger assigned (optional).
    """
    out: dict[str, Any] = {
        "regex_sites": int(probe.get("regex_sites") or 0),
        "dialect": dict(probe.get("dialect") or {}),
        "flags": dict(probe.get("flags") or {}),
        "predicted_buckets": dict(probe.get("predicted_buckets") or {}),
    }
    if "regex_sites_per_file" in probe:
        out["regex_sites_per_file"] = dict(probe["regex_sites_per_file"])
    if "security_boundary" in probe:
        out["security_boundary"] = probe["security_boundary"]
    if "pin" in probe:
        out["pin"] = probe["pin"]
    if "pin_probed" in probe:
        out["pin_probed"] = probe["pin_probed"]
    # E3 (luna gate 1): preserve pin_mined even when None — a null mined pin
    # (local-dir probe) must stay visible so artifacts consistently cite the
    # probe's pins; dropping the key made the pair inconsistent.
    if "pin_mined" in probe:
        out["pin_mined"] = probe["pin_mined"]
    if "construct_counts" in probe:
        out["construct_counts"] = dict(probe["construct_counts"])
    return out


def build_conditions(
    probe: dict[str, Any],
    *,
    met: set[str] | None = None,
    evidence_overrides: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    met = met or set()
    evidence_overrides = evidence_overrides or {}
    defaults = default_unmet_evidence(probe)
    conditions: list[dict[str, Any]] = []
    for cid in CONDITION_IDS:
        is_met = cid in met
        if cid in evidence_overrides:
            evidence = evidence_overrides[cid]
        elif is_met:
            raise AuthorError(
                f"condition {cid!r} is met but has no --evidence override"
            )
        else:
            evidence = defaults[cid]
        if not evidence:
            raise AuthorError(f"condition {cid!r} requires non-empty evidence")
        conditions.append({"id": cid, "met": is_met, "evidence": evidence})
    return conditions


def _validate(decision: dict[str, Any]) -> None:
    try:
        import jsonschema
    except ImportError as e:  # pragma: no cover
        raise AuthorError("jsonschema is required to validate gate decisions") from e
    try:
        jsonschema.validate(instance=decision, schema=gate_decision_schema())
    except jsonschema.ValidationError as e:
        raise AuthorError(f"schema validation failed: {e.message}") from e


def assemble_decision(
    draft: dict[str, Any],
    *,
    decision: str,
    rationale: str,
    conditions: list[dict[str, Any]],
    decision_basis: str | None = None,
    escape_hatch_applied: bool = False,
    related: dict[str, Any] | None = None,
    decision_date: date | None = None,
    clock: Clock | None = None,
    validate: bool = True,
) -> dict[str, Any]:
    """Build a schema-valid gate decision from a probe draft + author fields."""
    if not rationale or not str(rationale).strip():
        raise AuthorError("decision requires a non-empty rationale")
    if decision not in {"go", "no-go", "triage-trial"}:
        raise AuthorError(f"invalid decision: {decision!r}")

    probe = _probe_subset(dict(draft.get("probe") or {}))
    any_met = any(c.get("met") for c in conditions)
    met_ids = {c.get("id") for c in conditions if c.get("met")}
    # AC4 under-report rule (P3, cumulative review finding #9): enforced at
    # the SHARED builder so author_human/author_auto AND any direct call all
    # fail closed — go + new-surface with EMPTY predicted_buckets refuses.
    if (decision == "go" and "new-surface" in met_ids
            and not (probe.get("predicted_buckets") or {})):
        raise AuthorError(
            "go with condition new-surface requires NON-EMPTY "
            "probe.predicted_buckets (AC4 under-report rule); "
            "re-run merge-probe-draft.py or author triage-trial/no-go")
    basis = decision_basis
    if decision == "go" and not any_met:
        if basis not in {"grandfathered", "escape_hatch"}:
            raise AuthorError(
                "GO with zero met conditions requires decision_basis "
                "grandfathered or escape_hatch"
            )
    if basis is None:
        basis = "admission_conditions" if any_met or decision == "no-go" else None

    if decision == "triage-trial":
        basis = "escape_hatch"
        escape_hatch_applied = True

    day = decision_date or (clock or default_clock)()
    out: dict[str, Any] = {
        "schema_version": "1",
        "corpus": str(draft.get("corpus") or ""),
        "candidate_url": str(draft.get("candidate_url") or ""),
        "corpus_pin": draft.get("corpus_pin"),
        "decision": decision,
        "decision_basis": basis,
        "decision_date": day.isoformat(),
        "probe": probe,
        "conditions": conditions,
        "escape_hatch_applied": bool(escape_hatch_applied),
        "rationale": str(rationale).strip(),
    }
    if related is not None:
        out["related"] = related
    if not out["corpus"] or not out["candidate_url"]:
        raise AuthorError("draft must include corpus and candidate_url")
    if validate:
        _validate(out)
    return out


def author_human(
    draft: dict[str, Any],
    *,
    decision: str,
    rationale: str | None = None,
    template: str | None = None,
    met: set[str] | None = None,
    evidence: dict[str, str] | None = None,
    decision_basis: str | None = None,
    escape_hatch_applied: bool = False,
    related: dict[str, Any] | None = None,
    decision_date: date | None = None,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Human mode: fill remaining fields from CLI inputs."""
    met = met or set()
    unknown = met - set(CONDITION_IDS)
    if unknown:
        raise AuthorError(f"unknown condition id(s): {sorted(unknown)}")

    probe = dict(draft.get("probe") or {})
    if template:
        if template not in TEMPLATE_NAMES:
            raise TemplateError(f"unknown rationale template: {template!r}")
        if template == "repo-moved":
            if not related:
                raise TemplateError("repo-moved template requires related metadata")
            if met:
                raise TemplateError("repo-moved requires zero met conditions")
        rationale = render_rationale(template, probe=probe, related=related)
    if not rationale:
        raise AuthorError("provide --rationale or --template")

    conditions = build_conditions(probe, met=met, evidence_overrides=evidence)
    return assemble_decision(
        draft,
        decision=decision,
        rationale=rationale,
        conditions=conditions,
        decision_basis=decision_basis,
        escape_hatch_applied=escape_hatch_applied,
        related=related,
        decision_date=decision_date,
        clock=clock,
    )


def author_auto(
    draft: dict[str, Any],
    *,
    decision_date: date | None = None,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Auto-NO-GO path: restricted class only; always below-scale."""
    probe = dict(draft.get("probe") or {})
    require_auto_nogo(probe)
    # Guard: never emit go/triage-trial or repo-moved on auto path.
    rationale = render_rationale("below-scale", probe=probe)
    assert "below-scale" in AUTO_ALLOWED_TEMPLATES
    conditions = build_conditions(probe, met=set())
    return assemble_decision(
        draft,
        decision="no-go",
        rationale=rationale,
        conditions=conditions,
        decision_basis="admission_conditions",
        escape_hatch_applied=False,
        related=None,
        decision_date=decision_date,
        clock=clock,
    )


def emit_decision_text(decision: dict[str, Any]) -> str:
    return dumps_pinned(decision)


def default_output_path(corpus: str, *, repo_root: Path | None = None) -> Path:
    import re

    root = (repo_root or Path(__file__).resolve().parents[2]).resolve()
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", corpus.strip()) or "corpus"
    if safe in {".", ".."} or "/" in safe or "\\" in safe:
        raise AuthorError(f"unsafe corpus name for default output path: {corpus!r}")
    out = (root / "properties" / "generated" / f"{safe}_gate_decision.json").resolve()
    generated = (root / "properties" / "generated").resolve()
    if not out.is_relative_to(generated):
        raise AuthorError(f"refusing to write outside properties/generated: {out}")
    return out
