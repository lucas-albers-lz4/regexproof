"""Verification-tier derivation (design #213 D5/D15/S3/S15, Phase 3 PR A).

The tier is DERIVED at report time from the raw NDJSON evidence — never stored
(S15). Rules:

- abstain-aware (D5): any abstention (noodler abstain, cross-check abstained)
  caps the tier — NEVER cross-checked.
- S3 authority guard: `cross-checked` REQUIRES route:"mirror" (with the U9 DROP
  every harness route IS mirror; the guard is unit-tested with a synthetic
  non-mirror record — the original 'cross_check_backend != ecma' alternative is
  moot, no ECMA backend exists).
- seq-only: a stock-path result.
- escalated-unconfirmed: a noodler-decided result with the cross-check leg
  absent or abstained (or a route that fails the S3 guard).
- cross-checked: noodler-decided AND cross-check agrees AND route is mirror.
"""

from __future__ import annotations

from typing import Optional

TIER_SEQ_ONLY = "seq-only"
TIER_ESCALATED = "escalated-unconfirmed"
TIER_CROSS_CHECKED = "cross-checked"


def derive_tier(result: dict) -> str:
    """Derive the verification tier from the raw fields of one result record.
    Assumes the record carries: backend, state, noodler_verdict,
    cross_check_verdict (optional), cross_check_abstained (optional),
    route (optional, defaults 'mirror')."""
    backend = result.get("backend", "seq")

    # abstain-aware: any abstention caps the tier (D5)
    if result.get("not_proven"):
        return TIER_SEQ_ONLY if backend == "seq" else TIER_ESCALATED
    if result.get("cross_check_abstained"):
        return TIER_ESCALATED
    if str(result.get("noodler_verdict", "")).startswith("ABSTAIN"):
        return TIER_ESCALATED

    if backend == "seq":
        return TIER_SEQ_ONLY

    # S3 authority guard: cross-checked requires route:"mirror"
    if result.get("route", "mirror") != "mirror":
        return TIER_ESCALATED

    if result.get("cross_check_verdict") is None:
        return TIER_ESCALATED  # leg absent → escalated-unconfirmed

    if result["cross_check_verdict"] == result.get("noodler_verdict"):
        return TIER_CROSS_CHECKED
    return TIER_ESCALATED  # disagreement → never cross-checked (D15 handles the fail)


def tier_summary(results: list[dict]) -> dict:
    """Report-time summary: per-tier counts (the derived view — nothing stored)."""
    from collections import Counter

    c = Counter(derive_tier(r) for r in results)
    return {TIER_SEQ_ONLY: c[TIER_SEQ_ONLY],
            TIER_ESCALATED: c[TIER_ESCALATED],
            TIER_CROSS_CHECKED: c[TIER_CROSS_CHECKED]}
