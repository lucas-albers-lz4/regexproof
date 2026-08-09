"""Property kind and call_kind taxonomies (Phase 1 registry plumbing)."""

from __future__ import annotations

PROPERTY_KINDS = frozenset(
    {
        "property",
        "counterexample_finder",
        "mutation_guard",
        "bug_demo",
        "rule_diff",
    }
)

# Families that require a mutation_guard sibling (check_mutation_coverage).
KINDS_NEEDING_MUTATION_GUARD = frozenset(
    {
        "property",
        "counterexample_finder",
        "rule_diff",
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
