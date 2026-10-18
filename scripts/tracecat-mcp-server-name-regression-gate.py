#!/usr/bin/env python3
"""Replay Tracecat's exact MCP server-name separator invariant and mutation."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
import os
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.tracecat_server_name_replay import (  # noqa: E402
    PIN,
    SOURCE_FILE,
    SOURCE_PATTERN,
    server_name_separator_exclusion_reproduces,
    server_name_slash_mutation_reproduces,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.harness.tracecat_server_name import (  # noqa: E402
    CONTRACT,
    FAMILY,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

REPOSITORY = "https://github.com/TracecatHQ/tracecat"
SLICE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-tracecat-server-name"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "p6-wave" / "roster.json"
SOURCE_SHA256 = "41cf730ba1cb592cae684811bbb4d510961a0a441c156313a804b2593085f895"
PROTECTED = frozenset({"/", "\\"})
ALPHABET = "Aa0_-/\\\n\x00"


def _load_module(root: Path):
    source = root / SOURCE_FILE
    spec = importlib.util.spec_from_file_location("tracecat_mcp_server_name_gate", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load exact pinned Tracecat MCP validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _accepted_by_source(module, value: str) -> bool:
    try:
        module.validate_mcp_server_name(value)
    except module.MCPValidationError:
        return False
    return True


def _accepted_by_config(module, value: str) -> bool:
    try:
        module.validate_mcp_command_config(command="npx", name=value)
    except module.MCPValidationError:
        return False
    return True


def _model_accepts(value: str) -> bool:
    if not isinstance(value, str) or not value or len(value) > 64:
        return False
    if re.fullmatch(r"[A-Za-z0-9_-]+", value, flags=re.ASCII):
        return True
    return value.endswith("\n") and bool(
        re.fullmatch(r"[A-Za-z0-9_-]+", value[:-1], flags=re.ASCII)
    )


def _cases() -> list[str]:
    values = [chr(codepoint) for codepoint in range(128)]
    values.extend(
        "".join(chars)
        for chars in itertools.product(ALPHABET, repeat=2)
    )
    values.extend(
        [
            "tracecat",
            "safe-server_1",
            "/",
            "\\",
            "a/b",
            "a\\b",
            "A\n",
            "A\nB",
            "A" * 64,
            "A" * 63 + "\n",
            "A" * 64 + "\n",
            "A" * 65,
        ]
    )
    rng = random.Random(20261016)
    values.extend(
        "".join(rng.choice(ALPHABET) for _ in range(rng.randint(1, 80)))
        for _ in range(512)
    )
    return list(dict.fromkeys(values))


def _verify_source_pattern(root: Path) -> None:
    tree = ast.parse((root / SOURCE_FILE).read_text(encoding="utf-8"), filename=SOURCE_FILE)
    pattern_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "re"
        and node.func.attr == "match"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == SOURCE_PATTERN
    ]
    if len(pattern_calls) != 1:
        raise RuntimeError(
            f"expected one pinned server-name validator pattern, found {len(pattern_calls)}"
        )


def _verify_contract_roster() -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract) or contract != CONTRACT:
        raise RuntimeError("Tracecat MCP server-name contract is not a valid adopted contract")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("contract adoption differs from the pinned server-name source")
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    identities = [
        row
        for row in roster.get("identities", [])
        if row.get("site") == contract.get("site")
        and row.get("question_id") == PROPERTY_ID
    ]
    if (
        len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
        or roster.get("cohort_id") != "2026-09-12-calibration-20-r2"
    ):
        raise RuntimeError("P6 roster does not bind the adopted server-name contract")
    return contract


def _run(source: Path) -> dict:
    root = source.resolve()
    os.environ["TRACECAT_REPLAY_SOURCE"] = str(root)
    if root != source_root():
        raise RuntimeError("requested gate source differs from the verified Tracecat checkout")
    if hashlib.sha256((root / SOURCE_FILE).read_bytes()).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("Tracecat MCP validator source hash differs from the frozen pin")
    _verify_source_pattern(root)
    _verify_contract_roster()
    module = _load_module(root)

    cases = _cases()
    mismatches = []
    accepted_count = 0
    for index, value in enumerate(cases):
        actual = _accepted_by_source(module, value)
        config_actual = _accepted_by_config(module, value)
        expected = _model_accepts(value)
        if actual:
            accepted_count += 1
        if actual != config_actual or actual != expected:
            mismatches.append(
                {
                    "index": index,
                    "value": repr(value),
                    "source_accepts": actual,
                    "config_accepts": config_actual,
                    "model_accepts": expected,
                }
            )
            if len(mismatches) == 5:
                break
        if actual and any(separator in value for separator in PROTECTED):
            raise RuntimeError(f"pinned validator accepted path separator in {value!r}")
    if mismatches:
        raise RuntimeError(f"pinned MCP server-name validator/model mismatches: {mismatches!r}")

    witness_doc = {"name_char": "/"}
    if not server_name_separator_exclusion_reproduces({"name_char": "\\"}):
        raise RuntimeError("exact validator did not reject the backslash separator")
    if not server_name_slash_mutation_reproduces(witness_doc):
        raise RuntimeError("source-weakened slash mutation did not reproduce")

    return {
        "schema_version": "1",
        "gate_id": "tracecat-mcp-server-name-path-separator-exclusion",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": hashlib.sha256((root / SOURCE_FILE).read_bytes()).hexdigest(),
        "source_pattern": SOURCE_PATTERN,
        "product_engine": "CPython re through the exact pinned validate_mcp_server_name and validate_mcp_command_config functions",
        "property_id": PROPERTY_ID,
        "family": FAMILY,
        "mutation_id": MUTATION_ID,
        "guarantee": "accepted server-name strings contain neither slash nor backslash",
        "source_rejects_slash": not _accepted_by_source(module, "/"),
        "source_rejects_backslash": not _accepted_by_source(module, "\\"),
        "complete_config_rejects_slash": not _accepted_by_config(module, "/"),
        "mutation_accepts_slash": True,
        "differential_cases": len(cases),
        "mismatches": 0,
        "actual_accepted_cases": accepted_count,
        "impact_scope": "The gate checks a declared validator invariant only; it does not claim path traversal, authorization bypass, or security impact.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = _run(args.source_root)
        if args.output:
            atomic_write_text(args.output, json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True))
    except Exception as exc:
        print(f"tracecat-mcp-server-name-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
