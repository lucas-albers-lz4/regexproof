"""Independent-spec R1 catalog loader + rule-derived rejection gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CANONICAL_SCHEMA_VERSION = "1"


def load_canonical_specs(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != CANONICAL_SCHEMA_VERSION:
        raise ValueError(f"unsupported canonical_specs schema_version={data.get('schema_version')!r}")
    specs = data.get("specs") or []
    if not isinstance(specs, list):
        raise ValueError("canonical_specs.specs must be a list")
    for spec in specs:
        for key in (
            "id",
            "pattern",
            "flags",
            "dialect",
            "call_kind",
            "maps_to_rule_id",
            "provenance",
        ):
            if key not in spec:
                raise ValueError(f"canonical spec missing {key!r}: {spec.get('id')}")
    return specs


def gitleaks_rule_patterns(toml_path: Path) -> set[str]:
    """All regex strings from a gitleaks-style TOML (for integrity checks)."""
    try:
        import tomllib
    except ModuleNotFoundError:  # pragma: no cover
        import tomli as tomllib  # type: ignore

    data = tomllib.loads(toml_path.read_text(encoding="utf-8"))
    patterns: set[str] = set()
    for rule in data.get("rules") or []:
        if not isinstance(rule, dict):
            continue
        pat = rule.get("regex") or rule.get("pattern")
        if isinstance(pat, str) and pat:
            patterns.add(pat)
    return patterns


def reject_rule_derived_r1(
    specs: list[dict[str, Any]],
    *,
    rule_patterns: set[str],
) -> list[str]:
    """Return violation messages if any R1 pattern equals a rule-file pattern.

    Independent-spec R1 must not be a copy of a detector rule.
    """
    violations: list[str] = []
    for spec in specs:
        pat = spec.get("pattern") or ""
        if pat in rule_patterns:
            violations.append(
                f"rule-derived R1 forbidden: spec {spec.get('id')!r} pattern equals "
                f"gitleaks rule mapped as {spec.get('maps_to_rule_id')!r}"
            )
    return violations
