"""Exact-pin YARA-X replay for malcontent's CVE-2025-48384 rule."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

PIN = "ea3e83e24676a1678a9522141da29b636c9451ab"
REPOSITORY = "https://github.com/chainguard-dev/malcontent.git"
SOURCE_FILE = "rules/impact/exploit/cve-2025-48384.yara"
SOURCE_SHA256 = "b6d017494cd9ecc7a9843832229fa45789c7edc06ccba093c0381d151a2a2552"
YARA_X_VERSION = "1.19.0"
YARA_X_CLI_SHA256 = "dd5e5c07a0397ad922b597b8d6c35c22485ec9fe4bf26f064d242245042cdca2"
RULE_NAME = "git_submodule_carriage_return"
BENIGN_CRLF = (
    b'[submodule "lib"]\r\n'
    b"path = vendor/lib\r\n"
    b"url = https://example.invalid/lib.git\r\n"
)

_SOURCE_ENV = "MALCONTENT_REPLAY_SOURCE"
_YARA_X_ENV = "MALCONTENT_YARA_X"
_DEFAULT_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"malcontent-{PIN}"
)
_CACHED_ROOT: Path | None = None
_CACHED_YARA_X: Path | None = None


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
        shell=False,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_checkout(root: Path) -> None:
    if _git(root, "rev-parse", "HEAD") != PIN:
        raise RuntimeError(f"malcontent source must be checked out at {PIN}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("malcontent source must be a clean pinned checkout")
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"pinned YARA rule is missing or a symlink: {source}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or source.read_bytes() != committed:
        raise RuntimeError("malcontent rule bytes differ from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"malcontent rule digest is {digest}, expected {SOURCE_SHA256}")
    lines = [line for line in committed.splitlines() if b"$path_embedded_cr =" in line]
    if len(lines) != 1 or not lines[0].rstrip().endswith(b"\\r[^\\n]/ nocase"):
        raise RuntimeError("pinned $path_embedded_cr terminal class changed")


def source_root() -> Path:
    """Return a verified checkout of the exact frozen cohort source pin."""
    global _CACHED_ROOT
    configured = os.environ.get(_SOURCE_ENV)
    root = Path(configured).expanduser().resolve() if configured else _DEFAULT_ROOT
    if _CACHED_ROOT is not None:
        if root != _CACHED_ROOT:
            raise RuntimeError(f"{_SOURCE_ENV} changed during replay")
        return _CACHED_ROOT
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


def yara_x_cli() -> Path:
    """Return YARA-X 1.19.0 only when its executable digest matches the pin."""
    global _CACHED_YARA_X
    configured = os.environ.get(_YARA_X_ENV)
    requested = (
        Path(configured).expanduser().resolve()
        if configured
        else Path(shutil.which("yr") or "").resolve()
    )
    if _CACHED_YARA_X is not None:
        if requested != _CACHED_YARA_X:
            raise RuntimeError(f"{_YARA_X_ENV} changed during replay")
        return _CACHED_YARA_X
    if not requested.is_file() or requested.is_symlink():
        raise RuntimeError("YARA-X 1.19.0 CLI is required (set MALCONTENT_YARA_X or PATH)")
    digest = hashlib.sha256(requested.read_bytes()).hexdigest()
    if digest != YARA_X_CLI_SHA256:
        raise RuntimeError(f"YARA-X CLI digest is {digest}, expected {YARA_X_CLI_SHA256}")
    version = subprocess.run(
        [str(requested), "--version"],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
        shell=False,
    ).stdout.strip()
    if not version.endswith(YARA_X_VERSION):
        raise RuntimeError(f"YARA-X CLI version is {version!r}, expected {YARA_X_VERSION}")
    _CACHED_YARA_X = requested
    return requested


def run_scan(rule_path: Path, target_path: Path) -> str:
    """Run the exact pinned product matcher with argv-only bounded execution."""
    result = subprocess.run(
        [str(yara_x_cli()), "scan", str(rule_path), str(target_path)],
        cwd=source_root(),
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
        shell=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"YARA-X scan failed ({result.returncode}): {result.stderr.strip()}"
        )
    return result.stdout


def weaken_path_embedded_cr(rule_bytes: bytes) -> bytes:
    """Admit LF after the CR in exactly the pinned path-embedded branch."""
    needle = b"$path_embedded_cr ="
    lines = rule_bytes.splitlines(keepends=True)
    indexes = [index for index, line in enumerate(lines) if needle in line]
    if len(indexes) != 1:
        raise RuntimeError("cannot uniquely locate $path_embedded_cr for mutation")
    index = indexes[0]
    exact = b"\\r[^\\n]/ nocase"
    if lines[index].count(exact) != 1:
        raise RuntimeError("$path_embedded_cr no longer has the adopted terminal class")
    lines[index] = lines[index].replace(exact, b"\\r[\\r\\n]/ nocase", 1)
    return b"".join(lines)


def mutation_reproduces(next_byte: str) -> bool:
    """Replay the SAT LF witness through the exact class and full YARA rule."""
    if next_byte != "\n":
        return False
    root = source_root()
    cli = yara_x_cli()
    original = (root / SOURCE_FILE).read_bytes()
    mutated = weaken_path_embedded_cr(original)
    with tempfile.TemporaryDirectory(prefix="malcontent-cve48384-mutation-") as raw:
        work = Path(raw)
        class_rule = work / "class.yara"
        class_sample = work / "one-lf-byte"
        class_rule.write_text(
            "rule terminal_class { strings: $s = /[\\r\\n]/ condition: $s }\n",
            encoding="ascii",
        )
        class_sample.write_bytes(next_byte.encode("ascii"))
        class_match = subprocess.run(
            [str(cli), "scan", str(class_rule), str(class_sample)],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            shell=False,
        )
        if class_match.returncode or "terminal_class" not in class_match.stdout:
            return False

        mutated_rule = work / SOURCE_FILE
        mutated_rule.parent.mkdir(parents=True)
        mutated_rule.write_bytes(mutated)
        benign_file = work / "benign-crlf.gitmodules"
        benign_file.write_bytes(BENIGN_CRLF)
        full_rule_match = subprocess.run(
            [str(cli), "scan", str(mutated_rule), str(benign_file)],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            shell=False,
        )
        return (
            full_rule_match.returncode == 0
            and RULE_NAME in full_rule_match.stdout
        )


__all__ = [
    "BENIGN_CRLF",
    "PIN",
    "REPOSITORY",
    "RULE_NAME",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "YARA_X_CLI_SHA256",
    "YARA_X_VERSION",
    "mutation_reproduces",
    "run_scan",
    "source_root",
    "weaken_path_embedded_cr",
    "yara_x_cli",
]
