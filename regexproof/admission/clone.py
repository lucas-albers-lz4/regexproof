"""Partial-clone helper for admission probing (P1 A6)."""

from __future__ import annotations

import os
import shutil
import subprocess
from collections.abc import Callable, Sequence
from pathlib import Path
from urllib.parse import urlparse

# Injectable runner for tests: (argv, kwargs) -> CompletedProcess-like
RunFn = Callable[..., subprocess.CompletedProcess[str]]

_ALLOWED_CLONE_HOSTS = frozenset({"github.com", "www.github.com"})
_DEFAULT_CLONE_TIMEOUT_SEC = 300


class CloneError(RuntimeError):
    """Probe clone failed."""


def validate_clone_url(url: str) -> None:
    """Reject non-https / non-GitHub / credential-bearing clone URLs."""
    parsed = urlparse(url)
    scheme = (parsed.scheme or "").lower()
    if scheme != "https":
        raise CloneError(
            f"clone URL must use https scheme, got {scheme!r} (url={url!r})"
        )
    if parsed.username is not None or parsed.password is not None:
        raise CloneError(f"clone URL must not contain userinfo (url={url!r})")
    host = (parsed.hostname or "").lower()
    if host not in _ALLOWED_CLONE_HOSTS:
        raise CloneError(
            f"clone URL host not allowlisted: {host!r} "
            f"(allowed: {sorted(_ALLOWED_CLONE_HOSTS)}; url={url!r})"
        )


def _default_run(argv: Sequence[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    kwargs.setdefault("timeout", _DEFAULT_CLONE_TIMEOUT_SEC)
    return subprocess.run(
        list(argv),
        check=False,
        text=True,
        capture_output=True,
        **kwargs,  # type: ignore[arg-type]
    )


def dir_size_bytes(path: Path | str) -> int:
    """Sum on-disk file sizes under *path* (follows materialized blobs)."""
    total = 0
    root = Path(path)
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            fp = Path(dirpath) / fn
            try:
                total += fp.stat().st_size
            except OSError:
                continue
    return total


def enforce_disk_budget(path: Path | str, max_disk_mb: int) -> None:
    """Raise CloneError if *path* exceeds *max_disk_mb* (call after blob materialization)."""
    total = dir_size_bytes(path)
    if total > max_disk_mb * 1024 * 1024:
        raise CloneError(
            f"clone exceeds max_disk_mb={max_disk_mb} ({total} bytes)"
        )


def partial_clone(
    url: str,
    *,
    dest: Path,
    pin: str | None = None,
    max_disk_mb: int | None = 500,
    run: RunFn | None = None,
) -> str:
    """Clone *url* with ``--filter=blob:none`` into *dest*; return resolved pin.

    *dest* must not live under ``batch/corpora/``. Cleanup is the caller's
    responsibility (see :func:`cleanup_clone`).

    Note: with ``blob:none``, the on-disk check here only sees tree metadata.
    Callers that walk/read files should re-check via :func:`enforce_disk_budget`
    after materialization.
    """
    validate_clone_url(url)
    run_fn = run or _default_run
    dest = Path(dest)
    parts = dest.resolve().parts
    if any(
        parts[i] == "batch" and parts[i + 1] == "corpora"
        for i in range(len(parts) - 1)
    ):
        raise CloneError("probe clones must not land under batch/corpora/")

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)

    argv = [
        "git",
        "clone",
        "--filter=blob:none",
        url,
        str(dest),
    ]
    proc = run_fn(argv)
    if proc.returncode != 0:
        raise CloneError(
            f"git clone failed ({proc.returncode}): {proc.stderr or proc.stdout}"
        )

    if pin:
        # Fetch the pin explicitly — default-branch-only clones miss other SHAs.
        fetch = run_fn(
            ["git", "-C", str(dest), "fetch", "--filter=blob:none", "origin", pin]
        )
        if fetch.returncode != 0:
            raise CloneError(
                f"git fetch {pin} failed: {fetch.stderr or fetch.stdout}"
            )
        co = run_fn(["git", "-C", str(dest), "checkout", "--detach", pin])
        if co.returncode != 0:
            raise CloneError(f"git checkout {pin} failed: {co.stderr or co.stdout}")
        resolved = pin
    else:
        rev = run_fn(["git", "-C", str(dest), "rev-parse", "HEAD"])
        if rev.returncode != 0:
            raise CloneError(f"rev-parse failed: {rev.stderr or rev.stdout}")
        resolved = (rev.stdout or "").strip()

    if max_disk_mb is not None:
        # Pre-walk soft check (often undercounts with blob:none).
        try:
            enforce_disk_budget(dest, max_disk_mb)
        except CloneError:
            shutil.rmtree(dest, ignore_errors=True)
            raise

    return resolved


def cleanup_clone(path: Path | str) -> None:
    p = Path(path)
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)
