#!/usr/bin/env python3
"""Register a source-pinned, independently reviewed conversion idiom bucket."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.mine.conversion_bucket_registry import (  # noqa: E402
    BucketRegistryError,
    REGISTRY_PATH,
    append_registration,
    build_registration,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cluster", required=True)
    parser.add_argument("--bucket", required=True)
    parser.add_argument("--repository-url", required=True)
    parser.add_argument("--pin", required=True)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--gate-decision", type=Path, required=True)
    parser.add_argument("--product-engine", required=True)
    parser.add_argument(
        "--dialect-family",
        help="registered pattern dialect family; required for cohort-scoped scheduling",
    )
    parser.add_argument("--trust-map", action="append", required=True, metavar="CLASS=NOTE")
    parser.add_argument("--source-site", action="append", required=True, help="path:line:token")
    parser.add_argument("--question-family", required=True)
    parser.add_argument("--max-candidates", type=int, required=True)
    parser.add_argument("--registered-on", required=True)
    parser.add_argument("--rationale", required=True)
    parser.add_argument("--contract", type=Path, required=True, help="representative adopted contract JSON")
    parser.add_argument("--author", required=True)
    parser.add_argument("--reviewer", required=True)
    review = parser.add_mutually_exclusive_group(required=True)
    review.add_argument("--same-model", action="store_true")
    review.add_argument("--different-model", action="store_true")
    parser.add_argument("--registry", type=Path, default=REGISTRY_PATH)
    args = parser.parse_args(argv)
    try:
        decision = json.loads(args.gate_decision.read_text(encoding="utf-8"))
        if not isinstance(decision, dict) or decision.get("decision") != "go":
            raise BucketRegistryError("cluster must have a current gated:go decision")
        if decision.get("corpus") != args.cluster:
            raise BucketRegistryError("gate-decision corpus does not match cluster")
        if decision.get("corpus_pin") != args.pin:
            raise BucketRegistryError("gate-decision pin does not match registration pin")
        trust_map = {}
        for assignment in args.trust_map:
            if "=" not in assignment:
                raise BucketRegistryError("--trust-map must use CLASS=NOTE")
            key, value = assignment.split("=", 1)
            if key in trust_map:
                raise BucketRegistryError(f"duplicate trust-map class {key!r}")
            trust_map[key] = value
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
        entry = build_registration(
            cluster=args.cluster,
            bucket=args.bucket,
            repository_url=args.repository_url,
            pin=args.pin,
            checkout=args.checkout,
            product_engine=args.product_engine,
            trust_map=trust_map,
            source_sites=args.source_site,
            question_family=args.question_family,
            max_candidates=args.max_candidates,
            registered_on=args.registered_on,
            rationale=args.rationale,
            contract=contract,
            author=args.author,
            reviewer=args.reviewer,
            same_model=args.same_model,
            dialect_family=args.dialect_family,
        )
        append_registration(entry, args.registry)
    except (OSError, json.JSONDecodeError, BucketRegistryError, ValueError) as exc:
        print(f"register-conversion-bucket: error: {exc}", file=sys.stderr)
        return 2
    print(f"registered {args.cluster}/{args.bucket} for {args.max_candidates} candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
