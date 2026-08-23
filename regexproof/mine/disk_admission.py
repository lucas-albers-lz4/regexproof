"""Wave 2 (#559): disk-admission semaphore for the batch probe.

Shared across workers via the state lock: each clone reserves a FIXED
``per_clone_cap_mb`` slot; the semaphore admits only while the total
reserved stays under ``--max-disk-mb``. W=0 fails closed (no workers →
no admission). Reservations are RELEASED on failure (clone error, timeout,
budget) so a dead probe cannot hold the budget hostage.

State is persisted in the registry file (durable across crashes); stale
reservations are reaped by owner PID liveness like leases.
"""

from __future__ import annotations

import json
import os
import pathlib
from typing import Any, Optional

ADMISSION_PATH = pathlib.Path("cache/admission.json")


def _proc_start_ticks(pid: int) -> Optional[int]:
    """Process start time from /proc/<pid>/stat field 22 (jiffies) — the
    anti-PID-reuse identity (same as lease_registry)."""
    try:
        stat = pathlib.Path(f"/proc/{pid}/stat").read_text(encoding="utf-8")
    except OSError:
        return None
    try:
        return int(stat.rsplit(")", 1)[1].split()[19])
    except (ValueError, IndexError):
        return None


def _read(path: Optional[pathlib.Path]) -> dict[str, Any]:
    p = pathlib.Path(path) if path is not None else ADMISSION_PATH
    if not p.is_file():
        return {"schema_version": "1", "reservations": {}}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(
            f"disk_admission: corrupt reservation file {p}: {exc} — fail closed"
        ) from exc


def reserve(
    *,
    worker_count: int,
    per_clone_cap_mb: int,
    max_disk_mb: int,
    owner_pid: int,
    path: Optional[pathlib.Path] = None,
) -> bool:
    """Reserve one per-clone slot. W=0 → fail closed (False). Returns False
    (no admission) when reservations + cap exceed max_disk_mb."""
    if worker_count <= 0:
        return False  # W=0 fail-closed (Luna r1 #4)
    p = pathlib.Path(path) if path is not None else ADMISSION_PATH
    lock = p.with_name(p.name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "a+", encoding="utf-8") as fh:
        import fcntl

        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        reg = _read(path)
        # Reap reservations whose owner died (like lease reaping). PID
        # liveness + start-ticks (Luna r2 #9: kill(pid,0) alone lets a
        # recycled PID inherit a stale reservation).
        live = {}
        for k, v in reg["reservations"].items():
            pid = int(v.get("owner_pid") or -1)
            try:
                os.kill(pid, 0)
            except PermissionError:
                live[k] = v  # alive but foreign-owned
                continue
            except (OSError, ProcessLookupError):
                continue  # dead owner — reservation released
            recorded = v.get("owner_start_ticks")
            current = _proc_start_ticks(pid)
            if recorded is not None and current is not None and int(recorded) != current:
                continue  # PID recycled
            live[k] = v
        reg["reservations"] = live
        # Worker limit FIRST (CodeRabbit #570): with worker_count=2, three
        # live owners must not all hold slots even when the byte budget
        # permits — the semaphore is a CONCURRENCY cap as well as a byte cap.
        if len(live) >= worker_count:
            return False
        used = sum(int(v.get("reserved_mb") or 0) for v in live.values())
        if used + per_clone_cap_mb > max_disk_mb:
            return False
        reg["reservations"][str(owner_pid)] = {
            "owner_pid": owner_pid,
            "owner_start_ticks": _proc_start_ticks(owner_pid),
            "reserved_mb": per_clone_cap_mb,
        }
        tmp = p.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, p)
        return True


def release(*, owner_pid: int, path: Optional[pathlib.Path] = None) -> None:
    p = pathlib.Path(path) if path is not None else ADMISSION_PATH
    lock = p.with_name(p.name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "a+", encoding="utf-8") as fh:
        import fcntl

        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        reg = _read(path)
        reg["reservations"].pop(str(owner_pid), None)
        tmp = p.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, p)
