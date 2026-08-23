"""Wave C (#558): conversion queue artifact + stub schema + context extractor.

Queue guards: top-15 requirement, gated:go-only claims, stubs never
contract, skip vocabulary, wave close-out skip reasons. The stub schema is
additionalProperties:false and provenance=stub is queue-only."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import pytest

from regexproof.mine import conversion_queue as cq

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _ranked():
    return [
        {
            "site": f"net/demo/files/etc/init.d/demo:{i}:token_{i}",
            "corpus": "openwrt_packages",
            "pin": "abc123",
            "idiom_bucket": "validator-charsets",
            "provenance": "stub",
            "suggested_shape": "NUL-free ASCII",
            "cheap_signals": {"capture_group": "x", "trust_guess": "config"},
        }
        for i in range(1, 20)
    ]


def _queue(tmp_path, ranked=None, corpus="openwrt_packages"):
    ranked = ranked if ranked is not None else _ranked()
    path = cq.emit(
        corpus,
        wave_id="ow_w1",
        generation=0,  # matches the opened wave's derived generation
        ranked=ranked,
        root=tmp_path,
        clock_iso="2026-08-23T00:00:00",
    )
    return path, cq.load_queue(corpus, root=tmp_path)


def _open_wave(tmp_path, corpus="openwrt_packages", wave_id="ow_w1"):
    """Open an active wave at generation 0 so claims pass the lock gate."""
    from regexproof.mine.corpus_lock import wave_open

    log = tmp_path / "events.jsonl"
    wave_open(corpus, wave_id, log=log)
    return log


# --- emit / artifact shape ------------------------------------------------


def test_emit_creates_queue_with_ranked_rows(tmp_path):
    path, q = _queue(tmp_path)
    assert path.is_file()
    assert q["cluster"] == "openwrt_packages"
    assert q["wave_generation"] == 0
    assert len(q["candidate_sites"]) == 19
    assert q["candidate_sites"][0]["rank"] == 1
    assert q["candidate_sites"][0]["status"] == "emitted"


# --- claim guards ----------------------------------------------------------


def test_claim_refused_on_non_gated_go(tmp_path):
    _, q = _queue(tmp_path)
    with pytest.raises(SystemExit, match="not 'gated:go'"):
        cq.claim(
            q["cluster"], q["candidate_sites"][0]["site"],
            corpus_status="gated:triage-trial",
            ledger_state={"now_iso": "2026-08-23"},
            generation=0,
            root=tmp_path,
            lock_log=_open_wave(tmp_path),
        )


def test_claim_refused_outside_top15(tmp_path):
    _, q = _queue(tmp_path)
    site16 = q["candidate_sites"][15]["site"]  # rank 16
    with pytest.raises(SystemExit, match="top-15"):
        cq.claim(
            q["cluster"], site16,
            corpus_status="gated:go",
            ledger_state={"now_iso": "2026-08-23"},
            generation=0,
            root=tmp_path,
            lock_log=_open_wave(tmp_path),
        )


def test_claim_success_within_top15(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    row = cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={"now_iso": "2026-08-23", "n": 853},
        generation=0,
        root=tmp_path,
        lock_log=_open_wave(tmp_path),
    )
    assert row["status"] == "claimed"
    assert row["ledger_state_at_claim"]["n"] == 853
    assert row["wave_generation_at_claim"] == 0


def test_claim_refused_when_not_emitted(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(tmp_path)
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=tmp_path, lock_log=lock_log,
    )
    with pytest.raises(SystemExit, match="not 'emitted'"):
        cq.claim(
            q["cluster"], site,
            corpus_status="gated:go",
            ledger_state={}, generation=0, root=tmp_path, lock_log=lock_log,
        )


# --- contract / stub rule --------------------------------------------------


def test_stub_never_contracts(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=tmp_path, lock_log=_open_wave(tmp_path),
    )
    with pytest.raises(SystemExit, match="stub"):
        cq.contract(
            q["cluster"], site,
            contract={"guarantee": "x", "input_source": "y"}, root=tmp_path,
        )


def test_contract_after_human_adoption(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=tmp_path, lock_log=_open_wave(tmp_path),
    )
    # Human adoption replaces provenance (queue state), then contracts.
    q = cq.load_queue(q["cluster"], root=tmp_path)
    q["candidate_sites"][0]["provenance"] = "human"
    (tmp_path / f"{q['cluster']}.json").write_text(
        json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    row = cq.contract(
        q["cluster"], site,
        contract={"guarantee": "x", "input_source": "y", "declared_domain": "z"},
        root=tmp_path,
    )
    assert row["status"] == "contracted"
    assert row["contract"]["guarantee"] == "x"


# --- skip vocabulary / close-out -------------------------------------------


def test_claim_refused_on_stale_generation(tmp_path):
    """Luna r1 #3: a claim at a stale generation (wave moved) is refused."""
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(tmp_path)
    with pytest.raises(SystemExit, match="stale snapshot"):
        cq.claim(
            q["cluster"], site,
            corpus_status="gated:go",
            ledger_state={}, generation=999, root=tmp_path, lock_log=lock_log,
        )


