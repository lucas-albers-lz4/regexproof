#!/usr/bin/env python3
"""Replay Anax's exact pinned organization deny-list helper against Go RE2."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.anax_org_validate_replay import (  # noqa: E402
    PIN,
    SOURCE_FILE,
    SOURCE_PATTERN,
    SOURCE_SHA256,
    run_validate_org,
    source_root,
)
from regexproof.harness.anax_org_validate import (  # noqa: E402
    FORBIDDEN_ASCII,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-anax-org-validate-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
FORBIDDEN = frozenset(FORBIDDEN_ASCII)
MUTATED_FORBIDDEN = FORBIDDEN - {"?"}
SAFE_SAMPLES = (
    "",
    "org",
    "myorg-1",
    "org.with.dots",
    "org/child",
    "../org",
    r"org\child",
    "org#fragment",
    "org:name",
    "组织",
    "組織",
    "org-😀",
)
RANDOM_ALPHABET = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "-._/@:#\\+%"
    "é中😀"
)


def _verify_contract_roster_and_source(root: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("Anax organization deny-list contract is not validly adopted")
    expected_site = f"open-horizon/anax@{PIN}:cli/cliutils/cliutils.go:2277:MatchString"
    if contract.get("site") != expected_site:
        raise RuntimeError("Anax contract differs from the exact pinned ValidateOrg site")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git")
        != "https://github.com/open-horizon/anax"
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("Anax contract adoption is not bound to the verified source")

    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if roster.get("cohort_id") != "2026-09-12-calibration-20-r2":
        raise RuntimeError("Anax roster is not bound to frozen 20-r2")
    identities = [
        item for item in roster.get("identities", [])
        if item.get("site") == expected_site and item.get("question_id") == PROPERTY_ID
    ]
    if len(identities) != 1 or identities[0].get("contract_sha256") != contract_digest(contract):
        raise RuntimeError("frozen Anax roster does not bind the adopted contract")
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("pinned Anax ValidateOrg source is missing or a symlink")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Anax cliutils source digest differs: {digest}")
    return contract


def _cases() -> tuple[list[str], dict[str, int]]:
    inputs = list(SAFE_SAMPLES)
    classes = {"safe_and_scope_samples": len(inputs)}

    one_character = [chr(value) for value in range(1, 128)]
    inputs.extend(one_character)
    classes["non_nul_ascii_single_character"] = len(one_character)

    for character in FORBIDDEN_ASCII:
        for value in (character, f"org{character}name", f"{character}org"):
            inputs.append(value)
    classes["documented_forbidden_positions"] = len(FORBIDDEN_ASCII) * 3

    rng = random.Random(20261015)
    random_inputs = [
        "".join(rng.choice(RANDOM_ALPHABET) for _ in range(rng.randint(0, 160)))
        for _ in range(512)
    ]
    inputs.extend(random_inputs)
    classes["seeded_mixed_strings"] = len(random_inputs)

    # Every forbidden character also appears in a long value with the
    # character on both sides, checking Go MatchString search behavior.
    for character in FORBIDDEN_ASCII:
        inputs.append(("safeOrg" * 256) + character + ("tail" * 256))
    classes["long_search_strings"] = len(FORBIDDEN_ASCII)
    return inputs, classes


def _run_product() -> dict:
    root = source_root()
    _verify_contract_roster_and_source(root)
    inputs, case_classes = _cases()
    replay = run_validate_org(inputs)
    original = replay["original"]
    mutated = replay["mutated"]
    for index, value in enumerate(inputs):
        expected_original = any(character in FORBIDDEN for character in value)
        expected_mutated = any(character in MUTATED_FORBIDDEN for character in value)
        if original[index] != expected_original:
            raise RuntimeError(
                f"pinned ValidateOrg differs from the documented deny-list at case {index}: {value!r}"
            )
        if mutated[index] != expected_mutated:
            raise RuntimeError(
                f"weakened pinned ValidateOrg differs from its mutated deny-list at case {index}: {value!r}"
            )

    question_mark = inputs.index("?")
    if original[question_mark] is not True or mutated[question_mark] is not False:
        raise RuntimeError("weakening the pinned source pattern did not admit `?`")
    return {
        "schema_version": "1",
        "gate_id": "anax-orgname-denylist-20r2",
        "repository": "https://github.com/open-horizon/anax",
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "product_engine": "Go regexp (RE2)",
        "go_version": replay["go_version"],
        "source_pattern": SOURCE_PATTERN,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "mutation_witness": "?",
        "mutation_original_invalid": original[question_mark],
        "mutation_weakened_invalid": mutated[question_mark],
        "differential_cases": len(inputs),
        "case_classes": case_classes,
        "mismatches": 0,
        "scope": (
            "exact pinned ValidateOrg deny-list behavior and its one-character source mutation; "
            "OrgCreate/OrgDel rejection is source-reviewed; this does not establish a complete "
            "organization-name allow-list or path safety for allowed characters"
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Anax checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="accepted for P6 gate configuration")
    parser.add_argument("--output", type=Path, help="write machine-readable gate report")
    args = parser.parse_args(argv)
    try:
        if args.source_root:
            os.environ["ANAX_REPLAY_SOURCE"] = str(
                Path(args.source_root).expanduser().resolve()
            )
        report = _run_product()
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(
            f"Anax Go RE2 deny-list gate: {report['differential_cases']} strings, "
            f"Go {report['go_version']}, zero mismatches; weakened `?` is admitted"
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Anax organization deny-list gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
