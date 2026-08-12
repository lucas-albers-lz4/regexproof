"""Property kind and call_kind taxonomies (Phase 1 registry plumbing)."""

from __future__ import annotations

from enum import StrEnum


class PropertyKind(StrEnum):
    """Harness / scanner property kinds — NDJSON values are the enum values."""

    PROPERTY = "property"
    COUNTEREXAMPLE_FINDER = "counterexample_finder"
    MUTATION_GUARD = "mutation_guard"
    BUG_DEMO = "bug_demo"
    RULE_DIFF = "rule_diff"
    # Scanner finding kinds (REPORTING.md)
    REDOS = "redos"
    USAGE_MISMATCH = "usage_mismatch"
    INTENT_MISMATCH = "intent_mismatch"
    TRIAGE = "triage"


class SolveResult(StrEnum):
    """Solver outcome strings in NDJSON (must stay identical)."""

    UNSAT = "unsat"
    SAT = "sat"
    TIMEOUT = "timeout"


PROPERTY_KINDS = frozenset(
    {
        PropertyKind.PROPERTY.value,
        PropertyKind.COUNTEREXAMPLE_FINDER.value,
        PropertyKind.MUTATION_GUARD.value,
        PropertyKind.BUG_DEMO.value,
        PropertyKind.RULE_DIFF.value,
    }
)

# Families that require a mutation_guard sibling (check_mutation_coverage).
KINDS_NEEDING_MUTATION_GUARD = frozenset(
    {
        PropertyKind.PROPERTY.value,
        PropertyKind.COUNTEREXAMPLE_FINDER.value,
        PropertyKind.RULE_DIFF.value,
    }
)

CALL_KINDS = frozenset(
    {
        "fullmatch",
        "match",
        "search",
        "exec",
        "substitution",
    }
)

DIALECTS = frozenset(
    {
        "py_re",
        "ecma",
        "re2",
        "pcre",
        "yara",
        "perl",
        "posix-shell",
    }
)

DOMAINS = frozenset(
    {
        "ascii",
        "wide",
    }
)


def validate_kind(kind: str) -> str:
    if kind not in PROPERTY_KINDS:
        raise ValueError(
            f"invalid kind {kind!r}; expected one of {sorted(PROPERTY_KINDS)}"
        )
    return kind


def validate_call_kind(call_kind: str | None) -> str | None:
    if call_kind is None:
        return None
    if call_kind not in CALL_KINDS:
        raise ValueError(
            f"invalid call_kind {call_kind!r}; expected one of {sorted(CALL_KINDS)}"
        )
    return call_kind


def validate_dialect(dialect: str) -> str:
    if dialect not in DIALECTS:
        raise ValueError(
            f"invalid dialect {dialect!r}; expected one of {sorted(DIALECTS)}"
        )
    return dialect


def validate_domain(domain: str) -> str:
    if domain not in DOMAINS:
        raise ValueError(
            f"invalid domain {domain!r}; expected one of {sorted(DOMAINS)}"
        )
    return domain
