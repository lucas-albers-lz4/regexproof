"""Product-reportability for harness results (#476).

UNSAT/SAT is hygiene until the property carries a contract and a declared
domain. Mutation guards are never product.
"""

from __future__ import annotations

from datetime import date
from functools import lru_cache
from typing import Any

from jsonschema import Draft202012Validator

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
# agent_derived is schema-valid but not product until an explicit adoption
# record documents direct user approval or the repository's standing delegation.
_PRODUCT_PROVENANCE = frozenset({"human", "version_diff", "cross_engine"})
_ADOPTION_AUTHORITIES = frozenset(
    {"direct_user_approval", "standing_user_delegation"}
)


def valid_contract_adoption(value: Any) -> bool:
    """Return whether an adoption record carries an approved decision and evidence."""
    if not isinstance(value, dict):
        return False
    if set(value) != {"status", "authority", "approved_on", "rationale", "evidence"}:
        return False
    if value.get("status") != "approved":
        return False
    if value.get("authority") not in _ADOPTION_AUTHORITIES:
        return False
    approved_on = value.get("approved_on")
    if not isinstance(approved_on, str) or not approved_on.strip():
        return False
    try:
        if date.fromisoformat(approved_on).isoformat() != approved_on:
            return False
    except ValueError:
        return False
    rationale = value.get("rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        return False
    evidence = value.get("evidence")
    return bool(
        isinstance(evidence, list)
        and evidence
        and all(isinstance(item, str) and item.strip() for item in evidence)
    )


def contract_is_adopted(contract: Any) -> bool:
    """True for valid human contracts or agent contracts with recorded approval."""
    if not valid_property_contract(contract):
        return False
    provenance = str(contract.get("provenance") or "").strip()
    if provenance == "human":
        return True
    return provenance == "agent_derived" and valid_contract_adoption(
        contract.get("adoption")
    )


@lru_cache(maxsize=1)
def _contract_validator() -> Draft202012Validator:
    return Draft202012Validator(property_contract_schema())


def valid_property_contract(contract: Any) -> bool:
    """Require the complete property-contract schema."""
    return isinstance(contract, dict) and _contract_validator().is_valid(contract)


def product_reportable(entry: dict[str, Any]) -> bool:
    """True when a solver verdict may be counted as a product property."""
    if entry.get("kind") not in _PRODUCT_KINDS:
        return False
    domain = entry.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        return False
    contract = entry.get("contract")
    if not valid_property_contract(contract):
        return False
    if "site" in entry and contract.get("site") != entry.get("site"):
        return False
    guarantee = str(contract.get("guarantee") or "").strip()
    declared = str(contract.get("declared_domain") or "").strip()
    provenance = str(contract.get("provenance") or "").strip()
    adopted_agent_contract = provenance == "agent_derived" and contract_is_adopted(
        contract
    )
    return bool(
        guarantee
        and declared
        and (provenance in _PRODUCT_PROVENANCE or adopted_agent_contract)
    )
