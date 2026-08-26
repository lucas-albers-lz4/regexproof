"""Wave 2 (#559): durable lease registry for the reference-clone cache.

A lease grants exclusive use of one cached clone to an owner (PID) for a
bounded TTL. Leases are DURABLE (persisted to ``cache/leases.json``, not
just memory) so a crash does not silently orphan a cache entry:

- ``acquire(url, pin, owner_pid, ttl_s)`` — atomically records the lease
  (flock-guarded); ``lease_reject`` when the entry is leased by a LIVE
  owner (start-time reaping clears dead owners first).
- ``reap_stale()`` — start-time reaping: leases whose start_time is older
  than the TTL (or whose owner PID is dead) are released. A live owner is
  one that still owns the lock file (PID alive + lock held), or whose
  lease has not yet expired.
- Two-phase probe→promote handoff: the probe phase holds a SHORT lease
  (``probe_ttl_s``); promotion to the durable cache re-acquires with a
  LONG TTL atomically (``promote()``), so a probe crash releases
  automatically while a promoted cache entry stays warm.
- Count + byte caps: ``acquire`` refuses (``lease_reject``) when the
  registry is at capacity and the entry is not already leased by the
  caller; ``purge --retain-go`` removes entries the batch GC no longer
  needs while keeping ``gated:go`` corpora.
"""

from __future__ import annotations

import fcntl
import json
import os
import pathlib
import time
from typing import Any

LEASES_PATH = pathlib.Path("cache/leases.json")
LOCK_PATH = pathlib.Path("cache/leases.json.lock")

DEFAULT_TTL_S = 3600
PROBE_TTL_S = 300  # two-phase handoff: probes hold short leases


def _now() -> float:
    return time.time()


def _read_registry(path: pathlib.Path | None = None) -> dict[str, Any]:
    p = pathlib.Path(path) if path is not None else LEASES_PATH
    if not p.is_file():
        return {"schema_version": "1", "leases": {}}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(
            f"lease_registry: corrupt registry {p}: {exc} — run "
            "`cache purge` or remove the file (fail-closed)"
        ) from exc


def _write_registry(reg: dict[str, Any], path: pathlib.Path | None = None) -> None:
    p = pathlib.Path(path) if path is not None else LEASES_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, p)


def _with_registry_lock(path: pathlib.Path | None, fn):
    """Exclusive flock on the dedicated never-renamed lock file — the same
    convention as corpus_lock (Wave C) and measure-p5-guarded. When a
    custom registry path is injected, the lock is derived as
    ``<registry>.lock`` (never the registry itself — that would create an
    empty file and corrupt reads). The DEFAULT lock path is used verbatim
    (Luna r1 #10: no double suffix)."""
    if path is not None:
        p = pathlib.Path(path)
        lock = p.with_name(p.name + ".lock")
    else:
        lock = LOCK_PATH  # already cache/leases.json.lock
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "a+", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        try:
            return fn()
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except PermissionError:
        return True  # exists but owned by another user — NOT dead (CodeRabbit #570)
    except (OSError, ProcessLookupError):
        return False
    return True


def _proc_start_ticks(pid: int) -> int | None:
    """Process start time from /proc/<pid>/stat field 22 (jiffies) — the
    anti-PID-reuse identity (#559 / Luna r1 #8: PID liveness alone lets a
    recycled PID inherit a stale lease)."""
    try:
        stat = pathlib.Path(f"/proc/{pid}/stat").read_text(encoding="utf-8")
    except OSError:
        return None
    try:
        # Comm may contain spaces/parens; take everything after the last ')'.
        return int(stat.rsplit(")", 1)[1].split()[19])
    except (ValueError, IndexError):
        return None


def _expired(lease: dict[str, Any], now: float) -> bool:
    start = float(lease.get("start_time") or 0)
    ttl = float(lease.get("ttl_s") or DEFAULT_TTL_S)
    if (now - start) > ttl:
        return True
    pid = int(lease.get("owner_pid") or -1)
    if not _pid_alive(pid):
        return True
    recorded = lease.get("owner_start_ticks")
    if recorded is not None:
        current = _proc_start_ticks(pid)
        if current is not None and int(recorded) != current:
            return True  # PID recycled — the lease belongs to a dead process
    return False


def _key(url: str, pin: str) -> str:
    return f"{url}#{pin}"


def reap_stale(*, now: float | None = None, path: pathlib.Path | None = None) -> int:
    """Start-time reaping: release leases that expired or whose owner died.
    Returns the number reaped. Runs under the registry lock."""

    def _reap() -> int:
        reg = _read_registry(path)
        n = 0
        for k in list(reg["leases"]):
            if _expired(reg["leases"][k], now if now is not None else _now()):
                del reg["leases"][k]
                n += 1
        if n:
            _write_registry(reg, path)
        return n

    return _with_registry_lock(path, _reap)


