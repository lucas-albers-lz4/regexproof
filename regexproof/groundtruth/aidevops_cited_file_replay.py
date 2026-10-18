"""Exact-pin replay for Aidevops' issue-body cited-file path handling."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
REPOSITORY = "https://github.com/marcusquinn/aidevops"
HELPER_FILE = ".agents/scripts/pre-dispatch-validator-helper.sh"
HELPER_SHA256 = "b68445d5eaf510e820831422c6e064ac58bbdc4496483ad562df30786e3723b5"
PRODUCER_FILE = ".agents/scripts/pulse-dispatch-large-file-gate.sh"
PRODUCER_SHA256 = "b7361a8d61bdc98bfc51909c059a8bbaaa05bf4d6664a86e61d3a4334ee9c4aa"
TEST_FILE = ".agents/scripts/tests/test-pre-dispatch-validator-large-file.sh"
TEST_SHA256 = "32d49c2421d9c05cb0069d8346d4e6fb2ff5be4041ee0f39297649e41575f5a7"
SOURCE_PATTERN = r"cited_file=[^ >]+"
TRAVERSAL_WITNESS = "../oracle.txt"
SOURCE_ENV = "AIDEVOPS_PREDISPATCH_CITED_FILE_SOURCE"
DEFAULT_SOURCE_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"aidevops-{PIN}"
)


def _run(
    argv: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    timeout: int = 45,
):
    return subprocess.run(
        argv,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
        shell=False,
    )


def _source_bytes(root: Path, relative: str, expected: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"Aidevops replay source is missing or a symlink: {relative}")
    shown = _run(["git", "-C", str(root), "show", f"{PIN}:{relative}"])
    if shown.returncode or shown.stdout.encode("utf-8") != path.read_bytes():
        raise RuntimeError(f"Aidevops worktree differs from pinned source: {relative}")
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != expected:
        raise RuntimeError(f"Aidevops source digest mismatch for {relative}: {digest}")
    return payload


def source_root() -> Path:
    """Return a clean checkout at the frozen pin, fetching only that commit if needed."""
    root = Path(os.environ.get(SOURCE_ENV, DEFAULT_SOURCE_ROOT)).expanduser()
    if root.is_symlink():
        raise RuntimeError(f"Aidevops pinned checkout must not be a symlink: {root}")
    if not root.exists():
        root.parent.mkdir(parents=True, exist_ok=True)
        root.mkdir()
        try:
            for argv in (
                ["git", "-C", str(root), "init", "--quiet"],
                ["git", "-C", str(root), "remote", "add", "origin", REPOSITORY],
                ["git", "-C", str(root), "fetch", "--quiet", "--depth=1", "origin", PIN],
                ["git", "-C", str(root), "checkout", "--quiet", "--detach", "FETCH_HEAD"],
            ):
                result = _run(argv, timeout=120)
                if result.returncode:
                    raise RuntimeError(result.stderr.strip() or f"git command failed: {argv[3:]}")
        except (OSError, RuntimeError, subprocess.SubprocessError):
            shutil.rmtree(root, ignore_errors=True)
            raise
    if not root.is_dir():
        raise RuntimeError(f"Aidevops pinned checkout is unavailable: {root}")
    head = _run(["git", "-C", str(root), "rev-parse", "HEAD"])
    origin = _run(["git", "-C", str(root), "remote", "get-url", "origin"])
    status = _run(["git", "-C", str(root), "status", "--porcelain=v1", "--untracked-files=all"])
    if head.returncode or head.stdout.strip() != PIN:
        raise RuntimeError(f"Aidevops checkout is not at frozen pin {PIN}")
    if origin.returncode or origin.stdout.strip().removesuffix(".git") != REPOSITORY:
        raise RuntimeError("Aidevops checkout origin differs from the frozen repository")
    if status.returncode or status.stdout.strip():
        raise RuntimeError("Aidevops pinned checkout must be clean")
    helper = _source_bytes(root, HELPER_FILE, HELPER_SHA256).decode("utf-8")
    producer = _source_bytes(root, PRODUCER_FILE, PRODUCER_SHA256).decode("utf-8")
    tests = _source_bytes(root, TEST_FILE, TEST_SHA256).decode("utf-8")
    if (
        helper.count("grep -oE 'cited_file=[^ >]+'") != 2
        or helper.count("CITED_FILE=$(printf '%s' \"$generator_line\"") != 1
    ):
        raise RuntimeError("pinned cited_file extraction changed or is ambiguous")
    if helper.count('local target_file="${SCRATCH_DIR}/repo/${CITED_FILE}"') != 2:
        raise RuntimeError("pinned helper no longer joins cited_file under the clone")
    if "# Clone repo into scratch dir for a fresh read against HEAD" not in helper:
        raise RuntimeError("pinned helper no longer documents the fresh-HEAD path")
    if 'cited_file=${lf_path}' not in producer:
        raise RuntimeError("pinned producer no longer derives cited_file from lf_path")
    if "cited_file=.agents/scripts/big-file.sh" not in tests:
        raise RuntimeError("pinned tests no longer exercise repository-relative paths")
    return root


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
if [[ "${1:-}" == "issue" || "${1:-}" == "label" ]]; then
  exit 0
fi
printf 'unexpected gh invocation: %s\n' "$*" >&2
exit 1
'''

_GIT_STUB = r'''#!/usr/bin/env bash
set -eu
if [[ "${1:-}" == "clone" ]]; then
  target=""
  for arg in "$@"; do target="$arg"; done
  mkdir -p "$target"
  parent="$(dirname "$target")"
  for n in $(seq 1 37); do printf 'fixture-line-%s\n' "$n"; done >"$parent/oracle.txt"
  exit 0
fi
exec /usr/bin/git "$@"
'''


def replay_cited_file(cited_file: str = TRAVERSAL_WITNESS) -> dict[str, Any]:
    """Run the pinned helper with local-only stubs and a file outside its clone."""
    root = source_root()
    if cited_file != TRAVERSAL_WITNESS:
        raise ValueError(f"replay fixture is intentionally limited to {TRAVERSAL_WITNESS!r}")
    helper = root / HELPER_FILE
    with tempfile.TemporaryDirectory(prefix="aidevops-cited-file-replay-") as temp_name:
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
            f"cited_file={cited_file} threshold=1000 -->\n",
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
        completed = _run(["bash", str(helper), "validate", "321", "owner/repo"], cwd=temp, env=env)
        output = completed.stdout + completed.stderr
        expected_log = "large-file-simplification-gate validator: ../oracle.txt is now 37 lines"
        return {
            "source_pin": PIN,
            "source_file": HELPER_FILE,
            "source_sha256": HELPER_SHA256,
            "producer_file": PRODUCER_FILE,
            "producer_sha256": PRODUCER_SHA256,
            "test_file": TEST_FILE,
            "test_sha256": TEST_SHA256,
            "product_engine": "Bash, GNU grep/sed, wc, and POSIX path resolution",
            "witness": cited_file,
            "fixture_line_count": 37,
            "exit_code": completed.returncode,
            "outside_clone_file_read": expected_log in output and completed.returncode == 10,
            "matched_log": expected_log in output,
            "output": output,
        }


def cited_file_traversal_reproduces(witness: dict[str, str]) -> bool:
    """Ground-truth callback: replay the model value through the actual helper."""
    value = witness.get("cited_file")
    if value != TRAVERSAL_WITNESS:
        return False
    return bool(replay_cited_file(value)["outside_clone_file_read"])


__all__ = [
    "HELPER_FILE",
    "HELPER_SHA256",
    "PIN",
    "PRODUCER_FILE",
    "PRODUCER_SHA256",
    "REPOSITORY",
    "SOURCE_PATTERN",
    "TEST_FILE",
    "TEST_SHA256",
    "TRAVERSAL_WITNESS",
    "cited_file_traversal_reproduces",
    "replay_cited_file",
    "source_root",
]
