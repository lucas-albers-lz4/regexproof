"""Deterministic rationale templates for gate decisions (P3 / #132)."""

from __future__ import annotations

from typing import Any

TEMPLATE_NAMES = frozenset(
    {"new-surface", "security-boundary", "below-scale", "repo-moved"}
)

# Auto-NO-GO may only fire this template (Finding D).
AUTO_ALLOWED_TEMPLATES = frozenset({"below-scale"})

CONDITION_IDS = ("new-surface", "security-boundary", "large-under-saturated")


class TemplateError(ValueError):
    """Invalid template selection or missing required metadata."""


def render_rationale(name: str, *, probe: dict[str, Any], related: dict[str, Any] | None = None) -> str:
    """Return the deterministic rationale string for *name*."""
    if name not in TEMPLATE_NAMES:
        raise TemplateError(f"unknown rationale template: {name!r}")
    sites = int(probe.get("regex_sites") or 0)
    boundary = str(probe.get("security_boundary") or "unknown")
    dialects = probe.get("dialect") or {}
    dial_s = ", ".join(f"{k}:{v}" for k, v in sorted(dialects.items())) or "none"

    if name == "below-scale":
        return (
            f"Below admission scale: {sites} regex sites "
            f"(auto-NO-GO bar 200); dialects [{dial_s}]; "
            f"boundary={boundary}."
        )
    if name == "new-surface":
        buckets = probe.get("predicted_buckets") or {}
        buck_s = ", ".join(f"{k}:{v}" for k, v in sorted(buckets.items())) or "none"
        return (
            f"New dialect/flag/encoding surface: dialects [{dial_s}]; "
            f"predicted_buckets [{buck_s}]."
        )
    if name == "security-boundary":
        return (
            f"Security-boundary corpus (boundary={boundary}) with findings-triage potential; "
            f"{sites} sites across [{dial_s}]."
        )
    # repo-moved
    if not related:
        raise TemplateError("repo-moved template requires related metadata")
    moved_to = related.get("moved_to") or related.get("successor") or "unknown"
    return (
        f"Repository moved or superseded (related={moved_to}); "
        f"no admission conditions met."
    )


def default_unmet_evidence(probe: dict[str, Any]) -> dict[str, str]:
    """Fixed unmet evidence strings for the three admission conditions."""
    sites = int(probe.get("regex_sites") or 0)
    boundary = str(probe.get("security_boundary") or "unknown")
    buckets = probe.get("predicted_buckets") or {}
    if buckets:
        surface = f"Predicted buckets present ({len(buckets)}) but not treated as novel surface."
    else:
        surface = "No novel dialect/flag/encoding surface."
    return {
        "new-surface": surface,
        "security-boundary": (
            f"Not a security boundary (probe.security_boundary={boundary})."
            if boundary != "deterministic-true"
            else "Security-boundary condition not asserted met."
        ),
        "large-under-saturated": f"{sites} sites < 1000 scale bar.",
    }
