"""Phase 4 corpus sweep (PR A): the four-bucket classification (S4), the
versioned manifest, metric 8, D10 divergence rate + decision, S14 triage
audit (enforced), U9 publication (consumed).

AC coverage (issue #220):
- every stock-unknown property classified into EXACTLY one of the four buckets
  (exact values: proven / finding / escalated-unconfirmed / still-unknown);
  the schema assertion covers all four; escalated-unconfirmed is never folded
  into proven or still-unknown
- residual-undetectable counts stated (metric 8 — disjoint classes)
- divergence rate → D10 decision record (with threshold + action)
- triage audit: zero unexplained disagreements; "explained" is ENFORCED
  (64-hex sha256 + structured reason)
- U9 decision CONSUMED from the committed artifact; a new decision only on
  the reopen trigger
- versioned corpus manifest (commit + repo-relative paths + hashes) consumed
  and published; verification works from any checkout
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from regexproof.harness.sweep import (
    BUCKET_ESCALATED,
    BUCKET_FINDING,
    BUCKET_PROVEN,
    BUCKET_UNKNOWN,
    BUCKETS,
    M8_CVC5_ABSTAINED,
    M8_ECMA_ROUTE,
    M8_NOODLER_ONLY,
    build_manifest,
    classify,
    d10_decision,
    divergence_rate,
    metric8,
    triage_audit,
    u9_publication,
    verify_manifest,
)


def _res(**kw):
    base = {"noodler_verdict": None, "ok": False, "not_proven": False,
            "disagreement": False, "wrong_verdict_event": False,
            "cross_check_abstained": False, "cross_check_absent": False,
            "cross_check_verdict": None, "witness": None,
            "d16_revalidated": False, "route": "mirror"}
    base.update(kw)
    return base


# --- the four buckets: exact values + distinctness (S4) ----------------------
def test_bucket_exact_values_and_distinctness():
    assert BUCKETS == ("proven", "finding", "escalated-unconfirmed",
                       "still-unknown")


def test_proven_requires_cross_checked_unsat():
    c = classify(_res(noodler_verdict="unsat", ok=True,
                      cross_check_verdict="unsat"))
    assert c.bucket == BUCKET_PROVEN


def test_proven_requires_route_mirror():
    # S3 guard inside the sweep (luna r1 on #234): a non-mirror route fails
    # the proven assignment even with agreeing verdicts.
    c = classify(_res(noodler_verdict="unsat", ok=True,
                      cross_check_verdict="unsat", route="ecma"))
    assert c.bucket == BUCKET_ESCALATED


def test_proven_requires_expectation_holds():
    # an unsat that CONTRADICTS the declared expectation is never proven
    # (luna r1 on #234 — the unused `holds` variable)
    c = classify(_res(noodler_verdict="unsat", ok=False,
                      cross_check_verdict="unsat"))
    assert c.bucket == BUCKET_ESCALATED
    assert "expectation not satisfied" in c.to_record()["reason"]


def test_proven_without_cross_check_is_escalated():
    # decided but cross-check abstained → escalated-unconfirmed, NEVER folded
    # into proven (S4)
    c = classify(_res(noodler_verdict="unsat", ok=True,
                      cross_check_abstained=True))
    assert c.bucket == BUCKET_ESCALATED
    c2 = classify(_res(noodler_verdict="unsat", ok=True,
                       cross_check_absent=True))
    assert c2.bucket == BUCKET_ESCALATED


def test_finding_requires_d16_validated_witness():
    c = classify(_res(noodler_verdict="sat", witness={"u": "x"},
                      d16_revalidated=True))
    assert c.bucket == BUCKET_FINDING
    # sat without a valid witness → still-unknown (unusable, S2)
    c2 = classify(_res(noodler_verdict="sat", witness={"u": "x"},
                       d16_revalidated=False))
    assert c2.bucket == BUCKET_UNKNOWN
    assert "witness-unvalidated" in c2.to_record()["reason"]


def test_still_unknown_abstains_and_absence():
    c = classify(_res(noodler_verdict="ABSTAIN-TIMEOUT", not_proven=True))
    assert c.bucket == BUCKET_UNKNOWN
    c2 = classify(_res(noodler_verdict="ABSENT"))
    assert c2.bucket == BUCKET_UNKNOWN
    assert "absent" in c2.to_record()["reason"]


def test_disagreement_is_still_unknown_with_triage_requirement():
    c = classify(_res(noodler_verdict="sat", cross_check_verdict="unsat",
                      disagreement=True, witness={"u": "x"},
                      d16_revalidated=True))
    assert c.bucket == BUCKET_UNKNOWN
    assert c.disagreement is True
    assert "triage required" in c.to_record()["reason"]


def test_every_combination_lands_in_exactly_one_bucket():
    import itertools

    combos = list(itertools.product(
        ("unsat", "sat", "unknown", "ABSTAIN-TIMEOUT", "ABSENT"),
        (True, False),              # cross_check_abstained
        (True, False),              # cross_check_absent
        (None, "unsat", "sat"),     # cross_check_verdict
        (True, False),              # d16
        (True, False),              # ok
    ))
    for (nd, abst, abs, ccv, d16, ok) in combos:
        r = _res(noodler_verdict=nd,
                 not_proven=(nd in ("unknown", "ABSTAIN-TIMEOUT")),
                 cross_check_abstained=abst, cross_check_absent=abs,
                 cross_check_verdict=ccv, d16_revalidated=d16, ok=ok)
        c = classify(r)
        assert c.bucket in BUCKETS, (nd, abst, abs, ccv, d16, ok)
        # escalated-unconfirmed is never folded into proven or still-unknown
        if c.bucket == BUCKET_ESCALATED:
            assert r["noodler_verdict"] not in ("unknown", "ABSTAIN-TIMEOUT", "ABSENT")


# --- manifest -----------------------------------------------------------------
def test_manifest_build_and_verify(tmp_path):
    f1 = tmp_path / "a.txt"
    f1.write_text("hello")
    m = build_manifest("abc123", [f1], tmp_path)
    assert m["schema_version"] == 1
    assert m["commit"] == "abc123"
    assert m["files"][0]["path"] == "a.txt"  # repo-relative
    assert m["files"][0]["sha256"] == hashlib.sha256(b"hello").hexdigest()
    assert verify_manifest(m, tmp_path) == []
    f1.write_text("tampered")
    assert len(verify_manifest(m, tmp_path)) == 1  # sha256 mismatch detected


def test_manifest_verifies_from_any_checkout(tmp_path):
    # repo-relative paths make verification work from a different root (luna r1)
    f1 = tmp_path / "a.txt"
    f1.write_text("hello")
    m = build_manifest("abc", [f1], tmp_path)
    other = tmp_path / "other-checkout"
    other.mkdir()
    (other / "a.txt").write_text("hello")  # same content, different root
    assert verify_manifest(m, other) == []


def test_manifest_missing_file_detected(tmp_path):
    f1 = tmp_path / "a.txt"
    f1.write_text("hello")
    m = build_manifest("abc", [f1], tmp_path)
    f1.unlink()
    assert verify_manifest(m, tmp_path) == ["a.txt: missing"]


def test_manifest_path_escape_rejected(tmp_path, monkeypatch):
    """#544: a manifest path must not escape the repo root — an outside
    target must be reported and never probed (no hash oracle)."""
    outside = tmp_path / "outside.txt"
    outside.write_text("secret")
    m = {
        "files": [
            {"path": "../../outside.txt", "sha256": "0" * 64},
        ]
    }
    calls: list[str] = []
    import regexproof.harness.sweep as sweep

    monkeypatch.setattr(
        sweep,
        "sha256_file",
        lambda p: (calls.append(str(p)) or "x"),
    )
    problems = verify_manifest(m, tmp_path)
    assert problems == ["../../outside.txt: outside root"], problems
    assert calls == [], f"outside path was probed: {calls}"


def test_manifest_symlink_rejected(tmp_path):
    """#544: a symlink anywhere under root must be rejected, not followed."""
    (tmp_path / "real.txt").write_text("hello")
    (tmp_path / "link.txt").symlink_to(tmp_path / "real.txt")
    m = {
        "files": [
            {"path": "link.txt", "sha256": hashlib.sha256(b"hello").hexdigest()},
        ]
    }
    assert verify_manifest(m, tmp_path) == ["link.txt: symlink rejected"]

    # symlink pointing OUTSIDE the root is caught by the symlink check
    # (and would be by containment even if followed).
    outside = tmp_path / "out" / "target.txt"
    outside.parent.mkdir()
    outside.write_text("secret")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "esc.txt").symlink_to(outside)
    m2 = {
        "files": [
            {"path": "sub/esc.txt", "sha256": "0" * 64},
        ]
    }
    assert verify_manifest(m2, tmp_path) == ["sub/esc.txt: symlink rejected"]


