#!/usr/bin/env python3
"""Prove and replay Tracecat's exact custom RBAC scope-name boundary."""

from __future__ import annotations

import argparse
import itertools
import json
import os
import random
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pydantic  # noqa: E402

from regexproof.contract_adoption import (  # noqa: E402
    contract_digest,
    verify_adoption_source,
)
from regexproof.groundtruth.tracecat_rbac_scope_replay import (  # noqa: E402
    ALLOWED_SCOPE_CHARS,
    MUTATION_REQUIRED_SCOPE,
    MUTATION_SCOPE,
    NONSTAR_GLOB_CHARS,
    PIN,
    REPOSITORY,
    ROUTER_FILE,
    SCHEMA_FILE,
    SERVICE_FILE,
    SOURCE_FILE,
    SOURCE_SHA256,
    current_helper_accepts,
    current_model_accepts,
    exact_scope_name_acceptance,
    rbac_scope_question_mark_mutation_reproduces,
    source_digests,
    source_root,
)
from regexproof.harness import REGISTRY  # noqa: E402
from regexproof.harness.contract import (  # noqa: E402
    product_reportable,
    valid_product_contract,
)
from regexproof.harness.tracecat_rbac_scope import (  # noqa: E402
    CONTRACT,
    FAMILY,
    MUTATION_ID,
    PROPERTY_ID,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

SLICE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-tracecat-rbac-scope-pattern"
CONTRACT_PATH = SLICE / "contract.json"
SAMPLE_CHARS = "aAz09:_.*-?[] /\\\n\r\t\x00é中٣\u200b"


def _prepare_source_root(raw: str | None) -> Path:
    if raw:
        requested = Path(raw).expanduser().resolve()
        configured = os.environ.get("TRACECAT_REPLAY_SOURCE")
        if configured and Path(configured).expanduser().resolve() != requested:
            raise RuntimeError("--source-root conflicts with TRACECAT_REPLAY_SOURCE")
        os.environ["TRACECAT_REPLAY_SOURCE"] = str(requested)
    return source_root()


def _run_proof() -> None:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "z3-verify.py"),
        PROPERTY_ID,
        MUTATION_ID,
        "--require-ground-truth",
        "--fail-on-property-failure",
    ]
    subprocess.run(
        command,
        cwd=ROOT,
        env=os.environ.copy(),
        shell=False,
        timeout=180,
        check=True,
    )


def _locked_pydantic_version(root: Path) -> str:
    lock = tomllib.loads((root / "uv.lock").read_text(encoding="utf-8"))
    versions = {
        package.get("version")
        for package in lock.get("package", [])
        if package.get("name") == "pydantic"
    }
    if len(versions) != 1:
        raise RuntimeError(f"expected one locked Pydantic version, found {versions!r}")
    return str(next(iter(versions)))


def _cases() -> list[str]:
    values = [
        "".join(chars)
        for width in (1, 2)
        for chars in itertools.product(SAMPLE_CHARS, repeat=width)
    ]
    values.extend(
        [
            "custom:read",
            "action:tools?okta.*:execute",
            "action:tools[ab].*\u003aexecute",
            "custom:read\n",
            "custom:read\nother",
            "custom:read\r",
            "custom:read\t",
            "custom:réad",
            "custom:read\x00",
            ":read",
            "custom:",
            "x" * 255,
            "x" * 256,
            "custom:" + "x" * 247,
            "custom:" + "x" * 248,
        ]
    )
    rng = random.Random(20261016)
    values.extend(
        "".join(rng.choice(SAMPLE_CHARS) for _ in range(rng.randint(0, 260)))
        for _ in range(2048)
    )
    return list(dict.fromkeys(values))


def _expected_acceptance(value: str) -> bool:
    return (
        1 <= len(value) <= 255
        and ":" in value
        and all(char in ALLOWED_SCOPE_CHARS for char in value)
    )


def _verify_contract(root: Path) -> dict[str, str]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if contract != CONTRACT or not valid_product_contract(contract):
        raise RuntimeError("RBAC scope contract is not the adopted product contract")
    adoption = contract["adoption"]
    if (
        adoption.get("source_url", "").removesuffix(".git") != REPOSITORY
        or adoption.get("source_pin") != PIN
        or adoption.get("source_file") != SOURCE_FILE
        or adoption.get("source_sha256") != SOURCE_SHA256
        or adoption.get("contract_sha256") != contract_digest(contract)
    ):
        raise RuntimeError("RBAC scope adoption does not bind the exact pinned source")
    verify_adoption_source(contract, root)
    entry = REGISTRY.get(PROPERTY_ID)
    if entry is None or not product_reportable(entry):
        raise RuntimeError("RBAC scope property is not product-reportable")
    if entry.get("input_domain") != "unicode":
        raise RuntimeError("RBAC scope property must declare Unicode input")
    return source_digests(root)


