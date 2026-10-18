#!/usr/bin/env python3
"""Replay the exact pinned Real-Router navigation control validator."""

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

from regexproof.contract_adoption import (  # noqa: E402
    contract_digest,
    contract_is_adopted,
)
from regexproof.groundtruth.real_router_navigation_replay import (  # noqa: E402
    DEFAULT_SOURCE_ROOT,
    NAVIGATION_FILE,
    PIN,
    REPO_ID,
    REPOSITORY,
    SOURCE_SHA256,
    del_removal_mutation_reproduces,
    run_helper_values,
    verify_source,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-16-p2-real-router-navigation-source-review"
CONTRACT_PATH = SLICE / "contract.json"
REVIEW_EVIDENCE_PATH = SLICE / "review-evidence.json"
HISTORY_BEFORE_PATH = SLICE / "question-history-before.json"
ROSTER_PATH = SLICE / "p6-wave" / "roster.json"
INVENTORY_PATH = ROOT / "properties" / "calibration" / "2026-10-15-p2-source-inventory-v3" / "sites.ndjson"
PROPERTY_ID = "RR-navigation-param-control-characters-rejected"
MUTATION_ID = "RR-navigation-param-del-omission-mutation"
EXPECTED_SITE = f"{REPO_ID}@{PIN}:{NAVIGATION_FILE}:69:column-25"
CONTROL_CHARS = frozenset([*range(0x00, 0x20), 0x7F])


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"expected a JSON object in {path}")
    return value


def _source_row() -> dict:
    matches = []
    for line in INVENTORY_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if (
            row.get("repo_id") == REPO_ID
            and row.get("pin") == PIN
            and row.get("site") == f"{NAVIGATION_FILE}:69:25"
        ):
            matches.append(row)
    if len(matches) != 1:
        raise RuntimeError(f"expected one exact frozen inventory row, found {len(matches)}")
    row = matches[0]
    if (
        row.get("regex_id") != "1e31ed0154408e832cf456d8422b6e38"
        or row.get("pattern") != r"[\u0000-\u001F\u007F]"
        or row.get("source_file_sha256") != SOURCE_SHA256
        or row.get("call_kind") != "search"
        or row.get("dialect_family") != "ecma"
    ):
        raise RuntimeError("frozen inventory regex/source identity changed")
    return row


def _verify_contract_roster() -> dict:
    contract = _json(CONTRACT_PATH)
    required_contract_fields = {
        "schema_version", "site", "guarantee", "input_source", "trust",
        "declared_domain", "provenance", "adoption",
    }
    if (
        not required_contract_fields.issubset(contract)
        or contract.get("schema_version") != "1"
        or contract.get("trust") not in {"untrusted-input", "config", "internal"}
        or not contract_is_adopted(contract)
        or contract.get("site") != EXPECTED_SITE
    ):
        raise RuntimeError("navigation contract is not adopted or exact-site bound")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != NAVIGATION_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("contract adoption differs from the exact pinned validator")

    evidence = _json(REVIEW_EVIDENCE_PATH)
    candidates = [
        item for item in evidence.get("candidates", [])
        if item.get("regex_id") == "1e31ed0154408e832cf456d8422b6e38"
        and item.get("source_pin") == PIN
        and item.get("decision") == "adopted"
    ]
    if len(candidates) != 1 or candidates[0].get("source_binding", {}).get("sha256") != SOURCE_SHA256:
        raise RuntimeError("frozen source review does not bind the adopted inventory site")

    roster = _json(ROSTER_PATH)
    identities = [
        item for item in roster.get("identities", [])
        if item.get("question_id") == PROPERTY_ID and item.get("site") == EXPECTED_SITE
    ]
    if (
        len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
        or roster.get("cohort_id") != "2026-09-12-calibration-20-r2"
    ):
        raise RuntimeError("P6 roster does not freeze the adopted contract")

    history = _json(HISTORY_BEFORE_PATH)
    anchors = {
        f"{NAVIGATION_FILE}:69:25",
        f"{NAVIGATION_FILE}:69:column-25",
        EXPECTED_SITE,
    }
    duplicate = [
        item for item in history.get("entries", [])
        if item.get("site") in anchors
        and (item.get("repo_id") in {None, REPO_ID})
        and (item.get("source_pin") in {None, PIN})
    ]
    if duplicate:
        raise RuntimeError("pre-run question-history index already reserves the candidate site")
    return {
        "contract": contract,
        "contract_sha256": contract_digest(contract),
        "review_evidence_sha256": _sha256(REVIEW_EVIDENCE_PATH.read_bytes()),
        "roster": roster,
        "history_before_sha256": _sha256(HISTORY_BEFORE_PATH.read_bytes()),
    }


