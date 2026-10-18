"""Exact-pin replay for Tracecat workspace-sync path segments."""

from __future__ import annotations

import ast
import copy
import hashlib
import subprocess
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_replay import PIN, source_root

SOURCE_FILE = "tracecat/workspace_sync/adapters/base.py"
SOURCE_SHA256 = "fee3084582517c417c3b8dab6f372b71e423f3c1b413cdec8dbb58663a99cce6"
SOURCE_PATTERN = r"[^A-Za-z0-9_.-]+"
WEAKENED_PATTERN = r"[^A-Za-z0-9_.:-]+"
SAFE_CHARS = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
)


def _source_bytes() -> tuple[Path, bytes]:
    root = source_root()
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"missing or symlinked pinned workspace-sync adapter: {source}")
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{SOURCE_FILE}"],
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout
    actual = source.read_bytes()
    if actual != committed:
        raise RuntimeError("workspace-sync adapter bytes differ from the pinned Git blob")
    digest = hashlib.sha256(actual).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"workspace-sync adapter digest {digest} differs from contract")
    return source, actual


def _helper_module(*, weaken: bool = False) -> ModuleType:
    source_path, source_bytes = _source_bytes()
    tree = ast.parse(source_bytes, filename=SOURCE_FILE)
    function = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "path_segment"
        ),
        None,
    )
    if function is None:
        raise RuntimeError("pinned source no longer contains path_segment")

    function = copy.deepcopy(function)
    pattern_calls = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "re"
        and node.func.attr == "sub"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == SOURCE_PATTERN
    ]
    if len(pattern_calls) != 1:
        raise RuntimeError(
            f"expected one exact path_segment regex substitution, found {len(pattern_calls)}"
        )
    if weaken:
        pattern_calls[0].args[0].value = WEAKENED_PATTERN

    module_ast = ast.Module(
        body=[ast.Import(names=[ast.alias(name="re")]), function],
        type_ignores=[],
    )
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_workspace_path_{PIN}"}
    exec(compile(module_ast, str(source_path), "exec"), namespace)
    module = ModuleType(str(namespace["__name__"]))
    module.__dict__.update(namespace)
    return module


def source_path_segment(value: str, fallback: str = "resource") -> str:
    """Run the exact pinned path_segment helper."""
    return _helper_module().path_segment(value, fallback=fallback)


def weakened_path_segment_preserves_colon(value: str) -> bool:
    """Mutate only the regex class and confirm colon reaches the result."""
    if value != ":":
        return False
    original = _helper_module().path_segment(value)
    mutated = _helper_module(weaken=True).path_segment(value)
    return original == "resource" and mutated == ":"


__all__ = [
    "PIN",
    "SAFE_CHARS",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "SOURCE_SHA256",
    "WEAKENED_PATTERN",
    "source_path_segment",
    "source_root",
    "weakened_path_segment_preserves_colon",
]
