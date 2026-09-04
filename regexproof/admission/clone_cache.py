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
import subprocess
from typing import Any

from regexproof.admission.clone import CloneError, RunFn, _default_run
from regexproof.mine import lease_registry

CACHE_ROOT = pathlib.Path("cache/reference_clones")
PROBE_FETCH_LIMIT_MB = 2048


def cache_dir(url: str, pin: str, root: pathlib.Path | None = None) -> pathlib.Path:
    """Cache dir keyed by a FULL (url, pin) content hash — the URL basename
    + pin prefix can collide across repos (Luna r1 #5)."""
    import hashlib

    base = pathlib.Path(root) if root is not None else CACHE_ROOT
    key = hashlib.sha256(f"{url}#{pin}".encode("utf-8")).hexdigest()
    return base / key[:32]


def cache_hit(url: str, pin: str, *, root: pathlib.Path | None = None) -> bool:
    d = cache_dir(url, pin, root)
    # .cache-key is the completeness marker (written only after the pin
    # fetch succeeds) — a partial dir is never a hit (Luna r2 #3). Must
    # agree with cache_acquire's hit decision.
    return d.is_dir() and (d / "refs").is_dir() and (d / ".cache-key").is_file()


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
    from regexproof.admission.clone import validate_clone_url

    validate_clone_url(url)  # Luna r2 #6: same control as admission/clone.py
    run_fn = run or _default_run
    d = cache_dir(url, pin, root)
    # Acquire FIRST, then verify the dir — closing the GC/acquire TOCTOU
    # (Luna r3 #4): a lease taken before the dir check means GC (which
    # holds the registry lock and never evicts leased dirs) cannot remove
    # it between the check and the hit return.
    lease_registry.acquire(
        url, pin, owner_pid=owner_pid,
        ttl_s=lease_registry.PROBE_TTL_S, path=registry_path,
    )
    if d.is_dir() and (d / "refs").is_dir() and (d / ".cache-key").is_file():
        # Complete reference clone: promote the probe lease to the durable
        # TTL and report a HIT.
        lease = lease_registry.promote(
            url, pin, owner_pid=owner_pid, ttl_s=ttl_s, path=registry_path,
        )
        return {**lease, "cache_hit": True, "dir": str(d)}
    # Miss: clone under the (already-held) probe lease, then promote.
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)
    d.parent.mkdir(parents=True, exist_ok=True)
    try:
        argv = [
            "git", "clone", "--bare", "--filter=blob:none", url, str(d),
        ]
        proc = run_fn(argv)
        if proc.returncode != 0:
            raise CloneError(
                f"git clone (bare, blob:none) failed ({proc.returncode}): "
                f"{proc.stderr or proc.stdout}"
            )
        # Fetch the pin explicitly — bare default-branch clones miss other SHAs.
        fetch = run_fn(["git", "-C", str(d), "fetch", "--filter=blob:none", "origin", pin])
        if fetch.returncode != 0:
            raise CloneError(f"git fetch {pin} failed: {fetch.stderr or fetch.stdout}")
    except (CloneError, subprocess.TimeoutExpired):
        # Timeout/failure must release the probe lease AND remove the
        # partial cache — never leave either behind (Luna r2 #3).
        lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)
        shutil.rmtree(d, ignore_errors=True)
        raise
    # Sidecar key maps the hashed dir back to (url, pin) for safe GC. It is
    # the COMPLETENESS marker — written only after the pin fetch succeeds.
    # Marker-write/disk-check failures MUST release the probe lease too
    # (Luna r3 #3: IsADirectoryError reproduced with the lease still
    # installed).
    try:
        (d / ".cache-key").write_text(f"{url}#{pin}", encoding="utf-8")
        if max_disk_mb is not None:
            size_mb = _dir_size_mb(d)
            if size_mb > max_disk_mb:
                raise CloneError(
                    f"probe fetch {size_mb:.1f} MB > --probe-fetch-limit-mb "
                    f"{max_disk_mb} (disk_budget)"
                )
    except (CloneError, OSError):
        lease_registry.release(url, pin, owner_pid=owner_pid, path=registry_path)
        shutil.rmtree(d, ignore_errors=True)
        raise
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
    # Resolve absolute paths before `git -C <bare> worktree add <path>`.
    # A relative --cache-root makes `git` interpret the worktree path relative
    # to the bare clone, nesting the checkout and leaving the returned path
    # empty (files_walked=0 → false auto-NO-GO).
    d = cache_dir(url, pin, root).resolve()
    if not (d / "refs").is_dir():
        raise CloneError(f"cache miss: no reference clone for ({url}, {pin})")
    wt = (d / f"worktree-{owner_pid}").resolve()
    if wt.exists():
        # Remove a stale worktree THROUGH GIT (Luna r2 #10: rmtree leaves
        # linked-worktree metadata behind if the subsequent add fails).
        run_fn(["git", "-C", str(d), "worktree", "remove", "--force", str(wt)])
        if wt.exists():
            shutil.rmtree(wt, ignore_errors=True)
    proc = run_fn(["git", "-C", str(d), "worktree", "add", "--detach", str(wt), pin])
    if proc.returncode != 0:
        raise CloneError(f"worktree add failed: {proc.stderr or proc.stdout}")
    return wt


