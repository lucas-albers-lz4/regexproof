#!/usr/bin/env python3
"""Freeze all four adopted webhook questions and preserve decided/timeout states."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2"
COHORT = ROOT / "properties" / "calibration" / "2026-09-12-calibration-20-r2" / "manifest.json"
CONVERSION = ROOT / "properties" / "generated" / "aidevops-webhook_conversion.ndjson"
REPO_ID = "marcusquinn/aidevops"
URL = "https://github.com/marcusquinn/aidevops"
PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
GATE_ID = "aidevops-webhook-action-protocol"
GATE_COMMAND = ".venv/bin/python scripts/aidevops-webhook-action-protocol-regression-gate.py"

QUESTIONS = {
    "AE-aidevops-webhook-secret-env-identifier": {
        "contract": "contract-secret-env-name.json",
        "pattern_cases": 64,
        "integrated_cases": 11,
    },
    "AE-aidevops-webhook-repository-action-token": {
        "contract": "contract-repository-slug.json",
        "pattern_cases": 305,
        "integrated_cases": 19,
        "timeout": True,
    },
    "AE-aidevops-webhook-check-sha-token": {
        "contract": "contract-check-sha.json",
        "pattern_cases": 39,
        "integrated_cases": 9,
    },
    "AE-aidevops-webhook-process-pr-number": {
        "contract": "contract-process-pr-number.json",
        "pattern_cases": 263,
        "integrated_cases": 9,
    },
}


def _run(argv: list[str]) -> None:
    completed = subprocess.run(
        argv,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if completed.returncode:
        raise RuntimeError((completed.stderr or completed.stdout).strip()[-4000:])


def main() -> int:
    report = json.loads((BUNDLE / "gate-report.json").read_text(encoding="utf-8"))
    slug_timeout = json.loads((BUNDLE / "slug-inclusion-attempt.json").read_text(encoding="utf-8"))
    if report.get("gate_id") != GATE_ID or report.get("local_gate_passed") is not True:
        raise RuntimeError("webhook regression gate is not passing")
    if slug_timeout.get("result") != "timeout" or slug_timeout.get("not_proven") is not True:
        raise RuntimeError("full-slug query no longer has its expected recorded not-proven result")
    formal = {row["name"]: row for row in report["formal_results"]}

    contracts: list[dict[str, Any]] = []
    attempts: list[dict[str, Any]] = []
    for question_id, spec in QUESTIONS.items():
        contract = json.loads((BUNDLE / spec["contract"]).read_text(encoding="utf-8"))
        contracts.append({
            "repo_id": REPO_ID,
            "url": URL,
            "pin": PIN,
            "site": contract["site"],
            "question_id": question_id,
            "kind": "property",
            "synthesized": False,
            "domain": (
                slug_timeout["claim"] + "; " + slug_timeout["input_domain"]
                if spec.get("timeout")
                else formal[question_id]["domain"]
            ),
            "contract": contract,
        })
        status = "timeout" if spec.get("timeout") else formal[question_id]["result"]
        if not spec.get("timeout") and status != "unsat":
            raise RuntimeError(f"decided proof is not UNSAT: {question_id}")
        detail = (
            "The 30-second whole-helper inclusion query timed out; finite differential and exact-helper cases passed, but the unbounded slug guarantee is not proven."
            if spec.get("timeout")
            else None
        )
        attempts.append({
            "repo_id": REPO_ID,
            "url": URL,
            "pin": PIN,
            "site": contract["site"],
            "question_id": question_id,
            "kind": "property",
            "synthesized": False,
            "contract": contract,
            "domain": contracts[-1]["domain"],
            "status": status,
            "detail": detail,
            "gate": {
                "source_pin_verified": True,
                "product_engine_replayed": True,
                "mutation_guard_passed": True,
                "differential_cases": spec["pattern_cases"] + spec["integrated_cases"],
                "gate_id": GATE_ID,
                "local_gate_command": GATE_COMMAND,
                "local_gate_passed": True,
                "consumer_adopted": False,
            },
        })

    contracts_path = BUNDLE / "roster-contracts.json"
    attempts_path = BUNDLE / "attempts.json"
    contracts_path.write_text(json.dumps(contracts, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    attempts_path.write_text(json.dumps(attempts, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    roster_path = BUNDLE / "roster.json"
    checkpoint_path = BUNDLE / "checkpoint.json"
    _run([
        sys.executable,
        str(ROOT / "scripts" / "freeze-product-roster.py"),
        "--cohort", str(COHORT),
        "--contracts", str(contracts_path),
        "--out", str(roster_path),
    ])
    _run([
        sys.executable,
        str(ROOT / "scripts" / "build-autonomous-checkpoint.py"),
        "--cohort", str(COHORT),
        "--roster", str(roster_path),
        "--attempts", str(attempts_path),
        "--conversion-rows", str(CONVERSION),
        "--out", str(checkpoint_path),
    ])
    print(f"frozen four exact-pin questions (3 UNSAT, 1 not proven) at {checkpoint_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(f"build-aidevops-webhook-checkpoint: {exc}", file=sys.stderr)
        raise SystemExit(1)
