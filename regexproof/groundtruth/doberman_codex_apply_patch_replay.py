"""Exact-pin replay of Doberman's Codex apply_patch path extraction helper."""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

PIN = "53ae43c5298a2426c6696147fdd75e2a4aef10e2"
REPOSITORY = "https://github.com/fu351/Doberman-Core"
REPO_ID = "fu351/Doberman-Core"
SOURCE_FILE = "src/doberman/hosthooks/codex.py"
SOURCE_SHA256 = "0144953c99a6620cbe9128ce7bc7ad6f6e9ea1a64311348db1f70ec0d14f42f3"
FILE_PATTERN = r"^\s*\*\*\* (?:Add|Update|Delete) File: (.+)$"
MOVE_PATTERN = r"^\s*\*\*\* Move to: (.+)$"
WEAKENED_FILE_PATTERN = r"^\s*\*\*\* (?:Add|Update) File: (.+)$"
QUESTION_IDS = (
    "DB-codex-apply-patch-file-target-path",
    "DB-codex-apply-patch-move-target-path",
)
DEFAULT_SOURCE_ROOT = (
    Path("/tmp/regexproof-pinned-sources") / f"Doberman-Core-{PIN}"
)
SLICE = (
    Path(__file__).resolve().parents[2]
    / "properties/calibration/2026-10-15-p2-doberman-source-review"
)
CONTRACTS_PATH = SLICE / "contracts.json"


def source_root(root: Path | None = None) -> Path:
    configured = os.environ.get("REGEXPROOF_DOBERMAN_CODEX_CHECKOUT")
    return root.resolve() if root is not None else (
        Path(configured).resolve() if configured else DEFAULT_SOURCE_ROOT
    )


def verify_source(root: Path | None = None) -> tuple[Path, bytes]:
    checkout = source_root(root)
    if checkout.is_symlink() or not checkout.is_dir():
        raise RuntimeError(f"exact pinned Doberman checkout is unavailable: {checkout}")
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=checkout, check=True,
        capture_output=True, text=True, timeout=10,
    ).stdout.strip()
    if head != PIN:
        raise RuntimeError(f"Doberman source pin mismatch: expected {PIN}, found {head}")
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=checkout, check=True, capture_output=True, text=True, timeout=10,
    ).stdout
    if status:
        raise RuntimeError("exact pinned Doberman checkout is not clean")
    source_path = checkout / SOURCE_FILE
    if source_path.is_symlink() or not source_path.is_file():
        raise RuntimeError(f"pinned Doberman source is missing or a symlink: {SOURCE_FILE}")
    committed = subprocess.run(
        ["git", "show", f"{PIN}:{SOURCE_FILE}"], cwd=checkout,
        check=True, capture_output=True, timeout=10,
    ).stdout
    if source_path.read_bytes() != committed:
        raise RuntimeError("Doberman source working bytes differ from pinned bytes")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Doberman source hash mismatch: {digest}")
    return checkout, committed


def load_exact_helpers(source: bytes) -> dict[str, Any]:
    """Execute only the two pinned regex assignments and exact adapter helpers."""
    tree = ast.parse(source.decode("utf-8"), filename=SOURCE_FILE)
    selected: list[ast.stmt] = []
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            target_names = {
                target.id for target in node.targets if isinstance(target, ast.Name)
            }
            if target_names & {"_APPLY_PATCH_FILE_RE", "_APPLY_PATCH_MOVE_RE"}:
                selected.append(node)
                names.update(target_names)
        elif isinstance(node, ast.FunctionDef) and node.name in {
            "_apply_patch_paths", "to_normalize_input",
        }:
            selected.append(node)
            names.add(node.name)
    required = {
        "_APPLY_PATCH_FILE_RE", "_APPLY_PATCH_MOVE_RE",
        "_apply_patch_paths", "to_normalize_input",
    }
    if names != required:
        raise RuntimeError(f"pinned Codex helper AST is incomplete: {sorted(names)}")
    namespace: dict[str, Any] = {"re": re, "Any": Any}
    exec(compile(ast.Module(body=selected, type_ignores=[]), SOURCE_FILE, "exec"), namespace)
    if namespace["_APPLY_PATCH_FILE_RE"].pattern != FILE_PATTERN:
        raise RuntimeError("pinned Add/Update/Delete regex differs from the reviewed pattern")
    if namespace["_APPLY_PATCH_MOVE_RE"].pattern != MOVE_PATTERN:
        raise RuntimeError("pinned Move-to regex differs from the reviewed pattern")
    if namespace["_APPLY_PATCH_FILE_RE"].flags & re.MULTILINE == 0:
        raise RuntimeError("pinned file regex lost MULTILINE semantics")
    if namespace["_APPLY_PATCH_MOVE_RE"].flags & re.MULTILINE == 0:
        raise RuntimeError("pinned Move-to regex lost MULTILINE semantics")
    return namespace