def test_claim_refused_on_wave_mismatch(tmp_path):
    """Luna r2 #1: a queue emitted for w1 can never be claimed during w2 —
    the claim must ride the wave the queue was bound to."""
    _, q = _queue(tmp_path)  # queue wave_id = ow_w1
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(tmp_path, wave_id="ow_w2")  # active wave = ow_w2
    with pytest.raises(SystemExit, match="bound to wave"):
        cq.claim(
            q["cluster"], site,
            corpus_status="gated:go",
            ledger_state={}, generation=0, root=tmp_path, lock_log=lock_log,
            wave_id="ow_w1",
        )


def test_claim_wave_id_param_cannot_override_artifact(tmp_path):
    """Luna r3 #2: a caller-supplied wave_id must NOT override the
    artifact's binding — the artifact is authoritative."""
    _, q = _queue(tmp_path)  # artifact wave_id = ow_w1
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(tmp_path, wave_id="ow_w2")  # active wave = ow_w2
    with pytest.raises(SystemExit, match="bound to wave"):
        cq.claim(
            q["cluster"], site,
            corpus_status="gated:go",
            ledger_state={}, generation=0, root=tmp_path, lock_log=lock_log,
            wave_id="ow_w2",  # must NOT override the artifact's ow_w1
        )


def test_emit_refuses_unbound_wave_id(tmp_path):
    """Luna r4 #2: emit() must refuse a blank wave_id — an unbound
    artifact would bypass claim-time wave binding."""
    with pytest.raises(SystemExit, match="wave_id must be nonblank"):
        cq.emit(
            "openwrt_packages",
            wave_id="",
            generation=0,
            ranked=_ranked(),
            root=tmp_path,
        )


def test_emit_refuses_path_like_cluster(tmp_path):
    """Luna r7 #6: cq.emit itself must reject path-like cluster names —
    the CLI guard alone is not enough for direct callers."""
    for bad in ("../victim", "/tmp/victim", ".", ".."):
        with pytest.raises(SystemExit, match="plain cluster name"):
            cq.emit(
                bad,
                wave_id="ow_w1",
                generation=0,
                ranked=_ranked(),
                root=tmp_path,
            )


def test_emit_preserves_cheap_signals(tmp_path):
    """CodeRabbit #569: the nested cheap_signals object must reach queue
    rows (the producer nests them; emit must not drop them)."""
    ranked = _ranked()
    path = cq.emit(
        "openwrt_packages",
        wave_id="ow_w1",
        generation=0,
        ranked=ranked,
        root=tmp_path,
        clock_iso="2026-08-23T00:00:00",
    )
    q = json.loads(path.read_text(encoding="utf-8"))
    row = q["candidate_sites"][0]
    assert row["cheap_signals"]["capture_group"] == "x"
    assert row["cheap_signals"]["trust_guess"] == "config"
    assert row["created_at"] == "2026-08-23T00:00:00"  # CodeRabbit #569


