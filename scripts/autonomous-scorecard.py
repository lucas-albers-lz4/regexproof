#!/usr/bin/env python3
"""Report the separate autonomous effort, proof/gate, bug, and outcome tracks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.mine.autonomous_work import (  # noqa: E402
    AutonomousWorkError,
    LOG_PATH,
    summarize,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=Path, default=LOG_PATH)
    parser.add_argument(
        "--cohort-id",
        action="append",
        help="include only this cohort ID (repeat to include multiple cohorts)",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = summarize(
            args.log,
            cohort_ids=set(args.cohort_id) if args.cohort_id is not None else None,
        )
    except (OSError, AutonomousWorkError) as exc:
        print(f"autonomous-scorecard: error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    counts = report["counts"]
    resources = report["resource_totals"]
    rates = report["rates"]
    print(f"autonomous runs: {report['run_count']}")
    print(
        "useful proofs/gates: "
        f"attempted={counts['proof_questions_attempted']} "
        f"decided={counts['decided_faithful_questions']} "
        f"UNSAT={counts['unsat_guarantees']} "
        f"local_gates={counts['local_runnable_gates']} "
        f"consumer_gates={counts['consumer_adopted_gates']} "
        f"mutations={counts['mutation_checks_passed']} "
        f"differential_cases={counts['differential_cases']}"
    )
    print(
        "bug discovery: "
        f"SAT={counts['sat_candidates']} replayed={counts['replayed_witnesses']} "
        f"reachable={counts['reachable_violations']} "
        f"impact_confirmed={counts['security_impact_confirmed']}"
    )
    print(
        "external outcomes: "
        f"sent={counts['third_party_reports_sent']} "
        f"confirmed={counts['maintainer_confirmations']} "
        f"fixed={counts['third_party_fixes']}"
    )
    print(
        "effort: "
        f"elapsed_seconds={resources['elapsed_seconds']} "
        f"wall_clock_seconds={resources['elapsed_seconds_by_basis']['wall_clock']} "
        f"phase_sum_seconds={resources['elapsed_seconds_by_basis']['phase_sum']} "
        f"contracts_per_hour={rates['contracts_per_agent_hour']} "
        f"cost_usd={resources['cost_usd']} "
        f"human_active_minutes={resources['human_active_minutes']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