def _run(source: Path, *, run_proof: bool = True) -> dict[str, object]:
    root = _prepare_source_root(str(source))
    digests = _verify_contract(root)
    locked_version = _locked_pydantic_version(root)
    if locked_version != "2.12.5" or pydantic.__version__ != locked_version:
        raise RuntimeError(
            f"Pydantic runtime {pydantic.__version__} differs from Tracecat lock {locked_version}"
        )

    cases = _cases()
    mismatches: list[dict[str, object]] = []
    accepted_count = 0
    nonstar_meta_rejections: dict[str, int] = {char: 0 for char in sorted(NONSTAR_GLOB_CHARS)}
    for index, value in enumerate(cases, 1):
        actual = exact_scope_name_acceptance(value)
        expected = _expected_acceptance(value)
        if actual != expected:
            mismatches.append(
                {
                    "case": index,
                    "input": repr(value),
                    "expected": expected,
                    "source_acceptance": actual,
                }
            )
            if len(mismatches) >= 5:
                break
        if actual:
            accepted_count += 1
            for char in NONSTAR_GLOB_CHARS:
                if char in value:
                    raise RuntimeError(
                        f"accepted scope contains fnmatch metacharacter {char!r}: {value!r}"
                    )
        for char in NONSTAR_GLOB_CHARS:
            if char in value and not current_model_accepts(value):
                nonstar_meta_rejections[char] += 1
    if mismatches:
        raise RuntimeError(f"scope request-model differential mismatches: {mismatches!r}")

    terminal_lf = "custom:read\n"
    if current_model_accepts(terminal_lf) or not current_helper_accepts(terminal_lf):
        raise RuntimeError("expected schema/helper terminal-LF distinction was not reproduced")
    if not rbac_scope_question_mark_mutation_reproduces({"scope_name": MUTATION_SCOPE}):
        raise RuntimeError("weakened exact-source question-mark mutation did not broaden matching")
    if run_proof:
        _run_proof()

    return {
        "schema_version": "1",
        "gate_id": "tracecat-rbac-scope-glob-alphabet",
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_files": digests,
        "request_schema_file": SCHEMA_FILE,
        "service_file": SERVICE_FILE,
        "route_file": ROUTER_FILE,
        "source_pattern": "^[a-z0-9:_.*-]+$",
        "property_id": PROPERTY_ID,
        "family": FAMILY,
        "mutation_id": MUTATION_ID,
        "contract_sha256": contract_digest(CONTRACT),
        "product_engine": f"Pydantic {pydantic.__version__} request model plus exact pinned Python re validator and fnmatch scope_matches",
        "guarantee": "A custom scope accepted by the pinned POST route's request schema and service validation contains no question-mark or bracket glob syntax; asterisk remains the only admitted glob metacharacter.",
        "differential_cases": len(cases),
        "accepted_cases": accepted_count,
        "nonstar_metacharacter_rejections": nonstar_meta_rejections,
        "mismatches": 0,
        "schema_rejects_terminal_lf": True,
        "standalone_python_helper_accepts_terminal_lf": True,
        "terminal_lf_note": "The helper alone has Python `$` final-newline behavior, but the exact Pydantic request schema rejects the value before the only pinned POST caller reaches it. This is not an HTTP acceptance or security finding at this pin.",
        "mutation_reproduced": True,
        "mutation_scope": MUTATION_SCOPE,
        "mutation_required_scope": MUTATION_REQUIRED_SCOPE,
        "mutation_effect": "Weakening both exact allowlists to admit `?` accepts the custom scope and the exact scope matcher treats `?` as a glob metacharacter when `*` is also present.",
        "limitations": "The contract covers newly submitted names through the pinned authorized create-scope route only. It does not cover pre-existing stored scopes, direct internal calls that bypass ScopeCreate, role assignment policy, least privilege, or deployed security impact. No current vulnerability, external report, maintainer confirmation, or fix is claimed.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--skip-proof",
        action="store_true",
        help="run only the exact-source product gate (the P6 wave owns proof execution)",
    )
    args = parser.parse_args(argv)
    try:
        report = _run(args.source_root, run_proof=not args.skip_proof)
        if args.output:
            atomic_write_text(
                args.output,
                json.dumps(report, indent=2, sort_keys=True) + "\n",
            )
        print(json.dumps(report, sort_keys=True))
    except Exception as exc:
        print(f"tracecat-rbac-scope-pattern-regression-gate: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
