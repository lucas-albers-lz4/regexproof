#!/usr/bin/env python3
"""Prove and replay Tracecat's pinned table/column identifier request gate."""

from __future__ import annotations

import argparse
import itertools
import json
import os
import random
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pydantic  # noqa: E402

from regexproof.contract_adoption import (  # noqa: E402
    contract_digest,
    verify_adoption_source,
)
from regexproof.groundtruth.tracecat_table_identifier_replay import (  # noqa: E402
    IDENTIFIER_PATTERN,
    MUTATION_NAME,
    PIN,
    REPOSITORY,
    SCHEMA_FILE,
    current_model_accepts,
    current_quote_identifier,
    current_service_accepts,
    exact_table_path_shape,
    source_digests,
    source_root,
    table_identifier_quote_mutation_reproduces,
)
from regexproof.harness import REGISTRY  # noqa: E402
from regexproof.harness.contract import (  # noqa: E402
    product_reportable,
    valid_product_contract,
)
from regexproof.harness.tracecat_table_identifier import (  # noqa: E402
    CONTRACT,
    FAMILY,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-17-autonomous-tracecat-table-identifier"
CONTRACT_PATH = SLICE / "contract.json"
SAMPLE_CHARS = 'aAZ0_";\\\n\r\t\x00é中٣'


def _prepare_source_root(raw: str | None) -> Path:
    if raw:
        requested = Path(raw).expanduser().resolve()
        configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            raise RuntimeError("--source-root conflicts with TRACECAT_REPLAY_SOURCE")
        os.environ["TRACECAT_REPLAY_SOURCE"] = str(requested)
    return source_root()


def _run_proof() -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            PROPERTY_ID,
            MUTATION_ID,
            "--require-ground-truth",
            "--fail-on-property-failure",
        ],
        cwd=ROOT,
        env=os.environ.copy(),
        shell=False,
        timeout=180,
        check=True,
    )


def _locked_pydantic_version(root: Path) -> str:
    lock = tomllib.loads((root / "uv.lock").read_text(encoding="utf-8"))
    versions = {
        package.get("version")
        for package in lock.get("package", [])
        if package.get("name") == "pydantic"
    }
    if len(versions) != 1:
        raise RuntimeError(f"expected one locked Pydantic version, found {versions!r}")
    return str(next(iter(versions)))


def _cases() -> list[str]:
    values = [
        "".join(chars)
        for width in (1, 2)
        for chars in itertools.product(SAMPLE_CHARS, repeat=width)
    ]
    values.extend(
        [
            "a",
            "_0",
            "a\"",
            'a"; DROP TABLE x; --',
            "a\n",
            "a\nother",
            "a\r",
            "a\t",
            "a\x00",
            "é",
            "中",
            "a" * 100,
            "a" * 101,
            "_" * 100,
            "a" * 99 + "\n",
            "a" * 100 + "\n",
        ]
    )
    rng = random.Random(20261017)
    values.extend(
        "".join(rng.choice(SAMPLE_CHARS) for _ in range(rng.randint(0, 103)))
        for _ in range(2048)
    )
    return list(dict.fromkeys(values))


def _expected_schema_accept(value: str) -> bool:
    if not 1 <= len(value) <= 100:
        return False
    exact = r"[a-zA-Z_][a-zA-Z0-9_]*"
    if re.fullmatch(exact, value):
        return True
    # Python's `$` permits a match immediately before one final line feed.
    return value.endswith("\n") and bool(re.fullmatch(exact, value[:-1]))


def _expected_service_accept(value: str) -> bool:
    return bool(
        value
        and all(char.isalnum() or char == "_" for char in value)
        and (value[0].isalpha() or value[0] == "_")
    )


def _verify_contract(root: Path) -> dict[str, str]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if contract != CONTRACT or not valid_product_contract(contract):
        raise RuntimeError("table identifier contract is not the adopted product contract")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SCHEMA_FILE
        or adoption.get("source_sha256") != source_digests(root)[SCHEMA_FILE]
        or adoption.get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("table identifier adoption does not bind the exact source")
    verify_adoption_source(contract, root)
    for property_id in (PROPERTY_ID, MUTATION_ID):
        entry = REGISTRY.get(property_id)
        if entry is None:
            raise RuntimeError(f"missing property registry entry {property_id}")
    if not product_reportable(REGISTRY[PROPERTY_ID]):
        raise RuntimeError("table identifier property is not product-reportable")
    return source_digests(root)


