"""Admit shape-5 pairs into batch only for machine-derivable contracts (#477)."""

from __future__ import annotations

from typing import Any

SCALE_PROVENANCE = frozenset({"version_diff", "cross_engine"})


def provenance_token(pair: dict[str, Any]) -> str:
    raw = pair.get("provenance")
    if isinstance(raw, str) and raw.strip():
        return raw.strip()
    if isinstance(raw, dict):
        for key in ("kind", "provenance", "pair_kind"):
            val = str(raw.get(key) or "").strip()
            if val:
                return val
    return str(pair.get("pair_kind") or "").strip()


def valid_family_contract(fc: Any) -> bool:
    if not isinstance(fc, dict):
        return False
    return bool(
        str(fc.get("R1") or "").strip()
        and str(fc.get("R2") or "").strip()
        and str(fc.get("provenance") or "").strip()
    )


def admit_shape5_for_batch(pair: dict[str, Any]) -> bool:
    if provenance_token(pair) not in SCALE_PROVENANCE:
        return False
    return valid_family_contract(pair.get("family_contract"))


def filter_batch_pairs(pairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [p for p in pairs if admit_shape5_for_batch(p)]
