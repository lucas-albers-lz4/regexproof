"""Atomic file writes (temp + fsync + os.replace) for generated artifacts."""

from __future__ import annotations

import os
import tempfile
from collections.abc import Callable, Iterable
from pathlib import Path


def atomic_write_text(
    path: Path | str,
    text: str,
    *,
    encoding: str = "utf-8",
    crash_before_replace: Callable[[], None] | None = None,
) -> None:
    """Write *text* to *path* atomically (same-dir temp file + ``os.replace``).

    *crash_before_replace* is a test seam: called after the temp write is
    flushed/fsynced and before rename. Raise from it to simulate a mid-write
    crash leaving the prior file intact.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{p.name}.", suffix=".tmp", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        if crash_before_replace is not None:
            crash_before_replace()
        os.replace(tmp_name, p)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def atomic_write_lines(
    path: Path | str,
    lines: Iterable[str],
    *,
    encoding: str = "utf-8",
    crash_before_replace: Callable[[], None] | None = None,
) -> None:
    """Atomically write newline-terminated *lines* (appends ``\\n`` if missing)."""
    parts: list[str] = []
    for line in lines:
        parts.append(line if line.endswith("\n") else line + "\n")
    atomic_write_text(
        path,
        "".join(parts),
        encoding=encoding,
        crash_before_replace=crash_before_replace,
    )
