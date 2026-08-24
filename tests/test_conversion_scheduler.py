"""Wave E (#562): conversion scheduler over GO clusters tests.

Covers (incl. Luna r1 #1-#5): next-unused selection with start-anchored
cycle guard (sentinel NEVER selected); queue blocking on PENDING sites only
(contracted/skipped queues don't block); wont-file classes from the REAL
disposition source with deterministic deny-list (wont-file-heavy target
blocked); GO-cluster inventory from gated:go artifacts (no fabricated
clusters on empty input); exact `_w<digits>` wave stripping (foo_west
unmangled); capacity reservation shares; no mine re-rank; cache note.
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


def _gate_decision(gen: pathlib.Path, corpus: str, decision: str = "go") -> None:
    gen.mkdir(parents=True, exist_ok=True)
    (gen / f"{corpus}_gate_decision.json").write_text(
        json.dumps({"corpus": corpus, "decision": decision,
                    "candidate_url": f"https://x/{corpus}"}) + "\n",
        encoding="utf-8")


def _queue(queues_dir: pathlib.Path, bucket: str, statuses: list[str]) -> None:
    queues_dir.mkdir(parents=True, exist_ok=True)
    (queues_dir / f"{bucket}.json").write_text(
        json.dumps({"cluster": bucket,
                    "candidate_sites": [{"site": f"s{i}", "status": st}
                                        for i, st in enumerate(statuses)]}) + "\n",
        encoding="utf-8")


def test_selects_next_unused_bucket(tmp_path):
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["cluster"] == "openwrt_packages"
    assert sel["selected_bucket"] == "openwrt_luci"  # named next, unused


def test_cycle_sentinel_never_selected(tmp_path):
    """Luna r1 #1: with every named bucket used, the traversal returns to
    the STARTING cluster — the cycle sentinel (openwrt_packages) is NEVER
    selected."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [
        _row("openwrt_packages_w1", b) for b in
        ("openwrt_luci", "form-validators", "qosify-network-dscp")
    ]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] is None
    assert sel["selection_basis"] == "none-available"


def test_queue_blocks_only_pending_sites(tmp_path):
    """Luna r1 #2: a queue with PENDING sites (emitted/claimed) blocks; a
    fully contracted/skipped queue does NOT (file existence alone is
    wrong)."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]

    # Pending queue for openwrt_luci -> blocked; next is form-validators.
    _queue(tmp_path / "queues", "openwrt_luci", ["emitted", "claimed"])
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "form-validators"

    # Closed queue (all contracted) -> openwrt_luci is selectable again.
    _queue(tmp_path / "queues", "openwrt_luci", ["contracted", "skipped_unreachable"])
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "openwrt_luci"


def test_wont_file_classes_from_real_source(tmp_path):
    """Luna r1 #3: wont-file classes come from the REAL disposition source
    (docs/conversion-upstream.jsonl shape: status=wont_file + class)."""
    cs = _load_cs()
    disp = tmp_path / "d.jsonl"
    disp.write_text("\n".join([
        json.dumps({"id": "CU-1", "status": "wont_file", "class": "third_party_security_tool"}),
        json.dumps({"id": "CU-2", "status": "wont_file", "class": "third_party_security_tool"}),
        json.dumps({"id": "CU-3", "status": "wont_file", "class": "no_sandbox"}),
        json.dumps({"id": "CU-4", "status": "false_positive", "class": "x"}),
        "",
    ]) + "\n", encoding="utf-8")
    assert cs.wont_file_classes(disp) == {
        "third_party_security_tool": 2, "no_sandbox": 1,
    }


def test_wont_file_blocks_named_next(tmp_path):
    """Luna r1 #3 + r2 #1: a wont-file-heavy next target (corpus-keyed,
    >= threshold) is DENIED — the scheduler refuses to pick it."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    disp = tmp_path / "d.jsonl"
    # openwrt_luci (the named next) has 2 wont_file rows -> denied.
    disp.write_text("\n".join([
        json.dumps({"id": "CU-1", "status": "wont_file", "class": "third_party",
                    "corpus": "openwrt_luci"}),
        json.dumps({"id": "CU-2", "status": "wont_file", "class": "third_party",
                    "corpus": "openwrt_luci"}),
    ]) + "\n", encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=disp)
    sel = sched["selections"][0]
    assert sel["selected_bucket"] is None
    assert sel["selection_basis"] == "wont-file-blocked"


