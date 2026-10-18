#!/usr/bin/env python3
"""Run the adopted Malcontent third-party-description Markdown counterexample."""

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

from regexproof.contract_adoption import contract_digest, verify_adoption_source  # noqa: E402
from regexproof.groundtruth.malcontent_description_markdown_replay import (  # noqa: E402
    EXPECTED_LINK,
    GO_REPLAY,
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_SHA256,
    WITNESS,
    run_description_replay,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-malcontent-description-markdown-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
PROPERTY_ID = "MC-malcontent-description-metadata-extra-markdown-link"
MUTATION_ID = "MC-malcontent-description-capture-mutation-guard"
_DOT = 'Union(Range("\\u0000","\\u0009"),Range("\\u000b","\\u007f"))'
_ANY = 'AllChar(Re("").sort())'
MIRROR_EXPR = (
    f"Concat(Star({_ANY}),Re(\"D\"),Re(\"e\"),Re(\"t\"),Re(\"e\"),"
    f"Re(\"c\"),Re(\"t\"),Re(\"i\"),Re(\"o\"),Re(\"n\"),Re(\" \"),"
    f"Re(\"p\"),Re(\"a\"),Re(\"t\"),Re(\"t\"),Re(\"e\"),Re(\"r\"),Re(\"n\"),"
    f"Re(\"s\"),Re(\" \"),Re(\"f\"),Re(\"o\"),Re(\"r\"),Re(\" \"),"
    f"Re(\"t\"),Re(\"h\"),Re(\"e\"),Re(\" \"),Re(\"t\"),Re(\"o\"),"
    f"Re(\"o\"),Re(\"l\"),Re(\" \"),Re(\"'\"),Star({_DOT}),Re(\"'\"),"
    f"Re(\" \"),Re(\"t\"),Re(\"a\"),Re(\"k\"),Re(\"e\"),Re(\"n\"),"
    f"Re(\" \"),Re(\"f\"),Re(\"r\"),Re(\"o\"),Re(\"m\"),Re(\" \"),"
    f"Re(\"t\"),Re(\"h\"),Re(\"e\"),Re(\" \"),Re(\"T\"),Re(\"h\"),"
    f"Re(\"r\"),Re(\"e\"),Re(\"a\"),Re(\"t\"),Re(\"H\"),Re(\"u\"),"
    f"Re(\"n\"),Re(\"t\"),Re(\"i\"),Re(\"n\"),Re(\"g\"),Re(\"-\"),"
    f"Re(\"K\"),Re(\"e\"),Re(\"y\"),Re(\"w\"),Re(\"o\"),Re(\"r\"),"
    f"Re(\"d\"),Re(\"s\"),Re(\" \"),Re(\"g\"),Re(\"i\"),Re(\"t\"),"
    f"Re(\"h\"),Re(\"u\"),Re(\"b\"),Re(\" \"),Re(\"p\"),Re(\"r\"),"
    f"Re(\"o\"),Re(\"j\"),Re(\"e\"),Re(\"c\"),Re(\"t\"),Star({_ANY}))"
)


class GateError(RuntimeError):
    """A source, solver, replay, or differential gate failed."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_contract_and_roster() -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"cannot read adopted contract/roster: {exc}") from exc
    if not valid_product_contract(contract):
        raise GateError("description-metadata contract is not validly adopted")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise GateError("contract is not bound to the exact parser source")
    identities = [
        item for item in roster.get("identities", [])
        if item.get("question_id") == PROPERTY_ID and item.get("site") == contract.get("site")
    ]
    if (
        roster.get("cohort_id") != "2026-09-12-calibration-20-r2"
        or roster.get("cohort_manifest_digest") != "5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d"
        or len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
    ):
        raise GateError("pre-outcome roster does not bind the exact adopted contract")
    return contract, roster


def _run_harness(source_root: Path) -> list[dict[str, Any]]:
    env = os.environ.copy()
    env["MALCONTENT_REPLAY_SOURCE"] = str(source_root)
    names = [PROPERTY_ID, MUTATION_ID]
    result = subprocess.run(
        [
            sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json",
            "--require-ground-truth", "--require-domain", "--require-contract",
            "--fail-on-property-failure", *names,
        ],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=180,
        check=False, shell=False,
    )
    if result.returncode:
        raise GateError(f"Z3 harness failed ({result.returncode}): {result.stdout}\n{result.stderr}")
    try:
        rows = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise GateError("Z3 harness emitted invalid NDJSON") from exc
    if {row.get("name") for row in rows} != set(names):
        raise GateError("harness did not return exactly the product question and mutation guard")
    by_name = {row["name"]: row for row in rows}
    for name, kind, product in (
        (PROPERTY_ID, "counterexample_finder", True),
        (MUTATION_ID, "mutation_guard", False),
    ):
        row = by_name[name]
        if (
            row.get("kind") != kind or row.get("result") != "sat"
            or row.get("ground_truth") != "reproduced"
            or row.get("not_proven") or not row.get("ok")
            or row.get("product") is not product
            or (row.get("witness") or {}).get("description_metadata") != WITNESS
        ):
            raise GateError(f"{name} did not return the replayed SAT witness")
    return rows


def _run_differential_fuzz(source_root: Path) -> dict[str, Any]:
    go = shutil.which("go")
    if not go:
        raise GateError("Go is required for the RE2 differential check")
    with tempfile.TemporaryDirectory(prefix="malcontent-description-regex-") as temp:
        binary = Path(temp) / "description-regex-accept"
        build = subprocess.run(
            [go, "build", "-o", str(binary), str(ROOT / "regexproof" / "groundtruth" / "malcontent_description_regex_accept.go")],
            cwd=source_root, capture_output=True, text=True, timeout=120,
            check=False, shell=False,
        )
        if build.returncode:
            raise GateError(f"cannot build Go RE2 adapter: {build.stderr.strip()}")
        result = subprocess.run(
            [
                sys.executable, str(ROOT / "scripts" / "differential-fuzz.py"),
                "--mirror-expr", MIRROR_EXPR,
                "--alphabet", "Detection patterns for the tool 'Benign'|[click](https:/attacker.invalid) github project",
                "--mutations", "|'[]()\r\n\t",
                "--targets", WITNESS,
                "Detection patterns for the tool 'Safe' taken from the ThreatHunting-Keywords github project",
                "malformed third-party description",
                "--runs", "20", "--seed", "20261015", "--exhaust-max-len", "2",
                "--max-len", "256", "--real-argv", str(binary),
            ],
            cwd=ROOT, capture_output=True, text=True, timeout=180,
            check=False, shell=False,
        )
    if result.returncode:
        raise GateError(f"differential-fuzz failed ({result.returncode}): {result.stdout}\n{result.stderr}")
    match = re.search(r"(?m)^(\d+) inputs, 0 mismatches \(seed=20261015\)$", result.stdout)
    if not match:
        raise GateError("differential-fuzz summary is missing or reports a mismatch")
    return {
        "command": "scripts/differential-fuzz.py --mirror-expr <search-language> --real-argv <pinned-Go-RE2-adapter>",
        "seed": 20261015,
        "inputs": int(match.group(1)),
        "mismatches": 0,
        "stdout": result.stdout,
    }


def run_gate() -> dict[str, Any]:
    contract, roster = _load_contract_and_roster()
    replay = run_description_replay(WITNESS)
    source_root = Path(replay["checkout_root"])
    if not verify_adoption_source(contract, source_root):
        raise GateError("contract adoption source verification failed")
    if EXPECTED_LINK not in replay["markdown"]:
        raise GateError("product Markdown did not contain the injected HTTPS link")
    rows = _run_harness(source_root)
    differential = _run_differential_fuzz(source_root)
    return {
        "schema_version": "1",
        "gate_id": "malcontent-description-markdown-extra-link-v1",
        "status": "reproduced",
        "observed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "interpretation": "The gate reproduces Markdown link and table-cell structure for this witness. It does not confirm a downstream consumer or security impact.",
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
        "question_id": PROPERTY_ID,
        "result_rows": rows,
        "product_replay": replay,
        "differential_fuzz": differential,
        "measurements": {
            "product_questions_asked": 1,
            "sat_candidates": 1,
            "ground_truthed_witnesses": 1,
            "reachable_markdown_link_and_table_injection": 1,
            "security_impact_confirmed": 0,
            "local_runnable_gates": 1,
            "mutation_guard_passed": 1,
            "differential_cases": differential["inputs"],
            "external_reports_sent": 0,
            "maintainer_confirmations": 0,
            "third_party_fixes": 0,
            "consumer_adopted_gates": 0,
        },
        "downstream_disposition": {
            "status": "pending_product_triage",
            "reason": "Raw Markdown contains the metadata-derived link and table delimiter; no downstream viewer or consumer impact is confirmed, and no report was sent.",
        },
        "limitations": [
            "One one-line ASCII description witness is replayed; no all-input guarantee is claimed.",
            "No Markdown viewer is executed, so link handling by downstream consumers is unknown.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SLICE / "gate-report.json")
    args = parser.parse_args(argv)
    try:
        report = run_gate()
        atomic_write_text(args.output, json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n")
        args.output.chmod(0o644)
        replay_artifact = {
            "schema_version": "1",
            "artifact_kind": "malcontent-description-markdown-product-replay",
            "gate_id": report["gate_id"],
            "status": report["status"],
            "source": report["source"],
            "product_replay": report["product_replay"],
            "downstream_disposition": report["downstream_disposition"],
            "limitations": report["limitations"],
        }
        replay_path = SLICE / "product-replay.json"
        atomic_write_text(replay_path, json.dumps(replay_artifact, ensure_ascii=True, indent=2, sort_keys=True) + "\n")
        replay_path.chmod(0o644)
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError, KeyError) as exc:
        print(f"malcontent-description-markdown-regression-gate: {exc}", file=sys.stderr)
        return 2
    print(
        f"{report['gate_id']}: {report['status']}; SAT witness reproduced; "
        f"differential cases={report['measurements']['differential_cases']}; "
        f"external reports=0; output={args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
