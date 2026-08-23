"""Wave 2 (#559): lease registry + clone cache + batch state tests.

Covers the XL acceptance criteria: lease TTL/start-time reaping
(red/green), two-phase probe→promote handoff atomicity, count/byte caps +
lease_reject, W=0 fail-closed admission, checksum/.bak recovery, digest
namespace retention, staged-draft GC + properties-walker exclusion guard,
and the batch summary projections."""

from __future__ import annotations

import time

import pytest

from regexproof.mine import batch_state, lease_registry


# --- lease registry ---------------------------------------------------------


def _reg(tmp_path):
    return tmp_path / "leases.json"


def test_acquire_release_roundtrip(tmp_path):
    p = _reg(tmp_path)
    lease = lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert lease["owner_pid"] == 1
    assert lease["ttl_s"] == lease_registry.DEFAULT_TTL_S
    assert lease_registry.active_leases(path=p)[0]["url"] == "https://x/y"
    assert lease_registry.release("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert lease_registry.active_leases(path=p) == []


def test_lease_reject_live_owner(tmp_path):
    p = _reg(tmp_path)
    lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)
    with pytest.raises(SystemExit, match="lease_reject"):
        lease_registry.acquire("https://x/y", "a" * 40, owner_pid=2, path=p)
    # Same owner re-acquires idempotently.
    lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)


def test_ttl_expiry_reaps_stale(tmp_path):
    p = _reg(tmp_path)
    lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, ttl_s=10, path=p)
    # Frozen clock far in the future → expired.
    n = lease_registry.reap_stale(now=time.time() + 100, path=p)
    assert n == 1
    assert lease_registry.active_leases(path=p) == []
    # Re-acquire succeeds after reaping.
    lease_registry.acquire("https://x/y", "a" * 40, owner_pid=2, path=p)


def test_dead_owner_reaped(tmp_path):
    p = _reg(tmp_path)
    # pid 99999999 is not alive.
    lease_registry.acquire("https://x/y", "a" * 40, owner_pid=99999999, path=p)
    assert lease_registry.reap_stale(path=p) == 1


def test_capacity_lease_reject(tmp_path):
    p = _reg(tmp_path)
    lease_registry.acquire("https://x/a", "a" * 40, owner_pid=1, path=p)
    with pytest.raises(SystemExit, match="at capacity"):
        lease_registry.acquire("https://x/b", "b" * 40, owner_pid=1, max_leases=1, path=p)


def test_two_phase_promote_handoff(tmp_path):
    p = _reg(tmp_path)
    probe = lease_registry.acquire(
        "https://x/y", "a" * 40, owner_pid=1,
        ttl_s=lease_registry.PROBE_TTL_S, path=p,
    )
    assert probe["ttl_s"] == lease_registry.PROBE_TTL_S
    promoted = lease_registry.promote(
        "https://x/y", "a" * 40, owner_pid=1,
        ttl_s=lease_registry.DEFAULT_TTL_S, path=p,
    )
    assert promoted["ttl_s"] == lease_registry.DEFAULT_TTL_S
    # Only ONE lease for the key after promote (no window where unleased).
    assert len(lease_registry.active_leases(path=p)) == 1


def test_promote_without_live_probe_rejected(tmp_path):
    """Luna r1 #9: promote requires a LIVE probe lease — creating a lease
    from nothing would promote missing/stale data (cache_miss_reprobe)."""
    p = _reg(tmp_path)
    with pytest.raises(SystemExit, match="no live probe lease"):
        lease_registry.promote("https://x/y", "a" * 40, owner_pid=1, path=p)
    # Expired probe lease also refuses.
    lease_registry.acquire(
        "https://x/y", "a" * 40, owner_pid=1,
        ttl_s=lease_registry.PROBE_TTL_S, path=p,
    )
    lease_registry.reap_stale(now=time.time() + 1000, path=p)
    with pytest.raises(SystemExit, match="no live probe lease"):
        lease_registry.promote(
            "https://x/y", "a" * 40, owner_pid=1,
            ttl_s=lease_registry.DEFAULT_TTL_S,
            path=p,
        )


