#!/usr/bin/env python3
"""Replay Malcontent's source-pinned author-metadata Markdown link finding."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import (  # noqa: E402
    contract_digest,
    verify_adoption_source,
)
from regexproof.groundtruth.malcontent_author_markdown_replay import (  # noqa: E402
    EXPECTED_SECOND_LINK,
    GO_REPLAY,
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_SHA256,
    WITNESS,
    run_metadata_replay,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-malcontent-author-markdown-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
PROPERTY_ID = "MC-malcontent-author-metadata-extra-markdown-link"
MUTATION_ID = "MC-malcontent-author-metadata-capture-mutation-guard"

_DOT = 'Union(Range("\\u0000","\\u0009"),Range("\\u000b","\\u007f"))'
_ANY = 'AllChar(Re("").sort())'
MIRROR_EXPR = (
    f"Concat(Star({_ANY}),Star({_DOT}),Re(\" \"),Re(\"(\"),Re(\"h\"),"
    f"Re(\"t\"),Re(\"t\"),Re(\"p\"),Star({_DOT}),Re(\")\"),Star({_ANY}))"
)


class GateError(RuntimeError):
    """A required source, proof, or replay gate did not complete."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_contract_and_roster() -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"cannot read adopted contract/roster: {exc}") from exc
    if not valid_product_contract(contract):
        raise GateError("author-metadata contract is not validly adopted")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise GateError("contract adoption is not bound to the pinned parser source")
    if (
        roster.get("cohort_id") != "2026-09-12-calibration-20-r2"
        or roster.get("cohort_manifest_digest")
        != "5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d"
    ):
        raise GateError("roster is not bound to the frozen 20-r2 cohort")
    matches = [
        identity
        for identity in roster.get("identities", [])
        if identity.get("question_id") == PROPERTY_ID
        and identity.get("site") == contract.get("site")
    ]
    if len(matches) != 1 or matches[0].get("contract_sha256") != contract_digest(contract):
        raise GateError("pre-outcome roster does not bind this exact contract digest")
    return contract, roster


