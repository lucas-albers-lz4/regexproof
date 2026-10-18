#!/usr/bin/env python3
"""Prove and replay Aidevops' pinned secret-basename pre-read guard."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.aidevops_secret_read_replay import (  # noqa: E402
    CALLER_SHA256,
    PIN,
    READ_TOOLS,
    REPOSITORY,
    SOURCE_BASENAME_PATTERN,
    SOURCE_FILE,
    SOURCE_SHA256,
    mutation_reproduces_secret_basename,
    run_secret_read,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-aidevops-node-secret-boundary"
CONTRACT_PATH = SLICE / "contract-basename.json"
COHORT_PATH = SLICE / "cohort-manifest.json"
ROSTER_PATH = SLICE / "roster-basename.json"
PROPERTY_ID = "AE-aidevops-secret-read-basename-coverage"
MUTATION_ID = "AE-aidevops-secret-read-mutated-basename-reaches-read"
BASENAME_DECLARATION = (
    f"const SECRET_BASENAME_RE = /{SOURCE_BASENAME_PATTERN}/i;"
)


def _verify_contract_roster_and_source(root: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("Aidevops secret-basename contract is not validly adopted")
    expected_site = (
        f"marcusquinn/aidevops@{PIN}:"
        ".agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs:7:SECRET_BASENAME_RE"
    )
    if contract.get("site") != expected_site:
        raise RuntimeError("Aidevops contract site differs from the allocated source site")
    adoption = contract.get("adoption", {})
    if (
        adoption.get("source_url") != REPOSITORY.removesuffix(".git")
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("Aidevops adoption record is not bound to the pinned helper")

    cohort = validate_manifest(json.loads(COHORT_PATH.read_text(encoding="utf-8")))
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if (
        roster.get("cohort_id") != cohort["cohort_id"]
        or roster.get("cohort_manifest_digest") != cohort["manifest_digest"]
    ):
        raise RuntimeError("Aidevops roster does not bind the separate ECMA calibration")
    matches = [
        row for row in roster.get("identities", [])
        if row.get("site") == expected_site and row.get("question_id") == PROPERTY_ID
    ]
    if len(matches) != 1 or matches[0].get("contract_sha256") != contract_digest(contract):
        raise RuntimeError("Aidevops roster does not bind the adopted basename contract")

    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("pinned Aidevops secret-read helper is missing or a symlink")
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("Aidevops helper bytes differ from the frozen source digest")
    helper = source.read_text(encoding="utf-8")
    if helper.count(BASENAME_DECLARATION) != 1:
        raise RuntimeError("pinned SECRET_BASENAME_RE declaration changed")
    for relative, digest in CALLER_SHA256.items():
        caller = root / relative
        if caller.is_symlink() or not caller.is_file():
            raise RuntimeError(f"pinned Aidevops caller is missing or a symlink: {relative}")
        if hashlib.sha256(caller.read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"pinned Aidevops caller digest differs: {relative}")
    return contract


def _verify_product() -> dict:
    variants = sorted({
        "".join(
            char.upper() if char.isalpha() and mask & (1 << index)
            else char.lower() if char.isalpha()
            else char
            for index, char in enumerate("secret")
        )
        for mask in range(1 << len("secret"))
    })
    read_paths = [f"/tmp/{name}" for name in variants]
    read_reasons = ["secret-bearing basename"] * len(read_paths)
    read_paths.extend((
        "/tmp/id_rsa", "/tmp/.env.local", "/tmp/credentials.json",
        "/tmp/service-account.json", "/tmp/kubeconfig", "/tmp/config.json",
        "/tmp/op-vault-export-2026.json", "/tmp/secret.pub", "/tmp/readme.txt",
    ))
    read_reasons.extend((
        "secret-bearing basename", "secret-bearing basename", "secret-bearing basename",
        "secret-bearing basename", "secret-bearing basename", "secret-bearing basename",
        "secret-bearing basename", "", "",
    ))
    paths = read_paths * len(READ_TOOLS)
    tools = [tool for tool in READ_TOOLS for _ in read_paths]
    expected_reasons = read_reasons * len(READ_TOOLS)
    paths.append("/tmp/secret")
    tools.append("Write")
    expected_reasons.append("secret-bearing basename")
    expected_blocked = [bool(reason) for reason in expected_reasons]
    expected_blocked[-1] = False  # Write does not pass through the read gate.

    results, node_version = run_secret_read(paths, tools=tools)
    if len(results) != len(paths):
        raise RuntimeError("Aidevops product replay returned the wrong output count")
    for index, (result, expected_reason, should_block) in enumerate(
        zip(results, expected_reasons, expected_blocked, strict=True)
    ):
        if result.get("reason") != expected_reason or result.get("blocked") is not should_block:
            raise RuntimeError(f"Aidevops basename helper disagreed at case {index}")

    mutated, _ = run_secret_read(
        ["/tmp/secret"] * len(READ_TOOLS),
        tools=list(READ_TOOLS),
        omit_secret_basename=True,
    )
    if (
        len(mutated) != len(READ_TOOLS)
        or any(result.get("reason") or result.get("blocked") for result in mutated)
        or not mutation_reproduces_secret_basename("secret")
    ):
        raise RuntimeError("Pinned secret-basename mutation did not reproduce read-through")

    return {
        "schema_version": "1",
        "gate_id": "aidevops-node-secret-read-basename",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "caller_sha256": CALLER_SHA256,
        "product_engine": "Node.js ECMAScript RegExp and node:path",
        "node_version": node_version,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "source_pattern": SOURCE_BASENAME_PATTERN,
        "declared_domain": "64 ASCII case variants of basename secret",
        "differential_cases": len(paths),
        "secret_case_variants": len(variants),
        "read_tools": list(READ_TOOLS),
        "representative_sensitive_basename_cases": 7,
        "public_key_and_negative_cases": 2,
        "write_tool_cases": 1,
        "mismatches": 0,
        "mutation_witness": "/tmp/secret",
        "mutation_product_results": mutated,
        "scope": (
            "SECRET_BASENAME_RE finite case-variant guarantee and exact pinned pre-read replay; "
            "does not establish policy completeness or false-positive rates."
        ),
    }


def _run_harness() -> list[dict]:
    completed = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "z3-verify.py"),
            "--json", "--require-ground-truth", "--require-domain", "--require-contract",
            "--fail-on-property-failure", PROPERTY_ID, MUTATION_ID,
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
        raise RuntimeError(f"Aidevops basename harness failed ({completed.returncode}): {detail}")
    try:
        return [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise RuntimeError("Aidevops basename harness returned invalid NDJSON") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Aidevops checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip Z3; run source/product checks")
    parser.add_argument("--output", type=Path, help="write the machine-readable gate report")
    args = parser.parse_args(argv)
    if args.source_root:
        requested = Path(args.source_root).expanduser().resolve()
        configured = os.environ.get("AIDEVOPS_SECRET_READ_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            parser.error("--source-root conflicts with AIDEVOPS_SECRET_READ_REPLAY_SOURCE")
        os.environ["AIDEVOPS_SECRET_READ_REPLAY_SOURCE"] = str(requested)
    try:
        root = source_root()
        print(f"Aidevops exact source: {root} @ {PIN}")
        _verify_contract_roster_and_source(root)
        formal = [] if args.product_only else _run_harness()
        report = _verify_product()
        report["formal_results"] = formal
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(
            f"Aidevops secret-basename gate: {report['differential_cases']} cases, "
            f"Node {report['node_version']}, 0 mismatches; pinned mutation reaches read"
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"Aidevops secret-basename gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
