#!/usr/bin/env python3
"""Prove and replay Tracecat's exact artifact path-segment sanitizer."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import (  # noqa: E402
    contract_digest,
    verify_adoption_source,
)
from regexproof.groundtruth.tracecat_artifact_path_segment_replay import (  # noqa: E402
    PIN,
    SOURCE_FILE,
    SOURCE_PATTERN,
    SOURCE_SHA256,
    safe_path_segment,
    source_root,
    weakened_path_escapes_artifact_root,
)
from regexproof.harness import REGISTRY  # noqa: E402
from regexproof.harness.contract import (  # noqa: E402
    product_reportable,
    valid_product_contract,
)
from regexproof.harness.tracecat_artifact_path_segment import (  # noqa: E402
    CONTRACT,
    FAMILY,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

REPOSITORY = "https://github.com/TracecatHQ/tracecat"
SLICE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-tracecat-artifact-path-segment"
CONTRACT_PATH = SLICE / "contract.json"
SAFE_CHARS = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
)
SAMPLE_CHARS = (
    "aZ0_.-/\\:%\n\r\t\x00"
    "é中٣\uff11\u200b\ud800"
)


def _reference_segment(value: str) -> str:
    """Independent run-wise statement of the pinned regex replacement."""
    translated: list[str] = []
    in_replaced_run = False
    for char in value:
        if char in SAFE_CHARS:
            translated.append(char)
            in_replaced_run = False
        elif not in_replaced_run:
            translated.append("_")
            in_replaced_run = True
    return "".join(translated).strip("._") or "artifact"


def _prepare_source_root(raw: str | None) -> Path:
    if raw:
        requested = Path(raw).expanduser().resolve()
        configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            raise RuntimeError("--source-root conflicts with TRACECAT_REPLAY_SOURCE")
        os.environ["TRACECAT_REPLAY_SOURCE"] = str(requested)
    return source_root()


def _run_proof() -> None:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "z3-verify.py"),
        PROPERTY_ID,
        MUTATION_ID,
        "--require-ground-truth",
        "--fail-on-property-failure",
    ]
    subprocess.run(
        command,
        cwd=ROOT,
        env=os.environ.copy(),
        shell=False,
        timeout=180,
        check=True,
    )


def _cases() -> list[str]:
    values = ["".join(chars) for chars in itertools.product(SAMPLE_CHARS, repeat=1)]
    values.extend("".join(chars) for chars in itertools.product(SAMPLE_CHARS, repeat=2))
    values.extend(
        [
            "../../etc/passwd",
            "../../../outside",
            "..\\..\\outside",
            "C:\\Windows\\system.ini",
            "/absolute/path",
            "\\\\server\\share",
            ".",
            "..",
            "...",
            "___",
            "a..b",
            "a/b",
            "a\\b",
            "a\x00b",
            "é/中/٣",
            "x" * 1024,
        ]
    )
    rng = random.Random(20261016)
    values.extend(
        "".join(rng.choice(SAMPLE_CHARS) for _ in range(rng.randint(0, 256)))
        for _ in range(2048)
    )
    return list(dict.fromkeys(values))


def _verify_contract(root: Path) -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if contract != CONTRACT or not valid_product_contract(contract):
        raise RuntimeError("path-segment contract is not the adopted product contract")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
        or adoption.get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("contract adoption does not bind the exact pinned source")
    verify_adoption_source(contract, root)
    entry = REGISTRY.get(PROPERTY_ID)
    if entry is None or not product_reportable(entry):
        raise RuntimeError("registered path-segment property is not product-reportable")
    if entry.get("input_domain") != "unicode":
        raise RuntimeError("path-segment proof must declare the Unicode input domain")


def _run(source: Path, *, run_proof: bool = True) -> dict:
    root = _prepare_source_root(str(source))
    _verify_contract(root)
    digest = hashlib.sha256((root / SOURCE_FILE).read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError("Tracecat artifact provider source digest differs from contract")

    cases = _cases()
    mismatches: list[dict[str, object]] = []
    traversal_cases = 0
    with tempfile.TemporaryDirectory(prefix="tracecat-artifact-path-gate-") as temp:
        artifact_root = (Path(temp) / ".tracecat" / "artifacts").resolve()
        for index, value in enumerate(cases, 1):
            actual = safe_path_segment(value)
            expected = _reference_segment(value)
            if actual != expected:
                mismatches.append(
                    {
                        "case": index,
                        "input": repr(value),
                        "source_output": repr(actual),
                        "reference_output": repr(expected),
                    }
                )
                if len(mismatches) >= 5:
                    break
            if (
                not actual
                or "/" in actual
                or "\\" in actual
                or actual in {".", ".."}
                or any(char not in SAFE_CHARS for char in actual)
            ):
                raise RuntimeError(f"source helper emitted an unsafe segment: {actual!r}")
            path = (artifact_root / "case" / actual).resolve()
            if not path.is_relative_to(artifact_root):
                raise RuntimeError(f"source path escaped artifact root for {value!r}")
            if any(separator in value for separator in ("/", "\\")):
                traversal_cases += 1
    if mismatches:
        raise RuntimeError(f"source/reference transformation mismatches: {mismatches!r}")

    if not weakened_path_escapes_artifact_root("/"):
        raise RuntimeError("source-weakened slash mutation did not escape the artifact root")
    if run_proof:
        _run_proof()

    return {
        "schema_version": "1",
        "gate_id": "tracecat-mount-only-artifact-path-segment",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": digest,
        "source_pattern": SOURCE_PATTERN,
        "property_id": PROPERTY_ID,
        "family": FAMILY,
        "mutation_id": MUTATION_ID,
        "contract_sha256": contract_digest(CONTRACT),
        "product_engine": "CPython re and pathlib through the exact pinned _safe_path_segment helper",
        "guarantee": "Each sanitized artifact type, ID, or hydrated filename is one nonempty relative path component without slash, backslash, or dot traversal components.",
        "differential_cases": len(cases),
        "separator_containing_inputs": traversal_cases,
        "mismatches": 0,
        "path_escape_mutation_reproduced": True,
        "mutation_input": "../../outside",
        "mutation_only_change": "The exact pinned regex class was weakened to preserve slash.",
        "limitations": "Component-level path safety only; symlink ancestry, host_root provenance, races, and collisions are outside this contract. No current vulnerability or attacker-controlled reachability is claimed.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--skip-proof",
        action="store_true",
        help="run only the product-engine replay (the P6 wave runner owns proof execution)",
    )
    args = parser.parse_args(argv)
    try:
        report = _run(args.source_root, run_proof=not args.skip_proof)
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, indent=2, sort_keys=True) + "\n",
            )
        print(json.dumps(report, sort_keys=True))
    except Exception as exc:
        print(f"tracecat-artifact-path-segment-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
