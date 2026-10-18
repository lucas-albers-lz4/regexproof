#!/usr/bin/env python3
"""Run the pinned Mycelium release-checksum proof and product regression gate."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.mycelium_release_replay import (  # noqa: E402
    PATTERN,
    PIN,
    PIN_20R2,
    preflight_rejects_without_sha256_line,
    source_root,
    valid_record_reaches_checksum_command,
)

PROPERTY = "MY-mycelium-release-preflight-requires-64-hex"
MUTATION = "MY-mycelium-release-preflight-mutated-empty-hash"
PROPERTY_BY_PIN = {
    PIN: PROPERTY,
    PIN_20R2: "MY-mycelium-20r2-release-preflight-requires-64-hex",
}
MUTATION_BY_PIN = {
    PIN: MUTATION,
    PIN_20R2: "MY-mycelium-20r2-release-preflight-mutated-empty-hash",
}
MIRROR_EXPR = (
    'Concat(Loop(Union(Range("0","9"),Range("A","F"),Range("a","f")),64,64),'
    'Plus(Union(Re(" "),Re("\\t"),Re("\\v"),Re("\\f"),Re("\\r"))),'
    'Union(Re(""),Re("*")),'
    'Union(Range("\\x01","\\x08"),Range("\\x0e","\\x1f"),Range("!","~"),Re("\\x7f")),'
    'Star(Union(Range("\\x01","\\t"),Range("\\x0b","\\x7f"))))'
)


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
        raise SystemExit(result.returncode)
    return output


def _differential_fuzz() -> int:
    alphabet = "0123456789abcdefABCDEF *x\t"
    targets = [
        "a" * 64 + " file.tar.gz",
        "a" * 63 + " file.tar.gz",
        "a" * 65 + " file.tar.gz",
        "<html>proxy error without a checksum line",
    ]
    output = _run(
        [
            sys.executable,
            str(ROOT / "scripts" / "differential-fuzz.py"),
            "--mirror-expr",
            MIRROR_EXPR,
            "--alphabet",
            alphabet,
            "--mutations",
            "!;=",
            "--runs",
            "30",
            "--seed",
            "20261015",
            "--exhaust-max-len",
            "1",
            "--max-len",
            "80",
            "--targets",
            *targets,
            "--real-argv",
            "grep",
            "-qE",
            PATTERN,
        ],
        env=os.environ.copy(),
        timeout=180,
    )
    match = re.search(r"^(\d+) inputs, 0 mismatches \(seed=20261015\)$", output, re.MULTILINE)
    if match is None:
        raise RuntimeError("differential fuzzer did not report its zero-mismatch case count")
    return int(match.group(1))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Mycelium checkout at the adopted pin")
    parser.add_argument(
        "--source-pin", choices=sorted(PROPERTY_BY_PIN), default=PIN,
        help="pinned Mycelium source identity (default: current off-cohort calibration pin)",
    )
    args = parser.parse_args(argv)
    try:
        pin = args.source_pin
        property_id = PROPERTY_BY_PIN[pin]
        mutation_id = MUTATION_BY_PIN[pin]
        source_env = "MYCELIUM_REPLAY_SOURCE" if pin == PIN else "MYCELIUM_20R2_REPLAY_SOURCE"
        if args.source_root:
            requested = Path(args.source_root).expanduser().resolve()
            configured = os.environ.get(source_env)
            if configured and Path(configured).expanduser().resolve() != requested:
                raise RuntimeError(f"--source-root conflicts with {source_env}")
            os.environ[source_env] = str(requested)
        root = source_root(pin)
        print(f"Mycelium source: {root} @ {pin}")

        from regexproof.harness import REGISTRY
        from regexproof.harness.contract import product_reportable

        entry = REGISTRY.get(property_id)
        if entry is None or not product_reportable(entry):
            raise RuntimeError("release-preflight property lacks an eligible adopted contract")
        if entry.get("input_domain") != "ascii" or entry.get("pattern") != PATTERN:
            raise RuntimeError("release-preflight property domain or source pattern changed")
        _run(
            [
                sys.executable,
                str(ROOT / "scripts" / "z3-verify.py"),
                property_id,
                mutation_id,
                "--require-ground-truth",
                "--fail-on-property-failure",
            ],
            env=os.environ.copy(),
            timeout=180,
        )
        if not preflight_rejects_without_sha256_line(pin=pin):
            raise RuntimeError("empty/checksum-free text reached the platform checksum command")
        if not valid_record_reaches_checksum_command(pin=pin):
            raise RuntimeError("well-formed checksum record did not reach the checksum command")
        print(
            "Mycelium product replay: empty/checksum-free text rejected before the "
            "checksum command; valid record reached a lenient checksum fixture"
        )
        cases = _differential_fuzz()
        print(f"Mycelium source-pattern differential: {cases} inputs, 0 mismatches")
    except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"Mycelium release-preflight gate failed: {exc}", file=sys.stderr)
        return 1
    print("Mycelium release-preflight proof and regression gate passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
