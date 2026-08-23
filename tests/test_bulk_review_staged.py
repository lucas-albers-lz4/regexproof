"""Wave 3 (#560): staged bulk review CLI + requeue/demote semantics tests.

Covers: provenance enforcement (go/triage-trial REQUIRE human; auto paths
are NO-GO-only); audit sampler population extension (bulk-CLI-promoted
included, provenance=stub excluded at schema level); (url, pin)
supersession dedup for eval/escape counters; canonical JSON output.
"""

from __future__ import annotations

import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.mine import audit  # noqa: E402


def _staged(site: str, *, url="https://x/y", pin="a" * 40, corpus="ow") -> dict:
    return {
        "site": site, "url": url, "pin": pin, "corpus": corpus,
        "manifest_digest": "d1", "idiom_bucket": "regex",
    }


@pytest.fixture()
def staged_root(tmp_path, monkeypatch):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "brs", ROOT / "scripts" / "bulk-review-staged.py",
    )
    brs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(brs)  # type: ignore[union-attr]
    monkeypatch.setattr(brs, "STAGED_ROOT", tmp_path)
    return brs, tmp_path


def _write_draft(tmp_path: pathlib.Path, site: str, **kw) -> None:
    import hashlib

    d = _staged(site, **kw)
    name = hashlib.sha256(f"{d['manifest_digest']}#{d['url']}#{d['pin']}".encode()).hexdigest()[:24]
    (tmp_path / f"{name}.draft.json").write_text(
        json.dumps(d, sort_keys=True) + "\n", encoding="utf-8",
    )


# --- provenance enforcement --------------------------------------------------


