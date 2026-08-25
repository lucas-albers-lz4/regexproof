"""Isolated harness runner for a scaffolded gate (no built-in P1–P6 registry).

Scaffolded ``gate.py`` must ``REGISTRY.clear()`` after importing ``prop``
because ``import regexproof.harness.core`` still executes
``harness/__init__.py``, which registers the built-in suites.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys

from regexproof.harness.core import (
    REGISTRY,
    check_contract_coverage,
    check_domain_coverage,
    check_mutation_coverage,
    run_one,
    validate_registry,
)

USAGE = """scaffolded regexproof gate

  python3 gate.py --list
  python3 gate.py --all --require-ground-truth --fail-on-property-failure
  python3 gate.py --check-mutation-coverage
"""


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        print(USAGE.strip())
        return 0
    require_ground_truth = "--require-ground-truth" in args
    require_domain = "--require-domain" in args
    require_contract = "--require-contract" in args
    as_json = "--json" in args
    check_cov_only = "--check-mutation-coverage" in args
    skip_gates = "--skip-registration-gate" in args
    fail_on_property_failure = "--fail-on-property-failure" in args
    flags = {
        "--require-ground-truth",
        "--require-domain",
        "--require-contract",
        "--json",
        "--check-mutation-coverage",
        "--skip-registration-gate",
        "--fail-on-property-failure",
    }
    args = [a for a in args if a not in flags]
    if check_cov_only:
        return check_mutation_coverage()
    if not skip_gates:
        failures, checked = validate_registry()
        if failures:
            for item in failures:
                print(f"REGISTRATION GATE FAILURE: {item}", file=sys.stderr)
            print(
                f"registration gate: {len(failures)} failure(s) across "
                f"{checked} pattern-declaring properties",
                file=sys.stderr,
            )
            return 2
    if not args or "--all" in args:
        names = sorted(REGISTRY)
    elif "--list" in args:
        for name in sorted(REGISTRY):
            entry = REGISTRY[name]
            print(
                f"{name}  expect_unsat={entry['expect_unsat']}  "
                f"kind={entry['kind']}  family={entry['family']}"
            )
        return 0
    else:
        names = [a for a in args if a in REGISTRY]
        missing = [a for a in args if a not in REGISTRY]
        if missing:
            print(f"unknown properties: {missing}", file=sys.stderr)
            return 2

    coverage_fail = check_mutation_coverage()
    domain_fail = check_domain_coverage(require=require_domain)
    contract_fail = check_contract_coverage(require=require_contract)
    failures = 0
    not_proven_count = 0
    results = []
    if as_json:
        sink = io.StringIO()
        with contextlib.redirect_stdout(sink):
            for name in names:
                res = run_one(name, REGISTRY[name], require_ground_truth)
                results.append(res)
                if not res["ok"]:
                    failures += 1
                if res.get("not_proven"):
                    not_proven_count += 1
                print(json.dumps(res, sort_keys=True), file=sys.__stdout__)
    else:
        for name in names:
            res = run_one(name, REGISTRY[name], require_ground_truth)
            results.append(res)
            if not res["ok"]:
                failures += 1
            if res.get("not_proven"):
                not_proven_count += 1
        print(f"\n{len(names) - failures}/{len(names)} passed")
    failures += domain_fail
    failures += contract_fail
    if not_proven_count or coverage_fail or domain_fail or contract_fail:
        return 1
    if fail_on_property_failure and failures:
        return 1
    return 0
