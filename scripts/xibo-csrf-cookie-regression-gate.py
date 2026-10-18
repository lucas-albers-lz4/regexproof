#!/usr/bin/env python3
"""Replay Xibo's pinned OAuth consent CSRF cookie helper and mutation gate."""

from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.xibo_csrf_cookie_replay import (  # noqa: E402
    COMPONENT_FILE,
    CSRF_FILE,
    JSON_ENTRY_FILE,
    PIN,
    REPOSITORY,
    ROUTES_FILE,
    SOURCE_FILES,
    _verify_checkout,
    run_helper,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-xibo-csrf-cookie-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "pre-outcome-roster.json"
QUESTION_ID = "XC-xibo-csrf-cookie-capture-isolation"
MUTATION_ID = "XC-xibo-csrf-cookie-mutated-capture-spills"
EXPECTED_SITE = (
    f"xibosignage/xibo-cms@{PIN}:"
    "frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx:42:38"
)
COHORT_ID = "2026-09-12-calibration-20-r2"
MANIFEST_DIGEST = "5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d"
TOKEN = "a1b2c3d4" * 5
_COOKIE_VALUE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz._~-"
_COOKIE_NAME = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789_-"


class GateError(RuntimeError):
    """A source, proof, mutation, or product replay gate did not complete."""


def _load_frozen_inputs() -> dict[str, Any]:
    try:
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"cannot load the adopted contract and frozen roster: {exc}") from exc
    if not valid_product_contract(contract):
        raise GateError("Xibo contract is not validly adopted")
    adoption = contract["adoption"]
    if (
        contract.get("site") != EXPECTED_SITE
        or adoption.get("source_url") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != COMPONENT_FILE
        or adoption.get("source_sha256") != SOURCE_FILES[COMPONENT_FILE]
    ):
        raise GateError("contract adoption is not bound to the exact Xibo helper source")
    if (
        roster.get("cohort_id") != COHORT_ID
        or roster.get("cohort_manifest_digest") != MANIFEST_DIGEST
        or roster.get("scope") != "one-site, pre-outcome retrospective calibration"
    ):
        raise GateError("roster does not identify the frozen 20-r2 one-site calibration")
    identities = [
        row
        for row in roster.get("identities", [])
        if row.get("question_id") == QUESTION_ID and row.get("site") == EXPECTED_SITE
    ]
    if (
        len(identities) != 1
        or identities[0].get("pin") != PIN
        or identities[0].get("repo_id") != "xibosignage/xibo-cms"
        or identities[0].get("contract_sha256") != contract_digest(contract)
    ):
        raise GateError("pre-outcome roster does not bind the adopted contract digest")
    return contract


def _run_harness(source_root_path: Path) -> list[dict[str, Any]]:
    env = os.environ.copy()
    env["XIBO_CSRF_REPLAY_SOURCE"] = str(source_root_path)
    names = [QUESTION_ID, MUTATION_ID]
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--require-ground-truth",
            "--require-domain",
            "--require-contract",
            "--fail-on-property-failure",
            *names,
        ],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if result.returncode:
        raise GateError(
            f"Z3 proof/mutation harness failed ({result.returncode}):\n"
            f"{(result.stderr or result.stdout).strip()[-5000:]}"
        )
    try:
        rows = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise GateError("Z3 harness emitted invalid NDJSON") from exc
    if {row.get("name") for row in rows} != set(names):
        raise GateError("Z3 output does not contain exactly the contract and mutation guard")
    by_name = {row["name"]: row for row in rows}
    proof = by_name[QUESTION_ID]
    guard = by_name[MUTATION_ID]
    if (
        proof.get("kind") != "property"
        or proof.get("result") != "unsat"
        or proof.get("product") is not True
        or proof.get("not_proven")
        or not proof.get("ok")
    ):
        raise GateError("capture-body property did not produce one product UNSAT result")
    if (
        guard.get("kind") != "mutation_guard"
        or guard.get("result") != "sat"
        or guard.get("ground_truth") != "reproduced"
        or guard.get("not_proven")
        or not guard.get("ok")
        or (guard.get("witness") or {}).get("captured_cookie_character") != ";"
    ):
        raise GateError("capture-widening mutation did not reproduce its semicolon witness")
    return rows


def _targeted_cases() -> list[tuple[str, str]]:
    return [
        ("token first", f"XSRF-TOKEN={TOKEN}; session=sid"),
        ("token middle", f"session=sid; XSRF-TOKEN={TOKEN}; theme=dark"),
        ("token last", f"session=sid; XSRF-TOKEN={TOKEN}"),
        ("token after tab", f"session=sid;\tXSRF-TOKEN={TOKEN}; theme=dark"),
        ("no token", "session=sid; theme=dark"),
        ("empty token", "session=sid; XSRF-TOKEN=; theme=dark"),
        ("similar name", f"OTHER-XSRF-TOKEN={TOKEN}; session=sid"),
    ]


