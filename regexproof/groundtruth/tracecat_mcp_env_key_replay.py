"""Pinned Tracecat MCP stdio environment-key validation replays."""

from __future__ import annotations

import hashlib
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_replay import PIN, REPOSITORY, source_root as _tracecat_root

SOURCE_FILE = "tracecat/integrations/mcp_validation.py"
SOURCE_SHA256 = "41cf730ba1cb592cae684811bbb4d510961a0a441c156313a804b2593085f895"
SOURCE_PATTERN = r"^[A-Za-z_][A-Za-z0-9_]*$"
STRICT_PATTERN = r"^[A-Za-z_][A-Za-z0-9_]*\Z"


def source_root() -> Path:
    """Return the clean Tracecat checkout after verifying the adopted file."""
    root = _tracecat_root()
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("pinned Tracecat MCP validator source is missing or a symlink")
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{SOURCE_FILE}"],
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout
    actual = source.read_bytes()
    if actual != committed:
        raise RuntimeError("Tracecat MCP validator bytes differ from its pinned commit")
    digest = hashlib.sha256(actual).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Tracecat MCP validator digest differs: {digest}")
    return root


def _load_from_path(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load pinned MCP validator module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_from_text(source_text: str, name: str) -> ModuleType:
    """Load the exact pinned module with only a requested regex edit."""
    with tempfile.TemporaryDirectory(prefix="tracecat-mcp-validator-") as temp:
        path = Path(temp) / "mcp_validation.py"
        path.write_text(source_text, encoding="utf-8")
        return _load_from_path(path, name)


def _module() -> ModuleType:
    root = source_root()
    return _load_from_path(root / SOURCE_FILE, f"tracecat_mcp_validation_{PIN}")


def _accepted_by(module: ModuleType, key: str) -> bool:
    try:
        module.validate_mcp_env_key(key)
    except module.MCPValidationError:
        return False
    return True


def accepted_terminal_lf_reproduces(witness: dict[str, str]) -> bool:
    """Replay an invalid final-LF name through the exact pinned validator."""
    key = witness.get("key")
    if not isinstance(key, str) or not key.endswith("\n") or "\n" in key[:-1]:
        return False
    module = _module()
    try:
        module.validate_mcp_command_config(command="npx", env={key: "synthetic"})
    except module.MCPValidationError:
        return False
    return True


def subprocess_receives_environment_key(key: str) -> bool:
    """Confirm a POSIX child environment can carry the validator's accepted key."""
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            "import os, sys; sys.exit(0 if sys.argv[1] in os.environ else 41)",
            key,
        ],
        env={key: "synthetic"},
        check=False,
        capture_output=True,
        timeout=10,
    )
    return completed.returncode == 0


def terminal_lf_mutation_reproduces(witness: dict[str, str]) -> bool:
    r"""Strengthen the pinned `$` to `\Z`, then reintroduce `$` as a mutation."""
    key = witness.get("key")
    if not isinstance(key, str) or not key.endswith("\n") or "\n" in key[:-1]:
        return False
    root = source_root()
    source = (root / SOURCE_FILE).read_text(encoding="utf-8")
    old = f'r"{SOURCE_PATTERN}"'
    strict = f'r"{STRICT_PATTERN}"'
    if source.count(old) != 1:
        raise RuntimeError("expected one exact source env-key regex to mutate")
    strict_text = source.replace(old, strict, 1)
    strict_module = _load_from_text(strict_text, "tracecat_mcp_validation_strict")
    weak_text = strict_text.replace(strict, old, 1)
    weak_module = _load_from_text(weak_text, "tracecat_mcp_validation_weak")
    return (
        not _accepted_by(strict_module, key)
        and _accepted_by(weak_module, key)
        and _accepted_by(_module(), key)
    )


__all__ = [
    "PIN",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "SOURCE_SHA256",
    "accepted_terminal_lf_reproduces",
    "source_root",
    "subprocess_receives_environment_key",
    "terminal_lf_mutation_reproduces",
]
