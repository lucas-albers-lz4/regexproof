#!/usr/bin/env python3
"""Replay two exact-pin LLM honeypot shell boundaries without network access."""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.llm_honeypot_replay import (  # noqa: E402
    PIN,
    PRIVATE_IP_PATTERN,
    REPO_URL,
    TOR_PATTERN,
    run_pinned_sanitizer,
    run_pinned_send_newnym,
    source_root,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402


AUTH_ONLY_THEN_SIGNAL_ERROR = (
    "250 OK\r\n"
    "551 Internal error\r\n"
    "250 closing connection\r\n"
)
SUCCESSFUL_SEQUENCE = (
    "250 OK\r\n"
    "250 OK\r\n"
    "250 closing connection\r\n"
)
FAILURE_ONLY_SEQUENCE = "551 Internal error\r\n"


class GateError(ValueError):
    """The pinned shell helper or a calibration control changed."""


def _tool_version(argv: list[str]) -> str:
    tool = shutil.which(argv[0])
    if tool is None:
        return "missing"
    completed = subprocess.run(
        [tool, *argv[1:]], capture_output=True, text=True, timeout=5, check=False
    )
    return (completed.stdout or completed.stderr).splitlines()[0].strip()


def _clean_response(result: dict[str, Any]) -> None:
    if result["commands"] != result["expected_commands"]:
        raise GateError("pinned send_newnym did not send the expected command sequence")


def build_report(checkout: Path) -> dict[str, Any]:
    # One whole eligible text file exercises the pinned find + sed helper over
    # every canonical 192.168/16 address, not just the regex in isolation.
    exhaustive_192 = "\n".join(
        f"192.168.{third}.{fourth}"
        for third in range(256)
        for fourth in range(256)
    )
    exhaustive = run_pinned_sanitizer(exhaustive_192, checkout=checkout)
    output_rows = exhaustive["output"].splitlines()
    if len(output_rows) != 65_536 or any(row != "[REDACTED]" for row in output_rows):
        raise GateError("the exact pinned sanitizer changed its 192.168/16 coverage")

    sample = "10.0.0.1 172.16.0.1 192.168.1.1 8.8.8.8\n"
    sample_result = run_pinned_sanitizer(sample, checkout=checkout)
    sample_output = sample_result["output"]
    expected_sample = "10.0.0.1 172.16.0.1 [REDACTED] 8.8.8.8\n"
    if sample_output != expected_sample:
        raise GateError(f"unexpected pinned sanitizer output: {sample_output!r}")

    # Sensitivity control: anchoring the replacement to the whole file makes
    # an address embedded in ordinary generated text pass through.
    mutation_input = "source=192.168.4.9;\n"
    mutation = run_pinned_sanitizer(
        mutation_input,
        checkout=checkout,
        pattern_override=r"^192\.168\.[0-9]+\.[0-9]+$",
    )
    if mutation["output"] != mutation_input:
        raise GateError("anchored-search mutation unexpectedly redacted embedded text")

    tor_success = run_pinned_send_newnym(SUCCESSFUL_SEQUENCE, checkout=checkout)
    _clean_response(tor_success)
    if not tor_success["success"]:
        raise GateError("successful AUTHENTICATE/SIGNAL sequence was rejected")

    tor_candidate = run_pinned_send_newnym(
        AUTH_ONLY_THEN_SIGNAL_ERROR, checkout=checkout
    )
    _clean_response(tor_candidate)
    if not tor_candidate["success"]:
        raise GateError("the pinned auth-success/signal-error candidate no longer reproduces")

    tor_failure_only = run_pinned_send_newnym(FAILURE_ONLY_SEQUENCE, checkout=checkout)
    _clean_response(tor_failure_only)
    if tor_failure_only["success"]:
        raise GateError("failure-only Tor control response unexpectedly reported success")

    tor_mutation = run_pinned_send_newnym(
        FAILURE_ONLY_SEQUENCE, checkout=checkout, pattern_override=".*"
    )
    _clean_response(tor_mutation)
    if not tor_mutation["success"]:
        raise GateError("widened grep mutation did not accept a failure-only response")

    return {
        "schema_version": "1",
        "artifact_kind": "llm-honeypot-p2-product-replay",
        "cohort_id": "2026-09-12-calibration-20-r2",
        "repo_id": "Leviticus-Triage/llm-honeypot-intelligence",
        "repository_url": REPO_URL,
        "pin": PIN,
        "result": "pass_candidate_reproduced",
        "source_replay": {
            "method": "Exact pinned function definitions were extracted from authenticated source files and run in isolated temporary directories. The Tor nc command was replaced by a local fixture that supplied fixed protocol replies; no network or real credentials were used.",
            "clean_checkout_head": PIN,
            "sanitizer_pattern": PRIVATE_IP_PATTERN,
            "tor_pattern": TOR_PATTERN,
        },
        "private_ip_redaction": {
            "exhaustive_192_168_addresses": 65_536,
            "exhaustive_redacted": len(output_rows),
            "sample_input": sample,
            "sample_output": sample_output,
            "mutation_input": mutation_input,
            "mutation_output": mutation["output"],
            "differential_cases": 65_541,
            "interpretation": "The exact helper redacts all tested 192.168/16 tokens but leaves representative 10/8 and 172.16/12 private addresses unchanged. No actual generated artifact or published repository data was inspected.",
        },
        "tor_newnym": {
            "successful_sequence": tor_success,
            "auth_success_then_signal_error": tor_candidate,
            "failure_only_sequence": tor_failure_only,
            "widened_matcher_mutation": tor_mutation,
            "differential_cases": 4,
            "interpretation": "The exact helper reports success when AUTHENTICATE returns 250 OK and the later SIGNAL NEWNYM reply returns 551. This demonstrates response-sequence handling in the pinned function; it does not establish that a deployed Tor instance reached this error state or that a scan used the unchanged exit.",
        },
        "engines": {
            "bash": _tool_version(["bash", "--version"]),
            "sed": _tool_version(["sed", "--version"]),
            "grep": _tool_version(["grep", "--version"]),
            "host_platform": platform.platform(),
            "python": platform.python_version(),
        },
        "confirmed_security_impact": 0,
        "external_report_sent": False,
        "maintainer_confirmation": False,
        "third_party_fix": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=source_root())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = build_report(args.source_root)
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        args.output.chmod(0o644)
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        print(f"llm-honeypot-boundary-regression-gate: error: {exc}", file=sys.stderr)
        return 2
    print(
        "LLM honeypot pinned candidates reproduced: "
        f"65,536 192.168 addresses redacted; private-IP gaps and Tor reply-sequence candidate confirmed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
