#!/usr/bin/env python3
"""Build the frozen Xibo CSRF-cookie P2 checkpoint from proof and gate evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_is_adopted, verify_adoption_source  # noqa: E402
from regexproof.groundtruth.xibo_csrf_cookie_replay import (  # noqa: E402
    PIN,
    REPOSITORY,
    SOURCE_FILES,
    _verify_checkout,
    source_root,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402
from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    build_product_roster,
    build_report,
    canonical_row_to_checkpoint,
    checkpoint_from_attempts,
)

QUESTION_ID = "XC-xibo-csrf-cookie-capture-isolation"
MUTATION_ID = "XC-xibo-csrf-cookie-mutated-capture-spills"
REPO_ID = "xibosignage/xibo-cms"
SITE = (
    f"{REPO_ID}@{PIN}:"
    "frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx:42:38"
)
SLICE = ROOT / "properties/calibration/2026-10-15-autonomous-xibo-csrf-cookie-20r2"
COHORT_PATH = ROOT / "properties/calibration/2026-09-12-calibration-20-r2/manifest.json"
SITES_PATH = ROOT / "properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson"


class EvidenceBuildError(ValueError):
    """Raised when proof, source, inventory, or gate evidence is inconsistent."""


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise EvidenceBuildError(f"{path}: invalid JSON: {exc.msg}") from exc


def _read_ndjson(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EvidenceBuildError(f"{path}:{number}: invalid NDJSON: {exc.msg}") from exc
        if not isinstance(row, dict):
            raise EvidenceBuildError(f"{path}:{number}: row must be an object")
        rows.append(row)
    return rows


def _write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
    )
    path.chmod(0o644)


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def build_evidence() -> dict[str, Any]:
    contract = _read_json(SLICE / "contract.json")
    if not contract_is_adopted(contract) or contract.get("site") != SITE:
        raise EvidenceBuildError("contract is not autonomously adopted for the exact Xibo site")
    checkout = source_root()
    _verify_checkout(checkout)
    if not verify_adoption_source(contract, checkout):
        raise EvidenceBuildError("adopted contract source does not match the frozen Xibo pin")

    gate = _read_json(SLICE / "gate-report.json")
    proofs = gate.get("proof_records")
    if (
        gate.get("gate_id") != "xibo-csrf-cookie-capture-20r2"
        or gate.get("source_pin") != PIN
        or gate.get("source_files") != SOURCE_FILES
        or gate.get("question_id") != QUESTION_ID
        or gate.get("cases") != 1007
        or gate.get("source_files_verified") != 4
        or gate.get("external_network_requests") != 0
        or gate.get("security_impact_confirmed") is not False
        or gate.get("weakened_mutation_output")
        != "a1b2c3d4" * 5 + "; session=neighbor"
        or not isinstance(proofs, list)
    ):
        raise EvidenceBuildError("product gate report is incomplete or bound to another source")
    proof_map = {row.get("name"): row for row in proofs}
    proof = proof_map.get(QUESTION_ID)
    mutation = proof_map.get(MUTATION_ID)
    if (
        proof is None
        or proof.get("kind") != "property"
        or proof.get("result") != "unsat"
        or proof.get("product") is not True
        or proof.get("not_proven") is not False
        or proof.get("ok") is not True
        or mutation is None
        or mutation.get("kind") != "mutation_guard"
        or mutation.get("result") != "sat"
        or mutation.get("ground_truth") != "reproduced"
        or mutation.get("ok") is not True
    ):
        raise EvidenceBuildError("proof report lacks the decided property and reproduced mutation")

    cohort = validate_manifest(_read_json(COHORT_PATH))
    if cohort["cohort_id"] != "2026-09-12-calibration-20-r2":
        raise EvidenceBuildError("cohort manifest identity changed")
    member = next(
        (row for row in cohort["repos"] if row["repo_id"] == REPO_ID and row["pin"] == PIN),
        None,
    )
    if member is None or member["url"] != REPOSITORY:
        raise EvidenceBuildError("Xibo exact pin is not in the frozen cohort")

    inventory_rows = _read_ndjson(SITES_PATH)
    matched_inventory = [
        row
        for row in inventory_rows
        if row.get("repo_id") == REPO_ID
        and row.get("pin") == PIN
        and row.get("source_file") == "frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx"
        and row.get("line") == 42
    ]
    if (
        len(matched_inventory) != 1
        or matched_inventory[0].get("pattern") != r"(?:^|;\s*)XSRF-TOKEN=([^;]*)"
        or matched_inventory[0].get("dialect") != "ecma"
        or matched_inventory[0].get("regex_id") != "ea730a13393d4601bafd7a851cf69403"
        or matched_inventory[0].get("source_file_sha256")
        != contract["adoption"]["source_sha256"]
    ):
        raise EvidenceBuildError("contract does not join one exact Xibo row in the frozen P2 inventory")
    source_site = matched_inventory[0]

    canonical = {
        "schema_version": "1",
        "name": QUESTION_ID,
        "question_id": QUESTION_ID,
        "site": SITE,
        "contract": contract,
        "domain": proof["domain"],
        "kind": "property",
        "synthesized": False,
        "result": "unsat",
        "ground_truth": None,
        "ground_truth_status": None,
        "engine_versions": dict(proof["engine_versions"]),
        "product_engine_version": gate["node_version"],
        "family": "XC-xibo-csrf-cookie-capture",
        "corpus": REPO_ID,
        "idiom_bucket": "csrf-cookie-pair-capture",
        "wave_id": "xibo-csrf-cookie-20r2-r1",
        "regex_id": source_site["regex_id"],
        "pattern": source_site["pattern"],
        "shape": 1,
        "product_reportable": True,
        "disclosure": None,
        "witness": None,
    }
    disposition = {
        "status": "not_applicable",
        "filed_at": None,
        "resolved_at": None,
        "approval_escape": None,
        "approval_ref": None,
        "reason_code": None,
        "backfilled": False,
        "disposition_date": None,
    }
    proof_row = canonical_row_to_checkpoint(
        canonical,
        repo_id=REPO_ID,
        url=REPOSITORY,
        pin=PIN,
        disposition=disposition,
    )
    attempt = {
        "repo_id": REPO_ID,
        "url": REPOSITORY,
        "pin": PIN,
        "site": SITE,
        "question_id": QUESTION_ID,
        "kind": "property",
        "synthesized": False,
        "contract": contract,
        "domain": proof["domain"],
        "status": "unsat",
        "detail": None,
        "gate": {
            "source_pin_verified": True,
            "product_engine_replayed": True,
            "mutation_guard_passed": True,
            "differential_cases": gate["cases"],
            "gate_id": gate["gate_id"],
            "local_gate_command": (
                "python scripts/xibo-csrf-cookie-regression-gate.py --output "
                "properties/calibration/2026-10-15-autonomous-xibo-csrf-cookie-20r2/gate-report.json"
            ),
            "local_gate_passed": True,
            "consumer_adopted": False,
        },
    }
    roster_input = {
        key: attempt[key]
        for key in (
            "repo_id", "url", "pin", "site", "question_id", "kind",
            "synthesized", "domain", "contract",
        )
    }
    roster = build_product_roster([roster_input], cohort)
    checkpoint = checkpoint_from_attempts(
        [attempt], [proof_row], cohort=cohort, product_coverage_manifest=roster
    )
    report = build_report(checkpoint)

    generated_path = SLICE / "conversion.ndjson"
    atomic_write_text(
        generated_path,
        json.dumps(canonical, ensure_ascii=True, sort_keys=True) + "\n",
    )
    generated_path.chmod(0o644)
    _write_json(SLICE / "checkpoint-roster.json", roster)
    _write_json(SLICE / "attempts.json", [attempt])
    _write_json(SLICE / "checkpoint.json", checkpoint)
    _write_json(SLICE / "report.json", report)
    atomic_write_text(
        SLICE / "proof-report.ndjson",
        "".join(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n" for row in proofs),
    )
    (SLICE / "proof-report.ndjson").chmod(0o644)
    return {
        "question_id": QUESTION_ID,
        "regex_id": source_site["regex_id"],
        "contract_sha256": contract["adoption"]["contract_sha256"],
        "proof_result": proof["result"],
        "mutation_ground_truth": mutation["ground_truth"],
        "differential_cases": gate["cases"],
        "checkpoint_report": report,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        result = build_evidence()
    except (OSError, ValueError, StopIteration, ConversionCheckpointError) as exc:
        print(f"build-xibo-csrf-cookie-evidence: error: {exc}", file=sys.stderr)
        return 2
    print(_canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
