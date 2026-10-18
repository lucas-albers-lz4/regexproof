#!/usr/bin/env python3
"""Prove and replay Tracecat's pinned nsjail environment-key separator gate."""

from __future__ import annotations

import argparse
import ast
import itertools
import json
import os
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest, verify_adoption_source  # noqa: E402
from regexproof.groundtruth.tracecat_sandbox_env_key_replay import (  # noqa: E402
    MUTATION_NAME,
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_PATTERN,
    SOURCE_SHA256,
    _accepts,
    _validator,
    equals_mutation_reproduces,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.harness.tracecat_sandbox_env_key import (  # noqa: E402
    CONTRACT,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-17-autonomous-tracecat-sandbox-env-equals"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "p6-wave" / "roster.json"
ALPHABET = "Aa_09=;\n\r\t\x00-éλ"


def _prepare_source_root(raw: str | None) -> Path:
    if raw:
        requested = Path(raw).expanduser().resolve()
        configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            raise RuntimeError("--source-root conflicts with TRACECAT_REPLAY_SOURCE")
        os.environ["TRACECAT_REPLAY_SOURCE"] = str(requested)
    return source_root()


def _method(tree: ast.Module, class_name: str, method_name: str) -> ast.FunctionDef | ast.AsyncFunctionDef:
    classes = [
        node for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    ]
    if len(classes) != 1:
        raise RuntimeError(f"expected one {class_name} class")
    methods = [
        node for node in classes[0].body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == method_name
    ]
    if len(methods) != 1:
        raise RuntimeError(f"expected one {class_name}.{method_name} method")
    return methods[0]


def _calls(node: ast.AST, name: str) -> list[ast.Call]:
    return [
        item for item in ast.walk(node)
        if isinstance(item, ast.Call)
        and isinstance(item.func, ast.Name)
        and item.func.id == name
    ]


def _calls_attr(node: ast.AST, name: str) -> list[ast.Call]:
    return [
        item for item in ast.walk(node)
        if isinstance(item, ast.Call)
        and isinstance(item.func, ast.Attribute)
        and item.func.attr == name
    ]


def _env_map_process_sink(method: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    calls = _calls_attr(method, "create_subprocess_exec")
    return any(
        any(
            keyword.arg == "env"
            and isinstance(keyword.value, ast.Name)
            and keyword.value.id == "env_map"
            for keyword in call.keywords
        )
        for call in calls
    )


def _validator_precedes_insertion(
    method: ast.FunctionDef | ast.AsyncFunctionDef,
) -> bool:
    validators = _calls(method, "_validate_env_key")
    insertions = [
        node for node in ast.walk(method)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and target.value.id == "env_map"
            and isinstance(target.slice, ast.Name)
            and target.slice.id == "key"
            for target in node.targets
        )
    ]
    return len(validators) == 1 and bool(insertions) and validators[0].lineno < insertions[0].lineno


def _verify_source_path(root: Path) -> dict[str, bool]:
    executor_tree = ast.parse(
        (root / SOURCE_FILE).read_text(encoding="utf-8"), filename=SOURCE_FILE
    )
    pattern_assignments = [
        node for node in executor_tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "_ENV_VAR_KEY_PATTERN"
            for target in node.targets
        )
    ]
    if len(pattern_assignments) != 1:
        raise RuntimeError("expected one pinned _ENV_VAR_KEY_PATTERN assignment")
    assignment = pattern_assignments[0]
    if (
        not isinstance(assignment.value, ast.Call)
        or not isinstance(assignment.value.func, ast.Attribute)
        or assignment.value.func.attr != "compile"
        or not assignment.value.args
        or not isinstance(assignment.value.args[0], ast.Constant)
        or assignment.value.args[0].value != SOURCE_PATTERN
    ):
        raise RuntimeError("pinned sandbox regex differs from the adopted pattern")

    build_env = _method(executor_tree, "NsjailExecutor", "_build_env_map")
    build_action_env = _method(executor_tree, "NsjailExecutor", "_build_action_env_map")
    execute = _method(executor_tree, "NsjailExecutor", "execute")
    execute_action = _method(executor_tree, "NsjailExecutor", "execute_action")
    if len(_calls(build_env, "_validate_env_key")) != 1:
        raise RuntimeError("run_python env-map builder no longer validates each key")
    if len(_calls(build_action_env, "_validate_env_key")) != 1:
        raise RuntimeError("action env-map builder no longer validates each key")
    if not _validator_precedes_insertion(build_env):
        raise RuntimeError("run_python env validation no longer precedes env-map insertion")
    if not _validator_precedes_insertion(build_action_env):
        raise RuntimeError("action env validation no longer precedes env-map insertion")
    if not _env_map_process_sink(execute) or not _env_map_process_sink(execute_action):
        raise RuntimeError("nsjail subprocess sinks changed; review this contract")
    if not _calls_attr(execute, "_build_env_map") or not _calls_attr(execute_action, "_build_action_env_map"):
        raise RuntimeError("nsjail execution no longer uses the validated env builders")
    for method in (execute, execute_action):
        if not any(
            isinstance(node, ast.Constant) and node.value == "--env"
            for node in ast.walk(method)
        ):
            raise RuntimeError("nsjail env-map no longer populates --env argv options")

    base_file = "tracecat/executor/backends/base.py"
    base_tree = ast.parse((root / base_file).read_text(encoding="utf-8"), filename=base_file)
    run_python = next(
        node for node in base_tree.body
        if isinstance(node, ast.ClassDef) and node.name == "ExecutorBackend"
    )
    run_python_method = next(
        node for node in run_python.body
        if isinstance(node, ast.AsyncFunctionDef) and node.name == "_execute_run_python"
    )
    uses_user_env = any(
        isinstance(node, ast.keyword)
        and node.arg == "user_env_vars"
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Attribute)
        and node.value.func.attr == "get"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Constant)
        and node.value.args[0].value == "env_vars"
        for node in ast.walk(run_python_method)
    )
    if not uses_user_env or not _calls_attr(run_python_method, "run_python"):
        raise RuntimeError("run_python workflow env_vars path changed; review the contract")

    return {
        "run_python_user_env_source_verified": True,
        "run_python_nsjail_builder_validator_verified": True,
        "action_nsjail_builder_validator_verified": True,
        "both_subprocess_sinks_verified": True,
    }


