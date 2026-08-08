"""Shape-5 rule_diff: pair discovery, complement-free encoding, reports."""

from regexproof.rule_diff.encode import shape5_constraints
from regexproof.rule_diff.pairs import discover_pairs
from regexproof.rule_diff.specs import load_canonical_specs, reject_rule_derived_r1

__all__ = [
    "shape5_constraints",
    "discover_pairs",
    "load_canonical_specs",
    "reject_rule_derived_r1",
]

__all__ = [
    "discover_pairs",
    "load_canonical_specs",
    "reject_rule_derived_r1",
    "shape5_constraints",
]