def acquire(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    ttl_s: float = DEFAULT_TTL_S,
    max_leases: int | None = None,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Acquire a lease on (url, pin). Returns the lease record. Raises
    SystemExit with ``lease_reject`` when at capacity or leased by a live
    owner."""

    def _acquire() -> dict[str, Any]:
        reg = _read_registry(path)
        k = _key(url, pin)
        now = _now()
        # Reap stale entries FIRST — a dead/expired lease must not consume
        # the cap and cause a false lease_reject (Luna r1 #7).
        for kk in list(reg["leases"]):
            if _expired(reg["leases"][kk], now):
                del reg["leases"][kk]
        existing = reg["leases"].get(k)
        if existing is not None and not _expired(existing, now):
            # Leased by a LIVE owner — reject unless it's the same owner
            # re-acquiring (idempotent).
            if int(existing.get("owner_pid") or -1) != owner_pid:
                raise SystemExit(
                    f"lease_registry: lease_reject — ({url}, {pin}) is leased "
                    f"by pid {existing.get('owner_pid')} until "
                    f"{existing.get('expires_at')}"
                )
            existing["ttl_s"] = ttl_s
            existing["expires_at"] = now + ttl_s
            existing["start_time"] = now
            existing["owner_start_ticks"] = _proc_start_ticks(owner_pid)
            _write_registry(reg, path)
            return existing
        if max_leases is not None and len(reg["leases"]) >= max_leases:
            raise SystemExit(
                f"lease_registry: lease_reject — registry at capacity "
                f"({max_leases}); purge or wait"
            )
        lease = {
            "url": url,
            "pin": pin,
            "owner_pid": owner_pid,
            "owner_start_ticks": _proc_start_ticks(owner_pid),
            "start_time": now,
            "ttl_s": ttl_s,
            "expires_at": now + ttl_s,
        }
        reg["leases"][k] = lease
        _write_registry(reg, path)
        return lease

    return _with_registry_lock(path, _acquire)


def promote(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    ttl_s: float = DEFAULT_TTL_S,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Two-phase probe→promote handoff: re-acquire the SAME key with a
    longer TTL atomically. The probe lease is replaced in one locked step —
    no window where the entry is unleased (Luna: handoff atomicity)."""

    def _promote() -> dict[str, Any]:
        reg = _read_registry(path)
        k = _key(url, pin)
        now = _now()
        existing = reg["leases"].get(k)
        # Promote requires a LIVE probe lease owned by the caller — creating
        # a lease from nothing, or promoting a dead/expired probe, would let
        # stale or missing data into the durable cache (Luna r1 #9 /
        # cache_miss_reprobe semantics).
        if existing is None or _expired(existing, now):
            raise SystemExit(
                f"lease_registry: lease_reject — cannot promote ({url}, {pin}): "
                "no live probe lease (cache_miss_reprobe)"
            )
        if int(existing.get("owner_pid") or -1) != owner_pid:
            raise SystemExit(
                f"lease_registry: lease_reject — cannot promote ({url}, {pin}): "
                f"leased by pid {existing.get('owner_pid')}"
            )
        lease = {
            "url": url,
            "pin": pin,
            "owner_pid": owner_pid,
            "owner_start_ticks": _proc_start_ticks(owner_pid),
            "start_time": now,
            "ttl_s": ttl_s,
            "expires_at": now + ttl_s,
        }
        reg["leases"][k] = lease
        _write_registry(reg, path)
        return lease

    return _with_registry_lock(path, _promote)


def release(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    path: pathlib.Path | None = None,
) -> bool:
    """Release the caller's lease (no-op when not leased by the caller)."""

    def _release() -> bool:
        reg = _read_registry(path)
        k = _key(url, pin)
        existing = reg["leases"].get(k)
        if existing is None:
            return False
        if int(existing.get("owner_pid") or -1) != owner_pid:
            return False
        del reg["leases"][k]
        _write_registry(reg, path)
        return True

    return _with_registry_lock(path, _release)


def purge(
    *,
    retain_go_corpora: set[str] | None = None,
    path: pathlib.Path | None = None,
) -> int:
    """Idempotent ``cache purge --retain-go``: drop all leases EXCEPT those
    whose URL names a corpus in ``retain_go_corpora`` (gated:go corpora the
    batch GC keeps warm). Returns the number purged."""

    def _purge() -> int:
        reg = _read_registry(path)
        keep = retain_go_corpora or set()
        n = 0
        for k in list(reg["leases"]):
            url = str(reg["leases"][k].get("url") or "")
            corpus = url.rstrip("/").rsplit("/", 1)[-1]
            if corpus not in keep:
                del reg["leases"][k]
                n += 1
        if n:
            _write_registry(reg, path)
        return n

    return _with_registry_lock(path, _purge)


def active_leases(*, path: pathlib.Path | None = None) -> list[dict[str, Any]]:
    return [
        {**v, "key": k}
        for k, v in _read_registry(path)["leases"].items()
        if not _expired(v, _now())
    ]


def run_under_lock(fn, *, path: pathlib.Path | None = None):
    """Run *fn* while holding the registry lock (Luna r2 #5: cache_gc's
    eviction sweep must be atomic against concurrent acquire/promote — a
    lease obtained between the snapshot and the rmtree would be evicted
    while live)."""
    return _with_registry_lock(path, fn)


def renew(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    ttl_s: float = DEFAULT_TTL_S,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Extend a lease's expiry (Luna r3 #5: a walk exceeding the original
    TTL must not be evicted mid-use). Refuses when the lease is gone,
    expired, or owned by someone else — fail closed."""

    def _renew() -> dict[str, Any]:
        reg = _read_registry(path)
        k = _key(url, pin)
        now = _now()
        existing = reg["leases"].get(k)
        if existing is None or _expired(existing, now):
            raise SystemExit(
                f"lease_registry: lease_reject — cannot renew ({url}, {pin}): "
                "no live lease"
            )
        if int(existing.get("owner_pid") or -1) != owner_pid:
            raise SystemExit(
                f"lease_registry: lease_reject — cannot renew ({url}, {pin}): "
                f"leased by pid {existing.get('owner_pid')}"
            )
        existing["ttl_s"] = ttl_s
        existing["expires_at"] = now + ttl_s
        existing["start_time"] = now
        ticks = _proc_start_ticks(owner_pid)
        if ticks is not None:
            existing["owner_start_ticks"] = ticks
        _write_registry(reg, path)
        return existing

    return _with_registry_lock(path, _renew)
