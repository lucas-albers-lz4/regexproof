"""CLI entry for the Z3 property harness."""

from __future__ import annotations

import contextlib
import io
import json
import sys

from regexproof.harness.core import (
    REGISTRY,
    check_domain_coverage,
    check_mutation_coverage,
    run_one,
    validate_registry,
)
# Side-effect: register built-in properties
import regexproof.harness.properties  # noqa: F401



def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    require_ground_truth = "--require-ground-truth" in args
    require_domain = "--require-domain" in args
    as_json = "--json" in args
    as_json_legacy = "--json-legacy" in args
    check_cov_only = "--check-mutation-coverage" in args
    skip_gates = "--skip-registration-gate" in args
    if as_json and as_json_legacy:
        print(
            "error: --json and --json-legacy are mutually exclusive",
            file=sys.stderr,
        )
        return 2
    args = [
        a
        for a in args
        if a
        not in (
            "--require-ground-truth",
            "--require-domain",
            "--json",
            "--json-legacy",
            "--check-mutation-coverage",
            "--skip-registration-gate",
        )
    ]
    if check_cov_only:
        return check_mutation_coverage()
    if not skip_gates:
        failures, checked = validate_registry()
        if failures:
            for f in failures:
                print(f"REGISTRATION GATE FAILURE: {f}", file=sys.stderr)
            print(
                f"registration gate: {len(failures)} failure(s) across "
                f"{checked} pattern-declaring properties (pass "
                "--skip-registration-gate to bypass)",
                file=sys.stderr,
            )
            return 2
    if not args or "--all" in args:
        named = [a for a in args if a != "--all"]
        if named:
            print(
                f"WARNING: --all ignores explicitly named properties: {named}",
                file=sys.stderr,
            )
        names = sorted(REGISTRY)
    elif "--list" in args:
        for n in sorted(REGISTRY):
            e = REGISTRY[n]
            print(
                f"{n}  expect_unsat={e['expect_unsat']}  "
                f"timeout={e['timeout_ms']}ms  "
                f"kind={e['kind']}  family={e['family']}  "
                f"call_kind={e.get('call_kind')}  "
                f"input_domain={e['input_domain']}  "
                f"ground_truth={'yes' if e.get('ground_truth') else 'no'}"
            )
            print(f"    domain: {e['domain']}")
        return 0
    else:
        names = [a for a in args if a in REGISTRY]
        missing = [a for a in args if a not in REGISTRY]
        if missing:
            print(f"unknown properties: {missing}", file=sys.stderr)
            return 2

    coverage_fail = check_mutation_coverage()
    domain_fail = check_domain_coverage(require=require_domain)
    failures = 0
    results = []
    if as_json or as_json_legacy:
        sink = io.StringIO()
        with contextlib.redirect_stdout(sink):
            for n in names:
                res = run_one(n, REGISTRY[n], require_ground_truth)
                results.append(res)
                if not res["ok"]:
                    failures += 1
                if as_json:
                    # Flush each record immediately so partial streams stay valid.
                    print(json.dumps(res, sort_keys=True), file=sys.__stdout__)
    else:
        for n in names:
            res = run_one(n, REGISTRY[n], require_ground_truth)
            results.append(res)
            if not res["ok"]:
                failures += 1
    failures += domain_fail
    if as_json_legacy:
        print(json.dumps(results, indent=2, sort_keys=True))
    elif not as_json:
        print(f"\n{len(names) - failures}/{len(names)} passed")
    return 1 if (failures or coverage_fail) else 0


if __name__ == "__main__":
    sys.exit(main())
