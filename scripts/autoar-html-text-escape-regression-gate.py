#!/usr/bin/env python3
"""Prove and replay AutoAR's pinned scan-result HTML text escaper."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.autoar_html_escape_replay import (  # noqa: E402
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    SOURCE_SHA256,
    mutation_reproduces,
    run_esc,
    source_root,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-autoar-html-text-escape-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
EVIDENCE_PATH = SLICE / "source-evidence.json"
PROPERTY_ID = "AA-autoar-html-text-escape-codepoint-image"
MUTATION_ID = "AA-autoar-html-text-escape-mutated-less-than-leaks"
QUESTION_IDS = (PROPERTY_ID, MUTATION_ID)
TOKEN_MAP = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}
FORBIDDEN_OUTPUT = "<>\"'"
SEQUENCE_ALPHABET = ("a", "Z", "0", "&", "<", ">", '"', "'", "\x00", "\t", "\n", "é", "中", "😀")


def _verify_contract_roster_and_callers(root: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("AutoAR contract is not validly adopted")
    expected_site = f"h0tak88r/AutoAR@{PIN}:{SOURCE_FILE}:2:esc"
    if contract.get("site") != expected_site:
        raise RuntimeError("AutoAR contract site differs from the exact pinned esc helper")
    adoption = contract.get("adoption", {})
    if (
        adoption.get("source_url") != REPOSITORY.removesuffix(".git")
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("AutoAR adoption record is not bound to the verified source")
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if roster.get("cohort_id") != "2026-09-12-calibration-20-r2":
        raise RuntimeError("AutoAR roster is not bound to the frozen 20-r2 cohort")
    identities = [
        item for item in roster.get("identities", [])
        if item.get("site") == expected_site and item.get("question_id") == PROPERTY_ID
    ]
    if len(identities) != 1 or identities[0].get("contract_sha256") != contract_digest(contract):
        raise RuntimeError("frozen AutoAR roster does not bind this contract digest")

    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
    if evidence.get("pin") != PIN or evidence.get("repository") != REPOSITORY.removesuffix(".git"):
        raise RuntimeError("AutoAR caller evidence is not bound to the frozen repository pin")
    caller_hashes = {
        "internal/api/ui/index.html": "8593ab3c95a35caaedc87cc84de8b3d42d212be41367921f29a94b3fac97237f",
        "internal/api/ui/app.js": "467b5813b01cf3df6047f378656b3add5cf050dfbf2c55b04fcc883e9e8496c0",
        "internal/api/ui/pages/scan-detail.js": "e7b3fdc145d16245f3f62cca9791c6108b61afa7c767ff57fe9a2bec6b7bf06b",
        "internal/api/ui/pages/findings-rows.js": "3d969ba73629822201f2d5c07035fb3ee15cd0374db9c1679b63e817e8462bcd",
    }
    by_path = {item.get("path"): item for item in evidence.get("callers", [])}
    for relative, expected_hash in caller_hashes.items():
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"AutoAR source evidence file is missing or a symlink: {relative}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash or by_path.get(relative, {}).get("sha256") != expected_hash:
            raise RuntimeError(f"AutoAR caller source digest differs at {relative}")

    index = (root / "internal/api/ui/index.html").read_text(encoding="utf-8")
    app = (root / "internal/api/ui/app.js").read_text(encoding="utf-8")
    scan_detail = (root / "internal/api/ui/pages/scan-detail.js").read_text(encoding="utf-8")
    findings = (root / "internal/api/ui/pages/findings-rows.js").read_text(encoding="utf-8")
    if not (
        index.index('/ui/pages/html-escape.js') < index.index('/ui/app.js')
        and "callPageMethod('HtmlEscapePage', 'esc'" in app
        and "/results/file?file_name=" in scan_detail
        and "window.renderRowForUnifiedTab(r, rowIdx" in scan_detail
        and "tbody.innerHTML" in scan_detail
        and "raw finding object from the API" in findings
        and "${esc(display)}" in findings
    ):
        raise RuntimeError("AutoAR scan-result-to-text-node caller path changed")
    return contract


def _reference(value: str) -> str:
    return "".join(TOKEN_MAP.get(character, character) for character in value)


def _cases() -> list[str]:
    # Exhaust every valid BMP scalar value; supplementary values are included
    # explicitly and in the seeded composed strings below.
    values = [""]
    values.extend(chr(codepoint) for codepoint in range(0x10000) if not 0xD800 <= codepoint <= 0xDFFF)
    values.extend(("😀", "🧪", "𐐷", "\U0010ffff"))

    for length in (1, 2, 3):
        for parts in itertools.product(SEQUENCE_ALPHABET, repeat=length):
            values.append("".join(parts))

    values.extend(
        (
            "&lt;script&gt;alert(1)&lt;/script&gt;",
            "<script>alert('x')</script>",
            "\" onmouseover='alert(1)' <tag>",
            "prefix & middle < suffix > end",
            "target/é/😀/\U0010ffff",
        )
    )
    rng = random.Random(20261015)
    pool = (*SEQUENCE_ALPHABET, "\r", "\v", "\u2028", "\u2029", "🧪", "\U0010ffff")
    for _ in range(2048):
        values.append("".join(rng.choice(pool) for _ in range(rng.randint(1, 255))))
    return values


def _verify_product() -> dict:
    values = _cases()
    outputs, node_version = run_esc(values)
    if len(outputs) != len(values):
        raise RuntimeError("AutoAR product replay returned the wrong output count")
    for index, (value, actual) in enumerate(zip(values, outputs, strict=True)):
        expected = _reference(value)
        if actual != expected:
            raise RuntimeError(f"AutoAR helper differs from the independent image at case {index}")
        if any(token in actual for token in FORBIDDEN_OUTPUT):
            raise RuntimeError(f"AutoAR helper left a raw HTML delimiter in case {index}")

    mutated, _ = run_esc(["<"], leak_less_than=True)
    if mutated != ["<"] or not mutation_reproduces("<"):
        raise RuntimeError("pinned-source mutation did not replay a raw less-than output")

    report = {
        "schema_version": "1",
        "gate_id": "autoar-html-text-escape-20r2",
        "repository": REPOSITORY.removesuffix(".git"),
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "product_engine": "Node.js ECMAScript RegExp / String.replace",
        "node_version": node_version,
        "property_id": PROPERTY_ID,
        "mutation_id": MUTATION_ID,
        "mutation_witness": "<",
        "mutation_product_output": mutated[0],
        "differential_cases": len(values),
        "case_classes": {
            "valid_bmp_scalar_values": 0x10000 - 0x800,
            "supplementary_scalar_values": 4,
            "exhaustive_special_and_control_sequences": sum(len(SEQUENCE_ALPHABET) ** n for n in (1, 2, 3)),
            "targeted_strings": 5,
            "seeded_composed_strings": 2048,
        },
        "mismatches": 0,
        "raw_html_delimiter_outputs": 0,
        "scope": "HtmlEscapePage.esc output used in HTML text nodes; not an all-context XSS proof",
    }
    return report


def _run_harness() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--require-ground-truth",
            "--require-domain",
            "--require-contract",
            "--fail-on-property-failure",
            *QUESTION_IDS,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()[-4000:]
        raise RuntimeError(f"AutoAR property harness failed ({completed.returncode}): {detail}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean AutoAR checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip Z3; run source and product regressions")
    parser.add_argument("--output", type=Path, help="write the machine-readable product gate report")
    args = parser.parse_args(argv)
    if args.source_root:
        requested = Path(args.source_root).expanduser().resolve()
        configured = os.environ.get("AUTOAR_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            parser.error("--source-root conflicts with AUTOAR_REPLAY_SOURCE")
        os.environ["AUTOAR_REPLAY_SOURCE"] = str(requested)
    try:
        root = source_root()
        print(f"AutoAR exact source: {root} @ {PIN}")
        _verify_contract_roster_and_callers(root)
        if not args.product_only:
            _run_harness()
        report = _verify_product()
        if args.output:
            atomic_write_text(args.output, json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n")
        print(
            f"AutoAR product differential: {report['differential_cases']} values, "
            f"Node {report['node_version']}, 0 mismatches; pinned mutation leaks '<'"
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"AutoAR HTML text escape gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
