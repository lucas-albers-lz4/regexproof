"""LLM classify-then-template authoring (P3b / #134)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

from regexproof.admission.author import (
    AuthorError,
    Clock,
    assemble_decision,
    build_conditions,
    default_clock,
)
from regexproof.admission.auto_nogo import auto_nogo_eligible
from regexproof.admission.llm_client import ClassificationResult, GateClassifier
from regexproof.admission.templates import (
    AUTO_ALLOWED_TEMPLATES,
    TEMPLATE_NAMES,
    TemplateError,
    render_rationale,
)


@dataclass
class LlmDraftOutcome:
    """Result of an LLM draft attempt."""

    decision: dict[str, Any] | None
    needs_human_review: bool
    reason: str = ""
    classification: ClassificationResult | None = None
    template_fired: str | None = None


class LlmDraftError(ValueError):
    """LLM draft routing refused (human review required)."""


def author_llm_draft(
    draft: dict[str, Any],
    classifier: GateClassifier,
    *,
    related: dict[str, Any] | None = None,
    decision_date: date | None = None,
    clock: Clock | None = None,
) -> LlmDraftOutcome:
    """Classify then render a schema-valid no-go draft — never approve / auto-file.

    Locked routing (plan):
    - Auto-eligible probes: only ``below-scale`` (AUTO_ALLOWED_TEMPLATES).
    - Outside auto class: write ``no-go`` only for ``below-scale`` / ``repo-moved``
      (``repo-moved`` requires ``related``). Any GO/triage-trial intent, garbage,
      or disallowed class → ``needs_human_review`` with no decision artifact.
    """
    probe = dict(draft.get("probe") or {})
    result = classifier.classify(draft)
    label = result.label if result.ok else None

    if not label or label not in TEMPLATE_NAMES:
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason=result.error or "garbage or empty classification",
            classification=result,
        )

    # Never treat LLM class as GO / triage-trial approval.
    if label in {"new-surface", "security-boundary"}:
        # These templates describe GO-path rationale classes; LLM must not approve.
        if auto_nogo_eligible(probe):
            return LlmDraftOutcome(
                decision=None,
                needs_human_review=True,
                reason=(
                    f"auto-eligible probe: LLM class {label!r} is not a no-go "
                    f"template (allowed: {sorted(AUTO_ALLOWED_TEMPLATES)})"
                ),
                classification=result,
            )
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason=(
                f"LLM class {label!r} implies GO/triage path; "
                "LLM never approves — human review required"
            ),
            classification=result,
        )

    if auto_nogo_eligible(probe) and label not in AUTO_ALLOWED_TEMPLATES:
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason=(
                f"auto-eligible probe: LLM may only pick {sorted(AUTO_ALLOWED_TEMPLATES)}; "
                f"got {label!r}"
            ),
            classification=result,
        )

    if label == "repo-moved" and not related:
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason="repo-moved requires --related metadata",
            classification=result,
        )

    try:
        rationale = render_rationale(label, probe=probe, related=related)
    except TemplateError as e:
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason=str(e),
            classification=result,
        )

    conditions = build_conditions(probe, met=set())
    try:
        decision = assemble_decision(
            draft,
            decision="no-go",
            rationale=rationale,
            conditions=conditions,
            decision_basis="admission_conditions",
            escape_hatch_applied=False,
            related=related,
            decision_date=decision_date,
            clock=clock or default_clock,
        )
    except AuthorError as e:
        return LlmDraftOutcome(
            decision=None,
            needs_human_review=True,
            reason=str(e),
            classification=result,
        )

    return LlmDraftOutcome(
        decision=decision,
        needs_human_review=False,
        reason="",
        classification=result,
        template_fired=label,
    )
