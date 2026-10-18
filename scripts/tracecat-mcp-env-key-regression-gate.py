#!/usr/bin/env python3
"""Replay Tracecat's exact MCP stdio env-key validator and anchor mutation."""

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
from regexproof.groundtruth.tracecat_mcp_env_key_replay import (  # noqa: E402
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_PATTERN,
    SOURCE_SHA256,
    accepted_terminal_lf_reproduces,
    source_root,
    subprocess_receives_environment_key,
    terminal_lf_mutation_reproduces,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.harness.tracecat_mcp_env_key import (  # noqa: E402
    CONTRACT,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-tracecat-mcp-env-key"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "p6-wave" / "roster.json"
PROTECTED = frozenset(
    {
        "PATH",
        "LD_PRELOAD",
        "LD_LIBRARY_PATH",
        "PYTHONPATH",
        "NODE_PATH",
        "HOME",
        "USER",
        "SHELL",
    }
)
WITNESS = "TRACE_TOKEN\n"
ALPHABET = "Aa_09\n=;\x00"


def _load_module(root: Path):
    source = root / SOURCE_FILE
    spec = importlib.util.spec_from_file_location("tracecat_mcp_validation_gate", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load exact pinned Tracecat MCP validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _matches_source_model(key: str) -> bool:
    """Independent language model of Python `^...$` without MULTILINE."""
    if len(key) > 64 or key in PROTECTED:
        return False
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key, flags=re.ASCII):
        return True
    return key.endswith("\n") and bool(
        re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key[:-1], flags=re.ASCII)
    )


def _is_declared_name(key: str) -> bool:
    if len(key) < 1 or len(key) > 64 or key in PROTECTED:
        return False
    return re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key, flags=re.ASCII) is not None


def _cases() -> list[str]:
    values = [chr(value) for value in range(1, 128)]
    for length in range(1, 4):
        values.extend("".join(chars) for chars in itertools.product(ALPHABET, repeat=length))
    values.extend(
        [
            "TRACE_TOKEN",
            WITNESS,
            "_\n",
            "9TOKEN\n",
            "A\nB",
            "A" * 64,
            "A" * 63 + "\n",
            "A" * 64 + "\n",
            "PATH",
            "PATH\n",
        ]
    )
    rng = random.Random(20261015)
    values.extend(
        "".join(rng.choice(ALPHABET) for _ in range(rng.randint(1, 80)))
        for _ in range(512)
    )
    return list(dict.fromkeys(values))


def _verify_source_pattern(root: Path) -> None:
    tree = ast.parse(
        (root / SOURCE_FILE).read_text(encoding="utf-8"), filename=SOURCE_FILE
    )
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
            f"expected one pinned validator re.match call, found {len(pattern_calls)}"
        )


def _verify_contract_roster() -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract) or contract != CONTRACT:
        raise RuntimeError("Tracecat MCP env-key contract is not a valid adopted contract")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git")
        != REPOSITORY.removesuffix(".git")
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("contract adoption differs from the pinned validator source")
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
        raise RuntimeError("P6 roster does not bind the adopted contract to frozen 20-r2")
    return contract


def _run(source: Path) -> dict:
    root = source.resolve()
    os.environ["TRACECAT_REPLAY_SOURCE"] = str(root)
    if root != source_root():
        raise RuntimeError("requested gate source differs from the verified Tracecat checkout")
    _verify_source_pattern(root)
    _verify_contract_roster()
    module = _load_module(root)

    cases = _cases()
    mismatches = []
    actual_accepted = 0
    for index, key in enumerate(cases):
        try:
            module.validate_mcp_env_key(key)
            accepted = True
        except module.MCPValidationError:
            accepted = False
        expected = _matches_source_model(key)
        if accepted:
            actual_accepted += 1
        if accepted != expected:
            mismatches.append(
                {"index": index, "key": repr(key), "expected": expected, "actual": accepted}
            )
            if len(mismatches) == 5:
                break
    if mismatches:
        raise RuntimeError(f"pinned MCP validator/model mismatches: {mismatches!r}")

    try:
        module.validate_mcp_env_key(WITNESS)
        witness_accepted = True
    except module.MCPValidationError:
        witness_accepted = False
    if not witness_accepted or _is_declared_name(WITNESS):
        raise RuntimeError("terminal-LF counterexample did not reproduce at the exact source")
    try:
        module.validate_mcp_command_config(command="npx", env={WITNESS: "synthetic"})
    except module.MCPValidationError as exc:
        raise RuntimeError("complete stdio config validator rejected the modeled witness") from exc
    child_received = subprocess_receives_environment_key(WITNESS)
    if not child_received:
        raise RuntimeError("POSIX child process did not receive the accepted newline key")

    witness_doc = {"key": WITNESS}
    if not accepted_terminal_lf_reproduces(witness_doc):
        raise RuntimeError("registered counterexample ground-truth callback did not reproduce")
    if not terminal_lf_mutation_reproduces(witness_doc):
        raise RuntimeError("strict-anchor mutation guard did not distinguish the terminal LF")

    return {
        "schema_version": "1",
        "gate_id": "tracecat-mcp-env-key-declared-grammar",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": hashlib.sha256((root / SOURCE_FILE).read_bytes()).hexdigest(),
        "source_pattern": SOURCE_PATTERN,
        "product_engine": "CPython re through the exact pinned validate_mcp_env_key and validate_mcp_command_config functions",
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "witness": WITNESS,
        "witness_accepted_by_source": witness_accepted,
        "witness_matches_declared_name": _is_declared_name(WITNESS),
        "complete_config_validation_accepts": True,
        "posix_child_receives_environment_key": child_received,
        "mutation_strict_anchor_rejects": True,
        "mutation_reintroducing_dollar_accepts": True,
        "differential_cases": len(cases),
        "differential_case_classes": {
            "non_nul_ascii_single_characters": 127,
            "exhaustive_strings_over_Aa_09_lf_equals_semicolon_nul": sum(
                len(ALPHABET) ** length for length in range(1, 4)
            ),
            "explicit_boundary_and_protected_name_cases": 10,
            "seeded_mixed_ascii_strings": 512,
        },
        "mismatches": len(mismatches),
        "actual_accepted_cases": actual_accepted,
        "scope": (
            "The exact source validator accepts a terminal-LF key that is outside Tracecat's declared ASCII name grammar. "
            "This confirms a configuration-validation gap; it does not establish command injection, privilege escalation, "
            "or a security-impacting behavior in any launched MCP server."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = _run(args.source_root)
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(
            f"Tracecat MCP env-key gate: {report['differential_cases']} cases, "
            "zero model mismatches; terminal LF accepted and reproduced"
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Tracecat MCP env-key gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
