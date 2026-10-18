#!/usr/bin/env python3
"""Prove and replay Aidevops' pinned Node secret-read extension boundary."""

from __future__ import annotations

import argparse
import hashlib
import itertools
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
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_PATTERN,
    SOURCE_SHA256,
    mutation_reproduces,
    run_secret_read,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-aidevops-node-secret-boundary"
CONTRACT_PATH = SLICE / "contract.json"
COHORT_PATH = SLICE / "cohort-manifest.json"
ROSTER_PATH = SLICE / "roster.json"
EVIDENCE_PATH = SLICE / "source-evidence.json"
PROPERTY_ID = "AE-aidevops-secret-read-extension-coverage"
MUTATION_ID = "AE-aidevops-secret-read-mutated-pem-reaches-read"
EXTENSIONS = ("pem", "key", "p12", "pfx", "kdbx", "age", "asc", "gpg")
CASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def _verify_contract_roster_and_callers(root: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("Aidevops secret-read contract is not validly adopted")
    expected_site = (
        f"marcusquinn/aidevops@{PIN}:"
        ".agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs:8:28"
    )
    if contract.get("site") != expected_site:
        raise RuntimeError("Aidevops contract site differs from the exact pinned regex")
    adoption = contract.get("adoption", {})
    if (
        adoption.get("source_url") != REPOSITORY.removesuffix(".git")
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("Aidevops adoption record is not bound to the pinned helper")

    cohort = validate_manifest(json.loads(COHORT_PATH.read_text(encoding="utf-8")))
    if cohort.get("cohort_id") != "2026-10-15-aidevops-node-secret-boundary-calibration":
        raise RuntimeError("Aidevops Node contract is not in its separate calibration cohort")
    if cohort.get("repos") != [{
        "repo_id": "marcusquinn/aidevops",
        "url": REPOSITORY.removesuffix(".git"),
        "pin": PIN,
        "dialect_family": "ecma",
        "boundary_family": "security-boundary",
        "score": 1,
        "sites": 1042,
    }]:
        raise RuntimeError("Aidevops Node calibration cohort changed")

    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if (
        roster.get("cohort_id") != cohort["cohort_id"]
        or roster.get("cohort_manifest_digest") != cohort["manifest_digest"]
    ):
        raise RuntimeError("Aidevops roster does not bind the ECMA calibration cohort")
    identities = [
        row for row in roster.get("identities", [])
        if row.get("site") == expected_site and row.get("question_id") == PROPERTY_ID
    ]
    if len(identities) != 1 or identities[0].get("contract_sha256") != contract_digest(contract):
        raise RuntimeError("Aidevops roster does not bind the adopted contract digest")

    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
    if evidence.get("pin") != PIN or evidence.get("repository") != REPOSITORY.removesuffix(".git"):
        raise RuntimeError("Aidevops caller evidence is not bound to the pinned repository")
    callers = {row.get("path"): row for row in evidence.get("callers", [])}
    for relative, expected_hash in CALLER_SHA256.items():
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"Aidevops caller evidence file is missing or a symlink: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected_hash or callers.get(relative, {}).get("sha256") != expected_hash:
            raise RuntimeError(f"Aidevops caller source digest differs at {relative}")

    hooks = (root / ".agents/plugins/opencode-aidevops/quality-hooks.mjs").read_text(encoding="utf-8")
    approval = (root / ".agents/plugins/opencode-aidevops/source-access-approval.mjs").read_text(encoding="utf-8")
    helper = (root / SOURCE_FILE).read_text(encoding="utf-8")
    if not (
        "checkSecretReadWithApproval({" in hooks
        and "checkSecretReadGate," in hooks
        and "secretReadBlockReason(filePath)" in approval
        and "checkSecretReadGate(tool, args, log);" in approval
        and f"const SECRET_EXTENSION_RE = /{SOURCE_PATTERN}/i;" in helper
    ):
        raise RuntimeError("Aidevops exact-pin pre-read caller or extension rule changed")
    return contract


def _case_variants(extension: str) -> list[str]:
    letters = [index for index, char in enumerate(extension) if char.isalpha()]
    variants = []
    for bits in itertools.product((False, True), repeat=len(letters)):
        chars = list(extension)
        for index, uppercase in zip(letters, bits, strict=True):
            chars[index] = chars[index].upper() if uppercase else chars[index].lower()
        variants.append("." + "".join(chars))
    return variants


def _verify_product() -> dict:
    paths: list[str] = []
    expected_reasons: list[str] = []
    for extension in EXTENSIONS:
        for suffix in _case_variants(extension):
            paths.append(f"/tmp/fixture{suffix}")
            expected_reasons.append("secret-bearing file extension")
    paths.extend((
        "/tmp/id_rsa.pub",
        "/tmp/fixture.pem.pub",
        "/tmp/readme.txt",
        "/tmp/file-🧪.PEM",
        "/tmp/fixture.pem",
    ))
    expected_reasons.extend((
        "", "", "", "secret-bearing file extension", "secret-bearing file extension"
    ))
    expected_blocked = [bool(reason) for reason in expected_reasons]
    expected_blocked[-1] = False  # Write is not a read tool.
    tools = ["Read"] * (len(paths) - 1) + ["Write"]

    results, node_version = run_secret_read(paths, tools=tools)
    if len(results) != len(paths):
        raise RuntimeError("Aidevops product replay returned the wrong output count")
    for index, (result, expected_reason, should_block) in enumerate(
        zip(results, expected_reasons, expected_blocked, strict=True)
    ):
        if (
            result.get("reason") != expected_reason
            or result.get("blocked") is not should_block
        ):
            raise RuntimeError(f"Aidevops secret-read helper disagreed at case {index}")

    mutated, _ = run_secret_read(["/tmp/proof.pem"], omit_pem_extension=True)
    if (
        len(mutated) != 1
        or mutated[0].get("reason")
        or mutated[0].get("blocked")
        or not mutation_reproduces("proof.pem")
    ):
        raise RuntimeError("Pinned .pem mutation did not reproduce a read-through")

    return {
        "schema_version": "1",
        "gate_id": "aidevops-node-secret-read-extension",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "caller_sha256": CALLER_SHA256,
        "product_engine": "Node.js ECMAScript RegExp and node:path",
        "node_version": node_version,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "source_pattern": SOURCE_PATTERN,
        "declared_extensions": list(EXTENSIONS),
        "differential_cases": len(paths),
        "positive_extension_cases": sum(len(_case_variants(ext)) for ext in EXTENSIONS) + 1,
        "public_key_and_negative_cases": 4,
        "mismatches": 0,
        "mutation_witness": "/tmp/proof.pem",
        "mutation_product_result": mutated[0],
        "scope": "Private-key extension branch of the exact pinned pre-read gate; other path rules are out of scope.",
    }


def _run_harness() -> list[dict]:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--require-ground-truth",
            "--require-domain",
            "--require-contract",
            "--fail-on-property-failure",
            PROPERTY_ID,
            MUTATION_ID,
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
        raise RuntimeError(f"Aidevops property harness failed ({completed.returncode}): {detail}")
    try:
        return [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise RuntimeError("Aidevops property harness returned invalid NDJSON") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Aidevops checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip Z3; run source and product checks")
    parser.add_argument("--output", type=Path, help="write the machine-readable product gate report")
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
        _verify_contract_roster_and_callers(root)
        harness_results = [] if args.product_only else _run_harness()
        report = _verify_product()
        report["formal_results"] = harness_results
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(
            f"Aidevops secret-read gate: {report['differential_cases']} cases, "
            f"Node {report['node_version']}, 0 mismatches; pinned .pem mutation reaches read"
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"Aidevops secret-read gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
