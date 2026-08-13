"""Candidate ledger v1 — atomic load/save (umbrella C1 / P2 B0).

Rows written by the mine may carry additive repository metadata.  The loader
intentionally does not require those fields so ledgers produced before the
metadata enrichment remain valid.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from regexproof.io_atomic import atomic_write_text

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

# Optional fields populated by the GitHub repository enrichment call.  Keep
# this separate from CANDIDATE_FIELDS: old rows are valid without them.
ENRICH_FIELDS = ("fork", "size", "language", "archived")
OPTIONAL_CANDIDATE_FIELDS = (*ENRICH_FIELDS, "pin_probed")

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
    text = json.dumps(ledger, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(path, text, crash_before_replace=_crash_before_replace)


def find_candidate(ledger: dict[str, Any], url: str) -> dict[str, Any] | None:
    from regexproof.mine.exclusions import normalize_repo_url

    target = normalize_repo_url(url)
    for c in ledger["candidates"]:
        cand_url = c.get("url")
        if cand_url and normalize_repo_url(str(cand_url)) == target:
            return c
    return None
