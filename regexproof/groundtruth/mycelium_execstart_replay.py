"""Ground-truth replay for Mycelium's pinned systemd ExecStart parser."""

from __future__ import annotations

import hashlib
import os
import subprocess
import tempfile
from pathlib import Path

PIN = "4b53dc7629ca3bc88bf5467db481ad2af7130711"
REPOSITORY = "https://github.com/mycelium0/mycelium.git"
SOURCE_FILE = "scripts/update_unit_drift_drill.sh"
SOURCE_SHA256 = "4e28f0bd727ba842fed7840bdd163fbef32dc911f7c8e6bea409895ced4c6493"
PATTERN = r".*argv\[\]=\([^;]*\);.*"
CAPTURE_PIPELINE = (
    "sed -n 's/.*argv\\[\\]=\\([^;]*\\);.*/\\1/p' "
    "| sed 's/[[:space:]]*$//' | grep -v '^$'"
)
WEAKENED_PIPELINE = (
    "sed -n 's/.*argv\\[\\]=\\([^ ]*\\);.*/\\1/p' "
    "| sed 's/[[:space:]]*$//' | grep -v '^$'"
)
REPO_REF_PIPELINE = (
    "sed -n 's/.*--repo-ref[= ]\\{1,\\}\\([^ ]*\\).*/\\1/p'"
)
SOURCE_ENV = "MYCELIUM_DRIFT_REPLAY_SOURCE"
_CACHED_ROOT: Path | None = None


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_checkout(root: Path) -> None:
    if _git(root, "rev-parse", "HEAD") != PIN:
        raise RuntimeError(f"Mycelium replay source is not pinned at {PIN}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("Mycelium replay source must be a clean checkout")
    path = root / SOURCE_FILE
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned parser source is missing or a symlink: {path}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or path.read_bytes() != committed:
        raise RuntimeError("Mycelium parser source differs from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Mycelium parser source digest changed: {digest}")
    expected = b"sed -n 's/.*argv\\[\\]=\\([^;]*\\);.*/\\1/p'"
    if committed.count(expected) != 1:
        raise RuntimeError("pinned drift drill no longer has the adopted capture")


def source_root() -> Path:
    """Return a clean exact-pin source checkout, cloning it only if needed."""
    global _CACHED_ROOT
    configured = os.environ.get(SOURCE_ENV)
    if _CACHED_ROOT is not None:
        if configured and Path(configured).expanduser().resolve() != _CACHED_ROOT:
            raise RuntimeError(f"{SOURCE_ENV} changed during replay")
        return _CACHED_ROOT
    root = (
        Path(configured).expanduser().resolve()
        if configured
        else Path(tempfile.gettempdir()) / f"regexproof-pin-mycelium-{PIN}"
    )
    if not root.exists():
        root.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--no-checkout", REPOSITORY, str(root)],
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        subprocess.run(
            ["git", "-C", str(root), "checkout", "--detach", PIN],
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
    _verify_checkout(root)
    _CACHED_ROOT = root
    return root


def capture_execstart(raw: str, *, weakened: bool = False) -> str:
    """Run the pinned sed/grep capture (or a stated mutation) on one line."""
    if "\x00" in raw:
        raise ValueError("systemctl show text cannot be replayed with NUL")
    source_root()
    pipeline = WEAKENED_PIPELINE if weakened else CAPTURE_PIPELINE
    result = subprocess.run(
        ["bash", "-c", pipeline],
        input=raw + "\n",
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(
            f"pinned sed/grep replay exited {result.returncode}: {result.stderr.strip()}"
        )
    return result.stdout.rstrip("\n")


def capture_repo_ref(captured_execstart: str) -> str:
    """Run the pinned downstream --repo-ref capture on captured argv text."""
    source_root()
    result = subprocess.run(
        ["bash", "-c", REPO_REF_PIPELINE],
        input=captured_execstart + "\n",
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(f"pinned repo-ref replay exited {result.returncode}")
    return result.stdout.rstrip("\n")


def semicolon_drops_late_bypass(witness: dict) -> bool:
    """Verify an actual parser false negative against its semicolon-free control."""
    tail = witness.get("execstart_tail")
    if not isinstance(tail, str) or not tail:
        return False
    if ";" in tail or "\n" in tail or "\x00" in tail:
        return False
    if "--insecure-no-verify" not in tail or "--repo-ref v1" not in tail:
        return False
    raw = _semicolon_raw(tail)
    captured = capture_execstart(raw)
    control = capture_execstart(raw.replace("/etc/my;", "/etc/my", 1))
    return (
        "--insecure-no-verify" in raw
        and "--insecure-no-verify" not in captured
        and "--insecure-no-verify" in control
    )


def weakened_space_capture_drops_bypass(witness: dict) -> bool:
    """Check a weakened capture mutation against the original pinned pipeline."""
    tail = witness.get("execstart_tail")
    if not isinstance(tail, str) or not tail:
        return False
    if ";" in tail or "\n" in tail or "\x00" in tail:
        return False
    if "--insecure-no-verify" not in tail:
        return False
    raw = _plain_raw(tail)
    original = capture_execstart(raw)
    weakened = capture_execstart(raw, weakened=True)
    return "--insecure-no-verify" in original and "--insecure-no-verify" not in weakened


def _semicolon_raw(tail: str) -> str:
    return (
        "{ path=/usr/bin/printf ; argv[]=/usr/bin/printf %s\\n --update "
        "--allowed-signers /etc/my;"
        + tail
        + " ; ignore_errors=no ; start_time=[fixture] ; stop_time=[fixture] ; pid=1 ; code=exited ; status=0 }"
    )


def _plain_raw(tail: str) -> str:
    return (
        "{ path=/usr/bin/printf ; argv[]=/usr/bin/printf %s\\n --update "
        "--allowed-signers /etc/mycelium/allowed_signers "
        + tail
        + " ; ignore_errors=no ; start_time=[fixture] ; stop_time=[fixture] ; pid=1 ; code=exited ; status=0 }"
    )
