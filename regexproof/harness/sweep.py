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
import re
import stat
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
        rec = {
            "bucket": self.bucket,
            "noodler_verdict": self.noodler_verdict,
            "cross_check_verdict": self.cross_check_verdict,
            "cross_check_abstained": self.cross_check_abstained,
            "cross_check_absent": self.cross_check_absent,
            "disagreement": self.disagreement,
            "witness_d16_valid": self.witness_d16_valid,
        }
        if self.evidence:
            rec["reason"] = self.evidence.get("reason")
        return rec


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
    holds = bool(ok)  # the property's expectation is satisfied
    if not holds:
        # an unsat that CONTRADICTS the declared expectation is never proven —
        # escalated at best (the cross-check cannot rescue a failed property)
        return Classification(BUCKET_ESCALATED, noodler, cc_verdict,
                              cross_check_abstained=cc_abstained,
                              cross_check_absent=cc_absent,
                              evidence={"reason": "expectation not satisfied"})
    if cc_abstained or cc_absent:
        # decided but the cross-check leg did not confirm → escalated-unconfirmed
        return Classification(BUCKET_ESCALATED, noodler, cc_verdict,
                              cross_check_abstained=cc_abstained,
                              cross_check_absent=cc_absent)
    if cc_verdict == "unsat" and result.get("route") == "mirror":
        # S4 proven REQUIRES: expectation holds + cross-check agrees + the S3
        # authority guard (explicitly recorded route:"mirror")
        return Classification(BUCKET_PROVEN, noodler, cc_verdict)
    # cross-check absent/abstained already handled; disagreeing concrete
    # verdicts were handled above; reaching here = cc decided something else
    return Classification(BUCKET_ESCALATED, noodler, cc_verdict,
                          cross_check_abstained=cc_abstained,
                          evidence={"reason": f"cross-check {cc_verdict}"})


def _hash_fileobj(fh) -> str:
    h = hashlib.sha256()
    for chunk in iter(lambda: fh.read(65536), b""):
        h.update(chunk)
    return h.hexdigest()


def sha256_file(path: Path) -> str:
    with open(path, "rb") as f:
        return _hash_fileobj(f)


def build_manifest(commit: str, paths: list[Path], root: Path) -> dict:
    """Versioned corpus manifest (schema from Phase 1: commit + paths +
    hashes). Paths are REPO-RELATIVE. `commit` is the CORPUS commit (the last
    commit touching the corpus files — stable across sweep runs; pinning HEAD
    is self-invalidating since committing the refreshed manifest changes
    HEAD, luna r2 on #234)."""
    return {
        "schema_version": 1,
        "commit": commit,
        "files": [
            {"path": str(p.relative_to(root)), "sha256": sha256_file(p)}
            for p in paths
        ],
    }


