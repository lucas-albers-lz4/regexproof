"""Replay Mycelium's pinned release-checksum preflight in the real helper."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

PIN = "4b53dc7629ca3bc88bf5467db481ad2af7130711"
PIN_20R2 = "d4f01ba6202d50909d1977810d322259482e0b82"
REPOSITORY = "https://github.com/mycelium0/mycelium.git"
SOURCE_FILE = "scripts/verify-release.sh"
SOURCE_SHA256 = "df394a764f2ebd906ffbc9d6bafa58af896b39e895e503a271da3baf710e2b58"
PATTERN = r"^[0-9a-fA-F]{64}[[:space:]]+[*]?[^[:space:]]"
WEAK_PATTERN = r"^[0-9a-fA-F]{0,64}[[:space:]]+[*]?[^[:space:]]"

_SOURCE_PINS = {PIN, PIN_20R2}
_SOURCE_ENV = {
    PIN: "MYCELIUM_REPLAY_SOURCE",
    PIN_20R2: "MYCELIUM_20R2_REPLAY_SOURCE",
}
_CACHED_ROOTS: dict[str, Path] = {}


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_checkout(root: Path, pin: str) -> None:
    revision = _git(root, "rev-parse", "HEAD")
    if revision != pin:
        raise RuntimeError(f"Mycelium replay source is {revision}, expected {pin}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("Mycelium replay source must be a clean checkout")
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"Mycelium replay source is missing or is a symlink: {source}")
    committed = _git(root, "show", f"{pin}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or source.read_bytes() != committed:
        raise RuntimeError("Mycelium source bytes differ from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Mycelium source digest is {digest}, expected {SOURCE_SHA256}")
    needle = f"grep -cE '{PATTERN}' SHA256SUMS".encode("ascii")
    if committed.count(needle) != 1:
        raise RuntimeError("pinned verifier no longer has the adopted checksum preflight")


def source_root(pin: str = PIN) -> Path:
    """Return the clean exact-pin checkout, fetching it only when absent."""
    if pin not in _SOURCE_PINS:
        raise RuntimeError(f"unsupported Mycelium replay pin: {pin}")
    env_name = _SOURCE_ENV[pin]
    configured = os.environ.get(env_name)
    cached = _CACHED_ROOTS.get(pin)
    if cached is not None:
        if configured and Path(configured).expanduser().resolve() != cached:
            raise RuntimeError(f"{env_name} changed during replay")
        return cached

    root = (
        Path(configured).expanduser().resolve()
        if configured
        else Path(tempfile.gettempdir())
        / "regexproof-pinned-sources"
        / f"mycelium-{pin}"
    )
    if root.exists():
        _verify_checkout(root, pin)
        _CACHED_ROOTS[pin] = root
        return root

    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", pin)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _verify_checkout(root, pin)
    except (OSError, subprocess.SubprocessError, RuntimeError):
        shutil.rmtree(root, ignore_errors=True)
        raise
    _CACHED_ROOTS[pin] = root
    return root


def _run_verifier(
    line: str, *, weaken: bool = False, pin: str = PIN
) -> tuple[int, str, bool]:
    """Run the pinned Bash helper with a lenient checksum-command stand-in.

    The stub models the documented portability edge (a checker that exits 0
    when the checksum file has no usable lines). Bash and grep remain real.
    """
    if not isinstance(line, str) or any(char in line for char in "\x00\n"):
        return 2, "invalid checksum input line", False
    try:
        line_bytes = line.encode("ascii")
    except UnicodeEncodeError:
        return 2, "checksum input is outside the declared ASCII domain", False

    root = source_root(pin)
    original = (root / SOURCE_FILE).read_bytes()
    script_bytes = original
    if weaken:
        exact = b"[0-9a-fA-F]{64}[[:space:]]+"
        weakened = b"[0-9a-fA-F]{0,64}[[:space:]]+"
        if original.count(exact) != 1:
            return 2, "cannot uniquely apply the checksum-length mutation", False
        script_bytes = original.replace(exact, weakened, 1)

    bash = shutil.which("bash")
    if not bash:
        return 2, "bash is required for the pinned release helper", False
    with tempfile.TemporaryDirectory(prefix="mycelium-release-preflight-") as raw:
        work = Path(raw)
        fake_bin = work / "bin"
        fake_bin.mkdir()
        script = work / "verify-release.sh"
        script.write_bytes(script_bytes)
        script.chmod(0o755)
        sums = work / "SHA256SUMS"
        sums.write_bytes(line_bytes + (b"\n" if line else b""))
        marker = work / "checksum-command-was-called"
        checksum_stub = fake_bin / "sha256sum"
        checksum_stub.write_text(
            "#!/bin/sh\nprintf called > \"$CHECKSUM_CALL_MARKER\"\nexit 0\n",
            encoding="ascii",
        )
        checksum_stub.chmod(0o755)
        env = os.environ.copy()
        env["PATH"] = str(fake_bin) + os.pathsep + env.get("PATH", "")
        env["CHECKSUM_CALL_MARKER"] = str(marker)
        try:
            result = subprocess.run(
                [bash, str(script)],
                cwd=work,
                env=env,
                capture_output=True,
                text=True,
                timeout=20,
                check=False,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            return 2, str(exc), marker.exists()
        output = result.stdout + result.stderr
        return result.returncode, output, marker.exists()


def preflight_rejects_without_sha256_line(*, pin: str = PIN) -> bool:
    """Check empty and longer checksum-free text never reaches the checker."""
    cases = ("", "<html>" + ("proxy error " * 8))
    for line in cases:
        rc, output, checker_called = _run_verifier(line, pin=pin)
        if rc == 0 or checker_called or "FAIL:" not in output:
            return False
    return True


def valid_record_reaches_checksum_command(*, pin: str = PIN) -> bool:
    """Check a syntactically valid record passes preflight to the checker."""
    line = "0" * 64 + " file.tar.gz"
    rc, output, checker_called = _run_verifier(line, pin=pin)
    return (
        rc == 0
        and checker_called
        and "ok    integrity:" in output
        and "authenticity was NOT checked" in output
    )


def mutation_reproduces(line: str, *, pin: str = PIN) -> bool:
    """Replay a weakened 64-hex requirement against the actual release helper."""
    if not line or len(line) >= 64 or "\n" in line or "\x00" in line:
        return False
    try:
        line.encode("ascii")
    except UnicodeEncodeError:
        return False
    original_rc, original_output, original_called = _run_verifier(line, pin=pin)
    mutated_rc, mutated_output, mutated_called = _run_verifier(
        line, weaken=True, pin=pin
    )
    return (
        original_rc != 0
        and not original_called
        and "FAIL:" in original_output
        and mutated_rc == 0
        and mutated_called
        and "INTEGRITY ONLY" in mutated_output
    )


__all__ = [
    "PATTERN",
    "PIN",
    "PIN_20R2",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "WEAK_PATTERN",
    "mutation_reproduces",
    "preflight_rejects_without_sha256_line",
    "source_root",
    "valid_record_reaches_checksum_command",
]
