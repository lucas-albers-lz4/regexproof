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
- Checksum: the state file carries ``sha256`` of its own canonical JSON
  (computed over the canonical body with the ``sha256`` field excluded —
  it cannot checksum itself). SCOPE: the checksum covers the STRUCTURAL
  content (parsed + re-serialized canonical form), so data mutations and
  re-orderings trip it; byte-level whitespace/padding changes that decode
  to the same structure are intentionally tolerated (CodeRabbit #570).
  ``load_state`` verifies and falls back to ``.bak`` when corrupt (loud
  fallback — never silent).
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
        "auto_nogo",       # Luna r1 #13: complete #559 vocabulary
        "needs_human",
        "rate_limited",
        "error",
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
    return _migrate(reg)


def _migrate(reg: dict[str, Any]) -> dict[str, Any]:
    """Schema migration (Luna r2 #7): v1 rows were a LIST; v2 is keyed by
    (digest,url,pin). An existing valid v1 file must resume, not crash."""
    if isinstance(reg.get("rows"), list):
        reg["schema_version"] = "2"
        keyed: dict[str, dict[str, Any]] = {}
        for r in reg["rows"]:
            keyed[_row_key(r.get("manifest_digest", ""), r.get("url", ""), r.get("pin", ""))] = r
        reg["rows"] = keyed
        _rebuild_counts(reg)
    return reg


def _with_state_lock(path: pathlib.Path | None, fn):
    """Exclusive flock on the dedicated never-renamed lock file. With an
    injected state path, the lock is derived as ``<state>.lock`` — never
    the state file itself (an a+ open would create an empty file and
    corrupt reads). The DEFAULT lock path is used verbatim (Luna r1 #10:
    no double suffix)."""
    if path is not None:
        p = pathlib.Path(path)
        lock = p.with_name(p.name + ".lock")
    else:
        lock = LOCK_PATH  # already batch/state.json.lock
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
        return {"schema_version": "1", "manifest_digests": {}, "rows": {}}
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


def _row_key(manifest_digest: str, url: str, pin: str) -> str:
    return f"{manifest_digest}#{url}#{pin}"


def begin_item(
    manifest_digest: str,
    url: str,
    pin: str,
    *,
    at: str = "",
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Start a probe item (Luna r1 #11: keyed + resumable — an incomplete
    item has started_at but no completed_at and is re-run on resume)."""
    import datetime as _dt

    at = at or _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")

    def _begin() -> dict[str, Any]:
        reg = load_state(path)
        k = _row_key(manifest_digest, url, pin)
        row = {
            "key": k,
            "manifest_digest": manifest_digest,
            "url": url,
            "pin": pin,
            "started_at": at,
            "completed_at": "",
            "outcome": "",
        }
        reg["rows"][k] = row  # keyed: no duplicates, resume-safe
        reg["manifest_digests"].setdefault(manifest_digest, {"count": 0})
        _rebuild_counts(reg)
        _write(reg, path)
        return row

    return _with_state_lock(path, _begin)


def record_outcome(
    manifest_digest: str,
    url: str,
    pin: str,
    outcome: str,
    *,
    extra: dict[str, Any] | None = None,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Complete a probe item with an outcome (keyed upsert — no duplicate
    rows; prior-digest rows retained via the key namespace)."""
    if outcome not in OUTCOMES:
        raise SystemExit(f"batch_state: unknown outcome {outcome!r}")
    import datetime as _dt

    at = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")

    def _record() -> dict[str, Any]:
        reg = load_state(path)
        k = _row_key(manifest_digest, url, pin)
        prev = reg["rows"].get(k, {})
        row = {
            "key": k,
            "manifest_digest": manifest_digest,
            "url": url,
            "pin": pin,
            "started_at": prev.get("started_at", at),
            "completed_at": at,
            "outcome": outcome,
            **(extra or {}),
        }
        reg["rows"][k] = row
        reg.setdefault("manifest_digests", {}).setdefault(manifest_digest, {})
        _rebuild_counts(reg)
        _write(reg, path)
        return row

    return _with_state_lock(path, _record)


def _rebuild_counts(reg: dict[str, Any]) -> None:
    counts: dict[str, int] = {}
    for r in reg["rows"].values():
        counts[r["manifest_digest"]] = counts.get(r["manifest_digest"], 0) + 1
    reg["manifest_digests"] = {d: {"count": counts[d]} for d in counts}


def _write(reg: dict[str, Any], path: pathlib.Path | None = None) -> None:
    """Crash-safe install (Luna r1 #12): write temp, fsync, then atomically
    replace the state. The PREVIOUS verified state becomes .bak only after
    the new state is installed — a crash mid-write leaves the old state
    intact (never a window with no state file), and a good .bak is never
    overwritten by a corrupt current file."""
    p = pathlib.Path(path) if path is not None else STATE_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    reg["sha256"] = _checksum_of(reg)
    text = _canonical(reg)
    tmp = p.with_suffix(".json.tmp")
    fd = os.open(str(tmp), os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
    try:
        os.write(fd, text.encode("utf-8"))
        os.fsync(fd)
    finally:
        os.close(fd)
    # Verify the new temp BEFORE installing (write-then-verify-then-rename).
    _verify(tmp.read_text(encoding="utf-8"))
    # Rotate the current verified state to .bak — via temp + os.replace so
    # the backup install is ATOMIC (copy2 directly onto the live .bak can
    # truncate it on a crash mid-copy; CodeRabbit #570 heavy-lift). The
    # temp backup is fsynced BEFORE the atomic replace, and a disk-full or
    # backup failure BLOCKS the install (never install the new state over
    # a broken backup chain). Only when the current file verifies.
    if p.is_file():
        try:
            _verify(p.read_text(encoding="utf-8"))
            bak_tmp = p.with_suffix(".json.bak.tmp")
            fd = os.open(str(bak_tmp), os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
            try:
                os.write(fd, p.read_bytes())
                os.fsync(fd)
            finally:
                os.close(fd)
            os.replace(bak_tmp, p.with_suffix(".json.bak"))
        except (ValueError, json.JSONDecodeError, OSError):
            # Corrupt current OR backup failure: keep the existing .bak and
            # DO NOT install the new state (disk-full must not proceed).
            raise SystemExit(
                f"batch_state: cannot rotate verified backup for {p.name} — "
                "state install aborted (fail closed)"
            )
    os.replace(tmp, p)
    # fsync the parent directory so the primary install is durable across a
    # crash (CodeRabbit #570 heavy-lift).
    try:
        dfd = os.open(str(p.parent), os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    except OSError:
        pass  # dir-fsync is best-effort on some filesystems


def projection(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Batch summary projections from state.json: cache_hits, cache_misses,
    bytes_saved, lifecycle_bytes (probe_fetch only), clone_ms p50/p95, and
    the survivor rate for the escape clause."""
    reg = load_state(path)
    rows = list(reg["rows"].values()) if isinstance(reg.get("rows"), dict) else reg.get("rows", [])
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