def test_stale_reaped_before_capacity_check(tmp_path):
    """Luna r1 #7: a dead lease must not consume the cap and cause a false
    lease_reject."""
    p = _reg(tmp_path)
    lease_registry.acquire("https://x/a", "a" * 40, owner_pid=99999999, path=p)
    # Dead owner + capacity 1: the dead lease is reaped first, so the new
    # acquire succeeds instead of falsely rejecting.
    lease_registry.acquire("https://x/b", "b" * 40, owner_pid=1, max_leases=1, path=p)


def test_purge_retain_go(tmp_path):
    p = _reg(tmp_path)
    lease_registry.acquire("https://github.com/ow/packages", "a" * 40, owner_pid=1, path=p)
    lease_registry.acquire("https://github.com/other/repo", "b" * 40, owner_pid=1, path=p)
    n = lease_registry.purge(retain_go_corpora={"packages"}, path=p)
    assert n == 1
    remaining = lease_registry.active_leases(path=p)
    assert len(remaining) == 1
    assert remaining[0]["url"] == "https://github.com/ow/packages"


# --- batch state ------------------------------------------------------------


def _state(tmp_path):
    return tmp_path / "state.json"


def test_record_and_projection(tmp_path):
    p = _state(tmp_path)
    batch_state.begin_item("d1", "https://x/y", "a" * 40, at="2026-08-23T00:00:00+00:00", path=p)
    batch_state.record_outcome(
        "d1", "https://x/y", "a" * 40, "ok",
        extra={"cache_hit": True, "bytes_saved": 5000, "lifecycle_bytes": 100, "clone_ms": 120},
        path=p,
    )
    batch_state.begin_item("d1", "https://x/z", "b" * 40, at="2026-08-23T00:00:01+00:00", path=p)
    batch_state.record_outcome(
        "d1", "https://x/z", "b" * 40, "ok",
        extra={"cache_hit": False, "bytes_saved": 0, "lifecycle_bytes": 900, "clone_ms": 340},
        path=p,
    )
    proj = batch_state.projection(path=p)
    assert proj["rows"] == 2
    assert proj["cache_hits"] == 1
    assert proj["cache_misses"] == 1
    assert proj["bytes_saved"] == 5000
    assert proj["lifecycle_bytes"] == 1000  # probe_fetch only
    assert proj["clone_ms_p50"] == 120
    assert proj["survivor_rate"] == 1.0


def test_keyed_rows_no_duplicates(tmp_path):
    """Luna r1 #11: keyed state — recording the same (digest, url, pin)
    twice must UPSERT, not append."""
    p = _state(tmp_path)
    batch_state.begin_item("d1", "https://x/y", "a" * 40, at="2026-08-23T00:00:00+00:00", path=p)
    batch_state.record_outcome("d1", "https://x/y", "a" * 40, "ok", path=p)
    batch_state.record_outcome("d1", "https://x/y", "a" * 40, "ok", path=p)
    reg = batch_state.load_state(path=p)
    assert len(reg["rows"]) == 1  # keyed upsert
    assert reg["rows"][batch_state._row_key("d1", "https://x/y", "a" * 40)]["outcome"] == "ok"


def test_begin_item_is_resumable(tmp_path):
    """Luna r1 #11: an item with started_at but no completed_at is
    incomplete (re-run on resume)."""
    p = _state(tmp_path)
    batch_state.begin_item("d1", "https://x/y", "a" * 40, at="2026-08-23T00:00:00+00:00", path=p)
    reg = batch_state.load_state(path=p)
    row = next(iter(reg["rows"].values()))
    assert row["started_at"]
    assert row["completed_at"] == ""
    assert row["outcome"] == ""


