#!/usr/bin/env python3
"""Build the pinned Doberman secret-path product checkpoint from proof and gate evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_is_adopted, verify_adoption_source  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402
from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    build_product_roster,
    build_report,
    canonical_row_to_checkpoint,
    checkpoint_from_attempts,
)


COHORT_ID = "2026-09-12-calibration-20-r2"
REPO_ID = "fu351/Doberman-Core"
REPO_URL = "https://github.com/fu351/Doberman-Core"
PIN = "53ae43c5298a2426c6696147fdd75e2a4aef10e2"
SOURCE_FILE = "src/doberman/engine/rules/secrets.py"
SITE = f"{REPO_ID}@{PIN}:{SOURCE_FILE}:223:_SECRET_PATH"
QUESTION_ID = "PY-doberman-secret-store-windows-miss"
MUTATION_ID = "PY-doberman-secret-store-mutated-missing-credentials"
REGEX_ID = "1da0edb358526b5f1d6ae780f0116744"
ARTIFACT_DIR = ROOT / "properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2"


class EvidenceBuildError(ValueError):
    """Raised when proof, source, or product-gate evidence is inconsistent."""


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


def build_evidence(source_root: Path) -> dict[str, Any]:
    contract = _read_json(ARTIFACT_DIR / "contract.json")
    if not contract_is_adopted(contract):
        raise EvidenceBuildError("contract does not have a valid autonomous adoption")
    if not verify_adoption_source(contract, source_root):
        raise EvidenceBuildError("adopted source does not match the frozen pin")
    proof_rows = _read_ndjson(ARTIFACT_DIR / "proof-report.ndjson")
    proof_by_name = {row.get("name"): row for row in proof_rows}
    proof = proof_by_name.get(QUESTION_ID)
    mutation = proof_by_name.get(MUTATION_ID)
    if (
        proof is None
        or proof.get("result") != "sat"
        or proof.get("ground_truth") != "reproduced"
        or proof.get("ok") is not True
        or mutation is None
        or mutation.get("kind") != "mutation_guard"
        or mutation.get("result") != "sat"
        or mutation.get("ok") is not True
    ):
        raise EvidenceBuildError("proof report lacks the reproduced SAT and passing mutation guard")
    witness = proof.get("witness", {}).get("s")
    if not isinstance(witness, str) or not witness:
        raise EvidenceBuildError("proof report has no path witness")

    gate = _read_json(ARTIFACT_DIR / "gate-report.json")
    if (
        gate.get("artifact_kind") != "doberman-secret-path-regression-gate"
        or gate.get("pin") != PIN
        or gate.get("repo_id") != REPO_ID
        or gate.get("regex_id") != REGEX_ID
        or gate.get("source_sha256") != contract["adoption"]["source_sha256"]
        or gate.get("result") != "pass_current_gap_reproduced"
        or gate.get("security_impact") != "pending_product_triage"
        or not gate.get("windows_cases")
        or any(
            case.get("secret_rule_verdict") != "PASS"
            or case.get("objective_guardrail_verdict") != "PASS"
            or case.get("default_path_policy_matches") is not False
            for case in gate["windows_cases"]
        )
    ):
        raise EvidenceBuildError("product gate report does not reproduce the adopted path gap")

    cohort_path = ROOT / "properties/calibration/2026-09-12-calibration-20-r2/manifest.json"
    cohort = validate_manifest(_read_json(cohort_path))
    if cohort["cohort_id"] != COHORT_ID:
        raise EvidenceBuildError("cohort manifest identity changed")
    member = next(
        row for row in cohort["repos"]
        if row["repo_id"] == REPO_ID and row["pin"] == PIN
    )
    sites_path = ROOT / "properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson"
    source_sites = _read_ndjson(sites_path)
    source_site = next(
        (
            row for row in source_sites
            if row.get("repo_id") == REPO_ID
            and row.get("pin") == PIN
            and row.get("regex_id") == REGEX_ID
        ),
        None,
    )
    if (
        source_site is None
        or source_site.get("source_file") != SOURCE_FILE
        or source_site.get("line") != 223
    ):
        raise EvidenceBuildError("source site does not match the frozen P2 inventory")

    domain = proof["domain"]
    canonical = {
        "schema_version": "1",
        "name": QUESTION_ID,
        "site": SITE,
        "contract": contract,
        "domain": domain,
        "kind": "bug_demo",
        "synthesized": False,
        "result": "sat",
        "ground_truth": None,
        "ground_truth_status": "reproduced",
        "engine_versions": dict(proof["engine_versions"]),
        "product_engine_version": gate["python_version"],
        "family": "PY-doberman-secret-store-path",
        "corpus": "Doberman-Core",
        "idiom_bucket": "windows-secret-store-path",
        "wave_id": "doberman_secret_path_20r2_r1",
        "regex_id": REGEX_ID,
        "pattern": source_site["pattern"],
        "product_reportable": True,
        "disclosure": None,
        "witness": {"s": witness},
    }
    disposition = {
        "status": "pending_product_triage",
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
        url=member["url"],
        pin=PIN,
        disposition=disposition,
    )
    attempt = {
        "repo_id": REPO_ID,
        "url": member["url"],
        "pin": PIN,
        "site": SITE,
        "question_id": QUESTION_ID,
        "kind": "bug_demo",
        "synthesized": False,
        "contract": contract,
        "domain": domain,
        "status": "sat",
        "detail": None,
        "gate": {
            "source_pin_verified": True,
            "product_engine_replayed": True,
            "mutation_guard_passed": True,
            "differential_cases": 0,
            "gate_id": "doberman-secret-path-regression-gate-v1",
            "local_gate_command": (
                "PYTHONPATH=/tmp/regexproof-doberman-deps python3 "
                "scripts/doberman-secret-path-regression-gate.py "
                "--source-root /tmp/regexproof-pinned-sources/"
                "Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2 "
                "--output properties/calibration/2026-10-15-autonomous-doberman-"
                "win-secret-path-20r2/gate-report.json"
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

    generated_path = ROOT / "properties/generated/Doberman-Core_conversion.ndjson"
    generated_rows = _read_ndjson(generated_path)
    matching = [row for row in generated_rows if row.get("name") == QUESTION_ID]
    if matching:
        if len(matching) != 1 or _canonical_json(matching[0]) != _canonical_json(canonical):
            raise EvidenceBuildError("existing canonical row conflicts with this evidence")
    else:
        generated_rows.append(canonical)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    _write_json(ARTIFACT_DIR / "roster.json", roster)
    _write_json(ARTIFACT_DIR / "attempts.json", [attempt])
    _write_json(ARTIFACT_DIR / "checkpoint.json", checkpoint)
    _write_json(ARTIFACT_DIR / "report.json", report)
    atomic_write_text(
        ARTIFACT_DIR / "conversion.ndjson",
        json.dumps(canonical, ensure_ascii=True, sort_keys=True) + "\n",
    )
    (ARTIFACT_DIR / "conversion.ndjson").chmod(0o644)
    atomic_write_text(
        generated_path,
        "".join(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n" for row in generated_rows),
    )
    generated_path.chmod(0o644)
    return {
        "question_id": QUESTION_ID,
        "witness": witness,
        "source_sha256": contract["adoption"]["source_sha256"],
        "contract_sha256": contract["adoption"]["contract_sha256"],
        "checkpoint_report": report,
        "generated_row_count": len(generated_rows),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = build_evidence(args.source_root)
    except (OSError, ValueError, StopIteration, ConversionCheckpointError) as exc:
        print(f"build-doberman-secret-path-evidence: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"built {result['question_id']} checkpoint: "
        f"witness={result['witness']!r}, "
        f"local_gates={result['checkpoint_report']['useful_gate_outcomes']['useful_regression_gates']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