def _run_harness(source_root: Path) -> list[dict[str, Any]]:
    env = os.environ.copy()
    env["MALCONTENT_REPLAY_SOURCE"] = str(source_root)
    names = [PROPERTY_ID, MUTATION_ID]
    argv = [
        sys.executable,
        str(ROOT / "scripts" / "z3-verify.py"),
        "--json",
        "--require-ground-truth",
        "--require-domain",
        "--require-contract",
        "--fail-on-property-failure",
        *names,
    ]
    result = subprocess.run(
        argv,
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if result.returncode:
        raise GateError(
            f"Z3 harness failed ({result.returncode}):\n{result.stdout}\n{result.stderr}"
        )
    try:
        rows = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise GateError("Z3 harness emitted invalid NDJSON") from exc
    if {row.get("name") for row in rows} != set(names):
        raise GateError("Z3 output does not contain exactly the property and mutation guard")
    by_name = {row["name"]: row for row in rows}
    proof = by_name[PROPERTY_ID]
    guard = by_name[MUTATION_ID]
    if (
        proof.get("kind") != "counterexample_finder"
        or proof.get("result") != "sat"
        or proof.get("ground_truth") != "reproduced"
        or proof.get("product") is not True
        or proof.get("not_proven")
        or not proof.get("ok")
        or (proof.get("witness") or {}).get("author_metadata") != WITNESS
    ):
        raise GateError("counterexample finder did not return the replayed SAT witness")
    if (
        guard.get("kind") != "mutation_guard"
        or guard.get("result") != "sat"
        or guard.get("ground_truth") != "reproduced"
        or guard.get("not_proven")
        or not guard.get("ok")
        or (guard.get("witness") or {}).get("author_metadata") != WITNESS
    ):
        raise GateError("mutation guard did not reproduce the weakened-capture witness")
    return rows


def _run_differential_fuzz(source_root: Path) -> dict[str, Any]:
    go = shutil.which("go")
    if not go:
        raise GateError("Go is required for the RE2 differential check")
    with tempfile.TemporaryDirectory(prefix="malcontent-author-regex-") as temp:
        binary = Path(temp) / "author-regex-accept"
        build = subprocess.run(
            [go, "build", "-o", str(binary), str(ROOT / "regexproof" / "groundtruth" / "malcontent_author_regex_accept.go")],
            cwd=source_root,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
            shell=False,
        )
        if build.returncode:
            raise GateError(f"cannot build pinned-engine regex adapter: {build.stderr.strip()}")
        argv = [
            sys.executable,
            str(ROOT / "scripts" / "differential-fuzz.py"),
            "--mirror-expr",
            MIRROR_EXPR,
            "--alphabet",
            "ahtp ()[]:/.",
            "--mutations",
            ")[]\r\n\t",
            "--targets",
            WITNESS,
            "Name (https://safe.invalid)",
            "malformed author metadata",
            "--runs",
            "20",
            "--seed",
            "20261015",
            "--exhaust-max-len",
            "2",
            "--max-len",
            "24",
            "--real-argv",
            str(binary),
        ]
        result = subprocess.run(
            argv,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
            shell=False,
        )
    if result.returncode:
        raise GateError(
            f"differential-fuzz failed ({result.returncode}):\n{result.stdout}\n{result.stderr}"
        )
    match = re.search(r"(?m)^(\d+) inputs, 0 mismatches \(seed=20261015\)$", result.stdout)
    if not match:
        raise GateError("differential-fuzz summary was missing or reported a mismatch")
    return {
        "command": "scripts/differential-fuzz.py --mirror-expr <search-language> --real-argv <pinned-Go-regexp-adapter>",
        "seed": 20261015,
        "inputs": int(match.group(1)),
        "mismatches": 0,
        "stdout": result.stdout,
    }


def run_gate() -> dict[str, Any]:
    contract, roster = _load_contract_and_roster()
    replay = run_metadata_replay(WITNESS)
    source_root = Path(replay["checkout_root"])
    if not verify_adoption_source(contract, source_root):
        raise GateError("autonomous adoption source verification failed")
    if EXPECTED_SECOND_LINK not in replay["markdown"]:
        raise GateError("full product replay did not emit the second Markdown link")
    rows = _run_harness(source_root)
    differential = _run_differential_fuzz(source_root)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return {
        "schema_version": "1",
        "gate_id": "malcontent-author-markdown-extra-link-v1",
        "status": "reproduced",
        "observed_at": now,
        "interpretation": "Successful gate completion means the adopted counterexample and mutation guard reproduced. It does not mean the upstream report is safe or that a Markdown consumer was impacted.",
        "cohort": {
            "cohort_id": roster["cohort_id"],
            "manifest_digest": roster["cohort_manifest_digest"],
            "roster_sha256": _sha256(ROSTER_PATH.read_bytes()),
            "contract_sha256": contract_digest(contract),
        },
        "source": {
            "repository_url": REPOSITORY,
            "pin": PIN,
            "file": SOURCE_FILE,
            "sha256": SOURCE_SHA256,
            "source_ref": f"{REPOSITORY}/blob/{PIN}/{SOURCE_FILE}",
        },
        "measurements": {
            "product_questions_asked": 1,
            "sat_candidates": 1,
            "ground_truthed_witnesses": 1,
            "reachable_markdown_link_injection": 1,
            "security_impact_confirmed": 0,
            "local_runnable_gates": 1,
            "mutation_guard_passed": 1,
            "differential_cases": differential["inputs"],
            "external_reports_sent": 0,
            "maintainer_confirmations": 0,
            "third_party_fixes": 0,
            "consumer_adopted_gates": 0,
        },
        "question_id": PROPERTY_ID,
        "result_rows": rows,
        "differential_fuzz": differential,
        "product_replay": replay,
        "downstream_disposition": {
            "status": "pending_product_triage",
            "reason": "The exact product emitted a second attacker-chosen HTTPS Markdown link. No downstream Markdown viewer or consumer impact has been independently confirmed, and no report was sent.",
        },
        "limitations": [
            "Input is one ASCII YARA author metadata value with a valid non-prefix reference URL; it is a concrete counterexample, not an all-metadata proof.",
            "This gate reproduces link structure in Markdown output. It does not execute a browser renderer or establish whether a specific consumer permits or sanitizes the resulting link.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SLICE / "gate-report.json")
    args = parser.parse_args(argv)
    try:
        report = run_gate()
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        args.output.chmod(0o644)
        replay_path = SLICE / "product-replay.json"
        replay_artifact = {
            "schema_version": "1",
            "artifact_kind": "malcontent-author-markdown-product-replay",
            "gate_id": report["gate_id"],
            "status": report["status"],
            "source": report["source"],
            "product_replay": report["product_replay"],
            "downstream_disposition": report["downstream_disposition"],
            "limitations": report["limitations"],
        }
        atomic_write_text(
            replay_path,
            json.dumps(replay_artifact, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        replay_path.chmod(0o644)
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError, KeyError) as exc:
        print(f"malcontent-author-markdown-regression-gate: {exc}", file=sys.stderr)
        return 2
    print(
        f"{report['gate_id']}: {report['status']}; "
        f"SAT witness reproduced; differential cases="
        f"{report['measurements']['differential_cases']}; "
        f"external reports=0; output={args.output}; product replay={SLICE / 'product-replay.json'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