def _random_case(rng: random.Random, serial: int) -> str:
    before_count = rng.randrange(0, 6)
    after_count = rng.randrange(0, 6)

    def neighbor(index: int) -> str:
        name = "n" + "".join(rng.choice(_COOKIE_NAME) for _ in range(rng.randrange(1, 11)))
        value = "".join(rng.choice(_COOKIE_VALUE) for _ in range(rng.randrange(0, 25)))
        return f"{name}{index}={value}"

    before = [neighbor(index) for index in range(before_count)]
    after = [neighbor(index + 20) for index in range(after_count)]
    pairs = [*before, f"XSRF-TOKEN={TOKEN}", *after]
    delimiters = ["; " if rng.randrange(2) else ";\t" for _ in range(len(pairs) - 1)]
    cookie = pairs[0]
    for delimiter, pair in zip(delimiters, pairs[1:]):
        cookie += delimiter + pair
    if not cookie.isascii() or cookie.count("XSRF-TOKEN=") != 1:
        raise GateError(f"generator emitted an out-of-domain cookie at case {serial}")
    return cookie


def _reference_token(cookie: str) -> str:
    matches = []
    for pair in cookie.split(";"):
        name, separator, value = pair.lstrip(" \t").partition("=")
        if separator and name == "XSRF-TOKEN":
            matches.append(value)
    if len(matches) > 1:
        raise GateError("reference parser received a duplicate XSRF-TOKEN pair")
    return matches[0] if matches else ""


def _verify_product(source_root_path: Path) -> dict[str, Any]:
    sources = _verify_checkout(source_root_path)
    targeted = _targeted_cases()
    cookies = [cookie for _, cookie in targeted]
    rng = random.Random(20261015)
    random_cookies = [_random_case(rng, serial) for serial in range(1000)]
    cookies.extend(random_cookies)

    outputs, node_version = run_helper(cookies)
    expected = [_reference_token(cookie) for cookie in cookies]
    if outputs != expected:
        mismatch = next(
            index for index, pair in enumerate(zip(outputs, expected)) if pair[0] != pair[1]
        )
        raise GateError(
            f"pinned helper disagrees with the independent cookie-pair parser at case {mismatch}"
        )
    if any(output != TOKEN for output in outputs[:4]):
        raise GateError("pinned helper changed or truncated a valid server-issued token")
    if outputs[4:] and outputs[4] != "":
        raise GateError("pinned helper did not return empty for a cookie string with no token")

    mutation_cookie = f"XSRF-TOKEN={TOKEN}; session=neighbor"
    baseline, _ = run_helper([mutation_cookie])
    weakened, _ = run_helper([mutation_cookie], spill_to_neighbor=True)
    if baseline != [TOKEN] or weakened != [f"{TOKEN}; session=neighbor"]:
        raise GateError("exact capture-widening mutation failed the product sensitivity check")

    return {
        "node_version": node_version,
        "component_sha256": SOURCE_FILES[COMPONENT_FILE],
        "csrf_middleware_sha256": SOURCE_FILES[CSRF_FILE],
        "route_table_sha256": SOURCE_FILES[ROUTES_FILE],
        "json_entrypoint_sha256": SOURCE_FILES[JSON_ENTRY_FILE],
        "source_files_verified": len(sources),
        "cases": len(cookies),
        "case_classes": {
            "targeted": len(targeted),
            "seeded_valid_cookie_strings": len(random_cookies),
            "token_first_middle_last": 3,
            "missing_empty_and_similar_name_controls": 3,
            "tab_separator_control": 1,
        },
        "mutation_input": mutation_cookie,
        "baseline_mutation_output": baseline[0],
        "weakened_mutation_output": weakened[0],
        "external_network_requests": 0,
        "security_impact_confirmed": False,
        "scope_note": (
            "The gate executes the exact pinned helper in Node after removing only its TypeScript "
            "return-type annotation, verifies pinned caller/route/middleware source, and compares "
            "1,007 valid-domain cookie strings with an independent split-pair reference parser. "
            "It does not launch Xibo's PHP application or a browser, formalize duplicate-cookie "
            "ordering, or establish a security vulnerability."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Xibo checkout at the exact frozen pin")
    parser.add_argument("--product-only", action="store_true", help="skip the Z3 proof run")
    parser.add_argument("--output", type=Path, help="write the machine-readable gate report")
    args = parser.parse_args(argv)
    try:
        if args.source_root:
            requested = Path(args.source_root).expanduser().resolve()
            configured = os.environ.get("XIBO_CSRF_REPLAY_SOURCE")
            if configured and Path(configured).expanduser().resolve() != requested:
                parser.error("--source-root conflicts with XIBO_CSRF_REPLAY_SOURCE")
            os.environ["XIBO_CSRF_REPLAY_SOURCE"] = str(requested)
        contract = _load_frozen_inputs()
        checkout = source_root()
        if contract["adoption"]["source_pin"] != PIN:
            raise GateError("adopted contract source pin differs from runner source pin")
        print(f"Xibo exact source: {checkout} @ {PIN}")
        proof_records = [] if args.product_only else _run_harness(checkout)
        product = _verify_product(checkout)
        report = {
            "schema_version": "1",
            "gate_id": "xibo-csrf-cookie-capture-20r2",
            "repository": REPOSITORY,
            "source_pin": PIN,
            "source_files": dict(SOURCE_FILES),
            "question_id": QUESTION_ID,
            "mutation_guard_id": MUTATION_ID,
            "capture_body_property": "UNSAT: ASCII capture characters exclude semicolon",
            "mutation_property": "SAT + exact helper replay: widened capture includes following pair",
            "proof_records": proof_records,
            **product,
        }
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(json.dumps(report, ensure_ascii=True, sort_keys=True))
        return 0
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"xibo-csrf-cookie-regression-gate: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