def _run(source: Path, *, run_proof: bool = True) -> dict[str, object]:
    root = _prepare_source_root(str(source))
    digests = _verify_contract(root)
    pinned_pydantic = _locked_pydantic_version(root)
    if pinned_pydantic != "2.12.5" or pydantic.__version__ != pinned_pydantic:
        raise RuntimeError(
            f"Pydantic runtime {pydantic.__version__} differs from Tracecat lock {pinned_pydantic}"
        )
    path_shape = exact_table_path_shape(root)
    cases = _cases()
    mismatches: list[dict[str, object]] = []
    model_accepts = 0
    service_accepts = 0
    final_lf_model_accepts = False
    final_lf_service_accepts = False
    for index, value in enumerate(cases, 1):
        expected_model = _expected_schema_accept(value)
        expected_service = _expected_service_accept(value)
        for kind in ("column", "table"):
            actual_model = current_model_accepts(value, kind=kind)
            if actual_model:
                model_accepts += 1
            if actual_model != expected_model:
                mismatches.append(
                    {
                        "case": index,
                        "kind": kind,
                        "value": repr(value),
                        "expected_request_model": expected_model,
                        "actual_request_model": actual_model,
                    }
                )
        actual_service = current_service_accepts(value)
        if actual_service:
            service_accepts += 1
        if actual_service != expected_service:
            mismatches.append(
                {
                    "case": index,
                    "kind": "service",
                    "value": repr(value),
                    "expected_service": expected_service,
                    "actual_service": actual_service,
                }
            )
        if '"' in value and (expected_model or expected_service):
            mismatches.append(
                {"case": index, "value": repr(value), "reason": "quote-admitted"}
            )
    final_lf_model_accepts = current_model_accepts("safe\n", kind="column")
    final_lf_service_accepts = current_service_accepts("safe\n")
    if current_quote_identifier("safe") != '"safe"':
        mismatches.append({"reason": "quote_identifier formatting changed"})
    mutation_reproduced = table_identifier_quote_mutation_reproduces()
    if not mutation_reproduced:
        mismatches.append({"reason": "schema weakening mutation did not reproduce"})
    if mismatches:
        raise RuntimeError(json.dumps(mismatches[:20], ensure_ascii=True))
    if run_proof:
        _run_proof()
    report: dict[str, object] = {
        "schema_version": "1",
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_files": digests,
        "source_pattern": IDENTIFIER_PATTERN,
        "contract_sha256": contract_digest(CONTRACT),
        "family": FAMILY,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "gate_id": "tracecat-table-identifier-quote-exclusion",
        "product_engine": "Pydantic 2.12.5 name fields rebuilt from exact pinned AST, exact service validate_identifier, and exact quote_identifier",
        "differential_cases": len(cases),
        "model_observations": model_accepts,
        "service_observations": service_accepts,
        "mismatches": 0,
        "mutation_reproduced": mutation_reproduced,
        "mutation_name": MUTATION_NAME,
        "quote_identifier_example": current_quote_identifier("safe"),
        "route_and_sink_shape": path_shape,
        "schema_accepts_terminal_lf": final_lf_model_accepts,
        "service_accepts_terminal_lf": final_lf_service_accepts,
        "terminal_lf_note": "The request model regex accepts a final line feed due Python '$' semantics, but the exact service validate_identifier rejects it before DDL. This is not a sink acceptance or SQL-injection finding at this pin.",
        "limitations": "The contract covers newly submitted table and column names through the pinned create paths. It does not cover arbitrary internal callers, stored legacy names, SQL correctness beyond double-quote exclusion, authorization correctness, or deployed security impact.",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--skip-proof", action="store_true")
    args = parser.parse_args()
    source = _prepare_source_root(
        str(args.source_root) if args.source_root is not None else None
    )
    report = _run(source, run_proof=not args.skip_proof)
    rendered = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        atomic_write_text(args.output, rendered)
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
