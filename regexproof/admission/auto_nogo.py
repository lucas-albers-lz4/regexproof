"""Restricted auto-NO-GO eligibility (umbrella C4 / Finding F)."""

from __future__ import annotations

from typing import Any

AUTO_NOGO_BAR = 200


class AutoNoGoError(ValueError):
    """Probe is not eligible for deterministic auto-NO-GO."""


def auto_nogo_eligible(probe: dict[str, Any]) -> bool:
    """Return True when the restricted auto-NO-GO class applies.

    ``(boundary == deterministic-false ∧ sites < 200) ∨ sites == 0``.
    """
    sites = int(probe.get("regex_sites") or 0)
    if sites == 0:
        return True
    boundary = str(probe.get("security_boundary") or "unknown")
    return boundary == "deterministic-false" and sites < AUTO_NOGO_BAR


def require_auto_nogo(probe: dict[str, Any]) -> None:
    """Raise AutoNoGoError with a human-routing reason when ineligible."""
    sites = int(probe.get("regex_sites") or 0)
    boundary = str(probe.get("security_boundary") or "unknown")
    if auto_nogo_eligible(probe):
        return
    if boundary == "deterministic-true":
        raise AutoNoGoError(
            "auto-NO-GO refused: security_boundary=deterministic-true "
            "(routes to human review)"
        )
    if boundary == "unknown" and sites > 0:
        raise AutoNoGoError(
            "auto-NO-GO refused: security_boundary=unknown with non-zero sites "
            "(routes to human review)"
        )
    if sites >= AUTO_NOGO_BAR:
        raise AutoNoGoError(
            f"auto-NO-GO refused: regex_sites={sites} >= {AUTO_NOGO_BAR} "
            "(routes to human review)"
        )
    raise AutoNoGoError(
        f"auto-NO-GO refused: boundary={boundary!r} sites={sites} "
        "(routes to human review)"
    )
