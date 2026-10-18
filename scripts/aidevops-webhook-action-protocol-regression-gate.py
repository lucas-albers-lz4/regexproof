#!/usr/bin/env python3
"""Run contract proofs, mutation guards, and exact-pin Bash protocol replays."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import z3

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.contract_adoption import verify_adoption_source  # noqa: E402
from regexproof.groundtruth.aidevops_webhook_replay import (  # noqa: E402
    PIN,
    RECEIVER_FILE,
    RECEIVER_SHA256,
    REPOSITORY,
    dispatches,
    secret_name_accepts,
    secret_resolution_and_clear,
    sha_reaches_invalidator,
    slug_accepts,
    source_root,
)
from regexproof.groundtruth.aidevops_cited_file_replay import SOURCE_ENV  # noqa: E402
from regexproof.harness.aidevops_webhook_receiver import (  # noqa: E402
    M_PR,
    M_SECRET,
    M_SHA,
    M_SLUG,
    PAT_OWNER,
    PAT_PR_NUMBER,
    PAT_SECRET,
    PAT_SHA,
    PAT_SLUG,
    Q_PR,
    Q_SECRET,
    Q_SHA,
    _SOURCE_PR,
    _SOURCE_SECRET,
    _SOURCE_SHA,
    _SOURCE_SLUG,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402

REPO_ID = REPOSITORY.removeprefix("https://github.com/").removesuffix(".git")
BUNDLE = ROOT / "properties" / "calibration" / "2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2"
CONTRACTS = {
    "contract-secret-env-name.json": f"{REPO_ID}@{PIN}:{RECEIVER_FILE}:167:1",
    "contract-repository-slug.json": f"{REPO_ID}@{PIN}:{RECEIVER_FILE}:197:1",
    "contract-check-sha-regex-only.json": f"{REPO_ID}@{PIN}:{RECEIVER_FILE}:224:1",
    "contract-process-pr-number-regex-only.json": f"{REPO_ID}@{PIN}:{RECEIVER_FILE}:302:6",
}
PROPERTY_IDS = (Q_SECRET, Q_SHA, Q_PR)
MUTATION_IDS = (M_SECRET, M_SLUG, M_SHA, M_PR)
PATTERNS = {
    "secret_env_name": (PAT_SECRET, _SOURCE_SECRET),
    "repository_slug": (PAT_SLUG, _SOURCE_SLUG),
    "repository_owner": (PAT_OWNER, None),
    "check_sha": (PAT_SHA, _SOURCE_SHA),
    "pr_number": (PAT_PR_NUMBER, _SOURCE_PR),
}


def _compile(pattern: str):
    compiled = compile_pattern(
        pattern,
        dialect="posix-shell",
        call_kind="search",
        max_length=256,
        domain="ascii",
        shell_flags={"syntax": "bash_ksh"},
    )
    if not compiled.encodable:
        raise RuntimeError(f"Bash ERE is not encodable: {compiled.unencodable_reason}")
    return compiled.mirror


def _verify_contracts(root: Path) -> dict[str, str]:
    result = {}
    for filename, expected_site in CONTRACTS.items():
        contract = json.loads((BUNDLE / filename).read_text(encoding="utf-8"))
        if not valid_product_contract(contract):
            raise RuntimeError(f"contract is not validly adopted: {filename}")
        if contract.get("site") != expected_site:
            raise RuntimeError(f"contract has the wrong source site: {filename}")
        if not verify_adoption_source(contract, root):
            raise RuntimeError(f"contract source verification failed: {filename}")
        result[filename] = contract["adoption"]["contract_sha256"]
    return result


def _verify_source(root: Path) -> None:
    source_path = root / RECEIVER_FILE
    if source_path.is_symlink() or not source_path.is_file():
        raise RuntimeError("pinned webhook receiver is missing or a symlink")
    source = source_path.read_bytes()
    if hashlib.sha256(source).hexdigest() != RECEIVER_SHA256:
        raise RuntimeError("pinned webhook receiver digest changed")
    text = source.decode("utf-8")
    for pattern in (PAT_SECRET, PAT_SLUG, PAT_OWNER, PAT_SHA, PAT_PR_NUMBER):
        if pattern not in text:
            raise RuntimeError(f"pinned receiver no longer contains source ERE {pattern!r}")


def _strings(alphabet: str, max_length: int) -> list[str]:
    values = [""]
    for length in range(1, max_length + 1):
        values.extend("".join(chars) for chars in itertools.product(alphabet, repeat=length))
    return values


def _regex_accepts(mirror, value: str) -> bool:
    solver = z3.Solver()
    solver.set(timeout=1000)
    solver.add(z3.InRe(z3.StringVal(value), mirror))
    verdict = solver.check()
    if verdict == z3.unknown:
        raise RuntimeError(f"concrete Z3 mirror evaluation timed out for {value!r}")
    return verdict == z3.sat


def _slug_helper_mirror_accepts(value: str, owner_mirror) -> bool:
    slug = z3.StringVal(value)
    slash = z3.IndexOf(slug, z3.StringVal("/"), 0)
    owner = z3.SubString(slug, 0, slash)
    name = z3.SubString(slug, slash + 1, z3.Length(slug) - slash - 1)
    solver = z3.Solver()
    solver.set(timeout=1000)
    solver.add(
        z3.InRe(slug, _SOURCE_SLUG),
        z3.InRe(owner, owner_mirror),
        name != z3.StringVal("."),
        name != z3.StringVal(".."),
    )
    verdict = solver.check()
    if verdict == z3.unknown:
        raise RuntimeError(f"concrete slug mirror evaluation timed out for {value!r}")
    return verdict == z3.sat


def _bash_accepts(pattern: str, values: list[str]) -> list[bool]:
    if any("\x00" in value for value in values):
        raise ValueError("Bash argv cannot represent NUL; the declared protocol domain excludes it")
    script = (
        "pattern=$1; shift; "
        "for value do "
        'if [[ "$value" =~ $pattern ]]; then printf \'1\\n\'; '
        "else printf '0\\n'; fi; "
        "done"
    )
    try:
        completed = subprocess.run(
            ["/bin/bash", "-c", script, "regexproof", pattern, *values],
            cwd=ROOT,
            capture_output=True,
            env={**os.environ, "LC_ALL": "C"},
            text=True,
            timeout=30,
            check=False,
            shell=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Bash ERE replay timed out for {pattern!r}") from exc
    if completed.returncode != 0:
        raise RuntimeError(f"Bash ERE replay failed: {completed.stderr[-2000:]}")
    lines = completed.stdout.splitlines()
    if len(lines) != len(values) or any(line not in {"0", "1"} for line in lines):
        raise RuntimeError("Bash ERE replay returned malformed decisions")
    return [line == "1" for line in lines]


def _differential(pattern: str, mirror, values: list[str]) -> int:
    actual = _bash_accepts(pattern, values)
    for value, bash_result in zip(values, actual, strict=True):
        if _regex_accepts(mirror, value) != bash_result:
            raise RuntimeError(
                f"Bash/compiler disagreement for {pattern!r} on {value!r}: "
                f"bash={bash_result}"
            )
    return len(values)


def _run_harness() -> list[dict[str, Any]]:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "z3-verify.py"),
        "--json",
        "--require-ground-truth",
        "--require-domain",
        "--require-contract",
        "--fail-on-property-failure",
        *PROPERTY_IDS,
        *MUTATION_IDS,
    ]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        shell=False,
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()[-4000:]
        raise RuntimeError(f"contract proof/mutation harness failed: {detail}")
    try:
        records = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as exc:
        raise RuntimeError("proof harness emitted invalid NDJSON") from exc
    expected_names = set(PROPERTY_IDS + MUTATION_IDS)
    if {row.get("name") for row in records} != expected_names:
        raise RuntimeError("proof harness returned an incomplete property set")
    for row in records:
        if not row.get("ok"):
            raise RuntimeError(f"proof harness did not pass {row.get('name')}")
        if row["kind"] == "property" and (
            row["result"] != "unsat" or row.get("product") is not True
        ):
            raise RuntimeError(f"formal product property did not prove: {row['name']}")
        if row["kind"] == "mutation_guard" and (
            row["result"] != "sat" or row.get("ground_truth") != "reproduced"
        ):
            raise RuntimeError(f"mutation guard did not replay: {row['name']}")
    return records


def _verify_integrated_helpers(owner_mirror) -> dict[str, int]:
    checked = {
        "secret_env_name": 0,
        "repository_slug": 0,
        "check_sha": 0,
        "pr_number": 0,
        "secret_resolve_and_clear": 0,
    }
    secret_values = (
        "A", "_", "AIDEVOPS_WEBHOOK_SECRET", "x9_", "8SECRET", "-SECRET",
        "A-B", "AIDEVOPS_WEBHOOK_SECRET\n", "A\n", "A\t",
    )
    for value in secret_values:
        expected = _regex_accepts(_SOURCE_SECRET, value)
        actual = secret_name_accepts(value)
        if actual != expected:
            raise RuntimeError(f"secret helper/compiler mismatch for {value!r}")
        checked["secret_env_name"] += 1

    slug_values = (
        "owner/repo", "a/b", "1/repo", "owner/repo_name", "owner/repo-name",
        "owner/.", "owner/..", "owner/...", ".owner/repo", "-owner/repo",
        "_owner/repo", "owner/repo/extra", "owner/", "/repo", "owner/repo\n",
        "owner/re po", " owner/repo", "owner/repo\r", "owner;bad/repo",
    )
    for value in slug_values:
        expected = _slug_helper_mirror_accepts(value, owner_mirror)
        actual = slug_accepts(value)
        if actual != expected:
            raise RuntimeError(f"full slug helper/compiler mismatch for {value!r}")
        checked["repository_slug"] += 1

    sha_values = (
        "a" * 40, "A" * 40, "0123456789abcdef" * 2 + "01234567",
        "a" * 39, "a" * 41, "g" + "a" * 39, "a" * 39 + "\n",
        "", "0" * 40,
    )
    for value in sha_values:
        expected = _regex_accepts(_SOURCE_SHA, value)
        actual = sha_reaches_invalidator("owner/repo", value)
        if actual != expected:
            raise RuntimeError(f"SHA invalidator/compiler mismatch for {value!r}")
        checked["check_sha"] += 1

    process_values = ("1", "17", "482", "0", "00", "2#1", "-1", "x", "12extra")
    for value in process_values:
        canonical_positive = value.isascii() and value.isdecimal() and value[0] != "0"
        expected = _regex_accepts(_SOURCE_PR, value) and canonical_positive
        actual = dispatches(f"PROCESS_PR owner/repo {value}") == f"owner/repo|{value}"
        if actual != expected:
            raise RuntimeError(f"PR action dispatcher/compiler mismatch for {value!r}")
        checked["pr_number"] += 1

    secret_clear = secret_resolution_and_clear()
    if secret_clear["returncode"] != 0 or secret_clear["stdout"] != "ok":
        raise RuntimeError(f"pinned secret resolve/clear helper replay failed: {secret_clear}")
    checked["secret_resolve_and_clear"] += 1
    return checked


def _verify_finite_differential() -> tuple[int, dict[str, int]]:
    owner_mirror = _compile(PAT_OWNER)
    corpora = {
        "secret_env_name": sorted(set(_strings("Aa_18.-", 2)) | {
            "AIDEVOPS_SECRET", "8SECRET", "A\n", "_KEY\n", "A\t", "é", "\u00a0",
        }),
        "repository_slug": sorted(set(_strings("a0._-/", 3)) | {
            "owner/repo\n", ".owner/repo", "owner/..", "owner/repo\r",
            "owner/re po", "owner;repo/name", "a//b", "owner/repo\t",
        }),
        "repository_owner": sorted(set(_strings("A0._-", 2)) | {
            "Aowner", "0owner", ".owner", "-owner", "_owner", "owner\n", "é",
        }),
        "check_sha": sorted(set(_strings("a0Fg-", 2)) | {
            "a" * n for n in (39, 40, 41)
        } | {
            "A" * 40, "g" + "a" * 39, "a" * 39 + "\n", "\n" + "a" * 40,
            "a" * 19 + "-" + "a" * 20,
        }),
        "pr_number": sorted(set(_strings("012#-x", 3)) | {
            "1", "17", "482", "2#1", "1\n", "42\r", "00",
        }),
    }
    total = 0
    per_pattern = {}
    for name, (pattern, source_mirror) in PATTERNS.items():
        mirror = owner_mirror if name == "repository_owner" else source_mirror
        count = _differential(pattern, mirror, corpora[name])
        per_pattern[name] = count
        total += count
    return total, per_pattern


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="clean Aidevops checkout at the adopted pin")
    parser.add_argument("--output", type=Path, default=BUNDLE / "gate-report.json")
    args = parser.parse_args(argv)
    if args.source_root:
        requested = Path(args.source_root).expanduser().resolve()
        configured = os.environ.get(SOURCE_ENV)
        if configured and Path(configured).expanduser().resolve() != requested:
            parser.error(f"--source-root conflicts with {SOURCE_ENV}")
        os.environ[SOURCE_ENV] = str(requested)
    try:
        root = source_root()
        _verify_source(root)
        contract_digests = _verify_contracts(root)
        formal_results = _run_harness()
        differential_cases, per_pattern = _verify_finite_differential()
        owner_mirror = _compile(PAT_OWNER)
        integrated_by_helper = _verify_integrated_helpers(owner_mirror)
        integrated_cases = sum(integrated_by_helper.values())
        report = {
            "schema_version": "1",
            "gate_id": "aidevops-webhook-action-protocol",
            "repository": REPOSITORY.removesuffix(".git"),
            "source_pin": PIN,
            "source_file": RECEIVER_FILE,
            "source_sha256": RECEIVER_SHA256,
            "contract_digests": contract_digests,
            "formal_properties": 3,
            "formal_unsat_results": 3,
            "full_slug_inclusion": {
                "result": "not_proven",
                "attempt_record": "slug-inclusion-attempt.json",
                "note": "The 30-second whole-helper inclusion query timed out; finite Bash/product replays do not replace that unbounded proof.",
            },
            "mutation_guards": 4,
            "mutation_replays": 4,
            "differential_cases": differential_cases,
            "differential_cases_by_pattern": per_pattern,
            "integrated_helper_cases": integrated_cases,
            "integrated_helper_cases_by_contract": integrated_by_helper,
            "mismatches": 0,
            "local_gate_passed": True,
            "consumer_adopted": False,
            "confirmed_security_impact": 0,
            "external_reports": 0,
            "maintainer_confirmations": 0,
            "third_party_fixes": 0,
            "product_engine": "Bash [[ =~ ]] on /bin/bash with LC_ALL inherited from source replay; exact pinned receiver helper functions",
            "formal_results": formal_results,
            "scope": "Source-backed local receiver protocol checks only. Aidevops admission is scale-based with security-boundary=false; this gate does not claim a remote vulnerability.",
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(
            f"Aidevops webhook gate passed: 3 UNSAT properties, 4 reproduced mutations, "
            f"{differential_cases} Bash/compiler cases + {integrated_cases} integrated helper cases; "
            "whole-slug inclusion remains not proven."
        )
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
        print(f"Aidevops webhook gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
