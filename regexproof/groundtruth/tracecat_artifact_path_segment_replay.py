"""Exact-pin replay for Tracecat's mount-only artifact path segment helper."""

from __future__ import annotations

import ast
import copy
import hashlib
import subprocess
import tempfile
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_replay import PIN, source_root

SOURCE_FILE = (
    "packages/tracecat-ee/tracecat_ee/agent/artifacts/mount_only_provider.py"
)
SOURCE_SHA256 = "b9ef06e9fa2582b4c376ab8eb526eef1dc9adeb1c7d2d92e1c8da92ac14a3b11"
SOURCE_PATTERN = r"[^A-Za-z0-9_.-]+"
WEAKENED_PATTERN = r"[^A-Za-z0-9_./-]+"


def _source_bytes() -> tuple[Path, bytes]:
    root = source_root()
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"missing or symlinked pinned artifact provider: {source}")
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{SOURCE_FILE}"],
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout
    actual = source.read_bytes()
    if actual != committed:
        raise RuntimeError("artifact provider bytes differ from the pinned Git blob")
    digest = hashlib.sha256(actual).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"artifact provider digest {digest} differs from the contract")
    return source, actual


def _helper_module(*, weaken: bool = False) -> ModuleType:
    source_path, source_bytes = _source_bytes()
    tree = ast.parse(source_bytes, filename=SOURCE_FILE)
    assignment = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "_SAFE_PATH_SEGMENT_RE"
                for target in node.targets
            )
        ),
        None,
    )
    function = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "_safe_path_segment"
        ),
        None,
    )
    if assignment is None or function is None:
        raise RuntimeError("pinned source no longer contains the reviewed helper")
    if (
        not isinstance(assignment.value, ast.Call)
        or not isinstance(assignment.value.func, ast.Attribute)
        or not isinstance(assignment.value.func.value, ast.Name)
        or assignment.value.func.value.id != "re"
        or assignment.value.func.attr != "compile"
        or not assignment.value.args
        or not isinstance(assignment.value.args[0], ast.Constant)
        or assignment.value.args[0].value != SOURCE_PATTERN
    ):
        raise RuntimeError("pinned path-segment regex differs from the adopted pattern")

    assignment = copy.deepcopy(assignment)
    function = copy.deepcopy(function)
    if weaken:
        assignment.value.args[0].value = WEAKENED_PATTERN
    module_ast = ast.Module(
        body=[ast.Import(names=[ast.alias(name="re")]), assignment, function],
        type_ignores=[],
    )
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_path_segment_{PIN}"}
    exec(compile(module_ast, str(source_path), "exec"), namespace)
    module = ModuleType(str(namespace["__name__"]))
    module.__dict__.update(namespace)
    return module


def source_pattern() -> str:
    """Return the regex from the exact pinned helper after source verification."""
    _source_bytes()
    return SOURCE_PATTERN


def safe_path_segment(value: str) -> str:
    """Run the exact source helper with its adopted regex."""
    return _helper_module()._safe_path_segment(value)


def weakened_path_escapes_artifact_root(segment_char: str) -> bool:
    """Mutate only the class to pass slash through, then replay Path joining."""
    if segment_char != "/":
        return False
    original = _helper_module()
    weakened = _helper_module(weaken=True)
    raw = "../../outside"
    safe_name = original._safe_path_segment(raw)
    unsafe_name = weakened._safe_path_segment(raw)
    with tempfile.TemporaryDirectory(prefix="tracecat-artifact-path-") as temp:
        artifact_root = (Path(temp) / ".tracecat" / "artifacts").resolve()
        safe_path = (artifact_root / "case" / safe_name).resolve()
        mutated_path = (artifact_root / "case" / unsafe_name).resolve()
        safe_stays_below_root = safe_path.is_relative_to(artifact_root)
        mutation_escapes_root = not mutated_path.is_relative_to(artifact_root)
    return (
        "/" not in safe_name
        and "\\" not in safe_name
        and safe_stays_below_root
        and "/" in unsafe_name
        and mutation_escapes_root
    )


__all__ = [
    "PIN",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "SOURCE_SHA256",
    "WEAKENED_PATTERN",
    "safe_path_segment",
    "source_pattern",
    "source_root",
    "weakened_path_escapes_artifact_root",
]
