"""Exact-pin replay for Aidevops issue-body threshold arithmetic."""
from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from regexproof.groundtruth.aidevops_cited_file_replay import (
    HELPER_FILE,
    HELPER_SHA256,
    PIN,
    PRODUCER_FILE,
    PRODUCER_SHA256,
    REPOSITORY,
    TEST_FILE,
    TEST_SHA256,
    _run,
    _source_bytes,
    source_root,
)

SOURCE_PATTERN = r"threshold=[0-9]+"
WITNESS = "08"
FIXTURE_LINES = 5

_GH_STUB = r'''#!/usr/bin/env bash
set -eu
if [[ "${1:-}" == "api" ]]; then
  if [[ "${3:-}" == "--jq" && "${4:-}" == *body* ]]; then
    cat "$AIDEVOPS_REPLAY_BODY_FILE"
  elif [[ "${3:-}" == "--jq" && "${4:-}" == *created_at* ]]; then
    printf '\t\t\n'
  else
    printf '{}\n'
  fi
  exit 0
fi
if [[ "${1:-}" == "issue" || "${1:-}" == "label" ]]; then exit 0; fi
printf 'unexpected gh invocation: %s\n' "$*" >&2
exit 1
'''

_GIT_STUB = r'''#!/usr/bin/env bash
set -eu
if [[ "${1:-}" == "clone" ]]; then
  target=""
  for arg in "$@"; do target="$arg"; done
  mkdir -p "$target"
  for n in $(seq 1 5); do printf 'fixture-line-%s\n' "$n"; done >"$target/threshold-fixture.txt"
  exit 0
fi
exec /usr/bin/git "$@"
'''


def _replay_threshold(value: str) -> dict[str, Any]:
    root = source_root()
    helper_bytes = _source_bytes(root, HELPER_FILE, HELPER_SHA256)
    producer = _source_bytes(root, PRODUCER_FILE, PRODUCER_SHA256).decode("utf-8")
    tests = _source_bytes(root, TEST_FILE, TEST_SHA256).decode("utf-8")
    helper = helper_bytes.decode("utf-8")
    if "CITED_THRESHOLD=$(printf '%s' \"$generator_line\" | grep -oE 'threshold=[0-9]+'" not in helper:
        raise RuntimeError("pinned helper threshold extraction changed")
    if '[[ "$line_count" -lt "$CITED_THRESHOLD" ]]' not in helper:
        raise RuntimeError("pinned helper threshold comparison changed")
    if 'threshold=${LARGE_FILE_LINE_THRESHOLD}' not in producer:
        raise RuntimeError("pinned producer no longer emits its configured threshold")
    if 'threshold=100 -->' not in tests:
        raise RuntimeError("pinned large-file regression tests no longer cover threshold=100")

    with tempfile.TemporaryDirectory(prefix="aidevops-threshold-replay-") as temp_name:
        temp = Path(temp_name)
        bin_dir = temp / "bin"
        home = temp / "home"
        tmpdir = temp / "tmp"
        bin_dir.mkdir()
        home.mkdir()
        tmpdir.mkdir()
        body_file = temp / "issue-body.txt"
        body_file.write_text(
            "<!-- aidevops:generator=large-file-simplification-gate "
            f"cited_file=threshold-fixture.txt threshold={value} -->\n",
            encoding="ascii",
        )
        gh = bin_dir / "gh"
        git = bin_dir / "git"
        gh.write_text(_GH_STUB, encoding="utf-8")
        git.write_text(_GIT_STUB, encoding="utf-8")
        gh.chmod(0o755)
        git.chmod(0o755)
        env = os.environ.copy()
        env.update({
            "PATH": f"{bin_dir}{os.pathsep}{env.get('PATH', '')}",
            "HOME": str(home),
            "TMPDIR": str(tmpdir),
            "AIDEVOPS_REPLAY_BODY_FILE": str(body_file),
            "AIDEVOPS_DISPATCH_PATH_FILES_CONF": str(temp / "missing-self-hosting.conf"),
            "PULSE_STATS_FILE": str(temp / "missing-pulse-stats.json"),
            "LC_ALL": "C",
        })
        completed = _run(
            ["bash", str(root / HELPER_FILE), "validate", "321", "owner/repo"],
            cwd=temp,
            env=env,
        )
        output = completed.stdout + completed.stderr
        return {
            "source_pin": PIN,
            "repository_url": REPOSITORY,
            "source_file": HELPER_FILE,
            "source_sha256": HELPER_SHA256,
            "producer_file": PRODUCER_FILE,
            "producer_sha256": PRODUCER_SHA256,
            "test_file": TEST_FILE,
            "test_sha256": TEST_SHA256,
            "product_engine": "Bash, GNU grep/sed, wc, and POSIX shell",
            "threshold": value,
            "fixture_path": "threshold-fixture.txt",
            "fixture_lines": FIXTURE_LINES,
            "exit_code": completed.returncode,
            "arithmetic_error": "value too great for base" in output or "syntax error in expression" in output,
            "premise_falsified": "premise falsified by validator" in output,
            "validator_passed": "validator passed — dispatch proceeds" in output,
            "output": output,
            "network_access": False,
            "gh_and_git_stubbed": True,
        }


def threshold_replay() -> dict[str, Any]:
    """Compare the same five-line fixture under decimal 8 and octal-invalid 08."""
    normal = _replay_threshold("8")
    witness = _replay_threshold(WITNESS)
    return {
        "schema_version": "1",
        "source_pin": PIN,
        "witness": WITNESS,
        "normal_decimal_control": normal,
        "leading_zero_witness": witness,
        "interpretation": (
            "With threshold=8 the exact helper recognizes 5 < 8 and returns 10. "
            "With threshold=08 Bash rejects the arithmetic operand as invalid octal; "
            "the failed [[ -lt ]] is treated as false, the helper logs that the "
            "premise still holds, returns 0, and allows dispatch."
        ),
        "public_disclosure_proven": False,
        "security_impact_confirmed": False,
    }


def threshold_failure_reproduces(witness: dict[str, str]) -> bool:
    if witness.get("threshold") != WITNESS:
        return False
    result = threshold_replay()
    normal = result["normal_decimal_control"]
    bug = result["leading_zero_witness"]
    return (
        normal["exit_code"] == 10
        and normal["premise_falsified"]
        and bug["exit_code"] == 0
        and bug["arithmetic_error"]
        and bug["validator_passed"]
    )


__all__ = ["SOURCE_PATTERN", "WITNESS", "threshold_failure_reproduces", "threshold_replay"]