def test_claim_refused_on_stale_artifact_generation(tmp_path):
    """CodeRabbit #569 + Luna r7 #3: a stale artifact (earlier generation)
    is unclaimable. Wave_id reuse is now impossible (uniqueness guard), so
    the freshness proof is the artifact generation == current generation."""
    _queue(tmp_path)  # artifact wave_generation = 0, bound to ow_w1
    from regexproof.mine.corpus_lock import wave_open, wave_close

    log = tmp_path / "events.jsonl"
    wave_open("openwrt_packages", "ow_w1", log=log)  # gen 0
    wave_close("openwrt_packages", "ow_w1", force=False, log=log)  # gen 1
    # Reopening ow_w1 is refused (uniqueness) — a fresh id means the old
    # artifact's generation no longer matches the current one.
    with pytest.raises(SystemExit, match="was used before"):
        wave_open("openwrt_packages", "ow_w1", log=log)


def test_skip_refused_on_contracted_row(tmp_path):
    """Luna r1 #11: a live contract can never be reverted to a skip state."""
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(tmp_path)
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=tmp_path, lock_log=lock_log,
    )
    q = cq.load_queue(q["cluster"], root=tmp_path)
    q["candidate_sites"][0]["provenance"] = "human"
    (tmp_path / f"{q['cluster']}.json").write_text(
        json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    cq.contract(
        q["cluster"], site,
        contract={"guarantee": "x", "input_source": "y"}, root=tmp_path,
    )
    with pytest.raises(SystemExit, match="cannot be reverted"):
        cq.skip(q["cluster"], site, reason="unreachable", root=tmp_path)


def test_queue_health_joins_candidate_rows(tmp_path):
    """Luna r1 #10: contract_queue_health must read per-candidate status —
    the real artifact stores state under candidate_sites, not top level."""
    import importlib.util

    # Real layout: <root>/conversion_queue/<cluster>.json, gen_dir = <root>/generated
    root = tmp_path / "root"
    gen_dir = root / "generated"
    qdir = root / "conversion_queue"
    gen_dir.mkdir(parents=True)
    _, q = _queue(qdir, corpus="openwrt_packages")
    site = q["candidate_sites"][0]["site"]
    lock_log = _open_wave(root, corpus="openwrt_packages")
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=qdir, lock_log=lock_log,
    )
    q = cq.load_queue(q["cluster"], root=qdir)
    q["candidate_sites"][0]["provenance"] = "human"
    (qdir / f"{q['cluster']}.json").write_text(
        json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    cq.contract(
        q["cluster"], site,
        contract={"guarantee": "x", "input_source": "y"}, root=qdir,
    )
    spec = importlib.util.spec_from_file_location(
        "conversion_ledger", ROOT / "scripts" / "conversion-ledger.py"
    )
    assert spec is not None and spec.loader is not None
    ledger = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ledger)
    health = ledger.contract_queue_health(gen_dir, clock_iso="2026-08-23")
    assert health["contracted"] == 1  # flattened from candidate_sites
    assert health["emitted"] == 18


def test_skip_requires_known_reason(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][1]["site"]
    with pytest.raises(SystemExit, match="unknown skip reason"):
        cq.skip(q["cluster"], site, reason="nonsense", root=tmp_path)


def test_skip_unreachable(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][1]["site"]
    row = cq.skip(q["cluster"], site, reason="unreachable", note="spec", root=tmp_path)
    assert row["status"] == "skipped_unreachable"
    assert row["reasons"][0]["reason"] == "unreachable"


