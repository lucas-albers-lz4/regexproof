#!/usr/bin/env python3
"""Run one bounded, serial wave from an immutable product roster.

This operator is intentionally limited to adopted UNSAT invariants and SAT
counterexample finders already present in the local harness registry.
Candidate ranking, source acquisition, and contract authoring remain upstream
stages. The frozen cohort, roster, and contract digests are checked before any
proof is run.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.harness import REGISTRY, check_mutation_coverage, run_one  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402
from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    build_product_roster,
    canonical_row_to_checkpoint,
    checkpoint_from_attempts,
)
from regexproof.harness.contract import valid_product_contract  # noqa: E402
from regexproof.contract_adoption import contract_digest  # noqa: E402

STATE_FIELDS = {
    "schema_version", "cohort_manifest_digest", "coverage_digest", "wave_id",
    "corpus", "idiom_bucket", "execution_caps", "contracts", "gate_config",
    "attempts", "conversion_rows", "runs",
}
ATTEMPT_FIELDS = {
    "repo_id", "url", "pin", "site", "question_id", "kind", "synthesized",
    "contract", "domain", "status", "detail", "gate",
}
MAX_SOLVER_TIMEOUT_MS = 30_000
MAX_GATE_TIMEOUT_SECONDS = 600
WAVE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,79}$")
SITE_RE = re.compile(r"^([^@]+)@([0-9a-f]{40}):(.+)$")


class WaveError(ValueError):
    """Raised when a wave input or its resumable state is invalid."""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _json(path: Path) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise WaveError(f"{path}: duplicate JSON key {key!r}")
            value[key] = item
        return value

    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    except OSError as exc:
        raise WaveError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise WaveError(f"invalid JSON in {path}: {exc.msg}") from exc


def _dump(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def _identity(row: dict[str, Any]) -> tuple[str, str, str, str, str]:
    return tuple(str(row[field]) for field in ("repo_id", "url", "pin", "site", "question_id"))  # type: ignore[return-value]


def _normalized_contracts(roster: dict[str, Any], cohort: dict[str, Any]) -> list[dict[str, Any]]:
    """Rebuild the frozen roster from exact registry entries, never result rows."""
    emitter = _conversion_emitter()
    contracts = []
    for identity in roster["identities"]:
        question_id = identity["question_id"]
        entry = REGISTRY.get(question_id)
        if not isinstance(entry, dict):
            raise WaveError(f"{question_id}: no local harness registry entry")
        contract = entry.get("contract")
        if not valid_product_contract(contract):
            raise WaveError(f"{question_id}: local registry contract is not adopted")
        kind = entry.get("kind")
        expected_unsat = {"property": True, "counterexample_finder": False}.get(kind)
        if expected_unsat is None or entry.get("expect_unsat") is not expected_unsat:
            raise WaveError(
                f"{question_id}: wave runner admits UNSAT invariants and "
                "SAT counterexample finders with matching expectations"
            )
        if question_id not in emitter.SHAPE:
            raise WaveError(
                f"{question_id}: canonical emitter has no registered shape"
            )
        if not isinstance(entry.get("domain"), str) or not entry["domain"].strip():
            raise WaveError(f"{question_id}: registry property has no declared domain")
        if contract.get("site") != identity["site"]:
            raise WaveError(f"{question_id}: registry contract site differs from frozen roster")
        contracts.append({
            "repo_id": identity["repo_id"],
            "url": identity["url"],
            "pin": identity["pin"],
            "site": identity["site"],
            "question_id": question_id,
            "kind": kind,
            "synthesized": False,
            "domain": entry["domain"],
            "contract": contract,
        })
    expected = build_product_roster(contracts, cohort)
    if expected != roster:
        raise WaveError("frozen roster does not match current adopted harness contracts")
    return contracts


def _load_campaign(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    campaign = _json(path)
    if not isinstance(campaign, dict) or campaign.get("schema_version") != "1":
        raise WaveError("campaign config must be a schema_version '1' object")
    execution = campaign.get("execution")
    if not isinstance(execution, dict):
        raise WaveError("campaign config is missing execution limits")
    if execution.get("max_active_conversion_waves") != 1:
        raise WaveError("campaign must permit exactly one active conversion wave")
    if execution.get("parallel_walk") is not False:
        raise WaveError("campaign parallel_walk must remain false")
    if execution.get("solver_retries") != 0:
        raise WaveError("campaign solver_retries must remain zero")
    for name in ("max_adopted_contracts_per_wave", "max_new_questions_per_run"):
        cap = execution.get(name)
        if isinstance(cap, bool) or not isinstance(cap, int) or not 1 <= cap <= 5:
            raise WaveError(f"campaign {name} must be an integer from 1 through 5")
    timeout_ms = execution.get("solver_timeout_ms")
    if isinstance(timeout_ms, bool) or not isinstance(timeout_ms, int) or not 1 <= timeout_ms <= MAX_SOLVER_TIMEOUT_MS:
        raise WaveError(f"campaign solver_timeout_ms must be in [1, {MAX_SOLVER_TIMEOUT_MS}]")
    gate_timeout = execution.get("local_gate_timeout_seconds")
    if isinstance(gate_timeout, bool) or not isinstance(gate_timeout, int) or not 1 <= gate_timeout <= MAX_GATE_TIMEOUT_SECONDS:
        raise WaveError(f"campaign local_gate_timeout_seconds must be in [1, {MAX_GATE_TIMEOUT_SECONDS}]")
    return campaign, execution


def _apply_contract_overrides(path: Path | None, cohort: dict[str, Any]) -> None:
    """Load source-bound autonomous revisions for historical harness contracts.

    The override may add adoption/source identity to an unchanged human
    contract. It cannot change the existing guarantee, input, trust, or domain.
    The resulting frozen roster still has to match these exact registry entries.
    """
    if path is None:
        return
    value = _json(path)
    if (
        not isinstance(value, dict)
        or set(value) != {"schema_version", "contracts"}
        or value.get("schema_version") != "1"
        or not isinstance(value.get("contracts"), list)
        or not value["contracts"]
    ):
        raise WaveError("contract overrides require schema_version '1' and a non-empty contracts array")
    repos = {
        (row["url"].rstrip("/").removesuffix(".git"), row["pin"]): row["repo_id"]
        for row in cohort["repos"]
    }
    seen: set[str] = set()
    for index, item in enumerate(value["contracts"]):
        if not isinstance(item, dict) or set(item) != {"question_id", "contract"}:
            raise WaveError(f"contract override {index} requires question_id and contract")
        question_id = item["question_id"]
        contract = item["contract"]
        if not isinstance(question_id, str) or question_id in seen:
            raise WaveError(f"contract override {index} has an invalid or duplicate question_id")
        seen.add(question_id)
        entry = REGISTRY.get(question_id)
        if not isinstance(entry, dict) or entry.get("kind") != "property":
            raise WaveError(f"{question_id}: contract overrides apply only to registered properties")
        original = entry.get("contract")
        if not isinstance(original, dict) or original.get("provenance") != "human":
            raise WaveError(f"{question_id}: override must revise a historical human contract")
        if not valid_product_contract(contract) or contract.get("provenance") != "agent_derived":
            raise WaveError(f"{question_id}: override is not an adopted autonomous contract")
        for field in ("schema_version", "guarantee", "input_source", "trust", "declared_domain"):
            if contract.get(field) != original.get(field):
                raise WaveError(f"{question_id}: override changed historical contract field {field}")
        adoption = contract["adoption"]
        source_identity = (
            adoption.get("source_url", "").rstrip("/").removesuffix(".git"),
            adoption.get("source_pin"),
        )
        repo_id = repos.get(source_identity)
        site = contract.get("site", "")
        site_prefix = f"{repo_id}@{source_identity[1]}:" if repo_id else None
        if not site_prefix or not isinstance(site, str) or not site.startswith(site_prefix):
            raise WaveError(f"{question_id}: override source identity is outside the frozen cohort")
        site_parts = site[len(site_prefix):].rsplit(":", 2)
        if len(site_parts) != 3 or adoption.get("source_file") != site_parts[0]:
            raise WaveError(f"{question_id}: adoption source_file differs from the source-bound site")
        old_without_revision = {
            key: value for key, value in original.items()
            if key not in {"site", "provenance", "adoption"}
        }
        new_without_revision = {
            key: value for key, value in contract.items()
            if key not in {"site", "provenance", "adoption"}
        }
        if old_without_revision != new_without_revision:
            raise WaveError(f"{question_id}: override changed fields beyond source identity/adoption")
        entry["contract"] = contract


def _execution_caps(execution: dict[str, Any]) -> dict[str, Any]:
    return {
        name: execution[name]
        for name in (
            "max_active_conversion_waves", "max_adopted_contracts_per_wave",
            "max_new_questions_per_run", "parallel_walk", "solver_timeout_ms",
            "solver_retries", "local_gate_timeout_seconds",
        )
    }


def _load_gate(path: Path | None, question_ids: set[str], timeout_cap: int) -> dict[str, Any] | None:
    if path is None:
        return None
    value = _json(path)
    required = {
        "schema_version", "gate_id", "question_ids", "command",
        "timeout_seconds", "evidence",
    }
    if not isinstance(value, dict) or set(value) != required or value.get("schema_version") != "1":
        raise WaveError("gate config requires schema_version, gate_id, question_ids, command, timeout_seconds, and evidence")
    if not isinstance(value["gate_id"], str) or not value["gate_id"].strip():
        raise WaveError("gate_id must be a non-empty string")
    covered = value["question_ids"]
    if not isinstance(covered, list) or not covered or any(not isinstance(item, str) for item in covered):
        raise WaveError("gate question_ids must be a non-empty list of strings")
    if len(covered) != len(set(covered)) or not set(covered) <= question_ids:
        raise WaveError("gate question_ids must be unique members of the frozen roster")
    command = value["command"]
    if not isinstance(command, list) or not command or any(not isinstance(item, str) or not item for item in command):
        raise WaveError("gate command must be a non-empty argv list")
    timeout = value["timeout_seconds"]
    if isinstance(timeout, bool) or not isinstance(timeout, int) or not 1 <= timeout <= timeout_cap:
        raise WaveError(f"gate timeout_seconds must be in [1, {timeout_cap}]")
    evidence = value["evidence"]
    evidence_fields = {"product_engine_replay_question_ids", "differential_case_counts"}
    if not isinstance(evidence, dict) or set(evidence) != evidence_fields:
        raise WaveError("gate evidence requires product_engine_replay_question_ids and differential_case_counts")
    replay_ids = evidence["product_engine_replay_question_ids"]
    case_counts = evidence["differential_case_counts"]
    if not isinstance(replay_ids, list) or any(not isinstance(item, str) for item in replay_ids):
        raise WaveError("product_engine_replay_question_ids must be a list of strings")
    if len(replay_ids) != len(set(replay_ids)) or not set(replay_ids) <= set(covered):
        raise WaveError("product-engine replay evidence must be unique and within gate question_ids")
    if not isinstance(case_counts, dict) or not set(case_counts) <= set(covered):
        raise WaveError("differential case evidence keys must be within gate question_ids")
    if any(isinstance(count, bool) or not isinstance(count, int) or count < 0 for count in case_counts.values()):
        raise WaveError("differential case counts must be non-negative integers")
    return value


def _checkout_args(values: list[str], repo_ids: set[str]) -> dict[str, Path]:
    checkouts: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise WaveError("--checkout must be REPO_ID=PATH")
        repo_id, raw_path = value.split("=", 1)
        if not repo_id or not raw_path or repo_id in checkouts:
            raise WaveError(f"invalid or duplicate --checkout value {value!r}")
        checkouts[repo_id] = Path(raw_path).expanduser().resolve()
    if set(checkouts) != repo_ids:
        missing = sorted(repo_ids - set(checkouts))
        extra = sorted(set(checkouts) - repo_ids)
        detail = f"missing checkout for {missing[0]}" if missing else f"unused checkout for {extra[0]}"
        raise WaveError(detail)
    return checkouts


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=not binary,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise WaveError(f"git {' '.join(args)} failed in {root}: {exc}") from exc
    return result.stdout if binary else result.stdout.strip()


def _source_location(item: dict[str, Any]) -> tuple[str, int]:
    match = SITE_RE.fullmatch(item["site"])
    if match is None or match.group(1) != item["repo_id"] or match.group(2) != item["pin"]:
        raise WaveError(f"{item['question_id']}: site must bind repo_id and source pin")
    parts = match.group(3).rsplit(":", 2)
    if len(parts) != 3 or not parts[1].isdigit() or not parts[2]:
        raise WaveError(f"{item['question_id']}: site must end in :line:symbol")
    if int(parts[1]) < 1:
        raise WaveError(f"{item['question_id']}: source line must be positive")
    source_file = parts[0]
    if not source_file or source_file.startswith("/") or ".." in Path(source_file).parts:
        raise WaveError(f"{item['question_id']}: site has an unsafe source path")
    adoption = item["contract"].get("adoption")
    if isinstance(adoption, dict) and adoption.get("source_file") != source_file:
        raise WaveError(f"{item['question_id']}: adoption source_file differs from site")
    return source_file, int(parts[1])


def _line_matches_symbol(source: str, lines: list[str], line_no: int, symbol: str) -> bool:
    """Accept a direct symbol line or a pinned Python definition/use scope.

    Contracts can cite a regex literal inside a named tuple assignment or a
    regex use inside a method body while naming the owning symbol. Requiring
    the symbol on that exact line rejects those valid, source-backed sites.
    """
    if symbol in lines[line_no - 1]:
        return True
    parts = symbol.split(".")
    if len(parts) not in {1, 2} or not all(parts):
        return False
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    if len(parts) == 1:
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            target_names = {
                child.id
                for target in targets
                for child in ast.walk(target)
                if isinstance(child, ast.Name)
            }
            if (
                symbol in target_names
                and node.lineno <= line_no <= (node.end_lineno or node.lineno)
            ):
                return True
        return False
    if len(parts) != 2:
        return False
    class_name, method_name = parts
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or node.name != class_name:
            continue
        for child in node.body:
            if (
                isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                and child.name == method_name
                and child.lineno <= line_no <= (child.end_lineno or child.lineno)
            ):
                return True
    return False


def _line_matches_shell_regex_site(line: str, column: int, pattern: str | None) -> bool:
    """Bind an extractor's numeric Bash column to its literal `[[ =~ ]]` site.

    `shell_posix` stores the start of the `[[` test for the common single
    comparison and the `=~` operator for multiple comparisons. A numeric
    selector is a zero-based line column, not a symbol name; accepting any
    matching digit on the line would let unrelated source text satisfy it.
    """
    if not pattern or column < 0 or column >= len(line):
        return False
    selected = line[column:]
    if not (selected.startswith("[[") or selected.startswith("=~")):
        return False
    operator = selected.find("=~")
    return operator >= 0 and pattern in selected[operator + 2:]


def _verify_checkouts(contracts: list[dict[str, Any]], checkouts: dict[str, Path]) -> dict[str, str | None]:
    """Verify exact clean checkouts and source bytes for every frozen site."""
    failures: dict[str, str | None] = {}
    repos = {item["repo_id"]: item for item in contracts}
    for repo_id, repo in repos.items():
        root = checkouts[repo_id]
        try:
            if not root.is_dir():
                raise WaveError(f"checkout does not exist: {root}")
            top_level = Path(str(_git(root, "rev-parse", "--show-toplevel"))).resolve()
            if top_level != root:
                raise WaveError(f"checkout path must be the repository root: {top_level}")
            pin = str(_git(root, "rev-parse", "HEAD"))
            if pin != repo["pin"]:
                raise WaveError(f"checkout HEAD {pin} does not match frozen pin {repo['pin']}")
            remote = str(_git(root, "remote", "get-url", "origin")).removesuffix(".git").rstrip("/")
            expected_url = repo["url"].removesuffix(".git").rstrip("/")
            if remote != expected_url:
                raise WaveError(f"origin {remote!r} does not match frozen repository {expected_url!r}")
            dirty = str(_git(root, "status", "--porcelain", "--untracked-files=all"))
            if dirty:
                raise WaveError("source checkout is not clean")
            for item in (row for row in contracts if row["repo_id"] == repo_id):
                source_file, line_no = _source_location(item)
                source_path = root / source_file
                if source_path.is_symlink():
                    raise WaveError(f"{item['question_id']}: source file is a symlink")
                resolved = source_path.resolve(strict=True)
                resolved.relative_to(root)
                if not resolved.is_file():
                    raise WaveError(f"{item['question_id']}: source file is not regular")
                if resolved.stat().st_size > 2 * 1024 * 1024:
                    raise WaveError(f"{item['question_id']}: source file exceeds the 2 MiB review limit")
                working = resolved.read_bytes()
                committed_size = str(_git(root, "cat-file", "-s", f"{repo['pin']}:{source_file}"))
                if not committed_size.isdigit() or int(committed_size) > 2 * 1024 * 1024:
                    raise WaveError(f"{item['question_id']}: pinned source file exceeds the 2 MiB review limit")
                committed = _git(root, "show", f"{repo['pin']}:{source_file}", binary=True)
                if working != committed:
                    raise WaveError(f"{item['question_id']}: working source bytes differ from pinned commit")
                source_text = working.decode("utf-8", errors="replace")
                lines = source_text.splitlines()
                selector = item["site"].rsplit(":", 1)[-1]
                column_match = re.fullmatch(r"column-(\d+)", selector)
                if column_match:
                    column = int(column_match.group(1))
                    location_matches = (
                        line_no <= len(lines)
                        and column < len(lines[line_no - 1])
                        and lines[line_no - 1][column] == "/"
                    )
                elif selector.isdigit():
                    if source_path.suffix.lower() not in {".sh", ".bash", ".ksh"}:
                        location_matches = False
                    else:
                        registered = REGISTRY.get(item["question_id"], {})
                        pattern = registered.get("pattern") if isinstance(registered, dict) else None
                        location_matches = (
                            line_no <= len(lines)
                            and _line_matches_shell_regex_site(
                                lines[line_no - 1], int(selector), pattern
                            )
                        )
                else:
                    symbol = selector.split(".")[-1]
                    location_matches = line_no <= len(lines) and _line_matches_symbol(
                        source_text, lines, line_no,
                        selector if "." in selector else symbol,
                    )
                if not location_matches:
                    raise WaveError(
                        f"{item['question_id']}: pinned source line does not match selector {selector!r}"
                    )
                adoption = item["contract"].get("adoption")
                if isinstance(adoption, dict):
                    digest = hashlib.sha256(working).hexdigest()
                    if digest != adoption.get("source_sha256"):
                        raise WaveError(f"{item['question_id']}: adopted source digest does not match pinned bytes")
                    if adoption.get("source_pin") != repo["pin"] or adoption.get("source_url", "").rstrip("/") != repo["url"].rstrip("/"):
                        raise WaveError(f"{item['question_id']}: adoption source identity differs from cohort")
            failures[repo_id] = None
        except (OSError, ValueError, WaveError, subprocess.SubprocessError) as exc:
            failures[repo_id] = str(exc)
    return failures


@contextmanager
def _wave_lock(path: Path):
    try:
        import fcntl
    except ImportError as exc:
        raise WaveError("proof-wave execution requires a platform with POSIX flock") from exc
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise WaveError(f"lock file must not be a symlink: {path}")
    flags = os.O_CREAT | os.O_RDWR
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(path, flags, 0o600)
    try:
        os.fchmod(fd, 0o600)
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        os.close(fd)
        raise WaveError("another autonomous proof wave is active") from exc
    except Exception:
        os.close(fd)
        raise
    try:
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def _new_gate(source_ok: bool, mutation_ok: bool, local_command: str | None, gate_id: str | None) -> dict[str, Any]:
    return {
        "source_pin_verified": source_ok,
        "product_engine_replayed": False,
        "mutation_guard_passed": mutation_ok,
        "differential_cases": 0,
        "gate_id": gate_id,
        "local_gate_command": local_command,
        "local_gate_passed": False,
        "consumer_adopted": False,
    }


def _initial_attempt(item: dict[str, Any]) -> dict[str, Any]:
    return {
        **{field: item[field] for field in ("repo_id", "url", "pin", "site", "question_id", "kind", "synthesized", "contract", "domain")},
        "status": "not_attempted",
        "detail": "not yet attempted",
        "gate": _new_gate(False, False, None, None),
    }


def _validate_state(state: Any, *, cohort: dict[str, Any], roster: dict[str, Any], contracts: list[dict[str, Any]], gate_config: dict[str, Any] | None, wave_id: str, corpus: str, idiom_bucket: str, execution_caps: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(state, dict) or set(state) != STATE_FIELDS or state.get("schema_version") != "1":
        raise WaveError("state.json has an unsupported or incomplete schema")
    if state["cohort_manifest_digest"] != cohort["manifest_digest"]:
        raise WaveError("state cohort digest differs from supplied frozen cohort")
    if state["coverage_digest"] != roster["coverage_digest"]:
        raise WaveError("state roster digest differs from supplied frozen roster")
    if state["wave_id"] != wave_id:
        raise WaveError("state wave_id differs; resume with the original wave_id")
    if state["corpus"] != corpus or state["idiom_bucket"] != idiom_bucket:
        raise WaveError("corpus or idiom bucket differs from the immutable wave snapshot")
    if state["execution_caps"] != execution_caps:
        raise WaveError("campaign execution limits differ from the immutable wave snapshot")
    if state["contracts"] != contracts:
        raise WaveError("registry contracts differ from the state snapshot")
    if state["gate_config"] != gate_config:
        raise WaveError("gate configuration differs from the immutable wave snapshot")
    if not isinstance(state["attempts"], list) or not isinstance(state["conversion_rows"], list) or not isinstance(state["runs"], list):
        raise WaveError("state attempts, conversion_rows, and runs must be lists")
    if any(not isinstance(item, dict) for item in state["conversion_rows"] + state["runs"]):
        raise WaveError("state conversion rows and run records must be objects")
    if len(state["attempts"]) != len(contracts):
        raise WaveError("state attempt count differs from frozen roster")
    expected = [_identity(item) for item in contracts]
    actual = [_identity(item) for item in state["attempts"] if isinstance(item, dict)]
    if actual != expected or any(not isinstance(item, dict) or set(item) != ATTEMPT_FIELDS for item in state["attempts"]):
        raise WaveError("state attempts do not exactly match frozen roster order/schema")
    return state


def _checkpoint(state: dict[str, Any], cohort: dict[str, Any], roster: dict[str, Any]) -> dict[str, Any]:
    attempt_by_id = {_identity(item): item for item in state["attempts"]}
    checkpoint_rows = []
    seen: set[tuple[str, str, str, str, str]] = set()
    for raw in state["conversion_rows"]:
        qid = raw.get("question_id") or raw.get("name")
        matches = [identity for identity in attempt_by_id if identity[3:] == (raw.get("site"), qid)]
        if len(matches) != 1:
            raise WaveError(f"conversion row has no unique frozen identity: {raw.get('name')!r}")
        identity = matches[0]
        if identity in seen:
            raise WaveError(f"duplicate conversion row for {identity!r}")
        seen.add(identity)
        attempt = attempt_by_id[identity]
        if raw.get("contract") != attempt["contract"] or raw.get("domain") != attempt["domain"]:
            raise WaveError(f"conversion row contract/domain differs from attempt {identity!r}")
        if raw.get("kind") != attempt["kind"] or raw.get("synthesized") is not False:
            raise WaveError(f"conversion row kind/synthesis differs from attempt {identity!r}")
        result = raw.get("result")
        if result not in {"sat", "unsat", "gap"}:
            raise WaveError(f"conversion row result is not decided for {identity!r}")
        status = raw.get("ground_truth_status")
        if status == "reproduced":
            disposition = {
                "status": "pending_product_triage", "filed_at": None, "resolved_at": None,
                "approval_escape": None, "approval_ref": None,
                "reason_code": "reachability_and_security_impact_unresolved",
                "backfilled": False, "disposition_date": None,
            }
        elif result in {"sat", "gap"}:
            disposition = {
                "status": "pending_ground_truth", "filed_at": None, "resolved_at": None,
                "approval_escape": None, "approval_ref": None,
                "reason_code": "product_replay_incomplete",
                "backfilled": False, "disposition_date": None,
            }
        else:
            disposition = {
                "status": "not_applicable", "filed_at": None, "resolved_at": None,
                "approval_escape": None, "approval_ref": None,
                "reason_code": "unsat_guarantee",
                "backfilled": False, "disposition_date": None,
            }
        checkpoint_rows.append(canonical_row_to_checkpoint(
            raw,
            repo_id=identity[0], url=identity[1], pin=identity[2],
            disposition=disposition,
        ))
    return checkpoint_from_attempts(
        state["attempts"], checkpoint_rows, cohort=cohort,
        product_coverage_manifest=roster,
    )


def _persist(state: dict[str, Any], state_dir: Path, cohort: dict[str, Any], roster: dict[str, Any]) -> None:
    checkpoint = _checkpoint(state, cohort, roster)
    atomic_write_text(state_dir / "state.json", _dump(state))
    atomic_write_text(state_dir / "attempts.json", _dump(state["attempts"]))
    conversion = "".join(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n" for row in state["conversion_rows"])
    atomic_write_text(state_dir / "conversion.ndjson", conversion)
    atomic_write_text(state_dir / "checkpoint.json", _dump(checkpoint))


def _mutation_guards(families: set[str], timeout_ms: int) -> tuple[dict[str, bool], list[str]]:
    from regexproof.kinds import PropertyKind

    guards_by_family: dict[str, list[tuple[str, dict[str, Any]]]] = {family: [] for family in families}
    for name, entry in REGISTRY.items():
        if entry.get("family") in families and entry.get("kind") == PropertyKind.MUTATION_GUARD.value:
            guards_by_family[entry["family"]].append((name, entry))
    outcome: dict[str, bool] = {}
    failures: list[str] = []
    for family, guards in guards_by_family.items():
        passed = bool(guards)
        for name, entry in sorted(guards):
            bounded = dict(entry)
            bounded["timeout_ms"] = min(int(entry.get("timeout_ms", timeout_ms)), timeout_ms)
            try:
                result = run_one(name, bounded, require_ground_truth=True)
            except Exception as exc:  # a broken replay/solver callback fails closed
                passed = False
                failures.append(f"{name}: {type(exc).__name__}: {exc}")
                continue
            if result.get("result") != "sat" or result.get("ok") is not True:
                passed = False
                failures.append(f"{name}: mutation guard result={result.get('result')!r}")
        if not guards:
            failures.append(f"{family}: no registered mutation guard")
        outcome[family] = passed
    if check_mutation_coverage() != 0:
        failures.append("registry-wide mutation coverage check failed")
    return outcome, failures


def _run_local_gate(gate_config: dict[str, Any] | None, source_ok: bool, mutation_ok: dict[str, bool]) -> tuple[bool, float, str | None]:
    if gate_config is None:
        return False, 0.0, None
    if not source_ok:
        return False, 0.0, "source pin verification failed"
    if not all(mutation_ok.values()):
        return False, 0.0, "mutation guard failed"
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            gate_config["command"], cwd=ROOT, capture_output=True, text=True,
            timeout=gate_config["timeout_seconds"], check=False,
        )
    except subprocess.TimeoutExpired:
        elapsed = round((time.perf_counter() - started) * 1000, 1)
        return False, elapsed, f"local gate timed out after {gate_config['timeout_seconds']}s"
    except OSError as exc:
        elapsed = round((time.perf_counter() - started) * 1000, 1)
        return False, elapsed, f"cannot start local gate: {exc}"
    elapsed = round((time.perf_counter() - started) * 1000, 1)
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()[-2000:]
        return False, elapsed, f"local gate exited {completed.returncode}: {detail}"
    return True, elapsed, None


def _run_property(item: dict[str, Any], timeout_ms: int) -> tuple[dict[str, Any] | None, str, str | None, bool]:
    name = item["question_id"]
    entry = dict(REGISTRY[name])
    entry["timeout_ms"] = min(int(entry.get("timeout_ms", timeout_ms)), timeout_ms)
    callback_error: list[str] = []
    callback = entry.get("ground_truth")
    if callable(callback):
        def replay(witness):
            try:
                return bool(callback(witness))
            except Exception as exc:
                callback_error.append(f"{type(exc).__name__}: {exc}")
                return False
        entry["ground_truth"] = replay
    try:
        result = run_one(name, entry, require_ground_truth=True)
    except Exception as exc:
        return None, "error", f"{type(exc).__name__}: {exc}", False
    verdict = result.get("result")
    if verdict == "unsat":
        if result.get("ok") is True:
            return result, "unsat", None, False
        return result, "error", "UNSAT result did not satisfy the registered invariant", False
    if verdict == "sat":
        gt = result.get("ground_truth")
        if gt == "reproduced":
            return result, "sat", None, True
        if gt == "failed":
            detail = callback_error[-1] if callback_error else "real implementation did not reproduce witness"
            return result, "sat_replay_failed", detail, False
        return result, "sat_pending_ground_truth", "SAT witness has no successful product replay", False
    if verdict == "timeout":
        return result, "timeout", f"solver did not decide within {entry['timeout_ms']}ms", False
    if verdict == "unknown":
        return result, "unknown", "solver returned unknown", False
    return result, "error", f"unexpected harness result {verdict!r}", False


def _row_for_result(item: dict[str, Any], result: dict[str, Any], status: str, corpus: str, wave_id: str, idiom_bucket: str) -> dict[str, Any]:
    # Use the repository's canonical emitter so proof rows keep the same
    # engine, family, site, and contract facts as normal conversion output.
    module = _conversion_emitter()
    if item["question_id"] not in module.SHAPE:
        raise WaveError(f"{item['question_id']}: canonical emitter has no registered shape")
    row = module.row_from_run(
        item["question_id"], REGISTRY[item["question_id"]], result, corpus,
        wave_id=wave_id, idiom_bucket=idiom_bucket,
    )
    if status == "sat_pending_ground_truth":
        row["ground_truth_status"] = "not_run"
    elif status == "sat_replay_failed":
        row["ground_truth_status"] = "failed"
    elif status == "sat":
        row["ground_truth_status"] = "reproduced"
    return row


def _conversion_emitter():
    """Load the canonical emitter used by both preflight and result writes."""
    import importlib.util

    emitter_path = ROOT / "scripts" / "emit-conversion-ndjson.py"
    spec = importlib.util.spec_from_file_location("regexproof_conversion_emitter", emitter_path)
    if spec is None or spec.loader is None:
        raise WaveError("cannot load canonical conversion emitter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _recover_result_from_gate_report(
    *,
    args: argparse.Namespace,
    cohort: dict[str, Any],
    roster: dict[str, Any],
    contracts: list[dict[str, Any]],
    gate_config: dict[str, Any] | None,
    execution_caps: dict[str, Any],
    checkouts: dict[str, Path],
) -> int:
    """Complete a persisted in-flight attempt from its same-run gate artifact.

    This is for the narrow failure where the solver and real-engine gate
    finished but the runner crashed before serializing its result row. It does
    not rerun the solver. The immutable local gate report must contain the
    exact adopted identity, SAT witness, successful ground-truth callback, and
    pinned product replay.
    """
    if gate_config is None:
        raise WaveError("--recover-result requires the wave's local gate config")
    if not args.corpus or not args.idiom_bucket:
        raise WaveError("result recovery requires the original corpus and idiom bucket")
    state_dir = args.state_dir.resolve()
    if not state_dir.is_dir():
        raise WaveError("--recover-result requires an existing wave state directory")
    for name, expected in (("cohort.json", cohort), ("roster.json", roster)):
        stored = state_dir / name
        if not stored.is_file() or _json(stored) != expected:
            raise WaveError(f"state snapshot {name} differs from supplied immutable input")
    state_path = state_dir / "state.json"
    state = _validate_state(
        _json(state_path), cohort=cohort, roster=roster, contracts=contracts,
        gate_config=gate_config, wave_id=args.wave_id,
        corpus=args.corpus, idiom_bucket=args.idiom_bucket,
        execution_caps=execution_caps,
    )
    failures = _verify_checkouts(contracts, checkouts)
    if any(failures.values()):
        raise WaveError("result recovery requires every exact source checkout to verify")

    running = [run for run in state["runs"] if run.get("status") == "running"]
    if len(running) != 1 or not running[0].get("active_question_id"):
        raise WaveError("state must have exactly one persisted in-flight question")
    run = running[0]
    question_id = run["active_question_id"]
    attempts = [item for item in state["attempts"] if item["question_id"] == question_id]
    if len(attempts) != 1:
        raise WaveError("in-flight question is not unique in the frozen roster")
    attempt = attempts[0]
    if attempt["status"] != "error" or attempt["detail"] != "attempt started; terminal result not yet recorded":
        raise WaveError("only an attempt interrupted before result serialization can be recovered")
    if question_id not in gate_config["question_ids"]:
        raise WaveError("same-run gate report does not cover the in-flight question")
    command = gate_config["command"]
    output_positions = [index for index, value in enumerate(command[:-1]) if value == "--output"]
    if len(output_positions) != 1:
        raise WaveError("recovery requires one explicit --output path in the frozen gate command")
    expected_report = (ROOT / command[output_positions[0] + 1]).resolve()
    if expected_report != args.recover_result.resolve():
        raise WaveError("recovery artifact path differs from the frozen gate command output")
    if any(
        row.get("question_id") == question_id or row.get("name") == question_id
        for row in state["conversion_rows"]
    ):
        raise WaveError("in-flight question already has a persisted conversion row")

    report = _json(args.recover_result)
    if not isinstance(report, dict) or report.get("status") != "reproduced":
        raise WaveError("recovery artifact must be a reproduced local gate report")
    if report.get("gate_id") != gate_config["gate_id"]:
        raise WaveError("recovery artifact gate_id differs from frozen gate config")
    contract = attempt["contract"]
    adoption = contract.get("adoption", {})
    if (
        report.get("question_id") != question_id
        or report.get("cohort", {}).get("cohort_id") != cohort["cohort_id"]
        or report.get("cohort", {}).get("manifest_digest") != cohort["manifest_digest"]
        or report.get("cohort", {}).get("roster_sha256") != hashlib.sha256(args.roster.read_bytes()).hexdigest()
        or report.get("cohort", {}).get("contract_sha256") != contract_digest(contract)
        or report.get("source", {}).get("pin") != attempt["pin"]
        or report.get("source", {}).get("repository_url", "").rstrip("/") != attempt["url"].rstrip("/")
        or report.get("source", {}).get("file") != adoption.get("source_file")
        or report.get("source", {}).get("sha256") != adoption.get("source_sha256")
    ):
        raise WaveError("recovery artifact is not bound to this frozen question and source")
    matches = [
        row for row in report.get("result_rows", [])
        if isinstance(row, dict) and row.get("name") == question_id
    ]
    if len(matches) != 1:
        raise WaveError("recovery artifact must contain exactly one proof row for the question")
    result = matches[0]
    if (
        result.get("kind") != attempt["kind"]
        or result.get("result") != "sat"
        or result.get("ground_truth") != "reproduced"
        or result.get("product") is not True
        or result.get("not_proven") is not False
        or result.get("ok") is not True
        or not isinstance(result.get("witness"), dict)
    ):
        raise WaveError("recovery proof row is not a successful ground-truthed SAT result")
    entry = REGISTRY.get(question_id, {})
    callback = entry.get("ground_truth")
    previous_replay_source = os.environ.get("MALCONTENT_REPLAY_SOURCE")
    os.environ["MALCONTENT_REPLAY_SOURCE"] = str(checkouts[attempt["repo_id"]])
    try:
        reproduced = callable(callback) and bool(callback(result["witness"]))
    finally:
        if previous_replay_source is None:
            os.environ.pop("MALCONTENT_REPLAY_SOURCE", None)
        else:
            os.environ["MALCONTENT_REPLAY_SOURCE"] = previous_replay_source
    if not reproduced:
        raise WaveError("current real-engine callback no longer reproduces the saved witness")
    if report.get("product_replay", {}).get("source_pin") != attempt["pin"]:
        raise WaveError("recovery artifact has no matching pinned product replay")

    conversion_row = _row_for_result(
        attempt, result, "sat", args.corpus, args.wave_id, args.idiom_bucket
    )
    attempt["status"] = "sat"
    attempt["detail"] = (
        "SAT and real-engine replay recovered from the same-run local gate report "
        "after canonical-row serialization failed; solver was not retried"
    )
    state["conversion_rows"].append(conversion_row)
    run["status"] = "recovered"
    run["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    run["active_question_id"] = None
    run["solver_wall_ms"] = None
    run["reason"] = (
        "recovered the gate-bound SAT result without retrying the solver; exact "
        "runner solver timing was lost before row serialization"
    )
    run["recovery"] = {
        "artifact": args.recover_result.resolve().relative_to(ROOT).as_posix(),
        "artifact_sha256": hashlib.sha256(args.recover_result.read_bytes()).hexdigest(),
        "question_id": question_id,
        "solver_retried": False,
        "solver_timing": "unknown_after_serialization_error",
    }
    _persist(state, state_dir, cohort, roster)
    print(f"recovered {question_id} from same-run gate evidence without retrying the solver")
    return 0


def _initial_state(cohort: dict[str, Any], roster: dict[str, Any], contracts: list[dict[str, Any]], gate_config: dict[str, Any] | None, wave_id: str, corpus: str, idiom_bucket: str, execution_caps: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1",
        "cohort_manifest_digest": cohort["manifest_digest"],
        "coverage_digest": roster["coverage_digest"],
        "wave_id": wave_id,
        "corpus": corpus,
        "idiom_bucket": idiom_bucket,
        "execution_caps": execution_caps,
        "contracts": contracts,
        "gate_config": gate_config,
        "attempts": [_initial_attempt(item) for item in contracts],
        "conversion_rows": [],
        "runs": [],
    }


def _run_wave(args: argparse.Namespace) -> int:
    if args.status and args.dry_run:
        raise WaveError("--status and --dry-run are mutually exclusive")
    if args.recover_result is not None and (args.status or args.dry_run):
        raise WaveError("--recover-result cannot be combined with --status or --dry-run")
    cohort = validate_manifest(_json(args.cohort))
    _apply_contract_overrides(args.contract_overrides, cohort)
    roster = _json(args.roster)
    if not isinstance(roster, dict):
        raise WaveError("frozen roster must be a JSON object")
    contracts = _normalized_contracts(roster, cohort)
    if not contracts:
        raise WaveError("frozen roster has no product identities")
    _, execution = _load_campaign(args.campaign)
    execution_caps = _execution_caps(execution)
    if len(contracts) > execution["max_adopted_contracts_per_wave"]:
        raise WaveError("frozen roster exceeds max_adopted_contracts_per_wave")
    max_new = (
        execution["max_new_questions_per_run"]
        if args.max_new_questions is None else args.max_new_questions
    )
    if isinstance(max_new, bool) or not 1 <= max_new <= execution["max_new_questions_per_run"]:
        raise WaveError("--max-new-questions must be within the campaign run cap")
    if not WAVE_ID_RE.fullmatch(args.wave_id):
        raise WaveError("wave_id must be 1-80 safe letters, digits, dot, underscore, or hyphen")
    gate_config = _load_gate(
        args.gate, {item["question_id"] for item in contracts},
        execution["local_gate_timeout_seconds"],
    )
    repo_ids = {item["repo_id"] for item in contracts}
    state_dir = args.state_dir.resolve()

    if args.status:
        state_path = state_dir / "state.json"
        if not state_path.is_file():
            raise WaveError("--status requires an existing state.json")
        for name, expected in (("cohort.json", cohort), ("roster.json", roster)):
            stored = state_dir / name
            if not stored.is_file() or _json(stored) != expected:
                raise WaveError(f"state snapshot {name} differs from supplied immutable input")
        state = _validate_state(
            _json(state_path), cohort=cohort, roster=roster, contracts=contracts,
            gate_config=gate_config, wave_id=args.wave_id,
            corpus=args.corpus or _json(state_path).get("corpus"),
            idiom_bucket=args.idiom_bucket or _json(state_path).get("idiom_bucket"),
            execution_caps=execution_caps,
        )
        _checkpoint(state, cohort, roster)
        counts: dict[str, int] = {}
        for attempt in state["attempts"]:
            counts[attempt["status"]] = counts.get(attempt["status"], 0) + 1
        remaining = [attempt["question_id"] for attempt in state["attempts"] if attempt["status"] == "not_attempted"]
        totals = {
            "runs": len(state["runs"]),
            "source_wall_ms": round(sum(float(run.get("source_wall_ms", 0)) for run in state["runs"]), 1),
            "mutation_wall_ms": round(sum(float(run.get("mutation_wall_ms", 0)) for run in state["runs"]), 1),
            "solver_wall_ms": round(sum(float(run.get("solver_wall_ms", 0) or 0) for run in state["runs"]), 1),
            "solver_wall_ms_unknown_runs": sum(
                1 for run in state["runs"] if run.get("solver_wall_ms") is None
            ),
            "gate_wall_ms": round(sum(float(run.get("gate_wall_ms", 0)) for run in state["runs"]), 1),
        }
        print(f"wave {args.wave_id}: {counts}; resources={totals}")
        interrupted = any(run.get("status") == "running" for run in state["runs"])
        next_action = (
            "resume to record interruption (solver will not be retried)"
            if interrupted else remaining[0] if remaining else "inspect terminal outcomes / close-out"
        )
        print(f"next={next_action}")
        return 0

    checkouts = _checkout_args(args.checkout, repo_ids)
    if args.recover_result is not None:
        with _wave_lock(args.lock_file.resolve()):
            return _recover_result_from_gate_report(
                args=args, cohort=cohort, roster=roster, contracts=contracts,
                gate_config=gate_config, execution_caps=execution_caps,
                checkouts=checkouts,
            )
    if args.dry_run:
        source_failures = _verify_checkouts(contracts, checkouts)
        print(f"dry-run {args.wave_id}: roster={len(contracts)} max_new={max_new} solver_timeout_ms={execution['solver_timeout_ms']}")
        for repo_id, failure in sorted(source_failures.items()):
            print(f"source {repo_id}: {'verified' if failure is None else 'NOT VERIFIED: ' + failure}")
        if gate_config:
            print(f"gate {gate_config['gate_id']}: covers {len(gate_config['question_ids'])} question(s)")
        print("dry-run does not execute the gate, mutation guards, or properties and writes no state")
        return 0 if all(failure is None for failure in source_failures.values()) else 1

    if not args.corpus or not args.corpus.strip() or not args.idiom_bucket or not args.idiom_bucket.strip():
        raise WaveError("corpus and idiom bucket must be non-empty for execution")
    state_dir.mkdir(parents=True, exist_ok=True)

    with _wave_lock(args.lock_file.resolve()):
        # Frozen inputs are immutable snapshots. Replacing any one requires a
        # new state directory and wave id.
        for name, value in (("cohort.json", cohort), ("roster.json", roster)):
            path = state_dir / name
            if path.exists() and _json(path) != value:
                raise WaveError(f"{path} differs from the immutable wave input")
            if not path.exists():
                atomic_write_text(path, _dump(value))

        state_path = state_dir / "state.json"
        if state_path.exists():
            state = _validate_state(
                _json(state_path), cohort=cohort, roster=roster,
                contracts=contracts, gate_config=gate_config, wave_id=args.wave_id,
                corpus=args.corpus, idiom_bucket=args.idiom_bucket,
                execution_caps=execution_caps,
            )
            # Repair derivative artifacts after an interruption between atomic
            # writes; state.json is the single authoritative resume record.
            _persist(state, state_dir, cohort, roster)
        else:
            for name in ("attempts.json", "conversion.ndjson", "checkpoint.json"):
                if (state_dir / name).exists():
                    raise WaveError(f"{name} exists without state.json; refusing ambiguous resume")
            state = _initial_state(
                cohort, roster, contracts, gate_config, args.wave_id,
                args.corpus, args.idiom_bucket, execution_caps,
            )
            _persist(state, state_dir, cohort, roster)

        # An attempt is marked before solver entry. If the process dies during
        # the call, the identity remains terminal and solver_retries=0 prevents
        # a duplicate execution on resume.
        for run in state["runs"]:
            if run.get("status") == "running":
                run["status"] = "interrupted"
                run["finished_at"] = _now()
                run["reason"] = "process stopped before the run record closed"
                active = run.get("active_question_id")
                if active:
                    for attempt in state["attempts"]:
                        if attempt["question_id"] == active and attempt["status"] == "error":
                            attempt["detail"] = "interrupted during solve; configured solver retries are zero"
                run["active_question_id"] = None

        source_started = time.perf_counter()
        source_failures = _verify_checkouts(contracts, checkouts)
        source_ms = round((time.perf_counter() - source_started) * 1000, 1)
        all_sources_ok = all(value is None for value in source_failures.values())
        family_for_question = {item["question_id"]: REGISTRY[item["question_id"]]["family"] for item in contracts}
        mutation_started = time.perf_counter()
        mutation_ok, mutation_failures = _mutation_guards(set(family_for_question.values()), execution["solver_timeout_ms"])
        mutation_ms = round((time.perf_counter() - mutation_started) * 1000, 1)
        local_passed, gate_ms, gate_failure = _run_local_gate(gate_config, all_sources_ok, mutation_ok)
        gate_command = shlex.join(gate_config["command"]) if gate_config else None
        gate_id = gate_config["gate_id"] if gate_config else None
        covered = set(gate_config["question_ids"]) if gate_config else set()
        for item, attempt in zip(contracts, state["attempts"], strict=True):
            source_ok = source_failures[item["repo_id"]] is None
            family_ok = mutation_ok.get(family_for_question[item["question_id"]], False)
            attempt["gate"] = _new_gate(
                source_ok, family_ok,
                gate_command if item["question_id"] in covered else None,
                gate_id if item["question_id"] in covered else None,
            )
            if item["question_id"] in covered:
                attempt["gate"]["local_gate_passed"] = bool(local_passed and source_ok and family_ok)
                if attempt["gate"]["local_gate_passed"]:
                    evidence = gate_config["evidence"]
                    if item["question_id"] in evidence["product_engine_replay_question_ids"]:
                        attempt["gate"]["product_engine_replayed"] = True
                    attempt["gate"]["differential_cases"] = evidence["differential_case_counts"].get(item["question_id"], 0)
            if not source_ok and attempt["status"] == "not_attempted":
                attempt["detail"] = f"source checkout not verified: {source_failures[item['repo_id']]}"
        run = {
            "run_id": str(uuid.uuid4()), "started_at": _now(), "finished_at": None,
            "status": "running", "new_questions": 0, "question_ids": [],
            "source_wall_ms": source_ms, "mutation_wall_ms": mutation_ms,
            "solver_wall_ms": 0.0, "gate_wall_ms": gate_ms,
            "gate_passed": local_passed, "gate_failure": gate_failure,
            "source_failures": {key: value for key, value in source_failures.items() if value},
            "mutation_failures": mutation_failures,
            "active_question_id": None, "reason": None,
        }
        state["runs"].append(run)
        _persist(state, state_dir, cohort, roster)

        attempted = 0
        for item, attempt in zip(contracts, state["attempts"], strict=True):
            if attempt["status"] != "not_attempted" or attempted >= max_new:
                continue
            if source_failures[item["repo_id"]] is not None:
                continue
            attempted += 1
            run["new_questions"] = attempted
            run["question_ids"].append(item["question_id"])
            run["active_question_id"] = item["question_id"]
            attempt["status"] = "error"
            attempt["detail"] = "attempt started; terminal result not yet recorded"
            _persist(state, state_dir, cohort, roster)

            started = time.perf_counter()
            result, status, detail, replayed = _run_property(item, execution["solver_timeout_ms"])
            wall_ms = round((time.perf_counter() - started) * 1000, 1)
            attempt["status"] = status
            attempt["detail"] = detail
            attempt["gate"]["product_engine_replayed"] = (
                attempt["gate"]["product_engine_replayed"] or replayed
            )
            if result is not None:
                run["solver_wall_ms"] += float(result.get("wall_ms") or wall_ms)
                if status in {"unsat", "sat", "sat_pending_ground_truth", "sat_replay_failed"}:
                    row = _row_for_result(item, result, status, args.corpus, args.wave_id, args.idiom_bucket)
                    state["conversion_rows"].append(row)
            else:
                run["solver_wall_ms"] += wall_ms
            run["active_question_id"] = None
            _persist(state, state_dir, cohort, roster)

        for item, attempt in zip(contracts, state["attempts"], strict=True):
            if attempt["status"] == "not_attempted" and source_failures[item["repo_id"]] is None:
                attempt["detail"] = "deferred by per-run work cap; resume this wave to continue"

        unresolved = [attempt for attempt in state["attempts"] if attempt["status"] not in {"unsat", "sat"}]
        findings = [attempt for attempt in state["attempts"] if attempt["status"] == "sat"]
        uncovered_gates = [attempt for attempt in state["attempts"] if not attempt["gate"]["local_gate_passed"]]
        run["finished_at"] = _now()
        run["status"] = "complete" if not unresolved and not findings and not uncovered_gates else "needs_review"
        reasons = []
        if unresolved:
            reasons.append(f"{len(unresolved)} unresolved/not-attempted question(s)")
        if findings:
            reasons.append(f"{len(findings)} SAT candidate(s) require disposition")
        if uncovered_gates:
            reasons.append(f"{len(uncovered_gates)} question(s) lack a passing covered local gate")
        if gate_failure:
            reasons.append(gate_failure)
        if source_failures and not all_sources_ok:
            reasons.append("source pin verification failed")
        if mutation_failures:
            reasons.append("mutation guard coverage or replay failed")
        run["reason"] = "; ".join(reasons) if reasons else None
        _persist(state, state_dir, cohort, roster)

        counts: dict[str, int] = {}
        for attempt in state["attempts"]:
            counts[attempt["status"]] = counts.get(attempt["status"], 0) + 1
        print(f"wave {args.wave_id}: {counts}; new={attempted}/{max_new}; solver_ms={run['solver_wall_ms']:.1f}; gate_ms={gate_ms:.1f}")
        print(f"state={state_path} checkpoint={state_dir / 'checkpoint.json'}")
        return 0 if run["status"] == "complete" else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, required=True)
    parser.add_argument("--roster", type=Path, required=True)
    parser.add_argument("--campaign", type=Path, default=ROOT / "properties/calibration/autonomous-corpus-campaign.json")
    parser.add_argument("--state-dir", type=Path, required=True)
    parser.add_argument("--wave-id", required=True)
    parser.add_argument("--corpus")
    parser.add_argument("--idiom-bucket")
    parser.add_argument("--checkout", action="append", default=[], metavar="REPO_ID=PATH")
    parser.add_argument("--gate", type=Path, help="JSON argv gate config with explicit question coverage")
    parser.add_argument(
        "--contract-overrides",
        type=Path,
        help="adopted source-bound revisions of unchanged historical human contracts",
    )
    parser.add_argument("--lock-file", type=Path, default=ROOT / "properties/generated/.autonomous-proof-wave.lock")
    parser.add_argument("--max-new-questions", type=int)
    parser.add_argument(
        "--recover-result",
        type=Path,
        help="recover one persisted in-flight result from its exact same-run local gate report without rerunning the solver",
    )
    parser.add_argument("--dry-run", action="store_true", help="validate inputs and source pins without running gates or properties")
    parser.add_argument("--status", action="store_true", help="report the authoritative resumable state without running work")
    args = parser.parse_args(argv)
    try:
        return _run_wave(args)
    except (OSError, ValueError, KeyError, TypeError, ConversionCheckpointError, WaveError) as exc:
        print(f"run-autonomous-proof-wave: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
