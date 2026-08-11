"""Importable Z3 property harness (canonical REGISTRY + run_one).

Replaces path-based ``importlib`` loads of ``scripts/z3-verify.py`` (#192).
"""

from __future__ import annotations

# Register built-in properties before re-exporting (side effect on REGISTRY).
import regexproof.harness.properties  # noqa: F401
from regexproof.harness.cli import main
from regexproof.harness.core import (
    REGISTRY,
    SCHEMA_VERSION,
    Z3_VERSION,
    check_domain_coverage,
    check_mutation_coverage,
    ci,
    ci_class,
    engine_versions,
    prefix_match,
    prop,
    run_one,
    z3_str,
)

__all__ = [
    "REGISTRY",
    "SCHEMA_VERSION",
    "Z3_VERSION",
    "check_domain_coverage",
    "check_mutation_coverage",
    "ci",
    "ci_class",
    "engine_versions",
    "main",
    "prefix_match",
    "prop",
    "run_one",
    "z3_str",
]
