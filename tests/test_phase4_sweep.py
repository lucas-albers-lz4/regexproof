"""Phase 4 corpus sweep (PR A): the four-bucket classification (S4), the
versioned manifest, metric 8, D10 divergence rate, S14 triage audit, U9
publication.

AC coverage (issue #220):
- every stock-unknown property classified into EXACTLY one of the four buckets
  (exact values: proven / finding / escalated-unconfirmed / still-unknown);
  the schema assertion covers all four; escalated-unconfirmed is never folded
  into proven or still-unknown
- residual-undetectable counts stated (metric 8)
- divergence rate → D10 decision record
- triage audit: zero unexplained disagreements; "explained" requires the
  sha256 + structured reason record
- U9 decision published with sweep evidence; a new decision only on the
  reopen trigger
- versioned corpus manifest (commit + paths + hashes) consumed and published
"""

from __future__ import annotations

import json

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
    divergence_rate,
    metric8,
    triage_audit,
    u9_publication,
    verify_manifest,
)


def _res(**kw):
    base = {"noodler_verdict": None, "ok": False, "not_proven": False,
            "disagreement": False, "cross_check_abstained": False,
            "cross_check_absent": False, "cross_check_verdict": None,
            "witness": None, "d16_revalidated": False}
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
    assert "witness-unvalidated" in c2.evidence["reason"]


def test_still_unknown_abstains_and_absence():
    c = classify(_res(noodler_verdict="ABSTAIN-TIMEOUT", not_proven=True))
    assert c.bucket == BUCKET_UNKNOWN
    c2 = classify(_res(noodler_verdict="ABSENT"))
    assert c2.bucket == BUCKET_UNKNOWN
    assert "absent" in c2.evidence["reason"]


def test_disagreement_is_still_unknown_with_triage_requirement():
    c = classify(_res(noodler_verdict="sat", cross_check_verdict="unsat",
                      disagreement=True, witness={"u": "x"},
                      d16_revalidated=True))
    assert c.bucket == BUCKET_UNKNOWN
    assert c.disagreement is True
    assert "triage required" in c.evidence["reason"]


def test_every_combination_lands_in_exactly_one_bucket():
    import itertools

    combos = list(itertools.product(
        ("unsat", "sat", "unknown", "ABSTAIN-TIMEOUT", "ABSENT"),
        (True, False),              # cross_check_abstained
        (True, False),              # cross_check_absent
        (None, "unsat", "sat"),     # cross_check_verdict
        (True, False),              # d16
    ))
    for (nd, abst, abs, ccv, d16) in combos:
        r = _res(noodler_verdict=nd, not_proven=(nd in ("unknown", "ABSTAIN-TIMEOUT")),
                 cross_check_abstained=abst, cross_check_absent=abs,
                 cross_check_verdict=ccv, d16_revalidated=d16)
        c = classify(r)
        assert c.bucket in BUCKETS, (nd, abst, abs, ccv, d16)
        # escalated-unconfirmed is never folded into proven or still-unknown
        if c.bucket == BUCKET_ESCALATED:
            assert r["noodler_verdict"] not in ("unknown", "ABSTAIN-TIMEOUT", "ABSENT")


# --- manifest -----------------------------------------------------------------
def test_manifest_build_and_verify(tmp_path):
    import hashlib

    f1 = tmp_path / "a.txt"
    f1.write_text("hello")
    m = build_manifest("abc123", [f1])
    assert m["schema_version"] == 1
    assert m["commit"] == "abc123"
    assert m["files"][0]["sha256"] == hashlib.sha256(b"hello").hexdigest()
    assert verify_manifest(m) == []
    f1.write_text("tampered")
    assert len(verify_manifest(m)) == 1  # sha256 mismatch detected


def test_manifest_missing_file_detected(tmp_path):
    f1 = tmp_path / "a.txt"
    f1.write_text("hello")
    m = build_manifest("abc", [f1])
    f1.unlink()
    assert verify_manifest(m) == [f"{tmp_path}/a.txt: missing"]


# --- metric 8 + D10 + triage audit + U9 -------------------------------------
def test_metric8_counts():
    res = [_res(cross_check_abstained=True),
           _res(cross_check_absent=True),
           _res(cross_check_verdict="unsat"),
           _res(cross_check_reason="re.loop-cap (17)")]
    m = metric8(res)
    assert m[M8_CVC5_ABSTAINED] == 2
    assert m[M8_NOODLER_ONLY] == 1
    assert m[M8_ECMA_ROUTE] == 0  # post-U9-DROP: no ECMA leg


def test_divergence_rate():
    res = [_res(cross_check_verdict="unsat"),
           _res(cross_check_verdict="unsat", disagreement=True)]
    d = divergence_rate(res)
    assert d["decided_pairs"] == 2
    assert d["disagreements"] == 1
    assert d["divergence_rate"] == 0.5


def test_triage_audit_explained_requires_sha256_and_reason():
    records = [
        {"name": "a", "disagreement": True,
         "triage": {"sha256": "abc", "reason": "cvc5 re-loop parse gap"}},
        {"name": "b", "disagreement": True, "triage": {"sha256": "abc"}},
        {"name": "c", "disagreement": True},
        {"name": "d", "disagreement": False},
    ]
    audit = triage_audit(records, {"files": []})
    assert audit["disagreements"] == 3
    assert audit["explained"] == 1
    assert audit["unexplained"] == ["b", "c"]


def test_u9_publication_reopen_trigger():
    p = u9_publication(reopen_trigger_hit=False, evidence={"x": 1})
    assert "DROP" in p["decision"]
    p2 = u9_publication(reopen_trigger_hit=True, evidence={"x": 1})
    assert "REOPEN" in p2["decision"]
