#!/usr/bin/env python3
"""Replay AutoAR's exact phase-key sanitizer and its path-escape mutation."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.autoar_phase_key_replay import (  # noqa: E402
    GO_TOOLCHAIN,
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_SHA256,
    mutation_reproduces_path_escape,
    run_sanitizer,
    source_root,
    verify_source_evidence,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.harness.autoar_phase_key import QUESTION_ID, SITE  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-autoar-phasekey-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
COHORT_ID = "2026-09-12-calibration-20-r2"
MANIFEST_DIGEST = "5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d"


def _verify_contract_roster_and_source(checkout: Path) -> tuple[dict, dict, dict]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("AutoAR phase-key contract is not validly adopted")
    if contract.get("site") != SITE:
        raise RuntimeError("phase-key contract is not bound to the exact regex site")
    adoption = contract["adoption"]
    if (
        adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
        or adoption.get("source_url", "").rstrip("/").removesuffix(".git")
        != REPOSITORY
    ):
        raise RuntimeError("phase-key adoption does not bind the pinned source bytes")
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    identities = [
        row
        for row in roster.get("identities", [])
        if row.get("question_id") == QUESTION_ID and row.get("site") == SITE
    ]
    if (
        roster.get("cohort_id") != COHORT_ID
        or roster.get("cohort_manifest_digest") != MANIFEST_DIGEST
        or len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("frozen phase-key roster does not bind this contract")
    source = verify_source_evidence()
    if source.get("source_sha256") != SOURCE_SHA256:
        raise RuntimeError("source verifier did not confirm the phase-key source digest")
    if checkout.resolve() != source_root().resolve():
        raise RuntimeError("requested source checkout differs from the exact pinned checkout")
    return contract, roster, source


def _inputs() -> tuple[list[str], dict[str, int]]:
    values = [chr(codepoint) for codepoint in range(128)]
    classes = {"non_nul_ascii_single_character": 127, "nul_single_character": 1}
    punctuation = [
        "..", ".", "/", "\\", "../outside", "../../outside", "./../x",
        "a/../b", "a\\..\\b", "phase.logs", "__", "", " ", "\t", "\n",
        "cache--key", "URL Collection", "é/路径", "🧪..\\module",
        "\u202e../log", "\\\\server\\share", "a\x00/../b",
    ]
    classes["path_and_normalization_seeds"] = len(punctuation)
    rng = random.Random(0xA17C)
    alphabet = string.ascii_letters + string.digits + " _-./\\:@%?\t\r\n" + "é路径🧪"
    random_values = [
        "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 96)))
        for _ in range(512)
    ]
    classes["seeded_mixed_strings"] = len(random_values)
    return values + punctuation + random_values, classes


def run_gate(checkout: Path) -> dict:
    contract, roster, source = _verify_contract_roster_and_source(checkout)
    values, case_classes = _inputs()
    replay = run_sanitizer(values)
    if replay["go_version"] != GO_TOOLCHAIN:
        raise RuntimeError(f"product replay used {replay['go_version']}, expected {GO_TOOLCHAIN}")
    violations = [
        row
        for row in replay["results"]
        if any(char in row["component"] for char in (".", "/", "\\"))
        or not row["inside"]
    ]
    if violations:
        raise RuntimeError(
            f"pinned phase-key sanitizer had {len(violations)} unsafe output(s): "
            f"{violations[:3]!r}"
        )

    weakened = run_sanitizer(["../../outside"], weakened=True)["results"][0]
    if (
        weakened["component"] != "../../outside"
        or weakened["inside"]
        or not mutation_reproduces_path_escape({"path_character": "."})
    ):
        raise RuntimeError("weakened source mutation did not reproduce path escape")

    report = {
        "schema_version": "1",
        "gate_id": "autoar-phase-key-component-20r2",
        "question_id": QUESTION_ID,
        "status": "passed",
        "repository": REPOSITORY,
        "source": {
            "pin": PIN,
            "file": SOURCE_FILE,
            "sha256": source["source_sha256"],
            "caller_file": source["caller_file"],
            "caller_sha256": source["caller_sha256"],
            "routes_file": source["routes_file"],
            "routes_sha256": source["routes_sha256"],
            "results_root_file": source["results_root_file"],
            "results_root_sha256": source["results_root_sha256"],
        },
        "product_engine": "pinned Go sanitizePhaseKey and filepath.Join",
        "go_version": replay["go_version"],
        "differential_cases": len(values),
        "case_classes": case_classes,
        "mismatches": 0,
        "mutation": {
            "weakened_pattern": r"[^a-zA-Z0-9_./-]+",
            "input": "../../outside",
            "original_component": "outside",
            "weakened_component": weakened["component"],
            "weakened_relative_path": weakened["relative"],
            "weakened_escapes_phase_logs": not weakened["inside"],
            "real_source_replay": True,
        },
        "contract_sha256": contract_digest(contract),
        "roster_sha256": hashlib.sha256(ROSTER_PATH.read_bytes()).hexdigest(),
        "cohort": {"cohort_id": COHORT_ID, "manifest_digest": MANIFEST_DIGEST},
        "scope": (
            "The module-derived phase-log filename component contains no dot or path separator. "
            "The gate does not establish scanID or results-root containment, symlink safety, "
            "or uniqueness of sanitized names."
        ),
    }
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean AutoAR checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip solver proof")
    parser.add_argument("--output", type=Path, help="write machine-readable gate report")
    args = parser.parse_args(argv)
    try:
        if args.source_root:
            requested = Path(args.source_root).expanduser().resolve()
            configured = os.environ.get("AUTOAR_REPLAY_SOURCE")
            if configured and Path(configured).expanduser().resolve() != requested:
                parser.error("--source-root conflicts with AUTOAR_REPLAY_SOURCE")
            os.environ["AUTOAR_REPLAY_SOURCE"] = str(requested)
        checkout = source_root()
        print(f"AutoAR exact source: {checkout} @ {PIN}")
        report = run_gate(checkout)
        if not args.product_only:
            import subprocess

            completed = subprocess.run(
                [
                    ".venv/bin/python",
                    "scripts/z3-verify.py",
                    "--require-ground-truth",
                    "--fail-on-property-failure",
                    QUESTION_ID,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=240,
                check=False,
                shell=False,
                env={**os.environ, "AUTOAR_REPLAY_SOURCE": str(checkout)},
            )
            if completed.returncode:
                detail = (completed.stderr or completed.stdout).strip()[-4000:]
                raise RuntimeError(f"phase-key property proof failed: {detail}")
            rows = [
                json.loads(line)
                for line in completed.stdout.splitlines()
                if line.strip().startswith("{")
            ]
            matched = [row for row in rows if row.get("name") == QUESTION_ID]
            if len(matched) != 1 or matched[0].get("result") != "unsat":
                raise RuntimeError("phase-key gate did not emit one UNSAT property row")
            report["proof_result"] = matched[0]
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        print(json.dumps(report, ensure_ascii=True, sort_keys=True))
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"autoar-phase-key-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
