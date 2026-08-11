"""Phase 4 corpus sweep (design #213 P4 + S4 + S14 + metric 8, #220).

Every stock-unknown property is classified into EXACTLY ONE of the four
explicit buckets (S4 — distinct buckets, escalated-unconfirmed is never folded
into proven or still-unknown):

    proven                 noodler decided + expectation holds + cross-check
                           agrees (tier cross-checked) OR noodler unsat holding
                           with an abstained cross-check is NOT proven — see
                           classify() for the exact table
    finding                noodler sat counterexample with a D16-validated
                           witness
    escalated-unconfirmed  noodler decided but the cross-check leg abstained
                           or was absent (tier escalated-unconfirmed)
    still-unknown          noodler abstained (or the binary is absent — the
                           sweep records the environment honestly)

Outputs (published with the sweep report):
- versioned corpus manifest: commit + paths + sha256 (schema from Phase 1)
- the four-bucket classification with per-property evidence
- residual-undetectable counts (metric 8: noodler-only / ECMA-route /
  cvc5-abstained)
- divergence rate → the D10 decision record (reopen trigger evaluated)
- triage audit: every disagreement needs an "explained" record (sha256 +
  structured reason, S14); zero unexplained allowed
- the U9 publication: keep/drop is re-decided ONLY on the documented reopen
  trigger (a newly discovered fwlive pattern lacking a standard-encoding
  mirror) — otherwise the Phase-1 DROP decision stands
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# The four explicit buckets (S4 — exact values, schema-asserted)
BUCKET_PROVEN = "proven"
BUCKET_FINDING = "finding"
BUCKET_ESCALATED = "escalated-unconfirmed"
BUCKET_UNKNOWN = "still-unknown"
BUCKETS = (BUCKET_PROVEN, BUCKET_FINDING, BUCKET_ESCALATED, BUCKET_UNKNOWN)

# Residual-undetectable classes (metric 8)
M8_NOODLER_ONLY = "noodler-only"
M8_ECMA_ROUTE = "ecma-route"
M8_CVC5_ABSTAINED = "cvc5-abstained"


@dataclass
class Classification:
    bucket: str
    noodler_verdict: Optional[str]
    cross_check_verdict: Optional[str]
    cross_check_abstained: bool = False
    cross_check_absent: bool = False
    disagreement: bool = False
    witness_d16_valid: bool = False
    evidence: dict = field(default_factory=dict)

    def to_record(self) -> dict:
        return {
            "bucket": self.bucket,
            "noodler_verdict": self.noodler_verdict,
            "cross_check_verdict": self.cross_check_verdict,
            "cross_check_abstained": self.cross_check_abstained,
            "cross_check_absent": self.cross_check_absent,
            "disagreement": self.disagreement,
            "witness_d16_valid": self.witness_d16_valid,
        }


def classify(result: dict) -> Classification:
    """Classify ONE run_one result record into exactly one bucket (S4).

    The bucket decision uses the RAW evidence (never the derived tier — the
    tier is report-time; the bucket is the sweep's classification of the
    evidence).
    """
    noodler = result.get("noodler_verdict")
    ok = result.get("ok")
    not_proven = result.get("not_proven", False)
    disagreement = result.get("disagreement", False)
    cc_abstained = result.get("cross_check_abstained", False)
    cc_absent = result.get("cross_check_absent", False)
    cc_verdict = result.get("cross_check_verdict")
    witness = result.get("witness") or {}
    d16 = result.get("d16_revalidated", False)

    if not_proven or noodler is None or str(noodler).startswith("ABSTAIN") \
            or noodler == "unknown" or noodler == "ABSENT":
        # noodler could not decide (or the binary was absent → triage_fallback
        # → the record carries the STOCK verdict; noodler_verdict == "ABSENT")
        if noodler == "ABSENT":
            return Classification(BUCKET_UNKNOWN, "ABSENT", None,
                                  evidence={"reason": "binary absent"})
        return Classification(BUCKET_UNKNOWN, noodler, cc_verdict,
                              cross_check_abstained=cc_abstained,
                              cross_check_absent=cc_absent,
                              evidence={"reason": "noodler abstained"})

    if disagreement:
        # a genuine disagreement is a HARD FAIL — it is not folded into any
        # bucket silently; the sweep records it under still-unknown with the
        # triage-audit requirement (S14)
        return Classification(BUCKET_UNKNOWN, noodler, cc_verdict,
                              disagreement=True,
                              evidence={"reason": "disagreement (triage required)"})

    if noodler == "sat":
        if not (witness and d16):
            # sat without a D16-validated witness is unusable (S2/D16)
            return Classification(BUCKET_UNKNOWN, noodler, cc_verdict,
                                  cross_check_abstained=cc_abstained,
                                  cross_check_absent=cc_absent,
                                  evidence={"reason": "witness-unvalidated"})
        return Classification(BUCKET_FINDING, noodler, cc_verdict,
                              witness_d16_valid=True)

    # noodler == "unsat" (decided)
    holds = bool(ok)  # expect_unsat match
    if cc_abstained or cc_absent:
        # decided but the cross-check leg did not confirm → escalated-unconfirmed
        return Classification(BUCKET_ESCALATED, noodler, cc_verdict,
                              cross_check_abstained=cc_abstained,
                              cross_check_absent=cc_absent)
    if cc_verdict == "unsat":
        return Classification(BUCKET_PROVEN, noodler, cc_verdict)
    # cross-check absent/abstained already handled; disagreeing concrete
    # verdicts were handled above; reaching here = cc decided something else
    return Classification(BUCKET_ESCALATED, noodler, cc_verdict,
                          cross_check_abstained=cc_abstained,
                          evidence={"reason": f"cross-check {cc_verdict}"})


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(commit: str, paths: list[Path]) -> dict:
    """Versioned corpus manifest (schema from Phase 1: commit + paths +
    hashes)."""
    return {
        "schema_version": 1,
        "commit": commit,
        "files": [
            {"path": str(p), "sha256": sha256_file(p)} for p in paths
        ],
    }


def verify_manifest(manifest: dict) -> list[str]:
    """Verify the manifest against disk; returns a list of mismatches (empty
    = verified)."""
    problems = []
    for f in manifest.get("files", []):
        p = Path(f["path"])
        if not p.is_file():
            problems.append(f"{f['path']}: missing")
            continue
        if sha256_file(p) != f["sha256"]:
            problems.append(f"{f['path']}: sha256 mismatch")
    return problems


def metric8(results: list[dict]) -> dict:
    """Residual-undetectable counts (metric 8)."""
    m = {M8_NOODLER_ONLY: 0, M8_ECMA_ROUTE: 0, M8_CVC5_ABSTAINED: 0}
    for r in results:
        if r.get("cross_check_abstained") or r.get("cross_check_absent"):
            m[M8_CVC5_ABSTAINED] += 1
        if r.get("cross_check_reason", "").startswith("re.loop-cap"):
            m[M8_NOODLER_ONLY] += 1
    # ECMA-route: 0 post-U9-DROP (no ECMA leg exists)
    return m


def divergence_rate(results: list[dict]) -> dict:
    """D10 divergence-rate record: decided cross-check pairs vs disagreements."""
    decided = [r for r in results
               if r.get("cross_check_verdict") is not None]
    disagreed = [r for r in decided if r.get("disagreement")]
    return {
        "decided_pairs": len(decided),
        "disagreements": len(disagreed),
        "divergence_rate": round(len(disagreed) / len(decided), 4)
        if decided else None,
    }


def triage_audit(records: list[dict], manifest: dict) -> dict:
    """S14 triage audit: every disagreement must carry an 'explained' record
    (sha256 + structured reason). Returns the audit summary."""
    explained = 0
    unexplained = []
    for rec in records:
        if rec.get("disagreement"):
            tr = rec.get("triage") or {}
            if tr.get("sha256") and tr.get("reason"):
                explained += 1
            else:
                unexplained.append(rec.get("name", "?"))
    return {
        "disagreements": explained + len(unexplained),
        "explained": explained,
        "unexplained": unexplained,
        "manifest_verified": len(verify_manifest(manifest)) == 0,
    }


def u9_publication(reopen_trigger_hit: bool, evidence: dict) -> dict:
    """The U9 publication against the sweep evidence. A NEW keep/drop decision
    is reserved ONLY for the documented reopen trigger (a newly discovered
    fwlive pattern lacking a standard-encoding mirror)."""
    return {
        "decision": "DROP (from_ecma2020 out of scope)" if not reopen_trigger_hit
        else "REOPEN — new decision required",
        "reopen_trigger_hit": reopen_trigger_hit,
        "evidence": evidence,
    }


def render_report(manifest: dict, records: list[dict], m8: dict,
                  d10: dict, audit: dict, u9: dict) -> str:
    """Render the sweep report (the published artifact)."""
    from collections import Counter

    buckets = Counter(r["classification"]["bucket"] for r in records)
    lines = [
        "# Phase 4 sweep report (P4, #220)",
        "",
        f"- corpus commit: `{manifest['commit']}`",
        f"- manifest files: {len(manifest['files'])} (schema v1: commit + paths + sha256)",
        f"- manifest verified: {audit['manifest_verified']}",
        "",
        "## Four-bucket classification (S4)",
        "",
        "| property | bucket | noodler | cvc5 | evidence |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(records, key=lambda x: x["name"]):
        c = r["classification"]
        lines.append(
            f"| {r['name']} | {c['bucket']} | {c['noodler_verdict']} | "
            f"{c['cross_check_verdict'] or r.get('cross_check_reason') or '-'} | "
            f"{c.get('reason') or '-'} |"
        )
    lines += [
        "",
        f"Bucket counts: proven={buckets[BUCKET_PROVEN]}, "
        f"finding={buckets[BUCKET_FINDING]}, "
        f"escalated-unconfirmed={buckets[BUCKET_ESCALATED]}, "
        f"still-unknown={buckets[BUCKET_UNKNOWN]} (exactly one per property, S4)",
        "",
        "## Residual-undetectable (metric 8)",
        "",
        f"- noodler-only: {m8[M8_NOODLER_ONLY]}",
        f"- ecma-route: {m8[M8_ECMA_ROUTE]} (0 post-U9-DROP — no ECMA leg)",
        f"- cvc5-abstained: {m8[M8_CVC5_ABSTAINED]}",
        "",
        "## Divergence rate (D10)",
        "",
        f"- decided cross-check pairs: {d10['decided_pairs']}",
        f"- disagreements: {d10['disagreements']}",
        f"- divergence rate: {d10['divergence_rate']}",
        "",
        "## Triage audit (S14)",
        "",
        f"- disagreements: {audit['disagreements']}, explained: {audit['explained']}, "
        f"unexplained: {audit['unexplained'] or 'none'}",
        "",
        "## U9 publication",
        "",
        f"- decision: **{u9['decision']}**",
        f"- reopen trigger hit: {u9['reopen_trigger_hit']}",
        f"- evidence: {json.dumps(u9['evidence'])}",
        "",
    ]
    return "\n".join(lines)