def _run_helper(namespace: dict[str, Any], patch: object) -> list[str]:
    return namespace["_apply_patch_paths"](patch)


def mutation_reproduces(witness: dict[str, Any]) -> bool:
    line = witness.get("line")
    if line != "*** Delete File: .env":
        return False
    _checkout, source = verify_source()
    namespace = load_exact_helpers(source)
    original = _run_helper(namespace, line)
    namespace["_APPLY_PATCH_FILE_RE"] = re.compile(
        WEAKENED_FILE_PATTERN, re.MULTILINE
    )
    weakened = _run_helper(namespace, line)
    return original == [".env"] and weakened == []


def _case(namespace: dict[str, Any], directive: str, expected: list[str]) -> None:
    patch = f"*** Begin Patch\n{directive}\n*** End Patch"
    paths = _run_helper(namespace, patch)
    if paths != expected:
        raise RuntimeError(f"path helper mismatch for {directive!r}: {paths!r}")
    name, args = namespace["to_normalize_input"](
        "apply_patch", {"command": patch}
    )
    if name != "file_write" or args.get("raw_paths") != expected:
        raise RuntimeError(f"adapter did not surface all targets: {name!r} {args!r}")
    expected_path: str | list[str] = expected[0] if len(expected) == 1 else expected
    if args.get("path") != expected_path:
        raise RuntimeError(f"adapter path field mismatch: {args.get('path')!r}")


