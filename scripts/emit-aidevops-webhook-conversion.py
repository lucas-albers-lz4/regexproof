#!/usr/bin/env python3
"""Emit only the decided, source-matched Aidevops webhook properties."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.harness.contract import valid_product_contract  # noqa: E402

BUNDLE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2"
INVENTORY = ROOT / "properties" / "calibration" / "2026-10-16-p2-source-inventory-v5" / "sites.ndjson"
OUTPUT = ROOT / "properties" / "generated" / "aidevops-webhook_conversion.ndjson"
QUESTIONS = {
    "AE-aidevops-webhook-secret-env-identifier": (
        "contract-secret-env-name.json",
        "secret_env_name",
    ),
    "AE-aidevops-webhook-check-sha-token": (
        "contract-check-sha.json",
        "check_sha",
    ),
    "AE-aidevops-webhook-process-pr-number": (
        "contract-process-pr-number.json",
        "pr_number",
    ),
}


def _read_ndjson(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> int:
    report = json.loads((BUNDLE / "gate-report.json").read_text(encoding="utf-8"))
    if report.get("gate_id") != "aidevops-webhook-action-protocol" or report.get("local_gate_passed") is not True:
        raise SystemExit("webhook gate report is missing or did not pass")
    formal = {row["name"]: row for row in report.get("formal_results", [])}
    sites = _read_ndjson(INVENTORY)
    contracts: dict[str, dict] = {}
    for question_id, (filename, _) in QUESTIONS.items():
        contract = json.loads((BUNDLE / filename).read_text(encoding="utf-8"))
        if not valid_product_contract(contract):
            raise SystemExit(f"invalid product contract: {filename}")
        proof = formal.get(question_id)
        if not proof or proof.get("result") != "unsat" or proof.get("product") is not True:
            raise SystemExit(f"question is not a decided contract-backed UNSAT: {question_id}")
        contracts[question_id] = contract

    rows = []
    for question_id, (filename, pattern_key) in QUESTIONS.items():
        contract = contracts[question_id]
        site = contract["site"]
        source_row = next((row for row in sites if row.get("site") == site.removeprefix("marcusquinn/aidevops@8666b6c6c52472b5535aa295f2df593918152cb1:")), None)
        # P2 source inventory rows are repository/path-relative; the adopted
        # contract is fully qualified. Match its exact line/column suffix.
        if source_row is None:
            relative_anchor = site.split(":", 1)[1]
            source_row = next(
                (row for row in sites if row.get("site") == relative_anchor), None
            )
        if source_row is None:
            raise SystemExit(f"site is absent from the exact-pin P2 inventory: {site}")
        proof = formal[question_id]
        pattern_cases = int(report["differential_cases_by_pattern"][pattern_key])
        helper_cases = int(report["integrated_helper_cases_by_contract"][pattern_key])
        if question_id == "AE-aidevops-webhook-secret-env-identifier":
            # The exact resolve-and-clear replay is an additional workflow
            # case for this contract; it is not counted in the pattern corpus.
            helper_cases += int(
                report["integrated_helper_cases_by_contract"]["secret_resolve_and_clear"]
            )
        rows.append({
            "schema_version": "1",
            "name": question_id,
            "question_id": question_id,
            "corpus": "aidevops",
            "site": site,
            "regex_id": source_row["regex_id"],
            "kind": "property",
            "result": "unsat",
            "ground_truth": None,
            "ground_truth_status": "not_applicable",
            "domain": proof["domain"],
            "contract": contract,
            "family": proof["family"],
            "idiom_bucket": "webhook-action-protocol-validation",
            "wave_id": "aidevops-webhook-action-protocol-20r2-20261016-r1",
            "product_reportable": True,
            "product_engine_replayed": True,
            "synthesized": False,
            "witness": None,
            "engine_versions": proof["engine_versions"],
            "gate": {
                "gate_id": report["gate_id"],
                "local_gate_command": ".venv/bin/python scripts/aidevops-webhook-action-protocol-regression-gate.py",
                "local_gate_passed": True,
                "source_pin_verified": True,
                "product_engine_replayed": True,
                "mutation_guard_passed": True,
                "differential_cases": pattern_cases + helper_cases,
                "consumer_adopted": False,
            },
        })
    rows.sort(key=lambda row: row["site"])
    OUTPUT.write_text(
        "".join(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(f"wrote {len(rows)} decided product rows to {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