def _cases() -> list[str]:
    values = [chr(codepoint) for codepoint in range(128)]
    values.extend(
        first + second
        for first, second in itertools.product((chr(cp) for cp in range(128)), repeat=2)
    )
    values.extend(
        [
            "", "ordinary", "a\x00b", "a\x1fb", "a\x7fb", "\u0080", "\u009f",
            "é", "雪", "😀", "\u2028", "\u2029", "a" * 256,
            "prefix\x00" + "x" * 64, "prefix" + "x" * 63 + "\x7f",
        ]
    )
    rng = random.Random(20261016)
    alphabet = "Aa09 _-./\\\t\n\r\x00\x1f\x7f\u0080é😀"
    values.extend(
        "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 64)))
        for _ in range(512)
    )
    return list(dict.fromkeys(values))


def _expected(value: str) -> str:
    return "TypeError" if any(ord(char) in CONTROL_CHARS for char in value) else "accepted"


def run(source_root: Path) -> dict:
    source_binding = verify_source(source_root)
    evidence = _verify_contract_roster()
    source_row = _source_row()
    values = _cases()
    replay = run_helper_values(values, root=source_root)
    mismatches = []
    for index, (value, actual) in enumerate(zip(values, replay["outcomes"], strict=True)):
        expected = _expected(value)
        if actual != expected:
            mismatches.append({
                "case": index,
                "value": repr(value),
                "actual": actual,
                "expected": expected,
            })
            if len(mismatches) == 20:
                break

    mutation_reproduces = del_removal_mutation_reproduces(
        {"navigation_control_char": "\x7f"}
    )
    return {
        "schema_version": "1",
        "gate_id": "rr-navigation-control-validator-exact-pin",
        "repository_url": REPOSITORY,
        "repo_id": REPO_ID,
        "source_pin": PIN,
        "source_binding": source_binding,
        "source_site": source_row["site"],
        "qualified_site": EXPECTED_SITE,
        "regex_id": source_row["regex_id"],
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "contract_sha256": evidence["contract_sha256"],
        "review_evidence_sha256": evidence["review_evidence_sha256"],
        "history_before_sha256": evidence["history_before_sha256"],
        "node_version": replay["version"],
        "replay_case_count": len(values),
        "differential_comparison_count": len(values),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "mutation_replay": {
            "witness": "\\u007f",
            "original_outcome": "TypeError",
            "weakened_outcome": "accepted",
            "reproduced": mutation_reproduces,
            "source_mutation": "removed only \\u007F from CONTROL_CHARS_RE in a temporary exact-source copy",
        },
        "replay_adaptations": [
            "Rewrote the validator's one extensionless relative import to a temporary .mts type-guard barrel exporting the same four pinned functions.",
            "Copied the exact pinned helper and guard bodies. Node's type stripper removes erased TypeScript syntax.",
            "Rewrote the sole TypeScript parameter-property constructor in isParams as its equivalent JavaScript field assignment so Node can execute that exact guard body.",
        ],
        "passed": not mismatches and mutation_reproduces,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = run(args.source_root)
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        args.output.chmod(0o644)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"real-router-navigation-control-regression-gate: {exc}", file=sys.stderr)
        return 2
    print(
        f"navigation validator gate: cases={report['replay_case_count']} "
        f"mismatches={report['mismatch_count']} "
        f"mutation_reproduced={str(report['mutation_replay']['reproduced']).lower()} "
        f"node={report['node_version']}"
    )
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
