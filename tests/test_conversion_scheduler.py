"""Wave E (#562): conversion scheduler over GO clusters tests.

Covers (incl. Luna r1 #1-#5, r2 #1-#3, CodeRabbit #582): first-unused
selection from ordered per-cluster progression using COMMITTED idiom_bucket
vocabulary; progression exhaustion (no wrap, no sentinel); queue blocking on
PENDING sites only with FAIL-CLOSED malformed entries; wont-file deny-list
keyed on corpus with threshold; GO-cluster inventory from gated:go
artifacts; exact `_w<digits>` wave stripping; capacity reservation; no mine
re-rank; cache note; deterministic output.
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


def test_selects_first_unused_progression_bucket(tmp_path):
    """CodeRabbit #582: selection uses the COMMITTED idiom_bucket vocabulary
    (validator-charsets-and-captures, image-and-ddns-json, ...) — never
    cluster names."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["cluster"] == "openwrt_packages"
    assert sel["used_buckets"] == ["validator-charsets-and-captures"]
    assert sel["selected_bucket"] == "image-and-ddns-json"  # first unused


def test_progression_exhausted_no_wrap(tmp_path):
    """Luna r1 #1 + CodeRabbit #582 + r4: when every registered progression
    bucket is used, the DESIGN tails (qosify/network-js/firewall-dscp) are
    NOT emitted until registered — basis 'unregistered-next', nothing
    selected (no wrap, no sentinel)."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [
        _row("openwrt_packages_w1", b) for b in
        ("validator-charsets-and-captures", "image-and-ddns-json",
         "ddns-query-and-escape-image")
    ]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] is None
    assert sel["selection_basis"] == "unregistered-next"  # design tail refused


def test_design_tail_never_emitted_unregistered(tmp_path):
    """Luna r4: qosify/network-js/firewall-dscp are NOT in the committed
    ledger — the scheduler must never emit them as selected_bucket."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", b) for b in
            ("validator-charsets-and-captures", "image-and-ddns-json",
             "ddns-query-and-escape-image")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    for sel in sched["selections"]:
        assert sel["selected_bucket"] not in (
            "qosify-network-dscp", "network-js-dscp", "firewall-dscp")


def test_queue_blocks_only_pending_sites(tmp_path):
    """Luna r1 #2: a queue with PENDING sites (emitted/claimed) blocks; a
    fully contracted/skipped queue does NOT (file existence alone is
    wrong)."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]

    # Pending queue for image-and-ddns-json -> blocked; next is
    # ddns-query-and-escape-image.
    _queue(tmp_path / "queues", "image-and-ddns-json", ["emitted", "claimed"])
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "ddns-query-and-escape-image"

    # Closed queue (all contracted) -> image-and-ddns-json selectable again.
    _queue(tmp_path / "queues", "image-and-ddns-json", ["contracted", "skipped_unreachable"])
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "image-and-ddns-json"


def test_empty_queue_does_not_block(tmp_path):
    """Luna r2 #2: an empty candidate_sites queue is the valid
    empty_queue() shape — it must NOT block selection."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    _queue(tmp_path / "queues", "image-and-ddns-json", [])  # empty sites
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "image-and-ddns-json"  # not blocked


def test_malformed_queue_fails_closed(tmp_path):
    """CodeRabbit #582: ANY malformed queue entry (null, non-dict, or
    status-less) makes the queue BLOCK selection — malformed site data must
    never permit selection."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    queues_dir = tmp_path / "queues"
    queues_dir.mkdir(parents=True, exist_ok=True)
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]

    # null entry -> fail closed (block)
    (queues_dir / "image-and-ddns-json.json").write_text(
        json.dumps({"candidate_sites": [None]}) + "\n", encoding="utf-8")
    sched = cs.build_schedule(rows, queues_dir=queues_dir,
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    assert sched["selections"][0]["selected_bucket"] == "ddns-query-and-escape-image"

    # status-less entry -> fail closed (block); the registered progression
    # is now exhausted and the qosify design tail is UNREGISTERED -> refused.
    (queues_dir / "ddns-query-and-escape-image.json").write_text(
        json.dumps({"candidate_sites": [{"site": "s0"}]}) + "\n", encoding="utf-8")
    sched = cs.build_schedule(rows, queues_dir=queues_dir,
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    assert sched["selections"][0]["selected_bucket"] is None
    assert sched["selections"][0]["selection_basis"] == "unregistered-next"


def test_unknown_queue_status_fails_closed(tmp_path):
    """Luna r4: a status OUTSIDE the queue vocabulary (e.g. 'bogus') is
    malformed — the queue must BLOCK, never permit selection."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    queues_dir = tmp_path / "queues"
    queues_dir.mkdir(parents=True, exist_ok=True)
    (queues_dir / "image-and-ddns-json.json").write_text(
        json.dumps({"candidate_sites": [{"site": "s0", "status": "bogus"}]}) + "\n",
        encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=queues_dir,
                              gate_decisions_dir=gen,
                              dispositions_path=tmp_path / "d.jsonl")
    # image-and-ddns-json blocked (unknown status) -> ddns-query selected.
    assert sched["selections"][0]["selected_bucket"] == "ddns-query-and-escape-image"