def worktree_remove(
    url: str,
    pin: str,
    *,
    owner_pid: int,
    root: pathlib.Path | None = None,
    run: RunFn | None = None,
) -> None:
    """Remove a probe worktree THROUGH GIT (``git worktree remove``) so the
    linked-worktree metadata is cleaned; filesystem removal only as a
    guarded fallback (Luna r1 #16 — rmtree alone leaves dangling metadata
    that breaks future add/prune)."""
    run_fn = run or _default_run
    d = cache_dir(url, pin, root).resolve()
    wt = (d / f"worktree-{owner_pid}").resolve()
    if not wt.exists():
        return
    proc = run_fn(["git", "-C", str(d), "worktree", "remove", "--force", str(wt)])
    if proc.returncode != 0:
        # Guarded fallback: only if git refuses (e.g. dirty) AND the dir is
        # a real worktree we created.
        if wt.is_dir():
            shutil.rmtree(wt, ignore_errors=True)


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
    """Batch-start GC. NEVER removes a clone with an ACTIVE lease — eviction
    only touches unleased/expired entries (Luna r1 #6: purge-then-delete
    could remove a clone a live probe was using). Retained corpora keep
    their clones warm. Returns the number of cache dirs removed.

    NOTE: ``retain_go_corpora`` is honored via the lease registry (kept
    leases) — the directory sweep below only removes dirs whose lease is
    gone AND whose corpus is not retained."""
    base = pathlib.Path(root) if root is not None else CACHE_ROOT
    removed = 0
    if not base.is_dir():
        return 0

    def _sweep() -> int:
        nonlocal removed
        live: set[str] = set()
        for lease in lease_registry.active_leases(path=registry_path):
            live.add(str(lease.get("url") or "") + "#" + str(lease.get("pin") or ""))
        for d in base.iterdir():
            if not d.is_dir():
                continue
            # Map the dir back to (url, pin) via a sidecar key file written at
            # clone time; without one, refuse to guess (safety). A MALFORMED
            # or unreadable sidecar is treated like a missing one — skip the
            # dir, never abort the sweep (CodeRabbit #570).
            key_file = d / ".cache-key"
            if not key_file.is_file():
                continue
            try:
                url, pin = key_file.read_text(encoding="utf-8").split("#", 1)
            except (OSError, ValueError):
                continue  # malformed/unreadable sidecar — skip, don't delete
            if f"{url}#{pin}" in live:
                continue  # active lease — never evict
            corpus = url.rstrip("/").rsplit("/", 1)[-1]
            if retain_go_corpora and corpus in retain_go_corpora:
                continue
            shutil.rmtree(d, ignore_errors=True)
            removed += 1
        return removed

    # The whole sweep runs under the registry lock — a concurrent acquire
    # can never lease a dir that is about to be evicted (Luna r2 #5).
    return lease_registry.run_under_lock(_sweep, path=registry_path)


def _dir_size_mb(path: pathlib.Path) -> float:
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total / (1024 * 1024)
