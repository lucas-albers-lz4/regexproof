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
from typing import Any

ADMISSION_PATH = pathlib.Path("cache/admission.json")


def _read(path: pathlib.Path | None) -> dict[str, Any]:
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
    path: pathlib.Path | None = None,
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
        # Reap reservations whose owner died (like lease reaping).
        live = {}
        for k, v in reg["reservations"].items():
            try:
                os.kill(int(v.get("owner_pid") or -1), 0)
                live[k] = v
            except (OSError, ProcessLookupError):
                pass  # dead owner — reservation released
        reg["reservations"] = live
        used = sum(int(v.get("reserved_mb") or 0) for v in live.values())
        if used + per_clone_cap_mb > max_disk_mb:
            return False
        reg["reservations"][str(owner_pid)] = {
            "owner_pid": owner_pid,
            "reserved_mb": per_clone_cap_mb,
        }
        tmp = p.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, p)
        return True


def release(*, owner_pid: int, path: pathlib.Path | None = None) -> None:
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