def test_malformed_gate_artifact_skipped(tmp_path):
    """Luna r2 #3: a JSON-list gate artifact is skipped, not fatal."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages", "go")
    (gen / "bad_gate_decision.json").write_text("[1, 2, 3]", encoding="utf-8")
    assert cs.go_clusters(gen) == ["openwrt_packages"]


def test_wont_file_blocks_named_next(tmp_path):
    """Luna r1 #3 + r2 #1: a wont-file-heavy next target (corpus-keyed,
    >= threshold) is DENIED — the scheduler refuses to pick it."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    disp = tmp_path / "d.jsonl"
    # image-and-ddns-json (the first unused) has 2 wont_file rows -> denied.
    disp.write_text("\n".join([
        json.dumps({"id": "CU-1", "status": "wont_file", "class": "third_party",
                    "corpus": "image-and-ddns-json"}),
        json.dumps({"id": "CU-2", "status": "wont_file", "class": "third_party",
                    "corpus": "image-and-ddns-json"}),
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
    not a pattern — the selection stands."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages")
    disp = tmp_path / "d.jsonl"
    disp.write_text(json.dumps(
        {"id": "CU-1", "status": "wont_file", "class": "third_party",
         "corpus": "image-and-ddns-json"}) + "\n", encoding="utf-8")
    rows = [_row("openwrt_packages_w1", "validator-charsets-and-captures")]
    sched = cs.build_schedule(rows, queues_dir=tmp_path / "queues",
                              gate_decisions_dir=gen,
                              dispositions_path=disp)
    sel = sched["selections"][0]
    assert sel["selected_bucket"] == "image-and-ddns-json"
    assert sel["selection_basis"] == "named-next-unused"


def test_wont_file_classes_from_real_source(tmp_path):
    """Luna r1 #3: wont-file classes come from the REAL disposition source
    (docs/conversion-upstream.jsonl shape: status=wont_file + class)."""
    cs = _load_cs()
    disp = tmp_path / "d.jsonl"
    disp.write_text("\n".join([
        json.dumps({"id": "CU-1", "status": "wont_file", "class": "third_party",
                    "corpus": "openwrt_packages"}),
        json.dumps({"id": "CU-2", "status": "wont_file", "class": "third_party",
                    "corpus": "openwrt_packages"}),
        json.dumps({"id": "CU-3", "status": "wont_file", "class": "no_sandbox",
                    "corpus": "openwrt_luci"}),
        json.dumps({"id": "CU-4", "status": "false_positive", "class": "x",
                    "corpus": "y"}),
        "",
    ]) + "\n", encoding="utf-8")
    assert cs.wont_file_classes(disp) == {
        "third_party": 2, "no_sandbox": 1,
    }
    assert cs.wont_file_corpora(disp) == {
        "openwrt_packages": 2, "openwrt_luci": 1,
    }


def test_go_clusters_from_gate_decisions(tmp_path):
    """Luna r1 #4: clusters come from gated:go artifacts — no-go decisions
    and empty input never fabricate clusters."""
    cs = _load_cs()
    gen = tmp_path / "generated"
    _gate_decision(gen, "openwrt_packages", "go")
    _gate_decision(gen, "openwrt_luci", "go")
    _gate_decision(gen, "notadmitted", "no-go")  # NOT a GO cluster
    assert cs.go_clusters(gen) == ["openwrt_luci", "openwrt_packages"]
    assert cs.go_clusters(tmp_path / "missing") == []


def test_empty_input_no_selections(tmp_path):
    cs = _load_cs()
    sched = cs.build_schedule([], queues_dir=tmp_path / "queues",
                              gate_decisions_dir=tmp_path / "missing",
                              dispositions_path=tmp_path / "d.jsonl")
    assert sched["selections"] == []  # no fabricated clusters


def test_wave_strip_exact_suffix():
    """Luna r1 #5: only a trailing _w<digits> is stripped — foo_west is
    NOT mangled."""
    cs = _load_cs()
    rows = [_row("openwrt_packages_w2", "image-and-ddns-json"),
            _row("foo_west", "x"),
            _row("bar_w1x", "y")]  # _w1x is not a pure numeric generation
    used = cs.used_buckets_per_cluster(rows)
    assert "openwrt_packages" in used
    assert "openwrt_packages_w2" not in used
    assert "foo_west" in used  # untouched
    assert "bar_w1x" in used  # untouched


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
