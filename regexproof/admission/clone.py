"""Partial-clone helper for admission probing (P1 A6)."""

from __future__ import annotations

import os
import shutil
import subprocess
from collections.abc import Callable, Sequence
from pathlib import Path

# Injectable runner for tests: (argv, kwargs) -> CompletedProcess-like
RunFn = Callable[..., subprocess.CompletedProcess[str]]


class CloneError(RuntimeError):
    """Probe clone failed."""


def _default_run(argv: Sequence[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(argv),
        check=False,
        text=True,
        capture_output=True,
        **kwargs,  # type: ignore[arg-type]
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
    """
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
        total = 0
        for dirpath, _dirnames, filenames in os.walk(dest):
            for fn in filenames:
                fp = Path(dirpath) / fn
                try:
                    total += fp.stat().st_size
                except OSError:
                    continue
        if total > max_disk_mb * 1024 * 1024:
            shutil.rmtree(dest, ignore_errors=True)
            raise CloneError(
                f"clone exceeds max_disk_mb={max_disk_mb} ({total} bytes)"
            )

    return resolved


def cleanup_clone(path: Path | str) -> None:
    p = Path(path)
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)
