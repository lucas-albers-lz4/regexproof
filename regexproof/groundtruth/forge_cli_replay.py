"""Replay the pinned forge-cli command renderer against its real source tree."""

from __future__ import annotations

import importlib
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path
from types import ModuleType

PIN = "efcf8e4c0087def553a737dc1c4eebda5d8a90cd"
REPOSITORY = "https://github.com/Agenticstiger/forge-cli.git"
_CACHED_ROOT: Path | None = None
_CACHED_RUNNER: ModuleType | None = None
_LOCK = threading.RLock()
_SOURCE_SETTING_CAPTURED = False
_SOURCE_SETTING: Path | None = None


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout.strip()


def _verify_clean_pin(root: Path) -> None:
    revision = _git(root, "rev-parse", "HEAD")
    if revision != PIN:
        raise RuntimeError(f"forge-cli replay source is {revision}, expected {PIN}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("forge-cli replay source must be a clean checkout")


def source_root() -> Path:
    """Return a checkout at PIN, fetching it when no explicit checkout is set."""
    global _CACHED_ROOT, _SOURCE_SETTING_CAPTURED, _SOURCE_SETTING
    configured_value = os.environ.get("FORGE_CLI_REPLAY_SOURCE")
    configured = Path(configured_value).resolve() if configured_value else None
    with _LOCK:
        if _SOURCE_SETTING_CAPTURED and configured != _SOURCE_SETTING:
            raise RuntimeError("FORGE_CLI_REPLAY_SOURCE changed during replay")
        if not _SOURCE_SETTING_CAPTURED:
            _SOURCE_SETTING_CAPTURED = True
            _SOURCE_SETTING = configured
        if _CACHED_ROOT is not None:
            _verify_clean_pin(_CACHED_ROOT)
            return _CACHED_ROOT
        if configured is not None:
            _verify_clean_pin(configured)
            _CACHED_ROOT = configured
            return configured

        # A process-specific cache avoids concurrent workers deleting or
        # initializing the same shared checkout. The lock also serializes
        # threads in this process; a stale cache is safe to reuse only after
        # the revision and clean-tree checks above.
        root = (
            Path(tempfile.gettempdir())
            / "regexproof-pinned-sources"
            / f"forge-cli-{PIN}-{os.getpid()}"
        )
        if root.exists():
            try:
                _verify_clean_pin(root)
            except (RuntimeError, subprocess.CalledProcessError):
                shutil.rmtree(root)
            else:
                _CACHED_ROOT = root
                return root
        root.parent.mkdir(parents=True, exist_ok=True)
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", PIN)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _verify_clean_pin(root)
        _CACHED_ROOT = root
        return root


def _runner_module() -> ModuleType:
    global _CACHED_RUNNER
    with _LOCK:
        if _CACHED_RUNNER is not None:
            return _CACHED_RUNNER
        root = source_root()
        package_root = str(root)
        if package_root not in sys.path:
            sys.path.insert(0, package_root)
        module_name = "fluid_build.build_runners.dbt.runner"
        module = importlib.import_module(module_name)
        module_path = Path(module.__file__).resolve()
        if not module_path.is_relative_to(root):
            raise RuntimeError(f"loaded renderer outside pinned checkout: {module_path}")
        if _git(root, "rev-parse", "HEAD") != PIN:
            raise RuntimeError("forge-cli checkout changed during replay")
        _CACHED_RUNNER = module
        return module


def render_command(command: list[str], *, regex_pattern: str | None = None) -> str:
    """Invoke the pinned product helper, optionally with a weakened regex."""
    with _LOCK:
        module = _runner_module()
        original = module.SENSITIVE_ENV_KEY_RE
        try:
            if regex_pattern is not None:
                import re

                module.SENSITIVE_ENV_KEY_RE = re.compile(regex_pattern)
            return module._render_command_for_log(command)
        finally:
            module.SENSITIVE_ENV_KEY_RE = original


def product_regex_pattern() -> str:
    """Read the actual imported product pattern, after validating the source pin."""
    return _runner_module().SENSITIVE_ENV_KEY_RE.pattern


def renderer_source() -> Path:
    """Expose the pinned implementation path for provenance assertions."""
    return Path(_runner_module().__file__).resolve()


def redaction_mutation_reproduces(key: str, weakened_pattern: str) -> bool:
    """Replay a witness through the normal and weakened real helper policies."""
    sentinel = "CLEAR_SENTINEL"
    command = ["dbt", "run", "-e", f"{key}={sentinel}"]
    original = render_command(command)
    weakened = render_command(command, regex_pattern=weakened_pattern)
    return original == f"dbt run -e {key}=<redacted>" and weakened == " ".join(command)


__all__ = [
    "PIN",
    "product_regex_pattern",
    "redaction_mutation_reproduces",
    "render_command",
    "renderer_source",
    "source_root",
]