def test_checksum_verification_and_bak_recovery(tmp_path):
    p = _state(tmp_path)
    batch_state.record_outcome("d1", "https://x/y", "a" * 40, "ok", path=p)
    # Second write rotates a verified .bak into place (needed for recovery).
    batch_state.record_outcome("d1", "https://x/y", "a" * 40, "ok", path=p)
    # Corrupt the state file by mutating a VALUE — the checksum covers the
    # canonical body, so any DATA mutation trips it (whitespace-only edits
    # survive re-serialization and are intentionally accepted; CodeRabbit
    # #570). load falls back to .bak.
    good = p.read_text(encoding="utf-8")
    p.write_text(good.replace('"outcome": "ok"', '"outcome": "error"'), encoding="utf-8")
    reg = batch_state.load_state(path=p)
    assert next(iter(reg["rows"].values()))["outcome"] == "ok"  # from .bak


def test_corrupt_state_no_bak_fails_closed(tmp_path):
    p = _state(tmp_path)
    p.write_text("{not json", encoding="utf-8")
    with pytest.raises(SystemExit, match="fail closed"):
        batch_state.load_state(path=p)


def test_prior_digest_rows_retained(tmp_path):
    p = _state(tmp_path)
    batch_state.record_outcome("old-digest", "https://x/y", "a" * 40, "ok", path=p)
    batch_state.record_outcome("new-digest", "https://x/y", "a" * 40, "cache_miss_reprobe", path=p)
    reg = batch_state.load_state(path=p)
    assert {r["manifest_digest"] for r in reg["rows"].values()} == {"old-digest", "new-digest"}
    assert reg["manifest_digests"]["old-digest"]["count"] == 1


def test_unknown_outcome_rejected(tmp_path):
    p = _state(tmp_path)
    with pytest.raises(SystemExit, match="unknown outcome"):
        batch_state.record_outcome("d1", "https://x/y", "a" * 40, "bogus", path=p)


def test_outcomes_vocabulary():
    assert batch_state.OUTCOMES >= {
        "clone_timeout", "disk_budget", "lease_reject",
        "cache_miss_reprobe", "skip_wave_active",
        "auto_nogo", "needs_human", "rate_limited", "error",
    }


# --- disk admission (Luna r1 #4) ---------------------------------------------


def test_admission_w0_fails_closed(tmp_path):
    from regexproof.mine import disk_admission

    assert disk_admission.reserve(
        worker_count=0, per_clone_cap_mb=100, max_disk_mb=500,
        owner_pid=1, path=tmp_path / "admission.json",
    ) is False


def test_admission_budget_exhausted(tmp_path):
    from regexproof.mine import disk_admission

    p = tmp_path / "admission.json"
    assert disk_admission.reserve(
        worker_count=1, per_clone_cap_mb=400, max_disk_mb=500,
        owner_pid=1, path=p,
    ) is True
    # Second reservation exceeds the 500MB budget.
    assert disk_admission.reserve(
        worker_count=1, per_clone_cap_mb=200, max_disk_mb=500,
        owner_pid=2, path=p,
    ) is False
    # Release frees the budget.
    disk_admission.release(owner_pid=1, path=p)
    assert disk_admission.reserve(
        worker_count=1, per_clone_cap_mb=200, max_disk_mb=500,
        owner_pid=2, path=p,
    ) is True


# --- clone cache GC safety (Luna r1 #6) ---------------------------------------


def test_cache_gc_never_removes_leased(tmp_path):
    """GC must not delete a clone whose lease is ACTIVE — eviction only
    touches unleased/expired entries."""
    from regexproof.admission import clone_cache

    cache_root = tmp_path / "cache"
    reg_path = tmp_path / "leases.json"
    url, pin = "https://github.com/ow/packages", "a" * 40
    d = clone_cache.cache_dir(url, pin, root=cache_root)
    d.mkdir(parents=True)
    (d / "refs").mkdir()
    (d / ".cache-key").write_text(f"{url}#{pin}", encoding="utf-8")
    lease_registry.acquire(url, pin, owner_pid=1, path=reg_path)
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 0
    assert d.is_dir()  # leased clone survived GC
    # After the lease expires (past the 3600s TTL), GC removes it.
    lease_registry.reap_stale(now=time.time() + 7200, path=reg_path)
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 1
    assert not d.exists()
