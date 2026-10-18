#!/usr/bin/env python3
"""Replay the pinned AutoAR loopback script-fetch candidate on local fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import contract_digest  # noqa: E402
from regexproof.groundtruth.autoar_jsendpoints_scope_replay import (  # noqa: E402
    CALLER_SHA256,
    GO_TOOLCHAIN,
    PIN,
    README_SHA256,
    SOURCE_FILE,
    SOURCE_SHA256,
    origins_differ,
    run_collector,
    source_root,
    start_scope_fixture,
    verify_source_evidence,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-15-autonomous-autoar-jsendpoint-scope-escape-20r2"
CONTRACT_PATH = SLICE / "contract.json"
ROSTER_PATH = SLICE / "roster.json"
QUESTION_ID = "AA-autoar-jsendpoint-loopback-script-src-fetch"
EXPECTED_ENDPOINT = "/api/v1/users"


def _verify_contract_roster_and_source(checkout: Path) -> dict:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not valid_product_contract(contract):
        raise RuntimeError("AutoAR scope candidate contract is not validly adopted")
    expected_site = (
        f"h0tak88r/AutoAR@{PIN}:{SOURCE_FILE}:22:scriptSrcRe"
    )
    if contract.get("site") != expected_site:
        raise RuntimeError("AutoAR scope contract is not bound to the exact regex site")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").rstrip("/").removesuffix(".git")
        != "https://github.com/h0tak88r/AutoAR"
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
    ):
        raise RuntimeError("AutoAR scope adoption does not bind the verified parser source")
    roster = json.loads(ROSTER_PATH.read_text(encoding="utf-8"))
    if roster.get("cohort_id") != "2026-09-12-calibration-20-r2":
        raise RuntimeError("AutoAR scope roster is not bound to frozen 20-r2")
    identities = [
        row
        for row in roster.get("identities", [])
        if row.get("question_id") == QUESTION_ID and row.get("site") == expected_site
    ]
    if (
        len(identities) != 1
        or identities[0].get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("frozen AutoAR scope roster does not bind this contract")
    source_check = verify_source_evidence()
    if source_check.get("parser_sha256") != SOURCE_SHA256:
        raise RuntimeError("source-evidence verifier did not confirm the parser digest")
    if source_check.get("caller_sha256") != CALLER_SHA256:
        raise RuntimeError("source-evidence verifier did not confirm the caller digest")
    if source_check.get("readme_sha256") != README_SHA256:
        raise RuntimeError("source-evidence verifier did not confirm the README digest")
    if checkout.resolve() != source_root().resolve():
        raise RuntimeError("requested source checkout differs from the exact pinned checkout")
    return contract


def _has_endpoint(result: dict, script_url: str) -> bool:
    return any(
        endpoint.get("Path") == EXPECTED_ENDPOINT
        and endpoint.get("Source") == script_url
        for endpoint in result.get("endpoints", [])
    )


def _verify_local_product_replay() -> dict:
    fixture = start_scope_fixture()
    try:
        if not origins_differ(fixture.target_url, fixture.canary_script_url):
            raise RuntimeError("loopback canary fixture did not use a distinct origin")
        if urlparse(fixture.canary_script_url).hostname != "127.0.0.1":
            raise RuntimeError("canary fixture escaped IPv4 loopback")

        cross_origin = run_collector(
            [{"hosts": [fixture.target_url], "threads": 1}]
        )
        cross_result = cross_origin["results"][0]
        cross_counts = fixture.counts_snapshot()
        if (
            cross_counts.get("target /") != 1
            or cross_counts.get("canary /bundle.js") != 1
            or not _has_endpoint(cross_result, fixture.canary_script_url)
        ):
            raise RuntimeError(
                "pinned collector did not fetch the cross-origin loopback script "
                "and extract its harmless endpoint"
            )

        fixture.same_origin = True
        same_origin = run_collector(
            [{"hosts": [fixture.target_url], "threads": 1}]
        )
        same_result = same_origin["results"][0]
        final_counts = fixture.counts_snapshot()
        if (
            final_counts.get("target /") != 2
            or final_counts.get("canary /bundle.js") != 1
            or final_counts.get("target /bundle.js") != 1
            or not _has_endpoint(same_result, fixture.same_origin_script_url)
        ):
            raise RuntimeError("same-origin control did not fetch the local bundle")

        return {
            "go_version": cross_origin["go_version"],
            "target_url": fixture.target_url,
            "cross_origin_script_url": fixture.canary_script_url,
            "same_origin_script_url": fixture.same_origin_script_url,
            "cross_origin_origins_differ": True,
            "cross_origin_counts_after_case": cross_counts,
            "request_counts_after_both_cases": final_counts,
            "cross_origin_endpoint": EXPECTED_ENDPOINT,
            "same_origin_endpoint": EXPECTED_ENDPOINT,
            "cases": 2,
            "external_network_requests": 0,
            "impact_confirmed": False,
        }
    finally:
        fixture.close()


def _run_harness(source_root_path: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--require-ground-truth",
            "--require-domain",
            "--require-contract",
            "--fail-on-property-failure",
            QUESTION_ID,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=240,
        check=False,
        shell=False,
        env={**os.environ, "AUTOAR_REPLAY_SOURCE": str(source_root_path)},
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()[-4000:]
        raise RuntimeError(
            f"AutoAR scope counterexample proof/replay failed "
            f"({completed.returncode}): {detail}"
        )
    records = []
    for line in completed.stdout.splitlines():
        if line.strip().startswith("{"):
            records.append(json.loads(line))
    matched = [row for row in records if row.get("name") == QUESTION_ID]
    if (
        len(matched) != 1
        or matched[0].get("result") != "sat"
        or matched[0].get("ground_truth") != "reproduced"
        or not matched[0].get("product")
    ):
        raise RuntimeError("AutoAR scope proof did not emit one product SAT/reproduced record")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean AutoAR checkout at the adopted pin")
    parser.add_argument("--product-only", action="store_true", help="skip Z3 proof/replay")
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
        _verify_contract_roster_and_source(checkout)
        if not args.product_only:
            _run_harness(checkout)
        result = _verify_local_product_replay()
        report = {
            "schema_version": "1",
            "gate_id": "autoar-jsendpoint-scope-candidate-20r2",
            "repository": "https://github.com/h0tak88r/AutoAR",
            "source_pin": PIN,
            "parser_file": SOURCE_FILE,
            "parser_sha256": SOURCE_SHA256,
            "caller_sha256": CALLER_SHA256,
            "readme_sha256": README_SHA256,
            "product_engine": "pinned Go CollectEndpointsForHosts (Go net/http and regexp/RE2)",
            "go_version": result["go_version"],
            "property_id": QUESTION_ID,
            "property_kind": "counterexample_finder",
            "candidate_result": "cross_origin_loopback_fetch_reproduced",
            "target_url": result["target_url"],
            "cross_origin_script_url": result["cross_origin_script_url"],
            "same_origin_script_url": result["same_origin_script_url"],
            "differential_cases": result["cases"],
            "case_classes": {"cross_origin_loopback_fetch": 1, "same_origin_control": 1},
            "request_evidence": result["request_counts_after_both_cases"],
            "endpoint": result["cross_origin_endpoint"],
            "external_network_requests": 0,
            "security_impact_confirmed": False,
            "disposition": "reproduced_reachable_pending_impact_and_maintainer_triage",
            "scope_note": (
                "Exact-pinned source replay against two disposable IPv4 loopback HTTP servers. "
                "It proves that the collector follows this absolute .js URL to a different origin; "
                "it does not prove access to sensitive data, production reachability, or a maintainer-accepted vulnerability."
            ),
        }
        if result["go_version"] != GO_TOOLCHAIN:
            raise RuntimeError("local product replay used an unexpected Go version")
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            )
        replay_label = (
            "product-only replay"
            if args.product_only
            else "SAT proof and product replay"
        )
        print(
            f"AutoAR scope candidate: {replay_label}; cross-origin loopback "
            f"request reached local canary; {result['cases']} cases, "
            "no external requests; impact unconfirmed"
        )
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as exc:
        print(f"autoar-jsendpoint-scope-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
