"""Exact-pin replay for Inhale's remote-directory link scope helper."""

from __future__ import annotations

import hashlib
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from types import SimpleNamespace
from pathlib import Path
from urllib.parse import urlsplit
from typing import Any

PIN = "889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8"
REPOSITORY = "https://github.com/netspooky/inhale"
SOURCE_FILE = "iModules/rDownload.py"
SOURCE_SHA256 = "3350a9a3d1be11e44dfff3756f90b03f349cc0a59246959047fe4ed0633c6414"
SOURCE_PATTERN = r"^(([a-zA-Z_-]+)://([^/]+))(/.*)?$"
OUTPUT_PATH_PATTERN = r"https?://"
MUTATED_PATTERN = r"^(([a-zA-Z_-]+)://(.+))(/.*)?$"
MUTATED_PATH_PATTERN = r"https?://[^/]+/"


def source_root() -> Path:
    configured = os.environ.get("INHALE_DIRECTORY_REPLAY_SOURCE")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(tempfile.gettempdir()) / "regexproof-pinned-sources" / f"inhale-{PIN}"


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True,
        text=not binary, timeout=20, check=True, shell=False,
    )
    return completed.stdout if binary else completed.stdout.strip()


def verify_checkout(root: Path | None = None) -> dict[str, Any]:
    root = (root or source_root()).expanduser().resolve()
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Inhale checkout is missing or a symlink: {root}")
    head = _git(root, "rev-parse", "HEAD")
    if head != PIN:
        raise ValueError(f"Inhale checkout HEAD {head!r} does not match {PIN}")
    status = _git(root, "status", "--porcelain", "--untracked-files=all")
    if status:
        raise ValueError("Inhale checkout must be clean")
    current = root / SOURCE_FILE
    if current.is_symlink() or not current.is_file():
        raise ValueError(f"pinned Inhale source is missing or a symlink: {SOURCE_FILE}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if current.read_bytes() != committed:
        raise ValueError("Inhale source working file differs from pinned bytes")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise ValueError(f"Inhale source hash mismatch: {digest}")
    return {"head": head, "source_file": SOURCE_FILE, "source_sha256": digest}


def _load_module(root: Path, pattern_override: str | None = None) -> Any:
    path = root / SOURCE_FILE
    spec = importlib.util.spec_from_file_location(f"inhale_rdownload_{PIN}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Inhale rDownload helper")
    module = importlib.util.module_from_spec(spec)
    previous_bytecode_policy = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous_bytecode_policy
    if module.re_url.pattern != SOURCE_PATTERN:
        raise ValueError("pinned Inhale re_url differs from the inventory pattern")
    if pattern_override is not None:
        module.re_url = re.compile(pattern_override)
    return module


def _origin(url: str) -> tuple[str, str, int | None]:
    parsed = urlsplit(url)
    return (parsed.scheme.lower(), (parsed.hostname or "").lower(), parsed.port)


@contextmanager
def _working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def run_directory_replay(
    root_url: str,
    href: str,
    *,
    checkout: Path | None = None,
) -> dict[str, Any]:
    """Call the pinned parser and recursive downloader with a fake URL opener."""
    root = (checkout or source_root()).expanduser().resolve()
    source = verify_checkout(root)
    module = _load_module(root)
    calls: list[str] = []
    html = f'<html><body><a href="{href}">synthetic link</a></body></html>'.encode()

    class _Info:
        def __init__(self, content_type: str) -> None:
            self._content_type = content_type

        def get_content_type(self) -> str:
            return self._content_type

    class _Response:
        def __init__(self, url: str) -> None:
            self.url = url
            self.read_once = False

        def info(self) -> _Info:
            content_type = "text/html" if self.url == root_url else "application/octet-stream"
            return _Info(content_type)

        def read(self, _size: int = -1) -> bytes:
            if self.read_once:
                return b""
            self.read_once = True
            return html if self.url == root_url else b"INHALE_SYNTHETIC_SAMPLE"

    def _fake_urlopen(url: str, timeout: float | None = None) -> _Response:
        del timeout
        calls.append(url)
        if len(calls) > 4:
            raise RuntimeError("synthetic URL opener call cap exceeded")
        return _Response(url)

    module.urlopen = _fake_urlopen
    with tempfile.TemporaryDirectory(prefix="regexproof-inhale-directory-") as temporary:
        output_root = Path(temporary) / "output"
        output_root.mkdir()
        with _working_directory(Path(temporary)):
            module.parseDir(root_url, "./output/")
        files = sorted(
            path.relative_to(output_root).as_posix()
            for path in output_root.rglob("*")
            if path.is_file()
        )
    external = [url for url in calls if _origin(url) != _origin(root_url)]
    return {
        "source": source,
        "root_url": root_url,
        "href": href,
        "root_origin": list(_origin(root_url)),
        "fetch_calls": calls,
        "cross_origin_fetches": external,
        "cross_origin_fetch_observed": bool(external),
        "synthetic_output_files": files,
        "network_used": False,
    }


def _single_file_replay(
    url: str,
    *,
    checkout: Path | None = None,
    pattern_override: str | None = None,
) -> dict[str, Any]:
    root = (checkout or source_root()).expanduser().resolve()
    source = verify_checkout(root)
    module = _load_module(root)
    if pattern_override is not None:
        # getSingleFile/parseDir compile their own replacement regex locally.
        # Give this imported module a private `re` facade so the mutation does
        # not alter Python's process-wide `re` module.
        module.re = SimpleNamespace(
            compile=lambda pattern: re.compile(
                pattern_override if pattern == r"https?://" else pattern
            )
        )
    class _Response:
        status_code = 200
        headers = {"Content-Type": "application/octet-stream"}
        content = b"INHALE_SYNTHETIC_SAMPLE"

    module.requests.get = lambda _url, timeout=None: _Response()
    with tempfile.TemporaryDirectory(prefix="regexproof-inhale-file-url-") as temporary:
        output_root = Path(temporary) / "output"
        output_root.mkdir()
        with _working_directory(Path(temporary)):
            returned_path, _headers, _message = module.getSingleFile(url, "./output/")
            resolved = Path(returned_path).resolve()
        return {
            "source": source,
            "url": url,
            "returned_path": returned_path,
            "resolved_path": str(resolved),
            "output_root": str(output_root.resolve()),
            "under_output_root": resolved.is_relative_to(output_root.resolve()),
            "under_temporary_root": resolved.is_relative_to(Path(temporary).resolve()),
            "file_exists": resolved.is_file(),
            "synthetic_content_written": (
                resolved.read_bytes() == b"INHALE_SYNTHETIC_SAMPLE"
                if resolved.is_file() else False
            ),
            "network_used": False,
        }


def run_file_url_replay(
    url: str, *, checkout: Path | None = None, pattern_override: str | None = None
) -> dict[str, Any]:
    return _single_file_replay(
        url, checkout=checkout, pattern_override=pattern_override
    )


def _directory_root_replay(url: str, *, checkout: Path | None = None) -> dict[str, Any]:
    root = (checkout or source_root()).expanduser().resolve()
    source = verify_checkout(root)
    module = _load_module(root)
    calls: list[str] = []

    class _Info:
        def get_content_type(self) -> str:
            return "application/octet-stream"

    class _Response:
        def __init__(self) -> None:
            self.read_once = False

        def info(self) -> _Info:
            return _Info()

        def read(self, _size: int = -1) -> bytes:
            if self.read_once:
                return b""
            self.read_once = True
            return b"INHALE_SYNTHETIC_DIRECTORY_SAMPLE"

    def _fake_urlopen(requested: str, timeout: float | None = None) -> _Response:
        del timeout
        calls.append(requested)
        if len(calls) > 2:
            raise RuntimeError("synthetic URL opener call cap exceeded")
        return _Response()

    module.urlopen = _fake_urlopen
    with tempfile.TemporaryDirectory(prefix="regexproof-inhale-directory-root-") as temporary:
        output_root = Path(temporary) / "output"
        output_root.mkdir()
        with _working_directory(Path(temporary)):
            returned_path = module.parseDir(url, "./output/")
            resolved = Path(returned_path).resolve()
        return {
            "source": source,
            "url": url,
            "fetch_calls": calls,
            "returned_path": returned_path,
            "resolved_path": str(resolved),
            "output_root": str(output_root.resolve()),
            "under_output_root": resolved.is_relative_to(output_root.resolve()),
            "under_temporary_root": resolved.is_relative_to(Path(temporary).resolve()),
            "file_exists": resolved.is_file(),
            "synthetic_content_written": (
                resolved.read_bytes() == b"INHALE_SYNTHETIC_DIRECTORY_SAMPLE"
                if resolved.is_file() else False
            ),
            "network_used": False,
        }


def run_directory_root_replay(url: str, *, checkout: Path | None = None) -> dict[str, Any]:
    return _directory_root_replay(url, checkout=checkout)


def empty_authority_mutation_replays(_witness: dict[str, Any] | None = None) -> bool:
    """Prove real Python match behavior changes under the weaker authority class."""
    try:
        root = source_root().expanduser().resolve()
        verify_checkout(root)
        baseline = _load_module(root)
        mutated = _load_module(root, MUTATED_PATTERN)
        value = "https:///path"
        source_result = baseline.resolve_link(value, "https://trusted.example")
        mutant_result = mutated.resolve_link(value, "https://trusted.example")
        source_is_absolute = baseline.re_url.match(value) is not None
        mutant_match = mutated.re_url.match(value)
        return bool(
            not source_is_absolute
            and mutant_match is not None
            and mutant_match.group(3) == "/path"
            and source_result == "https://trusted.example/https:///path"
            and mutant_result == "https:///path/"
        )
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False


def widened_file_path_mutation_replays(_witness: dict[str, Any] | None = None) -> bool:
    url = "https://downloads.example/../escape.bin"
    try:
        baseline = run_file_url_replay(url)
        mutated = run_file_url_replay(url, pattern_override=r"https?://[^/]+/")
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    return bool(
        baseline["under_output_root"]
        and mutated["under_temporary_root"]
        and not mutated["under_output_root"]
        and mutated["synthetic_content_written"]
    )


def file_url_output_escapes_configured_root(witness: dict[str, Any]) -> bool:
    url = witness.get("file_url", witness.get("url", ""))
    if url != "https://downloads.example/../../escape.bin":
        return False
    try:
        result = run_file_url_replay(url)
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    return bool(
        not result["under_output_root"]
        and result["under_temporary_root"]
        and result["synthetic_content_written"]
    )


def directory_url_output_escapes_configured_root(witness: dict[str, Any]) -> bool:
    url = witness.get("directory_url", witness.get("url", ""))
    if url != "https://downloads.example/../../directory.bin":
        return False
    try:
        result = run_directory_root_replay(url)
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    return bool(
        not result["under_output_root"]
        and result["under_temporary_root"]
        and result["synthetic_content_written"]
    )


def cross_origin_prefix_replays(witness: dict[str, Any]) -> bool:
    root_url = witness.get("root_url", "")
    href = witness.get("href", "")
    if not root_url or not href or _origin(root_url) == _origin(href):
        return False
    try:
        result = run_directory_replay(root_url, href)
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    return href in result["cross_origin_fetches"]


__all__ = [
    "MUTATED_PATH_PATTERN", "MUTATED_PATTERN", "OUTPUT_PATH_PATTERN", "PIN", "REPOSITORY", "SOURCE_FILE", "SOURCE_PATTERN",
    "cross_origin_prefix_replays", "directory_url_output_escapes_configured_root",
    "empty_authority_mutation_replays", "file_url_output_escapes_configured_root",
    "run_directory_replay", "run_directory_root_replay", "run_file_url_replay",
    "source_root", "verify_checkout", "widened_file_path_mutation_replays",
]
