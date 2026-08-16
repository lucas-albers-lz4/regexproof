"""Product-reportability for harness results (#476).

UNSAT/SAT is hygiene until the property carries a contract and a declared
domain. Mutation guards are never product.
"""

from __future__ import annotations

from typing import Any

from regexproof.kinds import PropertyKind

_PRODUCT_KINDS = frozenset(
    {
        PropertyKind.PROPERTY.value,
        PropertyKind.COUNTEREXAMPLE_FINDER.value,
        PropertyKind.BUG_DEMO.value,
        PropertyKind.RULE_DIFF.value,
    }
)
# agent_derived is schema-valid but not product (smoke until a human adopts it).
_PRODUCT_PROVENANCE = frozenset({"human", "version_diff", "cross_engine"})


def product_reportable(entry: dict[str, Any]) -> bool:
    """True when a solver verdict may be counted as a product property."""
    if entry.get("kind") not in _PRODUCT_KINDS:
        return False
    domain = entry.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        return False
    contract = entry.get("contract")
    if not isinstance(contract, dict):
        return False
    guarantee = str(contract.get("guarantee") or "").strip()
    declared = str(contract.get("declared_domain") or domain).strip()
    provenance = str(contract.get("provenance") or "").strip()
    return bool(guarantee and declared and provenance in _PRODUCT_PROVENANCE)
