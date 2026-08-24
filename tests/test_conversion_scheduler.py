"""Wave E (#562): conversion scheduler over GO clusters tests.

Covers: next-unused-bucket selection per cluster; capacity reservation
shares; NO mine re-rank (scheduler never touches ranking); wont-file
pattern classes feed selection; cache-interplay note present in output;
full-cycle refusal (no wrap-around); deterministic output with --at.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _load_cs():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "cs", ROOT / "scripts" / "conversion-scheduler.py",
    )
    cs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cs)  # type: ignore[union-attr]
    return cs


def _row(cluster: str, bucket: str, **kw) -> dict:
    rec = {"wave_id": cluster, "idiom_bucket": bucket, "shape": 5}
    rec.update(kw)
    return rec


def test_selects_next_unused_bucket(tmp_path):
    cs = _load_cs()
    # openwrt_packages used; openwrt_luci NOT used → selected.
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path)
    sel = sched["selections"][0]
    assert sel["cluster"] == "openwrt_packages"
    assert sel["used_buckets"] == ["validator-charsets-and-captures"]
    assert sel["selected_bucket"] == "openwrt_luci"  # named next bucket, unused


def test_wave_generation_stripped():
    cs = _load_cs()
    rows = [_row("openwrt_packages_w2", "image-and-ddns-json")]
    used = cs.used_buckets_per_cluster(rows)
    assert "openwrt_packages" in used  # _w2 stripped
    assert "openwrt_packages_w2" not in used


def test_full_cycle_refused(tmp_path):
    cs = _load_cs()
    # openwrt_luci + form-validators + qosify + openwrt_packages all used.
    rows = [_row("luci", b) for b in
            ("openwrt_luci", "form-validators", "qosify-network-dscp", "openwrt_packages")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path, clusters=["luci"])
    sel = sched["selections"][0]
    assert sel["selected_bucket"] is None
    assert sel["selection_basis"] == "none-available"


def test_queue_artifact_blocks_selection(tmp_path):
    cs = _load_cs()
    # openwrt_luci has a QUEUE ARTIFACT (pending work) — not selected.
    (tmp_path / "openwrt_luci.json").write_text("{}", encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path)
    sel = next(s for s in sched["selections"] if s["cluster"] == "openwrt_packages")
    assert sel["selected_bucket"] == "form-validators"  # openwrt_luci skipped


def test_no_mine_re_rank():
    cs = _load_cs()
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures"),
            _row("openwrt_packages_w2", "image-and-ddns-json")]
    sched = cs.build_schedule(rows, queues_dir=pathlib.Path("/nonexistent"))
    for sel in sched["selections"]:
        assert sel["mine_re_ranked"] is False  # #550: never re-rank by similarity


def test_capacity_reservation_shares():
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=pathlib.Path("/nonexistent"))
    r = sched["capacity_reservation"]
    assert r["productive_share"] == 0.7
    assert r["novel_exploration_share"] == 0.2
    assert r["unbiased_slice_share"] == 0.1
    assert abs(sum(r.values()) - 1.0) < 1e-9  # partitions capacity


def test_wont_file_classes_feed_selection():
    cs = _load_cs()
    rows = [
        _row("packages", "packages", approval_escape="wont_file",
             reason_code="third_party_vendor"),
        _row("packages", "packages", approval_escape="wont_file",
             reason_code="third_party_vendor"),
        _row("packages", "packages", approval_escape="wont_file",
             reason_code="no_sandbox"),
    ]
    sched = cs.build_schedule(rows, queues_dir=pathlib.Path("/nonexistent"))
    assert sched["wont_file_classes"] == {
        "third_party_vendor": 2, "no_sandbox": 1,
    }  # sorted desc; feeds bucket selection


def test_cache_interplay_note_present():
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=pathlib.Path("/nonexistent"))
    note = sched["cache_interplay_note"]
    assert "lease" in note
    assert "NO immortal" in note or "no immortal" in note.lower()


def test_deterministic_with_at(tmp_path):
    cs = _load_cs()
    out = tmp_path / "schedule.json"
    rc = cs.main(["--ledger", str(tmp_path / "missing.ndjson"),
                  "--queues-dir", str(tmp_path),
                  "--out", str(out), "--at", "2026-08-24T03:00:00Z"])
    assert rc == 0
    d = json.loads(out.read_text(encoding="utf-8"))
    assert d["generated_at"] == "2026-08-24T03:00:00Z"
    assert list(d.keys()) == sorted(d.keys())  # canonical sorted keys
