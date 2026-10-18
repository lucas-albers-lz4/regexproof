#!/usr/bin/env python3
"""Replay the pinned Doberman Windows secret-store path classification gap."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path, PureWindowsPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402


PIN = "53ae43c5298a2426c6696147fdd75e2a4aef10e2"
REPO_URL = "https://github.com/fu351/Doberman-Core"
SOURCE_FILE = "src/doberman/engine/rules/secrets.py"
SOURCE_SHA256 = "a73b183b5ac0da101e1411384e12ffe7da9f48f59947ec76a447974e246179fa"
REGEX_ID = "1da0edb358526b5f1d6ae780f0116744"


class GateError(ValueError):
    """Raised when the pinned product cannot be replayed as recorded."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git(checkout: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(checkout), *args],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.stdout.strip()


def _windows_relative(path: str, root: str) -> str:
    return PureWindowsPath(path).relative_to(PureWindowsPath(root)).as_posix().lower()


def build_report(source_root: Path) -> dict[str, Any]:
    checkout = source_root.resolve()
    if _git(checkout, "rev-parse", "HEAD") != PIN:
        raise GateError("Doberman checkout is not at the frozen cohort pin")
    source_path = checkout / SOURCE_FILE
    committed = subprocess.run(
        ["git", "-C", str(checkout), "show", f"{PIN}:{SOURCE_FILE}"],
        check=True,
        capture_output=True,
        timeout=10,
    ).stdout
    source_bytes = source_path.read_bytes()
    if source_bytes != committed or _sha256(committed) != SOURCE_SHA256:
        raise GateError("secret-rule source bytes differ from the frozen pin/hash")

    # Import the exact pinned product modules after source authentication.
    sys.path.insert(0, str(checkout / "src"))
    from doberman.engine.objective import ObjectiveGuardrail
    from doberman.engine.rules.paths import DEFAULT_BLOCKED_GLOBS, DEFAULT_SENSITIVE_GLOBS
    from doberman.engine.rules.secrets import SecretLeakageRule, _SECRET_PATH
    from doberman.models import EvalContext, Verdict
    from doberman.proxy.normalize import normalize

    root = r"C:\repo"
    basenames = (".npmrc", "credentials")
    windows_cases: list[dict[str, Any]] = []
    objective = ObjectiveGuardrail(load_plugins=False)
    secret_rule = SecretLeakageRule()
    for basename in basenames:
        target = root + "\\" + basename
        action = normalize("fs_read", {"path": target})
        if action.target != target or action.action_type.value != "file_read":
            raise GateError(f"proxy normalize changed the declared path input: {target!r}")
        ctx = EvalContext(
            metadata={"repo_root": root, "raw_arguments": {"path": target}}
        )
        secret_result = secret_rule.evaluate(action, ctx)
        objective_result = objective.evaluate(action, ctx)
        relative = _windows_relative(target, root)
        policy_match = any(
            fnmatch.fnmatch(relative, pattern)
            for pattern in (*DEFAULT_BLOCKED_GLOBS, *DEFAULT_SENSITIVE_GLOBS)
        )
        if _SECRET_PATH.search(target) is not None:
            raise GateError(f"expected source regex miss did not reproduce: {target!r}")
        if secret_result.verdict is not Verdict.PASS:
            raise GateError(f"secret rule no longer reproduces the path miss: {target!r}")
        if policy_match:
            raise GateError(f"default path policy unexpectedly covers {relative!r}")
        if objective_result.verdict is not Verdict.PASS:
            raise GateError(
                f"objective guardrail no longer reproduces PASS for {target!r}: "
                f"{objective_result.verdict}"
            )
        windows_cases.append(
            {
                "target": target,
                "normalized_target": action.target,
                "native_windows_relative_path": relative,
                "secret_regex_matches": False,
                "secret_rule_verdict": secret_result.verdict.value,
                "default_path_policy_matches": False,
                "objective_guardrail_verdict": objective_result.verdict.value,
            }
        )

    posix_cases: list[dict[str, Any]] = []
    for basename in basenames:
        target = "C:/repo/" + basename
        action = normalize("fs_read", {"path": target})
        result = secret_rule.evaluate(action, EvalContext())
        matched = _SECRET_PATH.search(target) is not None
        if not matched or result.verdict is Verdict.PASS:
            raise GateError(f"POSIX-separator positive control failed: {target!r}")
        posix_cases.append(
            {
                "target": target,
                "secret_regex_matches": matched,
                "secret_rule_verdict": result.verdict.value,
            }
        )

    # Refute the nearby .env.local claim: the secret regex also misses this
    # native Windows spelling, but the independent canonical path rule's
    # default .env.* glob covers its Windows-normalized relative path.
    env_local_target = root + r"\.env.local"
    env_local_relative = _windows_relative(env_local_target, root)
    env_local_covered = any(
        fnmatch.fnmatch(env_local_relative, pattern)
        for pattern in DEFAULT_BLOCKED_GLOBS
    )
    if _SECRET_PATH.search(env_local_target) is not None or not env_local_covered:
        raise GateError("the .env.local false-positive control did not match its evidence")

    source_pattern = _SECRET_PATH.pattern
    widened_pattern = source_pattern.replace(
        r"(?:^|/)\.npmrc$", r"(?:^|[/\\])\.npmrc$"
    ).replace(r"(?:^|/)credentials$", r"(?:^|[/\\])credentials$")
    widened = re.compile(widened_pattern)
    if not all(widened.search(row["target"]) for row in windows_cases):
        raise GateError("separator-fix sensitivity control failed")

    return {
        "schema_version": "1",
        "artifact_kind": "doberman-secret-path-regression-gate",
        "cohort_id": "2026-09-12-calibration-20-r2",
        "repo_id": "fu351/Doberman-Core",
        "repository_url": REPO_URL,
        "pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "regex_id": REGEX_ID,
        "python_version": platform.python_version(),
        "host_platform": platform.platform(),
        "native_windows_runtime": os.name == "nt",
        "result": "pass_current_gap_reproduced",
        "interpretation": (
            "The exact Python regex and product rules reproduce the Windows-path "
            "classification gap. On a non-Windows host, native path canonicalization "
            "is not exercised; the report separately checks the pinned canonical "
            "path rule's Windows-normalized form against its exact default globs."
        ),
        "windows_cases": windows_cases,
        "posix_controls": posix_cases,
        "refuted_env_local_candidate": {
            "target": env_local_target,
            "secret_regex_matches": False,
            "windows_normalized_relative_path": env_local_relative,
            "default_blocked_glob_matches": env_local_covered,
            "interpretation": "Covered by the separate .env.* protected-path rule.",
        },
        "fix_sensitivity": {
            "backslash_separator_added": True,
            "all_windows_cases_match_after_fix": True,
            "kind": "repair_sensitivity_control; not a native Windows replay",
        },
        "security_impact": "pending_product_triage",
        "external_report_sent": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = build_report(args.source_root)
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        args.output.chmod(0o644)
    except (OSError, subprocess.SubprocessError, ValueError, ImportError) as exc:
        print(f"doberman-secret-path-regression-gate: error: {exc}", file=sys.stderr)
        return 2
    print(
        "Doberman secret-path gap reproduced: "
        f"{len(report['windows_cases'])} Windows cases, "
        f"{len(report['posix_controls'])} POSIX controls; "
        f"native_windows_runtime={report['native_windows_runtime']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
