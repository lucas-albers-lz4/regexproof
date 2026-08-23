"""Wave 2 (#559): batch probe state — `batch/state.json`.

Immutable manifest digest keyed ``(manifest_digest, url, pin)``. The state
file is NON-gitignored (a durable record of what was probed). Every row
records its outcome; prior-digest rows are RETAINED (never pruned) so the
escape projection can compare admission across manifest versions.

Integrity
---------
- Atomic writes: temp file + ``os.replace`` (a crash mid-write can never
  truncate the state).
- fsync before replace.
- Checksum: the state file carries ``sha256`` of its own canonical JSON;
  ``load_state`` verifies it and falls back to ``.bak`` when corrupt
  (loud fallback — never silent).
- Dedicated never-renamed lock file ``batch/state.json.lock`` (flock),
  matching the repo convention (corpus_lock / lease_registry).
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import pathlib
import sys
from typing import Any

STATE_PATH = pathlib.Path("batch/state.json")
LOCK_PATH = pathlib.Path("batch/state.json.lock")
BACKUP_PATH = pathlib.Path("batch/state.json.bak")

OUTCOMES = frozenset(
    {
        "ok",
        "clone_timeout",
        "disk_budget",
        "lease_reject",
        "cache_miss_reprobe",
        "skip_wave_active",
    }
)


def _canonical(reg: dict[str, Any]) -> str:
    return json.dumps(reg, indent=2, sort_keys=True) + "\n"


def _checksum_of(reg: dict[str, Any]) -> str:
    """SHA-256 over the canonical body WITHOUT the sha256 field — the field
    cannot checksum itself (chicken-and-egg)."""
    body = {k: v for k, v in reg.items() if k != "sha256"}
    return hashlib.sha256(_canonical(body).encode("utf-8")).hexdigest()


def _verify(text: str) -> dict[str, Any]:
    reg = json.loads(text)
    if _checksum_of(reg) != reg.get("sha256"):
        raise ValueError("checksum mismatch")
    return reg


def _with_state_lock(path: pathlib.Path | None, fn):
    """Exclusive flock on the dedicated never-renamed lock file. With an
    injected state path, the lock is derived as ``<state>.lock`` — never
    the state file itself (an a+ open would create an empty file and
    corrupt reads)."""
    p = pathlib.Path(path) if path is not None else LOCK_PATH
    lock = p.with_name(p.name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "a+", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        try:
            return fn()
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def load_state(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Load + verify the state checksum. On corruption, fall back to .bak
    (loud: prints a warning). Raises SystemExit if both are unreadable."""
    p = pathlib.Path(path) if path is not None else STATE_PATH
    if not p.is_file():
        return {"schema_version": "1", "manifest_digests": {}, "rows": []}
    text = p.read_text(encoding="utf-8")
    try:
        return _verify(text)
    except (ValueError, json.JSONDecodeError) as exc:
        bak = p.with_suffix(".json.bak")
        if bak.is_file():
            print(f"batch_state: WARNING {p} corrupt ({exc}); trying .bak", file=sys.stderr)
            try:
                return _verify(bak.read_text(encoding="utf-8"))
            except (ValueError, json.JSONDecodeError) as exc2:
                raise SystemExit(
                    f"batch_state: {p} AND .bak corrupt ({exc2}) — fail closed"
                ) from exc2
        raise SystemExit(
            f"batch_state: {p} corrupt ({exc}) and no .bak — fail closed"
        ) from exc


def record_outcome(
    manifest_digest: str,
    url: str,
    pin: str,
    outcome: str,
    *,
    extra: dict[str, Any] | None = None,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Append one probe outcome row under the state lock. Prior-digest rows
    are retained. Returns the updated registry."""
    if outcome not in OUTCOMES:
        raise SystemExit(f"batch_state: unknown outcome {outcome!r}")

    def _record() -> dict[str, Any]:
        reg = load_state(path)
        row = {
            "manifest_digest": manifest_digest,
            "url": url,
            "pin": pin,
            "outcome": outcome,
            **(extra or {}),
        }
        reg.setdefault("rows", []).append(row)
        reg.setdefault("manifest_digests", {})[manifest_digest] = reg.get(
            "manifest_digests", {}
        ).get(manifest_digest, {"count": 0, "first_seen": row.get("at", "")})
        # Recompute the digest map count from the rows (single source).
        counts: dict[str, int] = {}
        for r in reg["rows"]:
            counts[r["manifest_digest"]] = counts.get(r["manifest_digest"], 0) + 1
        reg["manifest_digests"] = {
            d: {"count": counts[d]} for d in counts
        }
        _write(reg, path)
        return reg

    return _with_state_lock(path, _record)


def _write(reg: dict[str, Any], path: pathlib.Path | None = None) -> None:
    p = pathlib.Path(path) if path is not None else STATE_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    reg["sha256"] = _checksum_of(reg)
    text = _canonical(reg)
    tmp = p.with_suffix(".json.tmp")
    fd = os.open(str(tmp), os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    try:
        os.write(fd, text.encode("utf-8"))
        os.fsync(fd)
    finally:
        os.close(fd)
    # Keep a .bak of the previous good state for recovery.
    if p.is_file():
        try:
            os.replace(p, p.with_suffix(".json.bak"))
        except OSError:
            pass
    os.replace(tmp, p)


def projection(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Batch summary projections from state.json: cache_hits, cache_misses,
    bytes_saved, lifecycle_bytes (probe_fetch only), clone_ms p50/p95, and
    the survivor rate for the escape clause."""
    reg = load_state(path)
    rows = reg["rows"]
    hits = [r for r in rows if r.get("cache_hit")]
    misses = [r for r in rows if not r.get("cache_hit")]
    bytes_saved = sum(int(r.get("bytes_saved") or 0) for r in rows)
    lifecycle = sum(int(r.get("lifecycle_bytes") or 0) for r in rows)
    clone_ms = sorted(int(r.get("clone_ms") or 0) for r in rows if r.get("clone_ms"))
    p50 = clone_ms[(len(clone_ms) - 1) // 2] if clone_ms else None
    p95 = clone_ms[min(len(clone_ms) - 1, int(len(clone_ms) * 0.95))] if clone_ms else None
    ok = [r for r in rows if r.get("outcome") == "ok"]
    return {
        "rows": len(rows),
        "cache_hits": len(hits),
        "cache_misses": len(misses),
        "bytes_saved": bytes_saved,
        "lifecycle_bytes": lifecycle,
        "clone_ms_p50": p50,
        "clone_ms_p95": p95,
        "survivor_rate": (len(ok) / len(rows)) if rows else None,
    }