def _model_accepts(key: str) -> bool:
    candidates = [key]
    if key.endswith("\n"):
        candidates.append(key[:-1])
    for candidate in candidates:
        if not candidate:
            continue
        if candidate[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_":
            continue
        if all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789" for char in candidate[1:]):
            return True
    return False


def _cases() -> list[str]:
    cases = [chr(codepoint) for codepoint in range(128)]
    for width in (1, 2, 3):
        cases.extend("".join(chars) for chars in itertools.product(ALPHABET, repeat=width))
    cases.extend(["A", "_0", "TRACE=TOKEN", "A\n", "A\nB", "A\n\n", "é", "Aé", "A" * 2048])
    rng = random.Random(20261017)
    random_alphabet = ALPHABET + "🛰中٣" + "A" * 8
    cases.extend(
        "".join(rng.choice(random_alphabet) for _ in range(rng.randint(1, 80)))
        for _ in range(1200)
    )
    return list(dict.fromkeys(cases))


def _verify_contract_and_roster() -> str:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract) or contract != CONTRACT:
        raise RuntimeError("sandbox env-key contract is not a valid adopted product contract")
    verify_adoption_source(contract, source_root())
    digest = contract_digest(contract)
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    rows = [
        row for row in roster.get("identities", [])
        if row.get("question_id") == PROPERTY_ID and row.get("site") == contract.get("site")
    ]
    if len(rows) != 1 or rows[0].get("contract_sha256") != digest:
        raise RuntimeError("P6 roster does not bind this exact source-backed contract")
    return str(digest)


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


def _run(source: Path, *, skip_proof: bool) -> dict:
    root = source.resolve()
    os.environ["TRACECAT_REPLAY_SOURCE"] = str(root)
    if root != source_root():
        raise RuntimeError("requested source differs from the verified Tracecat checkout")
    contract_sha = _verify_contract_and_roster()
    source_path = _verify_source_path(root)
    validator = _validator(root)
    mismatches = []
    accepted_count = 0
    cases = _cases()
    for index, key in enumerate(cases):
        actual = _accepts(validator, key)
        expected = _model_accepts(key)
        accepted_count += actual
        if actual != expected:
            mismatches.append(
                {"index": index, "key": repr(key), "expected": expected, "actual": actual}
            )
            if len(mismatches) == 5:
                break
    if mismatches:
        raise RuntimeError(f"exact validator/model mismatches: {mismatches!r}")

    witness = {"key": MUTATION_NAME}
    if _accepts(validator, MUTATION_NAME):
        raise RuntimeError("exact source validator admitted a key containing '='")
    if not equals_mutation_reproduces(witness):
        raise RuntimeError("the registered equals mutation did not replay against source")

    try:
        subprocess.run(
            [sys.executable, "-c", "pass"],
            env={MUTATION_NAME: "synthetic"},
            capture_output=True,
            timeout=10,
            check=False,
        )
    except ValueError:
        subprocess_rejects_equals = True
    else:
        raise RuntimeError("Python subprocess unexpectedly accepted '=' in an env key")

    if not skip_proof:
        _run_proof()
    return {
        "schema_version": "1",
        "gate_id": "tracecat-sandbox-env-key-equals-exclusion",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_sha256": SOURCE_SHA256,
        "contract_sha256": contract_sha,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "source_path": source_path,
        "differential_cases": len(cases),
        "accepted_cases": accepted_count,
        "mismatches": 0,
        "equal_sign_mutation_reproduced": True,
        "python_subprocess_rejects_equal_sign_key": subprocess_rejects_equals,
        "terminal_lf_accepted": _accepts(validator, "TRACE_TOKEN\n"),
        "proof_ran": not skip_proof,
        "limitations": "The gate covers the pinned nsjail env-map and subprocess paths. It proves only that accepted names exclude '='; Python '$' accepts one final LF, which is explicitly outside full POSIX name conformance. It does not cover the unsafe PID fallback or claim a current security impact.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skip-proof", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = _run(args.source_root, skip_proof=args.skip_proof)
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"tracecat-sandbox-env-key-regression-gate: error: {exc}", file=sys.stderr)
        return 1
    print(
        f"Tracecat sandbox env-key gate passed: {report['differential_cases']} "
        "cases, zero mismatches, equals mutation reproduced"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
