"""Candidate ledger v1 — atomic load/save (umbrella C1 / P2 B0)."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Callable

LEDGER_SCHEMA_VERSION = "1"

CANDIDATE_FIELDS = (
    "url",
    "default_branch",
    "pin",
    "pushed_date",
    "stars",
    "source_query",
    "first_seen",
    "status",
)

# Injectable crash hook for mid-write tests: called after temp write, before replace.
_crash_before_replace: Callable[[], None] | None = None


def set_crash_before_replace(hook: Callable[[], None] | None) -> None:
    """Test seam: raise from *hook* to simulate crash between write and rename."""
    global _crash_before_replace
    _crash_before_replace = hook


def empty_ledger() -> dict[str, Any]:
    return {"schema_version": LEDGER_SCHEMA_VERSION, "candidates": []}


def load_ledger(path: Path | str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return empty_ledger()
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("schema_version") != LEDGER_SCHEMA_VERSION:
        raise ValueError(
            f"unsupported ledger schema_version {data.get('schema_version')!r}; "
            f"expected {LEDGER_SCHEMA_VERSION!r}"
        )
    if "candidates" not in data or not isinstance(data["candidates"], list):
        raise ValueError("ledger missing candidates list")
    return data


def save_ledger(path: Path | str, ledger: dict[str, Any]) -> None:
    """Atomic write: temp file in same directory + os.replace."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(ledger, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix=f".{p.name}.", suffix=".tmp", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        if _crash_before_replace is not None:
            _crash_before_replace()
        os.replace(tmp_name, p)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def find_candidate(ledger: dict[str, Any], url: str) -> dict[str, Any] | None:
    for c in ledger["candidates"]:
        if c.get("url") == url:
            return c
    return None
