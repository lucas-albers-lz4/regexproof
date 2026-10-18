"""Source-pinned replay helpers for Tracecat registry artifact keys."""

from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Iterator

PIN = "c84d52528a489821f355fc63976fbc7783ae0ad5"
REPOSITORY = "https://github.com/TracecatHQ/tracecat.git"
SOURCE_FILE = "tracecat/registry/artifact_keys.py"
SOURCE_SHA256 = "26a7335ee1c219dbd844b7207f60809ae563c70249cf714896c91322a7899e06"
ORIGIN_CLASS = r"[^a-zA-Z0-9_-]"
WEAKENED_ORIGIN_CLASS = r"[^a-zA-Z0-9_/-]"

_CACHED_ROOT: Path | None = None
_CACHED_MODULE: ModuleType | None = None


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=20,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_checkout(root: Path) -> None:
    revision = _git(root, "rev-parse", "HEAD")
    if revision != PIN:
        raise RuntimeError(f"Tracecat replay source is {revision}, expected {PIN}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("Tracecat replay source must be a clean checkout")
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"Tracecat replay source is missing or is a symlink: {source}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or source.read_bytes() != committed:
        raise RuntimeError("Tracecat replay source bytes differ from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Tracecat source digest is {digest}, expected {SOURCE_SHA256}")


def source_root() -> Path:
    """Return the clean exact-pin checkout, fetching it only when absent."""
    global _CACHED_ROOT
    configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
    if _CACHED_ROOT is not None:
        if configured and Path(configured).expanduser().resolve() != _CACHED_ROOT:
            raise RuntimeError("TRACECAT_REPLAY_SOURCE changed during replay")
        return _CACHED_ROOT

    root = (
        Path(configured).expanduser().resolve()
        if configured
        else Path(tempfile.gettempdir())
        / "regexproof-pinned-sources"
        / f"tracecat-{PIN}"
    )
    if root.exists():
        _verify_checkout(root)
        _CACHED_ROOT = root
        return root

    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", PIN)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _verify_checkout(root)
    except (OSError, subprocess.SubprocessError, RuntimeError):
        shutil.rmtree(root, ignore_errors=True)
        raise
    _CACHED_ROOT = root
    return root


def _artifact_module() -> ModuleType:
    global _CACHED_MODULE
    if _CACHED_MODULE is not None:
        source_root()
        return _CACHED_MODULE
    root = source_root()
    source = root / SOURCE_FILE
    name = f"tracecat_artifact_keys_{PIN}"
    spec = importlib.util.spec_from_file_location(name, source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load pinned Tracecat helper: {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve() != source.resolve():
        raise RuntimeError("loaded Tracecat helper outside the pinned checkout")
    _CACHED_MODULE = module
    return module


def origin_substitution_pattern() -> str:
    """Extract and validate the first substitution class from the pinned helper."""
    import ast

    source = (source_root() / SOURCE_FILE).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=SOURCE_FILE)
    function = next(
        (
            item
            for item in tree.body
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
            and item.name == "_slugify_origin"
        ),
        None,
    )
    if function is None:
        raise RuntimeError("pinned Tracecat helper no longer defines _slugify_origin")
    patterns = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "re"
            and node.func.attr == "sub"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            patterns.append(node.args[0].value)
    if not patterns or patterns[0] != ORIGIN_CLASS:
        raise RuntimeError(f"unexpected pinned origin substitution class: {patterns!r}")
    return patterns[0]


@contextmanager
def _weakened_origin_class(module: ModuleType) -> Iterator[None]:
    original_re = module.re

    def sub(pattern: str, replacement: str, value: str, count: int = 0) -> str:
        if pattern == ORIGIN_CLASS:
            pattern = WEAKENED_ORIGIN_CLASS
        return original_re.sub(pattern, replacement, value, count=count)

    module.re = SimpleNamespace(sub=sub)
    try:
        yield
    finally:
        module.re = original_re


def slugify_origin(origin: str, *, weaken_class: bool = False) -> str:
    """Call the exact pinned helper, with an optional one-class mutation."""
    module = _artifact_module()
    if not weaken_class:
        return module._slugify_origin(origin)
    with _weakened_origin_class(module):
        return module._slugify_origin(origin)


def artifact_s3_key(
    organization_id: str,
    origin: str,
    version: str,
    *,
    weaken_class: bool = False,
) -> str:
    """Call the exact pinned S3-key builder, optionally with the mutation."""
    module = _artifact_module()
    if not weaken_class:
        return module.get_artifact_s3_key(organization_id, origin, version)
    with _weakened_origin_class(module):
        return module.get_artifact_s3_key(organization_id, origin, version)


def safe_origin_component(slug: str) -> bool:
    """Check the adopted S3 component alphabet and length bound."""
    return len(slug) <= 100 and all(
        ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
        for ch in slug
    )


def mutation_reproduces(component_char: str) -> bool:
    """Show the actual weakened product helper passes a slash into the key."""
    if component_char != "/":
        return False
    origin = "git+ssh://git@github.com/org/repo.git"
    slug = slugify_origin(origin, weaken_class=True)
    mutated_key = artifact_s3_key("test-org", origin, "v1", weaken_class=True)
    return (
        "/" in slug
        and not safe_origin_component(slug)
        and len(mutated_key.split("/")) > 5
    )


__all__ = [
    "PIN",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "artifact_s3_key",
    "mutation_reproduces",
    "origin_substitution_pattern",
    "safe_origin_component",
    "slugify_origin",
    "source_root",
]
