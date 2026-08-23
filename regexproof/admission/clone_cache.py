"""Wave 2 (#559): reference-clone cache keyed (url, pin).

Bare+blob:none reference clone per (url, pin) plus per-probe worktrees.
The cache is LEASE-CONTROLLED: a cached clone is only usable while its
lease is live (owner PID + TTL); the batch GC drops entries whose leases
expired or whose corpora are not ``gated:go`` (``purge --retain-go``).

Lifecycle
---------
1. ``cache_acquire(url, pin, ...)`` — if a leased cache entry exists for
   (url, pin), return it (cache HIT; ``bytes_saved`` accrues). Otherwise
   take a PROBE lease, clone bare+blob:none into the cache dir, then
   ``promote`` the lease to the durable TTL (two-phase handoff — a crash
   during the clone releases the short probe lease automatically).
2. ``worktree_for(url, pin)`` — create a throwaway worktree off the bare
   clone for the actual file walk (keeps the reference clone clean).
3. ``release`` / ``purge --retain-go`` / ``cache_gc`` — lease lifecycle.

Disk budget: ``--max-disk-mb`` unchanged (post-walk enforcement on the
worktree); NEW ``--probe-fetch-limit-mb`` bounds the bare clone itself;
``lifecycle_bytes = probe_fetch_bytes`` ONLY (no worktree/walk bytes).
"""

from __future__ import annotations

import pathlib
import shutil
from typing import Any

from regexproof.admission.clone import CloneError, RunFn, _default_run
from regexproof.mine import lease_registry

CACHE_ROOT = pathlib.Path("cache/reference_clones")
PROBE_FETCH_LIMIT_MB = 2048


def cache_dir(url: str, pin: str, root: pathlib.Path | None = None) -> pathlib.Path:
    base = pathlib.Path(root) if root is not None else CACHE_ROOT
    corpus = url.rstrip("/").rsplit("/", 1)[-1]
    return base / f"{corpus}__{pin[:16]}"


def cache_hit(url: str, pin: str, *, root: pathlib.Path | None = None) -> bool:
    d = cache_dir(url, pin, root)
    return d.is_dir() and (d / "refs").is_dir()


def cache_acquire(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    ttl_s: float = lease_registry.DEFAULT_TTL_S,
    max_disk_mb: int | None = PROBE_FETCH_LIMIT_MB,
    root: pathlib.Path | None = None,
    registry_path: pathlib.Path | None = None,
    run: RunFn | None = None,
) -> dict[str, Any]:
    """Return a leased cache entry: HIT when the reference clone exists and
    is leasable; otherwise clone bare+blob:none under a short probe lease
    and promote to the durable TTL (two-phase handoff). Raises SystemExit
    (``lease_reject``) when the entry is leased by a live owner."""
    run_fn = run or _default_run
    d = cache_dir(url, pin, root)
    if d.is_dir() and (d / "refs").is_dir():
        lease = lease_registry.acquire(
            url, pin, owner_pid=owner_pid, ttl_s=ttl_s,
            path=registry_path,
        )
        return {**lease, "cache_hit": True, "dir": str(d)}

    # Probe phase: short lease, then clone, then promote.
    lease_registry.acquire(
        url, pin, owner_pid=owner_pid,
        ttl_s=lease_registry.PROBE_TTL_S, path=registry_path,
    )
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)
    d.parent.mkdir(parents=True, exist_ok=True)
    argv = [
        "git", "clone", "--bare", "--filter=blob:none", url, str(d),
    ]
    proc = run_fn(argv)
    if proc.returncode != 0:
        lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)
        shutil.rmtree(d, ignore_errors=True)
        raise CloneError(
            f"git clone (bare, blob:none) failed ({proc.returncode}): "
            f"{proc.stderr or proc.stdout}"
        )
    # Fetch the pin explicitly — bare default-branch clones miss other SHAs.
    fetch = run_fn(["git", "-C", str(d), "fetch", "--filter=blob:none", "origin", pin])
    if fetch.returncode != 0:
        lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)
        shutil.rmtree(d, ignore_errors=True)
        raise CloneError(f"git fetch {pin} failed: {fetch.stderr or fetch.stdout}")
    if max_disk_mb is not None:
        size_mb = _dir_size_mb(d)
        if size_mb > max_disk_mb:
            lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)
            shutil.rmtree(d, ignore_errors=True)
            raise CloneError(
                f"probe fetch {size_mb:.1f} MB > --probe-fetch-limit-mb "
                f"{max_disk_mb} (disk_budget)"
            )
    lease = lease_registry.promote(
        url, pin, owner_pid=owner_pid, ttl_s=ttl_s, path=registry_path,
    )
    return {**lease, "cache_hit": False, "dir": str(d)}


def worktree_for(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    root: pathlib.Path | None = None,
    registry_path: pathlib.Path | None = None,
    run: RunFn | None = None,
) -> pathlib.Path:
    """Create a throwaway worktree off the bare reference clone for the
    walk. The worktree is per-probe and removed after the walk; the
    reference clone stays warm for the lease duration."""
    run_fn = run or _default_run
    d = cache_dir(url, pin, root)
    if not (d / "refs").is_dir():
        raise CloneError(f"cache miss: no reference clone for ({url}, {pin})")
    wt = d / f"worktree-{owner_pid}"
    if wt.exists():
        shutil.rmtree(wt, ignore_errors=True)
    proc = run_fn(["git", "-C", str(d), "worktree", "add", "--detach", str(wt), pin])
    if proc.returncode != 0:
        raise CloneError(f"worktree add failed: {proc.stderr or proc.stdout}")
    return wt


def release(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    registry_path: pathlib.Path | None = None,
) -> bool:
    return lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)


def cache_gc(
    *,
    retain_go_corpora: set[str] | None = None,
    root: pathlib.Path | None = None,
    registry_path: pathlib.Path | None = None,
) -> int:
    """Batch-start GC: drop leases not in the retain set AND remove their
    reference clones. Returns the number of cache dirs removed."""
    lease_registry.purge(
        retain_go_corpora=retain_go_corpora, path=registry_path,
    )
    base = pathlib.Path(root) if root is not None else CACHE_ROOT
    removed = 0
    if not base.is_dir():
        return 0
    for d in base.iterdir():
        if not d.is_dir():
            continue
        # Retain corpora keep their clone warm.
        corpus = d.name.split("__")[0]
        if retain_go_corpora and corpus in retain_go_corpora:
            continue
        shutil.rmtree(d, ignore_errors=True)
        removed += 1
    return removed


def _dir_size_mb(path: pathlib.Path) -> float:
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total / (1024 * 1024)
