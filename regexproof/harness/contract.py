"""Product-reportability for harness results (#476).

UNSAT/SAT is hygiene until the property carries a contract and a declared
domain. Mutation guards are never product.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

from jsonschema import Draft202012Validator

from regexproof.contract_adoption import contract_is_adopted
from regexproof.kinds import PropertyKind
from regexproof.schemas import property_contract_schema

_PRODUCT_KINDS = frozenset(
    {
        PropertyKind.PROPERTY.value,
        PropertyKind.COUNTEREXAMPLE_FINDER.value,
        PropertyKind.BUG_DEMO.value,
        PropertyKind.RULE_DIFF.value,
    }
)
# agent_derived needs a source-bound adoption record; bare drafts remain smoke.
_PRODUCT_PROVENANCE = frozenset({"human", "version_diff", "cross_engine"})


@lru_cache(maxsize=1)
def _contract_validator() -> Draft202012Validator:
    return Draft202012Validator(property_contract_schema())


def valid_product_contract(contract: Any) -> bool:
    """Require the full contract schema and a valid autonomous adoption when needed."""
    if not isinstance(contract, dict) or not _contract_validator().is_valid(contract):
        return False
    return contract_is_adopted(contract)


def product_reportable(entry: dict[str, Any]) -> bool:
    """True when a solver verdict may be counted as a product property."""
    if entry.get("kind") not in _PRODUCT_KINDS:
        return False
    domain = entry.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        return False
    contract = entry.get("contract")
    if not valid_product_contract(contract):
        return False
    if "site" in entry and contract.get("site") != entry.get("site"):
        return False
    guarantee = str(contract.get("guarantee") or "").strip()
    declared = str(contract.get("declared_domain") or domain).strip()
    provenance = str(contract.get("provenance") or "").strip()
    return bool(
        guarantee
        and declared
        and (provenance in _PRODUCT_PROVENANCE or provenance == "agent_derived")
    )


__all__ = ["contract_is_adopted", "product_reportable", "valid_product_contract"]