def test_wave_closeout_requires_skip_reasons(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=0, root=tmp_path, lock_log=_open_wave(tmp_path),
    )
    q = cq.load_queue(q["cluster"], root=tmp_path)
    q["candidate_sites"][0]["provenance"] = "human"
    (tmp_path / f"{q['cluster']}.json").write_text(
        json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    cq.contract(
        q["cluster"], site,
        contract={"guarantee": "x", "input_source": "y"}, root=tmp_path,
    )
    # Without skips, the other top-15 rows are close-out blockers.
    q = cq.load_queue(q["cluster"], root=tmp_path)
    first_two = dict(q)
    first_two["candidate_sites"] = [r for r in q["candidate_sites"] if r["rank"] <= 2]
    blockers = cq.non_contracted_top15(first_two)
    assert len(blockers) == 1  # rank-2 is still emitted
    assert blockers[0]["rank"] == 2
    # Skip the rest of the top-15 so close-out has no blockers.
    for r in q["candidate_sites"]:
        if r["status"] == "emitted" and int(r["rank"]) <= 15:
            cq.skip(q["cluster"], r["site"], reason="out_of_scope", root=tmp_path)
    q = cq.load_queue(q["cluster"], root=tmp_path)
    assert cq.non_contracted_top15(q) == []


# --- stub schema -----------------------------------------------------------


def test_stub_schema_rejects_contract_fields():

    schema = json.loads(
        (ROOT / "schemas" / "queue_stub.schema.json").read_text(encoding="utf-8")
    )
    import jsonschema

    ok = {
        "provenance": "stub",
        "corpus": "ow",
        "pin": "p",
        "site": "a/b.sh:1:x",
        "idiom_bucket": "b",
        "suggested_shape": "s",
    }
    jsonschema.validate(ok, schema)  # must pass

    bad = dict(ok)
    bad["guarantee"] = "smuggled contract semantics"  # additionalProperties
    with pytest.raises(Exception):
        jsonschema.validate(bad, schema)

    bad2 = dict(ok)
    bad2["provenance"] = "human"  # const violation
    with pytest.raises(Exception):
        jsonschema.validate(bad2, schema)


# --- stub emitter -----------------------------------------------------------


def test_stub_emitter_rejects_contract_fields(tmp_path):
    """A stub carrying contract semantics must be rejected (the emitter is
    the Gate-2 ranker, not the probe path — no guarantee/trust smuggling)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "emit_cq", ROOT / "scripts" / "emit-conversion-queue.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    with pytest.raises(SystemExit, match=r"contract field|Additional properties"):
        mod.validate_stub(
            {
                "provenance": "stub",
                "corpus": "ow",
                "pin": "p",
                "site": "a/b.sh:1:x",
                "idiom_bucket": "b",
                "suggested_shape": "s",
                "guarantee": "smuggled",
            }
        )


def test_stub_emitter_end_to_end(tmp_path):
    """Ranker output → schema-validated queue artifact (real ndjson input).
    Asserts NON-EMPTY output (Luna r1 #1 regression: the documented input
    must not produce an empty queue)."""
    ndjson = tmp_path / "ow_conversion.ndjson"
    ndjson.write_text(
        json.dumps(
            {
                "contract": {
                    "schema_version": "1",
                    "site": "net/demo/app.sh:10:host",
                    "provenance": "human",
                    "declared_domain": "x",
                    "trust": "config",
                },
                "corpus": "openwrt_packages",
                "idiom_bucket": "validator-charsets",
                "family": "OW-packages",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    out = tmp_path / "queue" / "openwrt_packages.json"
    r = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "emit-conversion-queue.py"),
            "--ndjson", str(ndjson), "--corpus", "openwrt_packages",
            "--wave-id", "ow_w1", "--generation", "1", "-o", str(out),
        ],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    q = json.loads(out.read_text(encoding="utf-8"))
    assert q["cluster"] == "openwrt_packages"
    assert q["wave_generation"] == 1
    assert len(q["candidate_sites"]) >= 1  # non-empty (Luna r1 #1)
    for row in q["candidate_sites"]:
        assert row["status"] == "emitted"
        assert row.get("provenance") == "stub"


def test_stub_emitter_real_corpus_nonempty(tmp_path):
    """The real openwrt_packages conversion corpus must emit >0 stubs —
    regression for Luna r1 #1 (empty-queue blocker)."""
    real = ROOT / "properties" / "generated" / "openwrt_packages_conversion.ndjson"
    if not real.is_file():
        pytest.skip("real conversion ndjson not present")
    out = tmp_path / "queue" / "openwrt_packages.json"
    r = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "emit-conversion-queue.py"),
            "--ndjson", str(real), "--corpus", "openwrt_packages",
            "--wave-id", "ow_w1", "--generation", "0", "-o", str(out),
        ],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    q = json.loads(out.read_text(encoding="utf-8"))
    assert len(q["candidate_sites"]) > 0