def test_corpus_commit_is_stable_sha():
    # the corpus commit is the last commit touching the corpus files — a
    # 40-hex sha that does NOT track the sweep's own HEAD (luna r2 on #234)
    from regexproof.harness.sweep import corpus_commit

    ROOT = Path(__file__).resolve().parents[1]
    commit = corpus_commit(ROOT, [ROOT / "README.md"])
    assert len(commit) == 40
    import re

    assert re.fullmatch(r"[0-9a-f]{40}", commit)


# --- metric 8 + D10 + triage audit + U9 -------------------------------------
def test_metric8_disjoint_classes():
    # re.loop-cap and absent are cvc5-side abstentions — NEVER noodler-only
    # (luna r1 on #234)
    res = [_res(cross_check_abstained=True),
           _res(cross_check_absent=True),
           _res(cross_check_verdict="unsat"),
           _res(cross_check_reason="re.loop-cap (17)")]
    m = metric8(res)
    assert m[M8_CVC5_ABSTAINED] == 3
    assert m[M8_NOODLER_ONLY] == 0
    assert m[M8_ECMA_ROUTE] == 0  # post-U9-DROP: no ECMA leg


def test_divergence_rate_counts_wrong_verdict_events():
    # a wrong-verdict event IS a divergent pair (concrete mismatch, resolved
    # by reproduction) — luna r1 on #234
    res = [_res(cross_check_verdict="unsat"),
           _res(cross_check_verdict="unsat", disagreement=True),
           _res(cross_check_verdict="sat", wrong_verdict_event=True)]
    d = divergence_rate(res)
    assert d["decided_pairs"] == 3
    assert d["disagreements"] == 1
    assert d["wrong_verdict_events"] == 1
    assert d["divergent_pairs"] == 2
    assert d["divergence_rate"] == pytest.approx(2 / 3, abs=1e-4)