def corpus_commit(root: Path, paths: list[Path]) -> str:
    """The last commit touching the corpus files (stable — the sweep does not
    modify the corpus, so this does not change when the manifest is
    committed)."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--"] +
        [str(p.relative_to(root)) for p in paths],
        cwd=root, capture_output=True, text=True,
        timeout=60,  # #543: local git op — bound it (runs inside CI gates)
    )
    return out.stdout.strip()


def _has_symlink_component(root: Path, target: Path) -> bool:
    """True if any path component from root to target is a symlink (#544).

    Mirrors the symlink discipline of admission/walk.py (walk skips
    symlinks): verification must not follow a symlink out of the tree.
    Non-existent components are not symlinks (is_symlink is False); the
    missing-file case is reported separately.
    """
    try:
        rel = target.relative_to(root)
    except ValueError:
        return False  # outside root — the containment check reports it
    cur = root
    for part in rel.parts:
        cur = cur / part
        if cur.is_symlink():
            return True
    return False


def verify_manifest(manifest: dict, root: Path) -> list[str]:
    """Verify the manifest against disk (repo-relative paths resolved against
    `root`); returns a list of problems (empty = verified). Issue #544: paths
    must stay under `root` (no ``..`` escapes) and must not traverse
    symlinks — a committed manifest must not act as an existence/hash oracle
    on arbitrary host files."""
    base = root.resolve()
    problems = []
    for f in manifest.get("files", []):
        rel = f["path"]
        raw = root / rel
        if _has_symlink_component(root, raw):
            problems.append(f"{rel}: symlink rejected")
            continue
        p = raw.resolve()
        if not p.is_relative_to(base):
            problems.append(f"{rel}: outside root")
            continue
        # Open ONCE after validation and hash the fd (CodeRabbit r3 fold):
        # reopening by pathname would let a concurrent swap re-point the hash
        # at a different inode than the one validated. O_NOFOLLOW also closes
        # the final-component symlink race; intermediate components were
        # checked by _has_symlink_component.
        try:
            fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
        except FileNotFoundError:
            problems.append(f"{rel}: missing")
            continue
        except OSError:
            problems.append(f"{rel}: unreadable")
            continue
        with os.fdopen(fd, "rb") as fh:
            try:
                if not stat.S_ISREG(os.fstat(fh.fileno()).st_mode):
                    problems.append(f"{rel}: not a regular file")
                    continue
                digest = _hash_fileobj(fh)
            except OSError:
                problems.append(f"{rel}: unreadable")
                continue
        if digest != f["sha256"]:
            problems.append(f"{rel}: sha256 mismatch")
    return problems


def metric8(results: list[dict]) -> dict:
    """Residual-undetectable counts (metric 8). The classes are DISJOINT:
    cvc5-abstained = the cross-check leg abstained OR was absent OR hit the
    D12 re.loop cap (all cvc5-side); noodler-only = properties with NO cvc5
    representation at all (none measured — both sweep classes are
    cvc5-expressible); ecma-route = 0 post-U9-DROP."""
    m = {M8_NOODLER_ONLY: 0, M8_ECMA_ROUTE: 0, M8_CVC5_ABSTAINED: 0}
    for r in results:
        if (r.get("cross_check_abstained") or r.get("cross_check_absent")
                or str(r.get("cross_check_reason", "")).startswith("re.loop-cap")):
            m[M8_CVC5_ABSTAINED] += 1
    return m


def divergence_rate(results: list[dict]) -> dict:
    """D10 divergence-rate record: decided cross-check pairs vs DIVERGENT
    pairs. A divergent pair is a hard disagreement OR a wrong-verdict event
    (both are concrete mismatches — the reproduction outcome only decides
    whether the mismatch is fatal)."""
    decided = [r for r in results
               if r.get("cross_check_verdict") is not None]
    divergent = [r for r in decided
                 if r.get("disagreement") or r.get("wrong_verdict_event")]
    return {
        "decided_pairs": len(decided),
        "divergent_pairs": len(divergent),
        "disagreements": len([r for r in decided if r.get("disagreement")]),
        "wrong_verdict_events": len(
            [r for r in decided if r.get("wrong_verdict_event")]),
        "divergence_rate": round(len(divergent) / len(decided), 4)
        if decided else None,
    }


def d10_decision(d10: dict) -> dict:
    """The D10 DECISION record (pre-committed threshold: any divergent pair
    keeps the disagreement machinery as the hard gate; a zero rate confirms
    the cross-check leg agrees on the measured set)."""
    rate = d10["divergence_rate"]
    if rate is None:
        decision = "NO-DECIDED-PAIRS — cross-check leg abstained everywhere; " \
                   "the machinery stays the gate by default"
    elif d10["divergent_pairs"] == 0:
        decision = "KEEP — zero divergence on the measured set; the " \
                   "cross-check agrees and the disagreement gate is dormant"
    else:
        decision = "KEEP-WITH-GATE — divergence present; the mechanical " \
                   "reproduction rule + exit 2 stay the hard gate (no silent " \
                   "convergence)"
    return {"decision": decision, "rate": rate,
            "threshold": "any divergent pair keeps the gate"}


def triage_audit(records: list[dict], manifest: dict, root: Path) -> dict:
    """S14 triage audit: every disagreement must carry an 'explained' record.
    'explained' is ENFORCED: the sha256 must be a 64-hex hash and the reason a
    non-empty structured string (format-validated, not just present)."""
    import re

    explained = 0
    unexplained = []
    for rec in records:
        if rec.get("disagreement"):
            tr = rec.get("triage") or {}
            # 'explained' is FILE-BACKED + REPO-BOUND (luna r2/r3 on #234):
            # the sha256 must hash an existing repository file (the committed
            # triage record) INSIDE the repo root — shape-only hashes and
            # out-of-tree paths fail
            sha = str(tr.get("sha256") or "")
            record_path = (root / str(tr.get("record_path") or "")).resolve()
            # containment via is_relative_to (a startswith prefix check is
            # vulnerable to sibling-prefix paths, luna r4 on #234)
            in_repo = record_path.is_relative_to(root.resolve())
            sha_ok = bool(re.fullmatch(r"[0-9a-f]{64}", sha)) and \
                in_repo and record_path.is_file() and \
                sha256_file(record_path) == sha
            # a structured reason: non-trivial length AND at least three
            # distinct tokens (filler/repetition fails, luna r4 on #234)
            rsn = str(tr.get("reason") or "")
            reason_ok = len(rsn) >= 20 and len(set(rsn.split())) >= 3
            if sha_ok and reason_ok:
                explained += 1
            else:
                unexplained.append(rec.get("name", "?"))
    return {
        "disagreements": explained + len(unexplained),
        "explained": explained,
        "unexplained": unexplained,
        "manifest_verified": len(verify_manifest(manifest, root)) == 0,
    }


def u9_publication(decision_file: Path, reopen_trigger_hit: bool,
                   evidence: dict) -> dict:
    """The U9 publication against the sweep evidence. CONSUMES the committed
    Phase-1 decision artifact (u9-decision.md must exist and carry the DROP
    decision — a missing/divergent file is a failure, not a silent re-decide).
    A NEW keep/drop decision is reserved ONLY for the documented reopen
    trigger (a newly discovered fwlive pattern lacking a standard-encoding
    mirror)."""
    if not decision_file.is_file():
        raise FileNotFoundError(
            f"U9 decision artifact missing: {decision_file} — the sweep "
            "consumes the committed decision, never re-decides silently")
    text = decision_file.read_text()
    # the DECISION STATEMENT must say DROP (luna r3 on #234: a KEEP decision
    # that merely MENTIONS the DROP flip criterion must not pass)
    if not re.search(r"##\s*Decision:\s*\*{0,2}DROP", text, re.IGNORECASE):
        raise ValueError("U9 decision artifact does not carry a DROP decision "
                         "statement (## Decision: DROP …) — refusing to publish")
    return {
        "decision": "DROP (from_ecma2020 out of scope)" if not reopen_trigger_hit
        else "REOPEN — new decision required",
        "reopen_trigger_hit": reopen_trigger_hit,
        "consumed_artifact": str(decision_file),
        "evidence": evidence,
    }


def render_report(manifest: dict, records: list[dict], m8: dict,
                  d10: dict, d10dec: dict, audit: dict, u9: dict) -> str:
    """Render the sweep report (the published artifact)."""
    from collections import Counter

    buckets = Counter(r["classification"]["bucket"] for r in records)
    lines = [
        "# Phase 4 sweep report (P4, #220)",
        "",
        f"- corpus commit: `{manifest['commit']}`",
        f"- manifest files: {len(manifest['files'])} (schema v1: commit + repo-relative paths + sha256)",
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
        f"- divergent pairs: {d10['divergent_pairs']} "
        f"(disagreements={d10['disagreements']}, "
        f"wrong-verdict events={d10['wrong_verdict_events']})",
        f"- divergence rate: {d10['divergence_rate']}",
        f"- **D10 decision: {d10dec['decision']}** "
        f"(threshold: {d10dec['threshold']})",
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
        f"- consumed artifact: `{u9['consumed_artifact']}`",
        f"- evidence: {json.dumps(u9['evidence'])}",
        "",
    ]
    return "\n".join(lines)
