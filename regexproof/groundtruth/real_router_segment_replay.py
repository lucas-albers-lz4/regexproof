"""Run the exact pinned Real-Router route segment helpers under Node."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "55aa7ef43a9c129beba90823cd8a4db10bb01211"
REPOSITORY = "https://github.com/greydragon888/real-router"
REPO_ID = "greydragon888/real-router"
CONSTANTS_FILE = "packages/route-utils/src/constants.ts"
TESTERS_FILE = "packages/route-utils/src/segmentTesters.ts"
CONSTANTS_SHA256 = "ba3add9f6367eb2b031b7bf5869f6703a8d6290fcb064e4855e09a17ce6011db"
TESTERS_SHA256 = "95d029dc8991b10818390ca195a625116668ffc9da23688944a4dd97d1c9d193"
SOURCE_PATTERN = r"^[\w.-]+$"
WEAK_PATTERN = r"^[\w.\/-]+$"
DEFAULT_SOURCE_ROOT = Path(
    "/tmp/regexproof-pinned-sources/real-router-55aa7ef43a9c129beba90823cd8a4db10bb01211"
)

_NODE_REPLAY = r'''import fs from "node:fs";
import { startsWithSegment, endsWithSegment, includesSegment } from "./segmentTesters.mts";

const input = JSON.parse(fs.readFileSync(0, "utf8"));
const funcs = [startsWithSegment, endsWithSegment, includesSegment];
const outcomes = [];
for (const value of input.values) {
  const row = [];
  for (const fn of funcs) {
    try {
      row.push(fn(value, value) === true);
    } catch (error) {
      row.push(error?.name || "Error");
    }
  }
  outcomes.push(row);
}
process.stdout.write(JSON.stringify({ version: process.version, outcomes }));
'''


def source_root() -> Path:
    return Path(os.environ.get("REAL_ROUTER_REPLAY_SOURCE", DEFAULT_SOURCE_ROOT)).resolve()


def _run(
    argv: list[str], *, cwd: Path | None = None, input_text: str | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv,
        cwd=cwd,
        input=input_text,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
        shell=False,
    )


def _pinned_source(root: Path, relative: str, expected_sha256: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned Real-Router source is missing or a symlink: {path}")
    source = path.read_bytes()
    shown = _run(
        ["git", "-C", str(root), "show", f"{PIN}:{relative}"], timeout=30
    )
    if shown.returncode != 0 or shown.stdout.encode("utf-8") != source:
        raise RuntimeError(f"working source differs from {PIN}:{relative}")
    digest = hashlib.sha256(source).hexdigest()
    if digest != expected_sha256:
        raise RuntimeError(
            f"Real-Router {relative} digest is {digest}, expected {expected_sha256}"
        )
    return source


def verify_source(root: Path | None = None) -> dict[str, str]:
    root = (root or source_root()).resolve()
    head = _run(["git", "-C", str(root), "rev-parse", "HEAD"], timeout=30)
    if head.returncode != 0 or head.stdout.strip() != PIN:
        raise RuntimeError(f"Real-Router checkout is not at expected pin {PIN}")
    status = _run(["git", "-C", str(root), "status", "--porcelain=v1"], timeout=30)
    if status.returncode != 0 or status.stdout.strip():
        raise RuntimeError("Real-Router source checkout is not clean")
    constants = _pinned_source(root, CONSTANTS_FILE, CONSTANTS_SHA256)
    testers = _pinned_source(root, TESTERS_FILE, TESTERS_SHA256)
    declaration = b"export const SAFE_SEGMENT_PATTERN = /^[\\w.-]+$/;"
    if constants.count(declaration) != 1:
        raise RuntimeError("pinned SAFE_SEGMENT_PATTERN declaration changed")
    if testers.count(b"if (!SAFE_SEGMENT_PATTERN.test(segment))") != 1:
        raise RuntimeError("pinned segment validation no longer uses SAFE_SEGMENT_PATTERN")
    for exported in (b"startsWithSegment", b"endsWithSegment", b"includesSegment"):
        if testers.count(b"export const " + exported) != 1:
            raise RuntimeError(f"expected one exported {exported.decode()} helper")
    return {
        "constants_sha256": hashlib.sha256(constants).hexdigest(),
        "testers_sha256": hashlib.sha256(testers).hexdigest(),
    }


def run_helpers(
    values: list[str], *, weakened: bool = False, root: Path | None = None
) -> dict[str, Any]:
    """Run the pinned helper body; only the extensionless import is adapted."""
    root = (root or source_root()).resolve()
    verify_source(root)
    constants = (root / CONSTANTS_FILE).read_text(encoding="utf-8")
    testers = (root / TESTERS_FILE).read_text(encoding="utf-8")
    original = "export const SAFE_SEGMENT_PATTERN = /^[\\w.-]+$/;"
    if weakened:
        changed = "export const SAFE_SEGMENT_PATTERN = /^[\\w.\\/-]+$/;"
        if constants.count(original) != 1:
            raise RuntimeError("cannot uniquely source-mutate SAFE_SEGMENT_PATTERN")
        constants = constants.replace(original, changed, 1)
    adapted_import = 'from "./constants.mts";'
    original_import = 'from "./constants";'
    if testers.count(original_import) != 1:
        raise RuntimeError("cannot adapt the one extensionless source import")
    testers = testers.replace(original_import, adapted_import, 1)

    with tempfile.TemporaryDirectory(prefix="regexproof-real-router-replay-") as temp:
        temp_root = Path(temp)
        (temp_root / "constants.mts").write_text(constants, encoding="utf-8")
        (temp_root / "segmentTesters.mts").write_text(testers, encoding="utf-8")
        entry = temp_root / "replay.mts"
        entry.write_text(_NODE_REPLAY, encoding="utf-8")
        proc = _run(
            ["node", "--experimental-strip-types", str(entry)],
            input_text=json.dumps({"values": values}, ensure_ascii=True),
            timeout=120,
        )
    if proc.returncode != 0:
        raise RuntimeError(
            "Node exact-source route tester replay failed: "
            f"{proc.stderr.strip() or proc.stdout.strip()}"
        )
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Node exact-source replay returned invalid JSON") from exc
    if result.get("version") is None or len(result.get("outcomes", [])) != len(values):
        raise RuntimeError("Node exact-source replay returned incomplete evidence")
    return result


def mutation_accepts_slash_in_all_segment_testers(witness: dict[str, str]) -> bool:
    if witness.get("segment_char") != "/":
        return False
    original = run_helpers(["/"])
    weakened = run_helpers(["/"], weakened=True)
    return (
        original["outcomes"] == [["TypeError", "TypeError", "TypeError"]]
        and weakened["outcomes"] == [[True, True, True]]
    )
