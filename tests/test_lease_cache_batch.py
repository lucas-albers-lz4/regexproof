"""Wave 2 (#559): lease registry + clone cache + batch state tests.

Covers the XL acceptance criteria: lease TTL/start-time reaping
(red/green), two-phase probe→promote handoff atomicity, count/byte caps +
lease_reject, W=0 fail-closed admission, checksum/.bak recovery, digest
namespace retention, staged-draft GC + properties-walker exclusion guard,
and the batch summary projections."""

from __future__ import annotations

import pathlib
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
    assert proj["probe_success_rate"] == 1.0
    assert "survivor_rate" not in proj


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


def test_v1_list_state_migrates_to_keyed(tmp_path):
    """Luna r2 #7: an existing valid v1 state (rows as a LIST) must resume —
    begin_item/record_outcome require the keyed v2 shape."""
    p = _state(tmp_path)
    v1 = {
        "schema_version": "1",
        "manifest_digests": {"d1": {"count": 1}},
        "rows": [
            {"manifest_digest": "d1", "url": "https://x/y", "pin": "a" * 40,
             "outcome": "ok"},
        ],
    }
    v1["sha256"] = batch_state._checksum_of(v1)
    p.write_text(batch_state._canonical(v1), encoding="utf-8")
    reg = batch_state.load_state(path=p)
    assert isinstance(reg["rows"], dict)
    assert len(reg["rows"]) == 1
    # record_outcome resumes on the migrated state.
    batch_state.record_outcome("d1", "https://x/y", "a" * 40, "ok", path=p)
    assert len(batch_state.load_state(path=p)["rows"]) == 1


def test_partial_cache_dir_is_not_a_hit(tmp_path):
    """Luna r2 #3: a partial clone dir (refs but NO .cache-key completeness
    marker) must never be treated as a cache hit."""
    from regexproof.admission import clone_cache

    cache_root = tmp_path / "cache"
    url, pin = "https://github.com/ow/packages", "a" * 40
    d = clone_cache.cache_dir(url, pin, root=cache_root)
    d.mkdir(parents=True)
    (d / "refs").mkdir()  # partial: no .cache-key
    assert not clone_cache.cache_hit(url, pin, root=cache_root)


def test_gc_sweep_holds_registry_lock(tmp_path):
    """Luna r2 #5 + #559 AC: eviction-vs-promote must be atomic — the GC
    sweep runs under the registry lock, so a concurrent acquire can never
    lease a dir that is about to be evicted."""
    from regexproof.admission import clone_cache

    cache_root = tmp_path / "cache"
    reg_path = tmp_path / "leases.json"
    url, pin = "https://github.com/ow/packages", "a" * 40
    d = clone_cache.cache_dir(url, pin, root=cache_root)
    d.mkdir(parents=True)
    (d / "refs").mkdir()
    (d / ".cache-key").write_text(f"{url}#{pin}", encoding="utf-8")
    # An acquire DURING the sweep must be serialized against it — acquiring
    # before the sweep makes the dir untouchable; after the sweep (lease
    # released) it is evictable. The lock ensures no interleave.
    lease_registry.acquire(url, pin, owner_pid=1, path=reg_path)
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 0
    assert d.is_dir()
    lease_registry.reap_stale(now=time.time() + 7200, path=reg_path)
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 1