def test_wont_file_single_occurrence_does_not_block(tmp_path):
    """Luna r2 #1: a SINGLE wont-file row on the target corpus is noise,
    not a pattern — the named-next selection stands."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    disp = tmp_path / "d.jsonl"
    disp.write_text(json.dumps(
        {"id": "CU-1", "status": "wont_file", "class": "third_party",
         "corpus": "openwrt_luci"}) + "\n", encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=disp)
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "openwrt_luci"
    assert sel["selection_basis"] == "named-next-unused"


def test_empty_queue_does_not_block(tmp_path):
    """Luna r2 #2: an empty candidate_sites queue is the valid
    empty_queue() shape — it must NOT block selection."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    _queue(tmp_path / "queues", "openwrt_luci", [])  # empty candidate_sites
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "openwrt_luci"  # not blocked


def test_malformed_queue_rows_skipped(tmp_path):
    """Luna r2 #3: non-dict queue rows are skipped, not fatal — a pending
    status on a VALID row still blocks."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    queues_dir = tmp_path / "queues"
    queues_dir.mkdir(parents=True, exist_ok=True)
    (queues_dir / "openwrt_luci.json").write_text(json.dumps({
        "candidate_sites": ["not-a-dict", {"site": "s1", "status": "claimed"}]}) + "\n",
        encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=queues_dir,
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "form-validators"  # openwrt_luci blocked


def test_malformed_gate_artifact_skipped(tmp_path):
    """Luna r2 #3: a JSON-list gate artifact is skipped, not fatal."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages", "go")
    (gen / "bad_gate_decision.json").write_text("[1, 2, 3]", encoding="utf-8")
    assert cs.go_clusters(gen) == ["openwrt_packages"]


def test_go_clusters_from_gate_decisions(tmp_path):
    """Luna r1 #4: clusters come from gated:go artifacts — no-go decisions
    and empty input never fabricate clusters."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages", "go")
    _gate_decision(gen, "openwrt_luci", "go")
    _gate_decision(gen, "notadmitted", "no-go")  # NOT a GO cluster
    assert cs.go_clusters(gen) == ["openwrt_luci", "openwrt_packages"]
    # Empty/missing dir -> NO selections (not the named-bucket map).
    assert cs.go_clusters(tmp_path / "missing") == []


def test_empty_input_no_selections(tmp_path):
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=tmp_path / "queues",
                              gate_decisions_dir=tmp_path / "missing",
                              dispositions_path=tmp_path / "d.jsonl")
    assert sched["selections"] == []  # no fabricated clusters


def test_wave_strip_exact_suffix(tmp_path):
    """Luna r1 #5: only a trailing _w<digits> is stripped — foo_west is
    NOT mangled."""
    cs = _load_cs()
    rows = [_row("openwrt_packages_w2", "image-and-ddns-json"),
            _row("foo_west", "x")]
    used = cs.used_buckets_per_cluster(rows)
    assert "openwrt_packages" in used
    assert "openwrt_packages_w2" not in used
    assert "foo_west" in used  # untouched


def test_no_mine_re_rank(tmp_path):
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    for sel in sched["selections"]:
        assert sel["mine_re_ranked"] is False


def test_capacity_reservation_shares():
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=pathlib.Path("/nonexistent"),
                              gate_decisions_dir=pathlib.Path("/missing"),
                              dispositions_path=pathlib.Path("/missing"))
    r = sched["capacity_reservation"]
    assert r["productive_share"] == 0.7
    assert r["novel_exploration_share"] == 0.2
    assert r["unbiased_slice_share"] == 0.1
    assert abs(sum(r.values()) - 1.0) < 1e-9


def test_cache_interplay_note_present():
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=pathlib.Path("/nonexistent"),
                              gate_decisions_dir=pathlib.Path("/missing"),
                              dispositions_path=pathlib.Path("/missing"))
    note = sched["cache_interplay_note"]
    assert "lease" in note
    assert "no immortal" in note.lower()


def test_deterministic_with_at(tmp_path):
    cs = _load_cs()
    out = tmp_path / "schedule.json"
    rc = cs.main(["--ledger", str(tmp_path / "missing.ndjson"),
                  "--gate-decisions", str(tmp_path / "missing"),
                  "--dispositions", str(tmp_path / "missing"),
                  "--queues-dir", str(tmp_path / "queues"),
                  "--out", str(out), "--at", "2026-08-24T03:00:00Z"])
    assert rc == 0
    d = json.loads(out.read_text(encoding="utf-8"))
    assert d["generated_at"] == "2026-08-24T03:00:00Z"
    assert list(d.keys()) == sorted(d.keys())  # canonical sorted keys
