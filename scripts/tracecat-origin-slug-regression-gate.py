#!/usr/bin/env python3
"""Run the pinned Tracecat origin-slug proof and product regression gate."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import os
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.tracecat_replay import (  # noqa: E402
    PIN,
    artifact_s3_key,
    mutation_reproduces,
    origin_substitution_pattern,
    safe_origin_component,
    slugify_origin,
    source_root,
)

PROPERTY = "TC-tracecat-origin-slug-safe-image"
MUTATION = "TC-tracecat-mutated-origin-slash-passthrough"
ALLOWED = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
SAFE_SAMPLES = "aZ0_-"
BAD_SAMPLES = (
    ".",
    "/",
    ":",
    "@",
    "%",
    "+",
    " ",
    "\t",
    "\n",
    "é",
    "中",
    "٣",
    "\uff11",
    "\u3000",
    "\\",
    "\x7f",
)


def _reference_slugify(origin: str) -> str:
    """Independent character-wise statement of the pinned helper's stages."""
    normalized = (
        origin.replace("git+ssh://", "")
        .replace("https://", "")
        .replace("http://", "")
    )
    translated = "".join(ch if ch in ALLOWED else "_" for ch in normalized)
    collapsed: list[str] = []
    for char in translated:
        if char != "_" or not collapsed or collapsed[-1] != "_":
            collapsed.append(char)
    slug = "".join(collapsed).strip("_")
    if len(slug) <= 100:
        return slug
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]
    return f"{slug[:87]}_{digest}"


def _prepare_source_root(raw: str | None) -> Path:
    if raw:
        requested = Path(raw).expanduser().resolve()
        configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            raise RuntimeError("--source-root conflicts with TRACECAT_REPLAY_SOURCE")
        os.environ["TRACECAT_REPLAY_SOURCE"] = str(requested)
    return source_root()


def _check_source_pattern_input() -> int:
    """Adapter for differential-fuzz.py: exit 0 when the source class matches."""
    value = sys.stdin.read()
    return 0 if re.fullmatch(origin_substitution_pattern(), value) is not None else 1


def _run(argv: list[str], *, env: dict[str, str], timeout: int) -> None:
    result = subprocess.run(
        argv,
        cwd=ROOT,
        env=env,
        shell=False,
        timeout=timeout,
        check=False,
    )
    if result.returncode:
        raise SystemExit(result.returncode)


def _check_product_case(origin: str, case_number: int) -> None:
    if not 1 <= len(origin) <= 255:
        raise RuntimeError(f"case {case_number}: origin is outside the API length domain")
    expected = _reference_slugify(origin)
    actual = slugify_origin(origin)
    if actual != expected:
        raise RuntimeError(
            f"case {case_number}: product slug differs from the independent image "
            f"reference for {origin!r}: {actual!r} != {expected!r}"
        )
    if not safe_origin_component(actual):
        raise RuntimeError(f"case {case_number}: unsafe product slug {actual!r}")
    key = artifact_s3_key("test-org", origin, "v1")
    parts = key.split("/")
    expected_parts = [
        "test-org",
        "tarball-venvs",
        actual,
        "v1",
        "site-packages.squashfs",
    ]
    if parts != expected_parts:
        raise RuntimeError(
            f"case {case_number}: origin changed S3 key path structure: {key!r}"
        )


def _run_product_differential() -> int:
    rng = random.Random(20261014)
    cases = 0
    alphabet = SAFE_SAMPLES + "".join(BAD_SAMPLES)

    def check(origin: str) -> None:
        nonlocal cases
        cases += 1
        _check_product_case(origin, cases)

    # Exhaust every short combination over safe, path, delimiter, whitespace,
    # and Unicode representatives before the seeded longer corpus.
    for length in (1, 2):
        for chars in itertools.product(alphabet, repeat=length):
            check("".join(chars))

    targets = [
        "git+ssh://git@github.com/org/repo.git",
        "https://github.com/TracecatHQ/tracecat",
        "https://",
        "./../%2e%2e//repo",
        "a" * 100,
        "a" * 101,
        "a" * 255,
        "/" * 255,
        "_" * 255,
        "git+ssh://" + "x" * 245,
    ]
    for origin in targets:
        check(origin)

    for _ in range(2000):
        length = rng.randint(1, 255)
        check("".join(rng.choice(alphabet) for _ in range(length)))

    print(f"Tracecat product differential: {cases} origins, exact pin verified")
    return cases


def _differential_fuzzer(root: Path) -> None:
    bad_unique = tuple(dict.fromkeys(BAD_SAMPLES))
    mirror = "Union(" + ",".join(f"Re({char!r})" for char in bad_unique) + ")"
    alphabet = SAFE_SAMPLES + "".join(bad_unique)
    command = [
        sys.executable,
        str(ROOT / "scripts" / "differential-fuzz.py"),
        "--mirror-expr",
        mirror,
        "--alphabet",
        alphabet,
        "--mutations",
        "!",
        "--runs",
        "0",
        "--exhaust-max-len",
        "1",
        "--max-len",
        "1",
        "--real-argv",
        sys.executable,
        str(Path(__file__).resolve()),
        "--match-source-pattern",
        "--source-root",
        str(root),
    ]
    _run(command, env=os.environ.copy(), timeout=90)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Tracecat checkout at the adopted pin")
    parser.add_argument(
        "--match-source-pattern",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args(argv)
    if args.match_source_pattern:
        _prepare_source_root(args.source_root)
        return _check_source_pattern_input()

    try:
        from regexproof.harness import REGISTRY
        from regexproof.harness.contract import product_reportable

        root = _prepare_source_root(args.source_root)
        print(f"Tracecat source: {root} @ {PIN}")
        # validate_registry uses call_kind=substitution to skip validator-only
        # full-string anchors while retaining syntax and unsupported-escape
        # checks for this source pattern.
        entry = REGISTRY.get(PROPERTY)
        if entry is None or not product_reportable(entry):
            raise RuntimeError("origin-slug property lacks an eligible adopted contract")
        if entry.get("input_domain") != "unicode":
            raise RuntimeError("origin-slug property must declare its Unicode input domain")
        # The proof property and the source-level weakening both require the
        # adopted contract, declared input domain, and real mutation replay.
        # Eligibility is checked for this selected question above because the
        # CLI's --require-contract/--require-domain gates are registry-wide.
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
        if not mutation_reproduces("/"):
            raise RuntimeError("weakened source regex did not expose slash in the real S3 key")
        print("Tracecat product mutation replay: slash changes S3 key path structure")
        _differential_fuzzer(root)
        _run_product_differential()
    except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"Tracecat origin-slug gate failed: {exc}", file=sys.stderr)
        return 1
    print("Tracecat origin-slug proof and regression gate passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
