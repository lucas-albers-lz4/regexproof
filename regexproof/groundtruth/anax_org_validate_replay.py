"""Replay Anax's pinned ValidateOrg function using the Go RE2 implementation."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

PIN = "2f3fa5a506d6565fa68858b7963450567ddda114"
REPOSITORY = "https://github.com/open-horizon/anax.git"
SOURCE_FILE = "cli/cliutils/cliutils.go"
SOURCE_SHA256 = "19e98c2f753ff03e83aa442a21cd352f8926efdff20d44d3c111016d908509d0"
SOURCE_PATTERN = r"[_,\s\?\']"
MUTATED_PATTERN = r"[_,\s\']"
_SOURCE_ENV = "ANAX_REPLAY_SOURCE"
_DEFAULT_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"anax-{PIN}"
)


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
        shell=False,
    )
    return result.stdout if binary else result.stdout.strip()


def _validate_source(root: Path) -> bytes:
    if root.is_symlink() or not root.is_dir():
        raise RuntimeError(f"Anax checkout is missing or a symlink: {root}")
    revision = _git(root, "rev-parse", "HEAD")
    if revision != PIN:
        raise RuntimeError(f"Anax source is {revision}, expected exact pin {PIN}")
    if _git(root, "status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Anax source must be a clean pinned checkout")
    source_path = root / SOURCE_FILE
    if source_path.is_symlink() or not source_path.is_file():
        raise RuntimeError(f"pinned Anax source is missing or a symlink: {source_path}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or source_path.read_bytes() != committed:
        raise RuntimeError("Anax ValidateOrg source bytes differ from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"Anax cliutils source digest is {digest}, expected {SOURCE_SHA256}")
    return committed


def source_root() -> Path:
    """Return the caller-supplied clean checkout or the established exact pin."""
    root = (
        Path(os.environ[_SOURCE_ENV]).expanduser().resolve()
        if os.environ.get(_SOURCE_ENV)
        else _DEFAULT_ROOT
    )
    if root.exists():
        _validate_source(root)
        return root
    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", PIN)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _validate_source(root)
    except (OSError, subprocess.SubprocessError, RuntimeError):
        shutil.rmtree(root, ignore_errors=True)
        raise
    return root


def _function(source: bytes, *, mutated: bool, name: str) -> str:
    marker = b"func ValidateOrg(org string) bool {"
    start = source.find(marker)
    if start < 0 or source.find(marker, start + 1) >= 0:
        raise RuntimeError("cannot uniquely locate pinned ValidateOrg")
    depth = 0
    end = -1
    for index in range(source.find(b"{", start), len(source)):
        if source[index : index + 1] == b"{":
            depth += 1
        elif source[index : index + 1] == b"}":
            depth -= 1
            if depth == 0:
                end = index + 1
                break
    if end < 0:
        raise RuntimeError("cannot find the end of pinned ValidateOrg")
    function = source[start:end]
    old = b"`" + SOURCE_PATTERN.encode("ascii") + b"`"
    replacement = b"`" + (MUTATED_PATTERN if mutated else SOURCE_PATTERN).encode("ascii") + b"`"
    if function.count(old) != 1 or b"return invalidCheck" not in function:
        raise RuntimeError("pinned ValidateOrg no longer has the reviewed MatchString/return path")
    function = function.replace(old, replacement, 1)
    function = function.replace(b"func ValidateOrg(", f"func {name}(".encode("ascii"), 1)
    return function.decode("utf-8")


def _wrapper(source: bytes) -> str:
    original = _function(source, mutated=False, name="validateOrg")
    weakened = _function(source, mutated=True, name="validateOrgMutated")
    return f'''package main

import (
    "encoding/json"
    "fmt"
    "os"
    "regexp"
    "runtime"
)

type messagePrinter struct{{}}
func (messagePrinter) Sprintf(format string, args ...interface{{}}) string {{ return fmt.Sprintf(format, args...) }}
type i18nStub struct{{}}
func (i18nStub) GetMessagePrinter() messagePrinter {{ return messagePrinter{{}} }}
var i18n i18nStub
const INTERNAL_ERROR = 1
func Fatal(_ int, message string) {{ panic(message) }}

{original}

{weakened}

type request struct {{ Inputs []string `json:"inputs"` }}
type response struct {{ GoVersion string `json:"go_version"`; Original []bool `json:"original"`; Mutated []bool `json:"mutated"` }}

func main() {{
    var input request
    if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {{ panic(err) }}
    result := response{{GoVersion: runtime.Version(), Original: make([]bool, 0, len(input.Inputs)), Mutated: make([]bool, 0, len(input.Inputs))}}
    for _, value := range input.Inputs {{
        result.Original = append(result.Original, validateOrg(value))
        result.Mutated = append(result.Mutated, validateOrgMutated(value))
    }}
    if err := json.NewEncoder(os.Stdout).Encode(result); err != nil {{ panic(err) }}
}}
'''


def run_validate_org(inputs: list[str]) -> dict:
    """Execute the exact pinned function body and a one-character source mutation."""
    if not shutil.which("go"):
        raise RuntimeError("Go is required for Anax's RE2 product replay")
    root = source_root()
    source = _validate_source(root)
    with tempfile.TemporaryDirectory(prefix="regexproof-anax-org-validate-") as temp:
        work = Path(temp)
        (work / "go.mod").write_text("module anax-org-validate-replay\n\ngo 1.23\n", encoding="utf-8")
        (work / "main.go").write_text(_wrapper(source), encoding="utf-8")
        try:
            proc = subprocess.run(
                ["go", "run", "."],
                cwd=work,
                input=json.dumps({"inputs": inputs}, ensure_ascii=True),
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
                shell=False,
                env={**os.environ, "GOTOOLCHAIN": "local", "GO111MODULE": "on"},
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("Anax ValidateOrg replay timed out") from exc
        if proc.returncode != 0:
            raise RuntimeError(
                f"Anax ValidateOrg replay failed ({proc.returncode}): {proc.stderr.strip()[-2000:]}"
            )
        try:
            result = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Anax ValidateOrg replay returned invalid JSON") from exc
    if (
        not isinstance(result, dict)
        or result.get("go_version") != subprocess.run(
            ["go", "env", "GOVERSION"], capture_output=True, text=True, check=True, timeout=10
        ).stdout.strip()
        or not isinstance(result.get("original"), list)
        or not isinstance(result.get("mutated"), list)
        or len(result["original"]) != len(inputs)
        or len(result["mutated"]) != len(inputs)
        or any(type(value) is not bool for value in result["original"] + result["mutated"])
    ):
        raise RuntimeError("Anax ValidateOrg replay returned an invalid result vector")
    return result


def mutation_reproduces_question_mark(witness: dict) -> bool:
    if witness.get("character") != "?":
        return False
    result = run_validate_org(["?"])
    return result["original"] == [True] and result["mutated"] == [False]


__all__ = [
    "MUTATED_PATTERN",
    "PIN",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
    "SOURCE_SHA256",
    "mutation_reproduces_question_mark",
    "run_validate_org",
    "source_root",
]
