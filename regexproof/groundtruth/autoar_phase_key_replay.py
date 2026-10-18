"""Replay AutoAR's pinned phase-key sanitizer with the exact Go helper."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from regexproof.groundtruth.autoar_html_escape_replay import source_root

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
REPOSITORY = "https://github.com/h0tak88r/AutoAR"
GO_TOOLCHAIN = "go1.25.7"
SOURCE_FILE = "internal/utils/phase_logs.go"
SOURCE_SHA256 = "3dec250b5802efadac77c6ba9cf9ce19f5fec09a8111674ab13a56d35e601ddc"
CALLER_FILE = "internal/api/scan_results_api.go"
CALLER_SHA256 = "1f77c4d3a709d839871db11c70c17c002c98f57bf1a8814e3ec04cb972834998"
ROUTES_FILE = "internal/api/api.go"
ROUTES_SHA256 = "8dc5737c711df971d84c28fb4ccc720f7c1f895b852edf7ec9525b4d72f46631"
RESULTS_FILE = "internal/utils/json_output.go"
RESULTS_SHA256 = "de0032fe9862995108414b3ebc0f75a49e7d93090f2646b6ea98caa8217938e5"
GO_MOD_SHA256 = "e94b543737a0e79aa5541e1fc6ee3b0fd112f44edf5800e9b8233d6149e89a6b"
_SOURCE_PATTERN = b"[^a-zA-Z0-9_-]+"
_WEAK_PATTERN = b"[^a-zA-Z0-9_./-]+"


def _pinned_bytes(root: Path, relative: str, expected_sha256: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned AutoAR source is missing or a symlink: {path}")
    source = path.read_bytes()
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{relative}"],
        capture_output=True,
        check=True,
        timeout=30,
        shell=False,
    ).stdout
    if source != committed:
        raise RuntimeError(f"AutoAR bytes differ from {PIN}:{relative}")
    digest = hashlib.sha256(source).hexdigest()
    if digest != expected_sha256:
        raise RuntimeError(
            f"AutoAR {relative} digest is {digest}, expected {expected_sha256}"
        )
    return source


def _function(source: bytes, name: bytes) -> bytes:
    start = source.find(name)
    if start < 0 or source.find(name, start + len(name)) >= 0:
        raise RuntimeError(f"cannot uniquely find pinned Go function {name!r}")
    end = source.find(b"\n}\n", start)
    if end < 0:
        raise RuntimeError(f"cannot bound pinned Go function {name!r}")
    return source[start : end + 2]


def verify_source_evidence() -> dict[str, Any]:
    """Bind the regex, sanitizer, API query, filename sink, and route."""
    root = source_root()
    source = _pinned_bytes(root, SOURCE_FILE, SOURCE_SHA256)
    caller = _pinned_bytes(root, CALLER_FILE, CALLER_SHA256)
    routes = _pinned_bytes(root, ROUTES_FILE, ROUTES_SHA256)
    results = _pinned_bytes(root, RESULTS_FILE, RESULTS_SHA256)
    go_mod = _pinned_bytes(root, "go.mod", GO_MOD_SHA256)
    declaration = b"var sanitizeRe = regexp.MustCompile(`" + _SOURCE_PATTERN + b"`)"
    if source.count(declaration) != 1:
        raise RuntimeError("pinned phase-log sanitizer regex changed")
    sanitizer = _function(source, b"func sanitizePhaseKey(")
    if (
        b"sanitizeRe.ReplaceAllString(s, \"_\")" not in sanitizer
        or b"strings.Trim(s, \"_\")" not in sanitizer
        or b'return "unknown"' not in sanitizer
    ):
        raise RuntimeError("pinned sanitizer transformation differs from reviewed behavior")
    if (
        caller.count(b'module := strings.TrimSpace(c.Query("module"))') != 1
        or caller.count(b"utils.ReadPhaseLogFile(scanID, module)") != 1
    ):
        raise RuntimeError("pinned API caller no longer passes the module query to the file reader")
    if (
        source.count(b'filename := sanitizePhaseKey(phaseKey) + ".jsonl"') != 2
        or source.count(b"path := filepath.Join(logDir, filename)") != 2
    ):
        raise RuntimeError("pinned reader/writer no longer sanitizes the filename component")
    if (
        b'apiGroup.Use(auth)' not in routes
        or b'apiGroup.GET("/scans/:id/logs", apiGetScanPhaseLogs)' not in routes
    ):
        raise RuntimeError("pinned phase-log API route changed")
    if b"return filepath.Join(GetResultsDir(), scanID)" not in results:
        raise RuntimeError("separate scanID result-root input changed; re-review scope")
    if b"go 1.25.7" not in go_mod:
        raise RuntimeError("pinned AutoAR go.mod no longer requires Go 1.25.7")
    return {
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_file": SOURCE_FILE,
        "source_sha256": SOURCE_SHA256,
        "caller_file": CALLER_FILE,
        "caller_sha256": CALLER_SHA256,
        "routes_file": ROUTES_FILE,
        "routes_sha256": ROUTES_SHA256,
        "results_root_file": RESULTS_FILE,
        "results_root_sha256": RESULTS_SHA256,
        "go_mod_sha256": GO_MOD_SHA256,
        "path": [
            "apiGetScanPhaseLogs reads caller-controlled query parameter module",
            "the handler passes module to ReadPhaseLogFile when no in-memory entries are returned",
            "ReadPhaseLogFile calls sanitizePhaseKey before appending .jsonl and filepath.Join",
            "GetScanResultsDir separately joins scanID; this contract does not cover scanID",
        ],
    }


def _wrapper(source: bytes, *, weakened: bool) -> str:
    declaration = b"var sanitizeRe = regexp.MustCompile(`" + _SOURCE_PATTERN + b"`)"
    if source.count(declaration) != 1:
        raise RuntimeError("cannot uniquely locate pinned sanitizeRe declaration")
    if weakened:
        declaration = declaration.replace(_SOURCE_PATTERN, _WEAK_PATTERN, 1)
    sanitizer = _function(source, b"func sanitizePhaseKey(").decode("utf-8")
    return f'''package main

import (
    "encoding/json"
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "runtime"
    "strings"
)

{declaration.decode("utf-8")}

{sanitizer}

type input struct {{ Values []string `json:"values"` }}
type output struct {{
    GoVersion string `json:"go_version"`
    Weakened bool `json:"weakened"`
    Results []result `json:"results"`
}}
type result struct {{
    Input string `json:"input"`
    Component string `json:"component"`
    Path string `json:"path"`
    Relative string `json:"relative"`
    Inside bool `json:"inside"`
}}

func main() {{
    var in input
    if err := json.NewDecoder(os.Stdin).Decode(&in); err != nil {{ panic(err) }}
    root := filepath.Join(os.TempDir(), "regexproof-phase-key-root", "scan-1", "phase-logs")
    out := output{{GoVersion: runtime.Version(), Weakened: {str(weakened).lower()}, Results: make([]result, 0, len(in.Values))}}
    for _, value := range in.Values {{
        component := sanitizePhaseKey(value) + ".jsonl"
        path := filepath.Join(root, component)
        relative, err := filepath.Rel(root, path)
        if err != nil {{ panic(err) }}
        inside := relative != ".." && !strings.HasPrefix(relative, ".."+string(filepath.Separator)) && !filepath.IsAbs(relative)
        out.Results = append(out.Results, result{{Input: value, Component: sanitizePhaseKey(value), Path: path, Relative: relative, Inside: inside}})
    }}
    if err := json.NewEncoder(os.Stdout).Encode(out); err != nil {{ panic(err) }}
    fmt.Fprintln(os.Stderr, "exact pinned sanitizePhaseKey replay")
}}
'''


def run_sanitizer(values: list[str], *, weakened: bool = False) -> dict[str, Any]:
    """Compile the exact pinned sanitizer body and return path components."""
    if not shutil.which("go"):
        raise RuntimeError("Go is required for AutoAR's RE2 product replay")
    root = source_root()
    source = _pinned_bytes(root, SOURCE_FILE, SOURCE_SHA256)
    with tempfile.TemporaryDirectory(prefix="regexproof-autoar-phase-key-") as temp:
        work = Path(temp)
        (work / "go.mod").write_text(
            "module regexproof-autoar-phase-key-replay\n\ngo 1.25.7\n",
            encoding="utf-8",
        )
        (work / "main.go").write_text(
            _wrapper(source, weakened=weakened), encoding="utf-8"
        )
        env = os.environ.copy()
        env["GOTOOLCHAIN"] = GO_TOOLCHAIN
        try:
            proc = subprocess.run(
                ["go", "run", "."],
                cwd=work,
                input=json.dumps({"values": values}, ensure_ascii=True),
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
                shell=False,
                env=env,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("AutoAR phase-key replay timed out") from exc
        if proc.returncode != 0:
            raise RuntimeError(
                f"AutoAR phase-key replay failed ({proc.returncode}): "
                f"{proc.stderr.strip()[-2000:]}"
            )
        try:
            result = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("AutoAR phase-key replay returned invalid JSON") from exc
    if (
        not isinstance(result, dict)
        or result.get("go_version") != GO_TOOLCHAIN
        or result.get("weakened") is not weakened
        or not isinstance(result.get("results"), list)
        or len(result["results"]) != len(values)
    ):
        raise RuntimeError("AutoAR phase-key replay returned invalid or unexpected output")
    return result


def mutation_reproduces_path_escape(witness: dict[str, Any]) -> bool:
    """A real weakened-source replay must escape the fixed phase-log root."""
    if witness.get("path_character") != ".":
        return False
    result = run_sanitizer(["../../outside"], weakened=True)["results"][0]
    return (
        result["component"] == "../../outside"
        and result["inside"] is False
        and result["relative"].startswith("..")
    )


__all__ = [
    "CALLER_FILE",
    "CALLER_SHA256",
    "GO_TOOLCHAIN",
    "PIN",
    "REPOSITORY",
    "ROUTES_FILE",
    "ROUTES_SHA256",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "RESULTS_FILE",
    "RESULTS_SHA256",
    "mutation_reproduces_path_escape",
    "run_sanitizer",
    "verify_source_evidence",
]
