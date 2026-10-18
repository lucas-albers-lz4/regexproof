#!/usr/bin/env python3
"""Prove and replay AutoAR's pinned Go JavaScript endpoint capture class."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.autoar_jsendpoints_replay import (  # noqa: E402
    GO_TOOLCHAIN,
    PIN,
    SOURCE_FILE,
    SOURCE_SHA256,
    mutation_reproduces_quote,
    run_extractor,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-autoar-jsendpoint-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
PROPERTY_ID = "AA-autoar-jsendpoint-assignment-capture-delimiter"
MUTATION_ID = "AA-autoar-jsendpoint-mutated-quote-capture"
QUESTION_IDS = (PROPERTY_ID, MUTATION_ID)
FORBIDDEN = ('"', "'", "`", " ", "\t", "\n", "\f", "\r")
NOISE = (
    ".js", ".css", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
    ".woff", ".woff2", ".ttf", ".eot", ".map", ".min.", "//",
    "localhost", "127.0.0.1", "example.com", "schema.org", "w3.org",
    "mozilla.org", "jquery", "${",
)
SAFE_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/_-:?=+~"


def _verify_contract_roster_and_source(root: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("AutoAR endpoint contract is not validly adopted")
    expected_site = f"h0tak88r/AutoAR@{PIN}:{SOURCE_FILE}:181:BASE_URL"
    if contract.get("site") != expected_site:
        raise RuntimeError("AutoAR endpoint contract differs from the exact pinned source site")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git")
        != "https://github.com/h0tak88r/AutoAR"
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("AutoAR endpoint adoption is not bound to the verified source")

    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if roster.get("cohort_id") != "2026-09-12-calibration-20-r2":
        raise RuntimeError("AutoAR endpoint roster is not bound to frozen 20-r2")
    identities = [
        item for item in roster.get("identities", [])
        if item.get("site") == expected_site and item.get("question_id") == PROPERTY_ID
    ]
    if len(identities) != 1 or identities[0].get("contract_sha256") != contract_digest(contract):
        raise RuntimeError("frozen AutoAR endpoint roster does not bind the adopted contract")

    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("pinned AutoAR endpoint source is missing or a symlink")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"AutoAR endpoint source digest differs: {digest}")
    return contract


def _accepted(value: str) -> bool:
    lowered = value.lower()
    return not any(token in lowered for token in NOISE)


def _assignment(value: str) -> str:
    return f'const apiUrl = "{value}";'


def _cases() -> tuple[list[str], dict[str, int], list[tuple[int, str]]]:
    contents: list[str] = []
    expected: list[tuple[int, str]] = []
    classes: dict[str, int] = {}

    def add(class_name: str, body: str, expected_value: str | None = None) -> None:
        index = len(contents)
        contents.append(body)
        classes[class_name] = classes.get(class_name, 0) + 1
        if expected_value is not None:
            expected.append((index, expected_value))

    boundaries = (4, 199, 200, 201, 300)
    for length in boundaries:
        value = "serv" if length == 4 else "service/" + ("a" * (length - 8))
        if len(value) != length or not _accepted(value):
            raise RuntimeError(f"invalid safe length-boundary fixture at {length}")
        add("capture_length_boundary", _assignment(value), value[:200])

    rng = random.Random(20261015)
    for _ in range(128):
        while True:
            suffix = "".join(rng.choice(SAFE_ALPHABET) for _ in range(rng.randint(4, 205)))
            value = "service/" + suffix
            if _accepted(value):
                break
        add("seeded_safe_ascii_assignment", _assignment(value), value[:200])

    delimiter_prefixes = ("serv", "service/", "service/v1/")
    for delimiter in FORBIDDEN:
        for prefix in delimiter_prefixes:
            add(
                "forbidden_delimiter_mutations",
                _assignment(prefix + delimiter + "users"),
                prefix,
            )

    unicode_values = ("service/é/v1/users", "service/中/v1/items", "service/😀/v1/lookup")
    for value in unicode_values:
        add("unicode_product_samples", _assignment(value), value)

    add("malformed_assignment", 'const apiUrl = "service/v1/users', "service/v1/users")
    add("malformed_assignment", 'const apiUrl = ""', None)
    add("malformed_assignment", "const apiUrl = service/v1/users;", None)
    return contents, classes, expected


def _verify_product() -> dict:
    contents, classes, expected_rows = _cases()
    outputs, go_version = run_extractor(contents)
    if go_version != GO_TOOLCHAIN or len(outputs) != len(contents):
        raise RuntimeError("AutoAR replay used the wrong Go toolchain or returned a bad output count")

    for index, row in enumerate(outputs):
        if any(any(character in endpoint for character in FORBIDDEN) for endpoint in row):
            raise RuntimeError(f"AutoAR emitted a forbidden delimiter in case {index}: {row!r}")
    for index, expected in expected_rows:
        if expected not in outputs[index]:
            raise RuntimeError(
                f"AutoAR did not emit the expected assignment capture in case {index}: "
                f"expected {expected!r}, got {outputs[index]!r}"
            )
    for index in range(len(contents)):
        if index not in {row for row, _ in expected_rows} and outputs[index]:
            raise RuntimeError(f"unexpected endpoint from malformed assignment case {index}: {outputs[index]!r}")

    mutated, mutated_go = run_extractor(
        [_assignment("service/v1/users")], allow_quote=True
    )
    if (
        mutated_go != GO_TOOLCHAIN
        or not mutated
        or not any('"' in endpoint for endpoint in mutated[0])
        or not mutation_reproduces_quote({"capture_character": '"'})
    ):
        raise RuntimeError("weakened pinned capture class did not store its real quote witness")

    return {
        "schema_version": "1",
        "gate_id": "autoar-jsendpoint-capture-20r2",
        "repository": "https://github.com/h0tak88r/AutoAR",
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "product_engine": "Go regexp (RE2)",
        "go_version": go_version,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "mutation_witness": '"',
        "mutation_product_output": mutated[0],
        "differential_cases": len(contents),
        "case_classes": classes,
        "forbidden_delimiter_outputs": 0,
        "expected_assignment_captures": len(expected_rows),
        "mismatches": 0,
        "scope": (
            "URL-assignment capture delimiter exclusion and local extractor replay; "
            "not endpoint validity, scope safety, or extraction completeness"
        ),
    }


def _run_harness() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--require-ground-truth",
            "--require-domain",
            "--require-contract",
            "--fail-on-property-failure",
            *QUESTION_IDS,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()[-4000:]
        raise RuntimeError(f"AutoAR endpoint proof harness failed ({completed.returncode}): {detail}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean AutoAR checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip Z3 and run source/product gates")
    parser.add_argument("--output", type=Path, help="write machine-readable product gate report")
    args = parser.parse_args(argv)
    if args.source_root:
        requested = Path(args.source_root).expanduser().resolve()
        configured = os.environ.get("AUTOAR_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            parser.error("--source-root conflicts with AUTOAR_REPLAY_SOURCE")
        os.environ["AUTOAR_REPLAY_SOURCE"] = str(requested)
    try:
        from regexproof.groundtruth.autoar_html_escape_replay import source_root

        root = source_root()
        print(f"AutoAR exact source: {root} @ {PIN}")
        _verify_contract_roster_and_source(root)
        if not args.product_only:
            _run_harness()
        report = _verify_product()
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(
            f"AutoAR Go product differential: {report['differential_cases']} values, "
            f"Go {report['go_version']}, 0 delimiter leaks; weakened capture stores quote"
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"AutoAR JavaScript endpoint capture gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