def test_d10_decision_records():
    d = d10_decision(divergence_rate([_res(cross_check_verdict="unsat")]))
    assert "KEEP" in d["decision"] and "zero divergence" in d["decision"]
    d2 = d10_decision(divergence_rate(
        [_res(cross_check_verdict="unsat", disagreement=True)]))
    assert "KEEP-WITH-GATE" in d2["decision"]
    d3 = d10_decision(divergence_rate([]))
    assert "NO-DECIDED-PAIRS" in d3["decision"]


def test_triage_audit_explained_is_enforced(tmp_path):
    # 'explained' is FILE-BACKED (luna r2 on #234): the sha256 must hash an
    # existing repository file (the committed triage record).
    rec_file = tmp_path / "triage-record.json"
    rec_file.write_text("{}")
    good_sha = hashlib.sha256(rec_file.read_bytes()).hexdigest()
    records = [
        {"name": "a", "disagreement": True,
         "triage": {"sha256": good_sha, "record_path": rec_file.name,
                    "reason": "cvc5 re-loop parse gap (17) — verified"}},
        {"name": "b", "disagreement": True,
         "triage": {"sha256": "ab" * 32, "record_path": rec_file.name,
                    "reason": "long enough reason text"}},  # hash mismatch
        {"name": "c", "disagreement": True,
         "triage": {"sha256": good_sha, "record_path": rec_file.name,
                    "reason": "short"}},  # reason too short
        {"name": "d", "disagreement": True},
        {"name": "e", "disagreement": False},
    ]
    audit = triage_audit(records, {"files": []}, tmp_path)
    assert audit["disagreements"] == 4
    assert audit["explained"] == 1
    assert audit["unexplained"] == ["b", "c", "d"]


def test_triage_audit_rejects_out_of_tree_record(tmp_path):
    # the triage record must live INSIDE the repo root (luna r3 on #234)
    outside = tmp_path.parent / "outside-record.json"
    outside.write_text("{}")
    good_sha = hashlib.sha256(outside.read_bytes()).hexdigest()
    records = [{"name": "x", "disagreement": True,
                "triage": {"sha256": good_sha,
                           "record_path": str(outside),
                           "reason": "long enough structured reason text"}}]
    audit = triage_audit(records, {"files": []}, tmp_path)
    assert audit["unexplained"] == ["x"]


def test_triage_audit_rejects_filler_reason(tmp_path):
    # a filler reason (repetition) must fail the structure check (luna r4)
    rec_file = tmp_path / "triage-record.json"
    rec_file.write_text("{}")
    good_sha = hashlib.sha256(rec_file.read_bytes()).hexdigest()
    records = [{"name": "x", "disagreement": True,
                "triage": {"sha256": good_sha, "record_path": rec_file.name,
                           "reason": "same same same same same same same"}}]
    audit = triage_audit(records, {"files": []}, tmp_path)
    assert audit["unexplained"] == ["x"]


def test_u9_publication_consumes_decision_file(tmp_path):
    d = tmp_path / "u9-decision.md"
    d.write_text("# U9 decision\n\n## Decision: **DROP** the from_ecma2020 branch.\n")
    p = u9_publication(d, reopen_trigger_hit=False, evidence={"x": 1})
    assert "DROP" in p["decision"]
    assert p["consumed_artifact"] == str(d)
    p2 = u9_publication(d, reopen_trigger_hit=True, evidence={"x": 1})
    assert "REOPEN" in p2["decision"]


def test_u9_publication_keep_mentioning_drop_fails(tmp_path):
    # a KEEP decision that merely MENTIONS the DROP flip criterion must NOT
    # publish as DROP (luna r3 on #234)
    d = tmp_path / "u9-decision.md"
    d.write_text("# U9 decision\n\n## Decision: **KEEP** the branch. The DROP\n"
                 "flip criterion was evaluated and not met.\n")
    with pytest.raises(ValueError):
        u9_publication(d, False, {})


def test_u9_publication_missing_file_fails(tmp_path):
    with pytest.raises(FileNotFoundError):
        u9_publication(tmp_path / "nope.md", False, {})


def test_u9_publication_non_drop_file_fails(tmp_path):
    d = tmp_path / "u9-decision.md"
    d.write_text("# not a decision\n")
    with pytest.raises(ValueError):
        u9_publication(d, False, {})