def test_default_probe_cap_consistent_with_max(tmp_path):
    """Luna r2 #1 + CodeRabbit #570: the CLI derives probe cap from
    --max-disk-mb when --probe-fetch-limit-mb is unset. PATCHES
    disk_admission.reserve to capture per_clone_cap_mb and return before
    any clone execution — no real Git ops, deterministic outcome."""
    import importlib.util
    from unittest import mock
    from regexproof.admission import clone_cache
    from regexproof.mine import disk_admission as da, lease_registry as lr

    root = pathlib.Path(__file__).resolve().parent.parent
    spec = importlib.util.spec_from_file_location("bp", root / "scripts" / "batch-probe.py")
    batch_probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(batch_probe)  # type: ignore[union-attr]

    captured: dict[str, int] = {}
    fake_dir = tmp_path / "fake-cache"
    fake_dir.mkdir()
    wt = tmp_path / "fake-wt"
    wt.mkdir()
    gen = tmp_path / "generated"
    gen.mkdir()
    from regexproof.mine.ledger import empty_ledger, save_ledger

    ledger = tmp_path / "ledger.json"
    led = empty_ledger()
    led["candidates"].append({
        "url": "https://github.com/openwrt/packages",
        "status": "mined",
        "pin": "a" * 40,
    })
    save_ledger(ledger, led)

    def fake_reserve(*, worker_count, per_clone_cap_mb, max_disk_mb, owner_pid, path):
        captured["per_clone_cap_mb"] = per_clone_cap_mb
        captured["worker_count"] = worker_count
        return True

    fake_entry = {"cache_hit": False, "dir": str(fake_dir), "owner_pid": 1}

    with (
        mock.patch.object(da, "reserve", side_effect=fake_reserve),
        mock.patch.object(clone_cache, "cache_acquire", return_value=fake_entry),
        mock.patch.object(clone_cache, "worktree_for", return_value=wt),
        mock.patch.object(clone_cache, "worktree_remove", return_value=None),
        mock.patch.object(lr, "renew", return_value=fake_entry),
    ):
        rc = batch_probe.main([  # type: ignore[attr-defined]
            "--url", "https://github.com/openwrt/packages",
            "--pin", "a" * 40, "--corpus", "openwrt_packages",
            "--state", str(tmp_path / "state.json"),
            "--walk-root", str(tmp_path / "staged"),
            "--generated", str(gen),
            "--ledger", str(ledger),
        ])
    # main completed through the patched path (return 0; no real Git ops).
    assert rc == 0, f"main returned {rc}"
    assert captured["per_clone_cap_mb"] == 500  # derived from --max-disk-mb
    from regexproof.mine import batch_state as bs

    st = bs.load_state(path=tmp_path / "state.json")
    row = next(iter(st["rows"].values()))
    assert row["outcome"] == "auto_nogo"  # empty worktree is below-scale, not ok


