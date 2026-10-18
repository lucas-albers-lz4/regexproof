#!/usr/bin/env python3
"""Record autonomous adoption for a contract after checking a pinned source checkout."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from jsonschema import Draft202012Validator, FormatChecker, ValidationError  # noqa: E402

from regexproof.contract_adoption import build_adoption_record  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.schemas import property_contract_schema  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--repository-url", required=True)
    parser.add_argument("--pin", required=True)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--source-file", required=True)
    parser.add_argument("--evidence", action="append", required=True)
    parser.add_argument("--rationale", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--reviewer", required=True)
    review = parser.add_mutually_exclusive_group(required=True)
    review.add_argument("--same-model", action="store_true")
    review.add_argument("--different-model", action="store_true")
    parser.add_argument("--approved-on", required=True, help="ISO date")
    parser.add_argument(
        "--authority",
        choices=("standing_user_delegation", "direct_user_approval"),
        default="standing_user_delegation",
    )
    args = parser.parse_args(argv)
    try:
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
        if not isinstance(contract, dict):
            raise ValueError("contract file must contain a JSON object")
        contract["provenance"] = "agent_derived"
        contract.pop("adoption", None)
        contract["adoption"] = build_adoption_record(
            contract,
            repository_url=args.repository_url,
            pin=args.pin,
            checkout=args.checkout,
            source_file=args.source_file,
            evidence=args.evidence,
            rationale=args.rationale,
            author=args.author,
            reviewer=args.reviewer,
            same_model=args.same_model,
            approved_on=args.approved_on,
            authority=args.authority,
        )
        Draft202012Validator(
            property_contract_schema(), format_checker=FormatChecker()
        ).validate(contract)
        atomic_write_text(
            args.contract,
            json.dumps(contract, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ValueError, ValidationError) as exc:
        print(f"adopt-property-contract: {exc}", file=sys.stderr)
        return 2
    print(f"adopted {contract.get('site')} under autonomous-contracts-v1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