def run_regression_gate(root: Path | None = None) -> dict[str, Any]:
    checkout, source = verify_source(root)
    namespace = load_exact_helpers(source)
    file_directives = (
        ("Add", "Add File:"),
        ("Update", "Update File:"),
        ("Delete", "Delete File:"),
    )
    paths = (
        ".env", "a.txt", "dir/with spaces/file.py", ".secrets/token",
        "../outside", "C:/Users/alice/.env", "x", " padded name ",
    )
    indents = [
        "".join(chars)
        for width in range(4)
        for chars in itertools.product(" \t", repeat=width)
    ]
    case_counts: dict[str, int] = {}
    question_specs = (
        (QUESTION_IDS[0], tuple(prefix for _kind, prefix in file_directives)),
        (QUESTION_IDS[1], ("Move to:",)),
    )
    for question_id, directive_prefixes in question_specs:
        count = 0
        for directive_prefix in directive_prefixes:
            for indent in indents:
                for path in paths:
                    directive = f"{indent}*** {directive_prefix} {path}"
                    _case(namespace, directive, [path.strip()])
                    count += 1
        # The contract domain excludes CR/LF, but the pinned comment promises
        # CRLF tolerance. Keep these compatibility cases separate from the
        # contract-domain matrix in the report.
        for directive_prefix in directive_prefixes:
            for path in paths:
                directive = f"*** {directive_prefix} {path}\r"
                _case(namespace, directive, [path.strip()])
                count += 1
        case_counts[question_id] = count

    multi_patch = (
        "*** Begin Patch\n"
        "*** Add File: notes.txt\n+ok\n"
        "*** Delete File: .env\n"
        "*** Move to: moved/.env\n"
        "*** End Patch"
    )
    multi_expected = ["notes.txt", ".env", "moved/.env"]
    if _run_helper(namespace, multi_patch) != multi_expected:
        raise RuntimeError("mixed multi-directive extraction lost a target")
    name, args = namespace["to_normalize_input"](
        "apply_patch", {"command": multi_patch}
    )
    if name != "file_write" or args.get("raw_paths") != multi_expected:
        raise RuntimeError("mixed multi-directive target mapping lost a target")
    if args.get("path") != multi_expected:
        raise RuntimeError("multi-directive path field does not contain all targets")
    for question_id in QUESTION_IDS:
        case_counts[question_id] += 1

    if _run_helper(namespace, None) != [] or _run_helper(namespace, "") != []:
        raise RuntimeError("non-string and empty patch inputs must return no paths")

    namespace["_APPLY_PATCH_FILE_RE"] = re.compile(
        WEAKENED_FILE_PATTERN, re.MULTILINE
    )
    if _run_helper(namespace, "*** Delete File: .env"):
        raise RuntimeError("weakened Delete alternative unexpectedly extracted the target")
    # Re-read the normal source and make sure the original behavior admits the
    # mutation witness before the report claims the guard is sensitive.
    original_namespace = load_exact_helpers(source)
    if _run_helper(original_namespace, "*** Delete File: .env") != [".env"]:
        raise RuntimeError("original pinned helper did not extract the mutation witness")

    contract_rows = json.loads(CONTRACTS_PATH.read_text(encoding="utf-8"))
    by_site = {item.get("site"): item for item in contract_rows}
    contract_hashes = {}
    for question_id, line, symbol in (
        (QUESTION_IDS[0], 69, "_APPLY_PATCH_FILE_RE"),
        (QUESTION_IDS[1], 70, "_APPLY_PATCH_MOVE_RE"),
    ):
        site = f"{REPO_ID}@{PIN}:{SOURCE_FILE}:{line}:{symbol}"
        contract = by_site.get(site)
        if not contract:
            raise RuntimeError(f"{question_id} has no source-bound contract")
        from regexproof.contract_adoption import contract_digest, contract_is_adopted

        if not contract_is_adopted(contract):
            raise RuntimeError(f"{question_id} contract is not validly adopted")
        adoption = contract["adoption"]
        if adoption.get("source_sha256") != SOURCE_SHA256:
            raise RuntimeError(f"{question_id} source hash differs from the contract")
        contract_hashes[question_id] = contract_digest(contract)

    return {
        "schema_version": "1",
        "gate_id": "doberman-codex-apply-patch-target-extraction",
        "status": "reproduced",
        "repository": REPOSITORY,
        "question_ids": list(QUESTION_IDS),
        "product_engine_replay_question_ids": list(QUESTION_IDS),
        "differential_case_counts": case_counts,
        "differential_cases": sum(case_counts.values()),
        "contract_domain_case_counts": {
            QUESTION_IDS[0]: 45,
            QUESTION_IDS[1]: 15,
        },
        "representative_long_path_case_counts": {
            QUESTION_IDS[0]: 315,
            QUESTION_IDS[1]: 105,
        },
        "crlf_compatibility_case_counts": {
            QUESTION_IDS[0]: 24,
            QUESTION_IDS[1]: 8,
        },
        "multi_directive_cases_per_question": 1,
        "mutation_guard_passed": True,
        "mutation_witness": "*** Delete File: .env",
        "source": {
            "repository_url": REPOSITORY,
            "pin": PIN,
            "file": SOURCE_FILE,
            "sha256": SOURCE_SHA256,
            "checkout": str(checkout),
        },
        "contract_sha256s": contract_hashes,
    }


__all__ = [
    "FILE_PATTERN", "MOVE_PATTERN", "PIN", "QUESTION_IDS", "REPOSITORY",
    "WEAKENED_FILE_PATTERN", "mutation_reproduces", "run_regression_gate",
    "source_root", "verify_source",
]