# --- context extractor ------------------------------------------------------


def _checkout(tmp_path):
    tree = tmp_path / "tree"
    (tree / "net/demo").mkdir(parents=True)
    (tree / "net/demo" / "app.sh").write_text(
        "\n".join(f"line {i}" for i in range(1, 201)), encoding="utf-8"
    )
    return tree


def test_extractor_window_around_target(tmp_path):
    tree = _checkout(tmp_path)
    r = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
            "--corpus", "openwrt_packages", "--checkout", str(tree),
            "--site", "net/demo/app.sh:100:token",
        ],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["target_line"] == 100
    assert 50 <= out["window_lines"] <= 150
    assert any(line["is_target"] and line["line"] == 100 for line in out["lines"])


def test_extractor_bounded_window_at_edge(tmp_path):
    """Luna r1 #8: a 200-line file with target line 1 yields <=150 lines
    (never the whole file)."""
    tree = _checkout(tmp_path)
    r = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
            "--corpus", "openwrt_packages", "--checkout", str(tree),
            "--site", "net/demo/app.sh:1:token",
        ],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["window_lines"] <= 150
    assert out["window_start"] == 1
    assert out["target_line"] == 1


def test_extractor_rejects_out_of_range_line(tmp_path):
    tree = _checkout(tmp_path)
    for bad in ("net/demo/app.sh:0:token", "net/demo/app.sh:201:token"):
        r = subprocess.run(
            [
                sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
                "--corpus", "openwrt_packages", "--checkout", str(tree),
                "--site", bad,
            ],
            capture_output=True, text=True,
        )
        assert r.returncode != 0, f"accepted bad line {bad}"


def test_extractor_rejects_checkout_escape(tmp_path):
    """Luna r1 #9: absolute paths / .. / symlinks may not read outside the
    checkout."""
    tree = _checkout(tmp_path)
    outside = tmp_path / "outside.txt"
    outside.write_text("SECRET", encoding="utf-8")
    for site in (
        "../outside.txt:1:token",
        str(outside) + ":1:token",
    ):
        r = subprocess.run(
            [
                sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
                "--corpus", "openwrt_packages", "--checkout", str(tree),
                "--site", site,
            ],
            capture_output=True, text=True,
        )
        assert r.returncode != 0, f"escape not blocked: {site}"
        assert "outside the checkout" in r.stderr or "not found" in r.stderr


def test_review_form_validation_enforced(tmp_path):
    tree = _checkout(tmp_path)
    form_path = tmp_path / "form.json"
    r = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
            "--corpus", "openwrt_packages", "--checkout", str(tree),
            "--site", "net/demo/app.sh:100:token",
            "--review-form", "-o", str(form_path),
        ],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    form = json.loads(form_path.read_text(encoding="utf-8"))
    assert form["witness_reachability"] is None  # human must fill

    # Validation fails without the required fields.
    r2 = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
            "--validate", str(form_path),
        ],
        capture_output=True, text=True,
    )
    assert r2.returncode != 0
    assert "witness_reachability" in r2.stderr

    # Filled form with evidence passes and derives the queue action.
    form["witness_reachability"] = "unreachable"
    form["evidence_ref"] = "app.sh:90-110: format spec §3"
    form["input_format_constraint"] = "ASCII NUL-free query values"
    form_path.write_text(json.dumps(form), encoding="utf-8")
    r3 = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "context-extractor.py"),
            "--validate", str(form_path),
        ],
        capture_output=True, text=True,
    )
    assert r3.returncode == 0, r3.stderr
    validated = json.loads(r3.stdout)
    assert validated["queue_action"] == "skipped_unreachable"
