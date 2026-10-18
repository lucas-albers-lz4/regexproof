"""Pinned Tracecat sandbox environment-key validator replay helpers."""

from __future__ import annotations

import ast
import copy
import hashlib
import os
import re
import subprocess
from pathlib import Path
from typing import Callable

from regexproof.groundtruth.tracecat_replay import (
    source_root as _tracecat_source_root,
)

PIN = "c84d52528a489821f355fc63976fbc7783ae0ad5"
REPOSITORY = "https://github.com/TracecatHQ/tracecat"
SOURCE_FILE = "tracecat/sandbox/executor.py"
SOURCE_SHA256 = "ddc89fbeeecffff54574283bf4bea064a0af0579fcbb4ba2f3fcd0d8e6b1d6e2"
SOURCE_PATTERN = r"^[A-Za-z_][A-Za-z0-9_]*$"
WEAKENED_PATTERN = r"^[A-Za-z_][A-Za-z0-9_=]*$"
MUTATION_NAME = "TRACE=TOKEN"


class _ReplaySandboxValidationError(Exception):
    """Stub for the source module's imported domain exception."""


def source_root() -> Path:
    """Return the exact clean Tracecat checkout and verify the target file."""
    root = _tracecat_source_root()
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("pinned Tracecat sandbox executor is missing or a symlink")
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{SOURCE_FILE}"],
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout
    actual = source.read_bytes()
    if actual != committed:
        raise RuntimeError("Tracecat sandbox executor differs from its pinned commit")
    digest = hashlib.sha256(actual).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Tracecat sandbox executor digest differs: {digest}")
    return root


def _validator(root: Path, *, pattern_override: str | None = None) -> Callable[[str], None]:
    """Compile the exact pinned pattern assignment and validator function."""
    source = root / SOURCE_FILE
    tree = ast.parse(source.read_text(encoding="utf-8"), filename=SOURCE_FILE)
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "_ENV_VAR_KEY_PATTERN"
            for target in node.targets
        )
    ]
    validators = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "_validate_env_key"
    ]
    if len(assignments) != 1 or len(validators) != 1:
        raise RuntimeError("expected one pinned env-key pattern and validator")
    assignment = copy.deepcopy(assignments[0])
    value = assignment.value
    if (
        not isinstance(value, ast.Call)
        or not isinstance(value.func, ast.Attribute)
        or not isinstance(value.func.value, ast.Name)
        or value.func.value.id != "re"
        or value.func.attr != "compile"
        or not value.args
        or not isinstance(value.args[0], ast.Constant)
        or value.args[0].value != SOURCE_PATTERN
    ):
        raise RuntimeError("pinned env-key declaration differs from the reviewed regex")
    if pattern_override is not None:
        value.args[0] = ast.Constant(value=pattern_override)
    isolated = ast.Module(
        body=[assignment, copy.deepcopy(validators[0])],
        type_ignores=[],
    )
    ast.fix_missing_locations(isolated)
    namespace = {
        "re": re,
        "SandboxValidationError": _ReplaySandboxValidationError,
    }
    exec(compile(isolated, SOURCE_FILE, "exec"), namespace)
    return namespace["_validate_env_key"]


def _accepts(validator: Callable[[str], None], key: str) -> bool:
    try:
        validator(key)
    except _ReplaySandboxValidationError:
        return False
    return True


def exact_validator_accepts(key: str) -> bool:
    return _accepts(_validator(source_root()), key)


def equals_mutation_reproduces(witness: dict[str, str]) -> bool:
    """Replay that weakening the exact source tail admits a name with '='."""
    key = witness.get("key", witness.get("mutated_sandbox_env_key"))
    if not isinstance(key, str) or "=" not in key:
        return False
    root = source_root()
    strict = _validator(root)
    weakened = _validator(root, pattern_override=WEAKENED_PATTERN)
    return not _accepts(strict, key) and _accepts(weakened, key)


__all__ = [
    "MUTATION_NAME",
    "PIN",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "SOURCE_SHA256",
    "WEAKENED_PATTERN",
    "equals_mutation_reproduces",
    "exact_validator_accepts",
    "source_root",
]
