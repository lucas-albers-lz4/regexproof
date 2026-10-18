"""Pinned Tracecat MCP server-name separator replay and source mutation."""

from __future__ import annotations

import ast
import importlib.util
import tempfile
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_mcp_env_key_replay import (
    PIN,
    SOURCE_FILE,
    source_root,
)

SOURCE_PATTERN = r"^[a-zA-Z0-9_-]+$"
WEAKENED_PATTERN = r"^[a-zA-Z0-9_/-]+$"


def _module_from_path(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load pinned MCP validator module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _module_from_text(source: str, name: str) -> ModuleType:
    with tempfile.TemporaryDirectory(prefix="tracecat-server-name-") as temp:
        path = Path(temp) / "mcp_validation.py"
        path.write_text(source, encoding="utf-8")
        return _module_from_path(path, name)


def _accepts(module: ModuleType, value: str) -> bool:
    try:
        module.validate_mcp_server_name(value)
    except module.MCPValidationError:
        return False
    return True


def _config_accepts(module: ModuleType, value: str) -> bool:
    try:
        module.validate_mcp_command_config(command="npx", name=value)
    except module.MCPValidationError:
        return False
    return True


def _source_pattern() -> str:
    root = source_root()
    source = (root / SOURCE_FILE).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=SOURCE_FILE)
    matches = [
        node.args[0].value
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "re"
        and node.func.attr == "match"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
        and node.args[0].value == SOURCE_PATTERN
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"expected one exact pinned server-name validator pattern, found {len(matches)}"
        )
    return source


def server_name_separator_exclusion_reproduces(witness: dict[str, str]) -> bool:
    """Confirm the exact validator rejects the proven slash/backslash cases."""
    character = witness.get("name_char")
    if character not in {"/", "\\"}:
        return False
    source = source_root()
    module = _module_from_path(
        source / SOURCE_FILE, f"tracecat_server_name_validator_{PIN}"
    )
    return not _accepts(module, character) and not _config_accepts(module, character)


def server_name_slash_mutation_reproduces(witness: dict[str, str]) -> bool:
    """Add slash to the exact pinned allowlist and confirm the guard flips."""
    character = witness.get("name_char")
    if character != "/":
        return False
    source_text = _source_pattern()
    original = f'r"{SOURCE_PATTERN}"'
    weakened = f'r"{WEAKENED_PATTERN}"'
    if source_text.count(original) != 1:
        raise RuntimeError("expected one exact server-name validator pattern to mutate")
    mutated_text = source_text.replace(original, weakened, 1)
    original_module = _module_from_text(source_text, "tracecat_server_name_original")
    mutated_module = _module_from_text(mutated_text, "tracecat_server_name_mutated")
    return (
        not _accepts(original_module, character)
        and not _config_accepts(original_module, character)
        and _accepts(mutated_module, character)
        and _config_accepts(mutated_module, character)
    )


__all__ = [
    "PIN",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "WEAKENED_PATTERN",
    "server_name_separator_exclusion_reproduces",
    "server_name_slash_mutation_reproduces",
    "source_root",
]
