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
        generation=1,
        ranked=ranked,
        root=tmp_path,
    )
    return path, cq.load_queue(corpus, root=tmp_path)


# --- emit / artifact shape ------------------------------------------------


def test_emit_creates_queue_with_ranked_rows(tmp_path):
    path, q = _queue(tmp_path)
    assert path.is_file()
    assert q["cluster"] == "openwrt_packages"
    assert q["wave_generation"] == 1
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
            generation=1,
            root=tmp_path,
        )


def test_claim_refused_outside_top15(tmp_path):
    _, q = _queue(tmp_path)
    site16 = q["candidate_sites"][15]["site"]  # rank 16
    with pytest.raises(SystemExit, match="top-15"):
        cq.claim(
            q["cluster"], site16,
            corpus_status="gated:go",
            ledger_state={"now_iso": "2026-08-23"},
            generation=1,
            root=tmp_path,
        )


def test_claim_success_within_top15(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    row = cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={"now_iso": "2026-08-23", "n": 853},
        generation=1,
        root=tmp_path,
    )
    assert row["status"] == "claimed"
    assert row["ledger_state_at_claim"]["n"] == 853
    assert row["wave_generation_at_claim"] == 1


def test_claim_refused_when_not_emitted(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=1, root=tmp_path,
    )
    with pytest.raises(SystemExit, match="not 'emitted'"):
        cq.claim(
            q["cluster"], site,
            corpus_status="gated:go",
            ledger_state={}, generation=1, root=tmp_path,
        )


# --- contract / stub rule --------------------------------------------------


def test_stub_never_contracts(tmp_path):
    _, q = _queue(tmp_path)
    site = q["candidate_sites"][0]["site"]
    cq.claim(
        q["cluster"], site,
        corpus_status="gated:go",
        ledger_state={}, generation=1, root=tmp_path,
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
        ledger_state={}, generation=1, root=tmp_path,
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
        ledger_state={}, generation=1, root=tmp_path,
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
    """Ranker output → schema-validated queue artifact (real ndjson input)."""
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
    for row in q["candidate_sites"]:
        assert row["status"] == "emitted"
        assert row.get("provenance") == "stub"


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