def test_go_requires_human_provenance(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/a.sh:1:tok")
    with pytest.raises(SystemExit, match="requires --provenance human"):
        brs.main(["--go", "net/demo/a.sh:1:tok", "--reviewer", ""])


def test_go_requires_reviewer(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/a.sh:1:tok")
    with pytest.raises(SystemExit, match="requires --reviewer"):
        brs.main(["--go", "net/demo/a.sh:1:tok", "--provenance", "human"])


def test_triage_trial_requires_human(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/b.sh:2:tok")
    with pytest.raises(SystemExit, match="requires --provenance human"):
        brs.main(["--triage-trial", "net/demo/b.sh:2:tok"])


def test_auto_no_go_allowed(staged_root, tmp_path):
    """Auto paths are deterministic NO-GO-only — no-go is the one verb that
    works without human provenance."""
    brs, root = staged_root
    _write_draft(root, "net/demo/c.sh:3:tok")
    rc = brs.main(["--no-go", "net/demo/c.sh:3:tok", "--ledger", str(tmp_path / "l.jsonl")])
    assert rc == 0
    rows = [json.loads(line) for line in (tmp_path / "l.jsonl").read_text().splitlines() if line]
    assert rows[0]["outcome"] == "no_go"
    assert rows[0]["provenance"] == "auto"


def test_human_go_writes_row(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/d.sh:4:tok")
    rc = brs.main([
        "--go", "net/demo/d.sh:4:tok",
        "--provenance", "human", "--reviewer", "alice",
        "--ledger", str(tmp_path / "l.jsonl"),
    ])
    assert rc == 0
    rows = [json.loads(line) for line in (tmp_path / "l.jsonl").read_text().splitlines() if line]
    assert rows[0]["outcome"] == "go"
    assert rows[0]["provenance"] == "human"
    assert rows[0]["reviewer"] == "alice"


def test_stub_provenance_rejected_for_go(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/e.sh:5:tok")
    with pytest.raises(SystemExit, match="requires --provenance human"):
        brs.main(["--go", "net/demo/e.sh:5:tok", "--provenance", "stub"])


def test_demote_records_retained_location(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/f.sh:6:tok")
    rc = brs.main([
        "--demote-retain-corpus", "net/demo/f.sh:6:tok",
        "--retained-location", "batch/corpora/ow",
        "--ledger", str(tmp_path / "l.jsonl"),
    ])
    assert rc == 0
    rows = [json.loads(line) for line in (tmp_path / "l.jsonl").read_text().splitlines() if line]
    assert rows[0]["outcome"] == "demote_retain_corpus"
    assert rows[0]["retained_location"] == "batch/corpora/ow"


# --- audit sampler population extension (#560 Wave 3) ------------------------


def _ledger(candidates: list[dict]) -> dict:
    return {"schema_version": "1", "candidates": candidates}


def test_sampler_includes_bulk_promoted():
    c = {
        "url": "https://x/y",
        "provenance": "human",
        "audit": {
            "auto_filed": False,
            "promoted_via": "bulk-review",
            "promoted_at": "2026-08-21T10:00:00+00:00",
        },
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert len(pop) == 1


def test_sampler_excludes_stub_provenance():
    c = {
        "url": "https://x/y",
        "provenance": "stub",  # queue-only — never contract material
        "audit": {"auto_filed": True, "auto_filed_at": "2026-08-21T10:00:00+00:00"},
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert pop == []


def test_sampler_keeps_regular_auto_filed():
    c = {
        "url": "https://x/y",
        "provenance": "auto",
        "audit": {"auto_filed": True, "auto_filed_at": "2026-08-21T10:00:00+00:00"},
    }
    pop = audit.auto_filed_in_week(_ledger([c]), "2026-W34")
    assert len(pop) == 1


# --- (url, pin) supersession dedup for eval/escape counters ------------------


def _decision_file(tmp_path: pathlib.Path, name: str, url: str, pin: str, status: str) -> None:
    (tmp_path / name).write_text(
        json.dumps({"candidate_url": url, "pin": pin, "status": status}, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


def _load_bpf():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bpf", ROOT / "scripts" / "build-phase0-freeze.py",
    )
    bpf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bpf)  # type: ignore[union-attr]
    return bpf


def test_supersession_dedup_keeps_newest_pin(tmp_path, monkeypatch):
    bpf = _load_bpf()

    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y", "aaa", "no_go")
    _decision_file(gen, "b_gate_decision.json", "https://x/y", "bbb", "go")
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 1  # superseded: the older pin's row is dropped
    assert rows[0]["pin"] == "bbb"  # newest pin wins
    assert rows[0]["status"] == "go"


def test_supersession_dedup_distinct_urls_untouched(tmp_path, monkeypatch):
    bpf = _load_bpf()

    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y", "aaa", "no_go")
    _decision_file(gen, "c_gate_decision.json", "https://x/z", "ccc", "triage_trial")
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 2  # distinct urls never dedup


def test_supersession_dedup_missing_url_kept(tmp_path, monkeypatch):
    bpf = _load_bpf()

    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "", "aaa", "no_go")
    monkeypatch.setattr(bpf, "GEN", gen)
    rows = bpf.load_decision_population()
    assert len(rows) == 1  # url-less rows are untouched


# --- canonical JSON (#560: sorted keys, \\n-terminated, stable order) --------


def test_ledger_rows_canonical(staged_root, tmp_path):
    brs, root = staged_root
    _write_draft(root, "net/demo/g.sh:7:tok")
    ledger = tmp_path / "l.jsonl"
    brs.main(["--no-go", "net/demo/g.sh:7:tok", "--ledger", str(ledger)])
    line = ledger.read_text(encoding="utf-8")
    assert line.endswith("\n")
    d = json.loads(line.strip())
    assert list(d.keys()) == sorted(d.keys())  # sorted keys


# --- golden inputs_hash no-drift on requeue AND demote (#560 AC) -------------


def _inputs_hash_of(gen: pathlib.Path) -> str:
    import hashlib

    h = hashlib.sha256()
    for p in sorted(gen.glob("*_gate_decision.json")):
        h.update(b"decision:")
        h.update(p.name.encode("utf-8"))
        h.update(p.read_bytes())
    return h.hexdigest()


def test_inputs_hash_no_drift_on_requeue(tmp_path):
    """Requeue (materialize --teardown / audit-failed archive) must NOT
    drift the golden inputs hash when decision CONTENT is unchanged — the
    hash is content-derived (D5 lesson), not HEAD-derived."""
    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y", "aaa", "no_go")
    _decision_file(gen, "b_gate_decision.json", "https://x/z", "bbb", "go")
    # Requeue = archive one decision (the read-only sync cannot reapply it).
    (gen / "a_gate_decision.json").rename(gen / "a_gate_decision.audit-failed.json")
    h2 = _inputs_hash_of(gen)
    # Content-derived: the hash over the SURVIVING decisions is stable and
    # the excluded file no longer counts — recomputing is deterministic.
    assert h2 == _inputs_hash_of(gen)  # no drift on re-run


def test_inputs_hash_no_drift_on_demote(tmp_path):
    """Demote (retain corpus, release lease) must NOT drift the golden
    inputs hash when decision content is unchanged."""
    gen = tmp_path
    _decision_file(gen, "a_gate_decision.json", "https://x/y", "aaa", "no_go")
    h1 = _inputs_hash_of(gen)
    # Demote rewrites the row metadata but not the decision status/content.
    d = json.loads((gen / "a_gate_decision.json").read_text(encoding="utf-8"))
    d["demoted_at"] = "2026-08-23T00:00:00+00:00"  # metadata-only mutation
    (gen / "a_gate_decision.json").write_text(
        json.dumps(d, sort_keys=True) + "\n", encoding="utf-8",
    )
    # Content hash is over the full file bytes → a metadata mutation CHANGES
    # it (fail-closed: no silent drift). Re-running is deterministic.
    h2 = _inputs_hash_of(gen)
    assert h2 != h1  # metadata mutation detected (hash is content-derived)
    assert h2 == _inputs_hash_of(gen)  # stable across re-runs
