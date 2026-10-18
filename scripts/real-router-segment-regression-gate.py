#!/usr/bin/env python3
"""Differentially replay Real-Router's exact pinned segment validators."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.real_router_segment_replay import (  # noqa: E402
    CONSTANTS_FILE,
    CONSTANTS_SHA256,
    PIN,
    REPO_ID,
    REPOSITORY,
    SOURCE_PATTERN,
    TESTERS_SHA256,
    TESTERS_FILE,
    mutation_accepts_slash_in_all_segment_testers,
    run_helpers,
    verify_source,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-16-p2-real-router-segment"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "p6-wave" / "roster.json"
MANIFEST_PATH = ROOT / "properties" / "calibration" / "2026-09-12-calibration-20-r2" / "manifest.json"
INVENTORY_PATH = ROOT / "properties" / "calibration" / "2026-10-15-p2-source-inventory-v3" / "sites.ndjson"
PROPERTY_ID = "RR-route-segment-allowed-alphabet"
MUTATION_ID = "RR-route-segment-slash-allowlist-mutation"
EXPECTED_SITE = (
    f"{REPO_ID}@{PIN}:packages/route-utils/src/constants.ts:13:column-36"
)
ALLOWED = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-"
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _source_row() -> dict:
    matches = []
    for line in INVENTORY_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if (
            row.get("repo_id") == REPO_ID
            and row.get("pin") == PIN
            and row.get("site") == "packages/route-utils/src/constants.ts:13:36"
        ):
            matches.append(row)
    if len(matches) != 1:
        raise RuntimeError(f"expected one frozen P2 inventory site, found {len(matches)}")
    row = matches[0]
    if row.get("regex_id") != "bb84d7f740e031ca1c1fc94bd75826bf":
        raise RuntimeError("frozen inventory regex identity changed")
    if row.get("pattern") != SOURCE_PATTERN or row.get("source_file_sha256") != CONSTANTS_SHA256:
        raise RuntimeError("frozen inventory pattern or source digest changed")
    return row


def _verify_contract_roster() -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("Real-Router segment contract is not adopted")
    if contract.get("site") != EXPECTED_SITE:
        raise RuntimeError("Real-Router contract site identity changed")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != CONSTANTS_FILE
        or adoption.get("source_sha256") != CONSTANTS_SHA256
    ):
        raise RuntimeError("Real-Router contract adoption differs from exact source")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    member = [
        item for item in manifest.get("repos", [])
        if item.get("repo_id") == REPO_ID and item.get("pin") == PIN
    ]
    if len(member) != 1 or member[0].get("url", "").removesuffix(".git") != REPOSITORY:
        raise RuntimeError("Real-Router contract is not bound to the frozen 20-r2 member")

    row = _source_row()
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    identities = [
        item for item in roster.get("identities", [])
        if item.get("site") == EXPECTED_SITE and item.get("question_id") == PROPERTY_ID
    ]
    if (
        len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
        or roster.get("cohort_id") != "2026-09-12-calibration-20-r2"
    ):
        raise RuntimeError("P6 roster does not bind the exact adopted contract")
    return {"contract": contract, "source_row": row, "roster": roster}


def _cases() -> list[str]:
    values = [chr(codepoint) for codepoint in range(128)]
    values.extend(
        "".join(chars)
        for chars in itertools.product(range(128), repeat=2)
        for chars in [(chr(chars[0]), chr(chars[1]))]
    )
    values.extend(
        [
            "a", "route_1", "with.dot", "-edge-", "under_score", "A-._9",
            "/", "a/b", "\\", "a\\b", "a b", "a\t", "a\n", "a\r\n",
            "é", "雪", "😀", "\u2028", "\x00", "A" * 10_000, "A" * 10_001,
        ]
    )
    rng = random.Random(20261016)
    alphabet = "Az09_.-/\\ \t\n\x00é😀"
    values.extend(
        "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 96)))
        for _ in range(512)
    )
    return list(dict.fromkeys(values))


def _expected(value: str) -> bool | str:
    # The over-length check precedes the regex in the pinned helper.
    if len(value) > 10_000:
        return "RangeError"
    if value and all(ord(char) < 128 and char in ALLOWED for char in value):
        return True
    return "TypeError"


def run(source_root: Path) -> dict:
    source_binding = verify_source(source_root)
    evidence = _verify_contract_roster()
    cases = _cases()
    replay = run_helpers(cases, root=source_root)
    mismatches = []
    accepted_by_helper = [0, 0, 0]
    for index, (value, outcomes) in enumerate(zip(cases, replay["outcomes"], strict=True)):
        expected = _expected(value)
        for helper_index, outcome in enumerate(outcomes):
            if outcome is True:
                accepted_by_helper[helper_index] += 1
            if outcome != expected:
                mismatches.append(
                    {
                        "case": index,
                        "value": repr(value),
                        "helper_index": helper_index,
                        "actual": outcome,
                        "expected": expected,
                    }
                )
                if len(mismatches) >= 10:
                    break
        if len(mismatches) >= 10:
            break
    if mismatches:
        raise RuntimeError(f"exact-source validator/model mismatches: {mismatches!r}")

    mutation_witness_reproduces = mutation_accepts_slash_in_all_segment_testers(
        {"segment_char": "/"}
    )
    if not mutation_witness_reproduces:
        raise RuntimeError("source-weakened slash mutation did not reproduce")

    return {
        "schema_version": "1",
        "gate_id": "real-router-route-segment-allowed-ascii-alphabet",
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_files": {
            CONSTANTS_FILE: source_binding["constants_sha256"],
            TESTERS_FILE: source_binding["testers_sha256"],
        },
        "source_pattern": SOURCE_PATTERN,
        "product_engine": f"{replay['version']} Node.js ECMAScript via the exact pinned TypeScript helper source (native type stripping)",
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "helper_count": 3,
        "helpers": ["startsWithSegment", "endsWithSegment", "includesSegment"],
        "differential_cases_per_helper": len(cases),
        "differential_comparisons": len(cases) * 3,
        "actual_accepted_cases_per_helper": accepted_by_helper,
        "mismatches": 0,
        "mutation_witness": "/",
        "mutation_accepts_in_all_helpers": mutation_witness_reproduces,
        "source_row_regex_id": evidence["source_row"]["regex_id"],
        "contract_sha256": contract_digest(evidence["contract"]),
        "impact_scope": "This proves the documented segment-character invariant for these route utility helpers. The Real-Router admission decision was scale-based; this result does not classify the repository as a security tool or claim a security impact.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = run(args.source_root)
        if args.output:
            atomic_write_text(args.output, json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True))
    except Exception as exc:
        print(f"real-router-segment-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
