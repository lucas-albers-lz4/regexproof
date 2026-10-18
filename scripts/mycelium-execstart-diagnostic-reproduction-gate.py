#!/usr/bin/env python3
"""Reproduce the pinned Mycelium systemd ExecStart diagnostic false negative."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.mycelium_execstart_replay import (  # noqa: E402
    CAPTURE_PIPELINE,
    PIN,
    REPO_REF_PIPELINE,
    SOURCE_ENV,
    capture_execstart,
    capture_repo_ref,
    source_root,
)

ARTIFACT = (
    ROOT
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-mycelium-script-slice"
    / "systemd-execstart-semicolon-replay.json"
)
CONTRACT = ARTIFACT.parent / "contract-execstart-diagnostic.json"
PROPERTY = "MY-mycelium-drift-systemd-semicolon-drops-bypass"
MUTATION = "MY-mycelium-drift-mutated-space-capture-drops-bypass"


def _run(argv: list[str], *, env: dict[str, str], timeout: int) -> str:
    result = subprocess.run(
        argv,
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        shell=False,
        timeout=timeout,
        check=False,
    )
    output = result.stdout + result.stderr
    if output:
        print(output, end="")
    if result.returncode:
        raise RuntimeError(f"command exited {result.returncode}: {argv[0]}")
    return output


def _verify_pinned_file(source: Path, relative: str, expected_sha256: str) -> None:
    path = source / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"related source is missing or a symlink: {relative}")
    committed = subprocess.run(
        ["git", "-C", str(source), "show", f"{PIN}:{relative}"],
        capture_output=True,
        check=True,
        timeout=20,
    ).stdout
    if path.read_bytes() != committed:
        raise RuntimeError(f"working source differs from {PIN}:{relative}")
    actual = hashlib.sha256(committed).hexdigest()
    if actual != expected_sha256:
        raise RuntimeError(f"{relative} digest is {actual}, expected {expected_sha256}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Mycelium checkout at the adopted pin")
    parser.add_argument("--systemd-artifact", type=Path, default=ARTIFACT)
    args = parser.parse_args(argv)
    try:
        requested = Path(args.source_root).expanduser().resolve() if args.source_root else None
        if requested is not None:
            configured = os.environ.get(SOURCE_ENV)
            if configured and Path(configured).expanduser().resolve() != requested:
                raise RuntimeError(f"--source-root conflicts with {SOURCE_ENV}")
            os.environ[SOURCE_ENV] = str(requested)
        source = source_root()

        artifact_bytes = args.systemd_artifact.read_bytes()
        replay = json.loads(artifact_bytes)
        if replay.get("source_pin") != PIN:
            raise RuntimeError("systemd replay artifact does not match the adopted source pin")
        if replay.get("pinned_parser", {}).get("exec_all_pipeline") != CAPTURE_PIPELINE:
            raise RuntimeError("systemd replay artifact does not match the pinned capture pipeline")
        if replay.get("pinned_parser", {}).get("repo_ref_pattern") != REPO_REF_PIPELINE:
            raise RuntimeError("systemd replay artifact does not match the pinned repo-ref capture")
        raw = replay.get("raw_output")
        if not isinstance(raw, str) or "--insecure-no-verify" not in raw:
            raise RuntimeError("systemd replay artifact has no late bypass flag")
        captured = capture_execstart(raw)
        ref = capture_repo_ref(captured)
        recorded = replay["pinned_parser"]
        if captured != recorded.get("captured_exec_all"):
            raise RuntimeError("pinned parser output differs from the saved systemd replay")
        if ref != recorded.get("captured_repo_ref"):
            raise RuntimeError("pinned repo-ref output differs from the saved systemd replay")
        if "--insecure-no-verify" in captured or ref:
            raise RuntimeError("the recorded parser false negative no longer reproduces")

        controls = replay["pinned_controls"]
        _verify_pinned_file(
            source, controls["control_file"], controls["control_sha256"]
        )
        _verify_pinned_file(source, controls["test_file"], controls["test_sha256"])

        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        if contract.get("site") != (
            f"mycelium0/mycelium@{PIN}:scripts/update_unit_drift_drill.sh:184:3"
        ):
            raise RuntimeError("diagnostic contract does not identify the pinned parser site")
        from regexproof.harness import REGISTRY
        from regexproof.harness.contract import product_reportable

        entry = REGISTRY.get(PROPERTY)
        if entry is None or not product_reportable(entry):
            raise RuntimeError("counterexample property lacks its adopted source contract")
        if entry.get("contract") != contract:
            raise RuntimeError("registered contract differs from the adopted contract file")

        print(f"Mycelium source: {source} @ {PIN}")
        print(
            "systemd replay: raw argv contains --insecure-no-verify; "
            "pinned exec_all omits it; repo-ref capture is empty"
        )
        _run(
            [
                sys.executable,
                str(ROOT / "scripts" / "z3-verify.py"),
                PROPERTY,
                MUTATION,
                "--require-ground-truth",
                "--fail-on-property-failure",
            ],
            env=os.environ.copy(),
            timeout=180,
        )
        digest = hashlib.sha256(artifact_bytes).hexdigest()
        print(f"systemd replay artifact sha256: {digest}")
        print(
            "Mycelium diagnostic counterexample reproduced. This gate records a parser defect; "
            "it does not establish an unattended authentication bypass or an upstream fix."
        )
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"Mycelium ExecStart diagnostic gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
