#!/usr/bin/env python3
"""Run exact-pin Node differentials for json-editor's EnumEditor escaper."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.json_editor_enum_escape_replay import (  # noqa: E402
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_SHA256,
    mutation_reproduces,
    run_differential_gate,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-p2-json-editor-source-review"
CONTRACT_PATH = SLICE / "contract.json"
PROPERTY_ID = "JE-json-editor-enum-string-html-text-codepoint-image"
MUTATION_ID = "JE-json-editor-enum-mutated-less-than-leaks"
GATE_ID = "json-editor-enum-html-text-escape"


def run_gate(root: Path | None = None) -> dict:
    checkout = source_root(root)
    report = run_differential_gate(checkout)
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("EnumEditor property contract is not validly adopted")
    if (
        contract.get("site")
        != f"json-editor/json-editor@{PIN}:src/editors/enum.js:123:column-24"
    ):
        raise RuntimeError("contract identity differs from the reviewed ampersand regex")
    adoption = contract.get("adoption", {})
    if (
        adoption.get("source_url") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
        or adoption.get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("adoption record is not bound to the exact reviewed source")
    if not mutation_reproduces("<", checkout):
        raise RuntimeError("weakened source mutation did not reproduce a raw '<'")
    report.update({
        "schema_version": "1",
        "gate_id": GATE_ID,
        "question_ids": [PROPERTY_ID],
        "product_engine_replay_question_ids": [PROPERTY_ID],
        "differential_case_counts": {PROPERTY_ID: report["cases"]},
        "mutation_guard_question_id": MUTATION_ID,
        "mutation_guard_passed": True,
        "mutation_witness": "<",
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_SHA256,
        "contract_sha256": contract_digest(contract),
    })
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = run_gate(args.source_root)
        encoded = json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
        if args.output:
            atomic_write_text(args.output, encoded)
        print(
            f"EnumEditor HTML text gate: {report['cases']} exact-source cases, "
            f"Node {report['node_version']}, 0 mismatches; less-than mutation replay passed"
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError, TimeoutError) as exc:
        print(f"json-editor EnumEditor gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