def test_lease_renew_extends_expiry(tmp_path):
    """Luna r3 #5: renew() extends a live lease's expiry under the lock and
    refuses when the lease is gone/expired/foreign."""
    p = _reg(tmp_path)
    lease = lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)
    old_expiry = lease["expires_at"]
    ticks_before = lease.get("owner_start_ticks")
    renewed = lease_registry.renew("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert renewed["expires_at"] > old_expiry
    ticks_after = renewed.get("owner_start_ticks")
    assert ticks_after == lease_registry._proc_start_ticks(1)
    assert ticks_before is None or ticks_after == ticks_before
    # Foreign owner cannot renew.
    with pytest.raises(SystemExit, match="lease_reject"):
        lease_registry.renew("https://x/y", "a" * 40, owner_pid=2, path=p)
    # Expired lease cannot renew.
    lease_registry.reap_stale(now=time.time() + 7200, path=p)
    with pytest.raises(SystemExit, match="no live lease"):
        lease_registry.renew("https://x/y", "a" * 40, owner_pid=1, path=p)


def test_lease_renew_fills_ticks_when_acquire_had_none(tmp_path):
    """Grok F3: acquire stored None → renew fills live ticks when lookup
    succeeds. Patch is scoped to acquire vs renew so _expired never sees a
    recycled-PID mismatch."""
    from unittest import mock

    p = _reg(tmp_path)
    with mock.patch.object(lease_registry, "_proc_start_ticks", return_value=None):
        lease = lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert lease.get("owner_start_ticks") is None
    with mock.patch.object(lease_registry, "_proc_start_ticks", return_value=4242):
        renewed = lease_registry.renew("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert renewed["owner_start_ticks"] == 4242


def test_lease_renew_preserves_ticks_when_lookup_fails(tmp_path):
    """Grok F3: a failed /proc lookup on renew must not wipe a stored
    identity (None would disable PID-reuse checks on the heartbeat path)."""
    from unittest import mock

    p = _reg(tmp_path)
    with mock.patch.object(lease_registry, "_proc_start_ticks", return_value=4242):
        lease = lease_registry.acquire("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert lease["owner_start_ticks"] == 4242
    with mock.patch.object(lease_registry, "_proc_start_ticks", return_value=None):
        renewed = lease_registry.renew("https://x/y", "a" * 40, owner_pid=1, path=p)
    assert renewed["owner_start_ticks"] == 4242


def test_heartbeat_renews_before_gc_eviction(tmp_path):
    """Luna r5-r8: the walk's lease heartbeat keeps the lease live BEFORE
    expiry so GC never evicts the clone mid-walk. The injected walk_fn
    OBSERVES the lease start_time DURING enumeration: streamed iteration
    renews mid-walk (start_time advances between yields); a sorted()
    mutant materializes the full traversal with NO renewal, so start_time
    stays frozen through every yield (Luna r8 #1 — deterministic
    detection, mutation-verified). The per-iteration heartbeat also covers
    directory/.git traversals (Luna r8 #2)."""
    import importlib.util
    from typing import Iterator
    from regexproof.admission import clone_cache

    root = pathlib.Path(__file__).resolve().parent.parent
    spec = importlib.util.spec_from_file_location("bp", root / "scripts" / "batch-probe.py")
    batch_probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(batch_probe)  # type: ignore[union-attr]

    cache_root = tmp_path / "cache"
    reg_path = tmp_path / "leases.json"
    url, pin = "https://github.com/ow/packages", "a" * 40
    d = clone_cache.cache_dir(url, pin, root=cache_root)
    d.mkdir(parents=True)
    (d / "refs").mkdir()
    (d / ".cache-key").write_text(f"{url}#{pin}", encoding="utf-8")
    # Short-TTL lease + a large tree with directory entries.
    lease_registry.acquire(url, pin, owner_pid=1, ttl_s=60, path=reg_path)
    wt = d / "worktree-1"
    wt.mkdir()
    for i in range(2100):
        (wt / f"f{i}.js").write_text("x", encoding="utf-8")
    # The walk_fn records the lease start_time on EVERY yield. With a
    # streamed walk the mid-walk heartbeat renews (start_time advances)
    # DURING enumeration; with a sorted() materialization the renewal can
    # only happen AFTER every yield, so the observed sequence is frozen.
    observed: list[float] = []

    def observing_walk() -> Iterator:
        for p in wt.rglob("*"):
            reg = lease_registry._read_registry(reg_path)
            observed.append(float(reg["leases"][lease_registry._key(url, pin)]["start_time"]))
            yield p

    walked = batch_probe._walk_and_heartbeat(  # type: ignore[attr-defined]
        wt, url=url, pin=pin, owner_pid=1, registry_path=reg_path,
        walk_fn=observing_walk,
    )
    assert walked == 2100
    # The heartbeat renewed DURING enumeration — start_time advanced
    # between yields. (A sorted() mutant would show a frozen sequence.)
    assert len(set(observed)) > 1, "lease was never renewed during the walk"
    # The heartbeat kept the lease live → GC evicts nothing.
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 0
    assert d.is_dir()


def test_acquire_before_dir_check_closes_toctou(tmp_path):
    """Luna r3 #4: cache_acquire takes the lease BEFORE the dir check — a
    GC sweep (which holds the lock and never evicts leased dirs) cannot
    remove the clone between check and hit return."""
    from regexproof.admission import clone_cache

    cache_root = tmp_path / "cache"
    reg_path = tmp_path / "leases.json"
    url, pin = "https://github.com/ow/packages", "a" * 40
    d = clone_cache.cache_dir(url, pin, root=cache_root)
    d.mkdir(parents=True)
    (d / "refs").mkdir()
    (d / ".cache-key").write_text(f"{url}#{pin}", encoding="utf-8")
    # A lease already held by us (simulating acquire-first) makes GC skip
    # the dir — eviction-vs-acquire cannot interleave.
    lease_registry.acquire(url, pin, owner_pid=1, path=reg_path)
    removed = clone_cache.cache_gc(root=cache_root, registry_path=reg_path)
    assert removed == 0
    assert d.is_dir()


def test_dogfood_excludes_staged_probes(tmp_path):
    """Luna r3 #1: dogfood-singleton-analysis must not walk staged_probes —
    the walker guard's false negative (Path(path).rglob) is closed."""
    import importlib.util

    root = pathlib.Path(__file__).resolve().parent.parent
    staged = tmp_path / "staged_probes"
    staged.mkdir()
    (staged / "x.draft.json").write_text("{}", encoding="utf-8")
    spec = importlib.util.spec_from_file_location(
        "dsa", root / "scripts" / "dogfood-singleton-analysis.py",
    )
    dsa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dsa)  # type: ignore[union-attr]
    scan = dsa.extract_repo("test", str(staged))
    assert scan.scanned_files == 0  # staged probes never walked


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
