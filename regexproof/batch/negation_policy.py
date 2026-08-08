"""Per-dialect ModSecurity negation policy (fix-wave #72).

Negated ``!@rx`` / variable-selector records must never silently compile as
positive languages. Stock Z3 ``Complement()`` is language complement (TRAPS #1),
not char-class negation — this wave rejects all four dialects as unsupported.
"""

from __future__ import annotations

from typing import Literal

Policy = Literal["reject", "complement"]

# Wave default: reject-unsupported for every stock dialect.
NEGATION_POLICY: dict[str, Policy] = {
    "py_re": "reject",
    "ecma": "reject",
    "re2": "reject",
    "pcre": "reject",
}

NEGATED_UNSUPPORTED_REASON = "negated-unsupported"


def negation_decision(dialect: str) -> Policy:
    """Return the policy for ``dialect`` (default reject if unknown)."""
    return NEGATION_POLICY.get(dialect, "reject")


def should_reject_negated(dialect: str) -> bool:
    return negation_decision(dialect) == "reject"
