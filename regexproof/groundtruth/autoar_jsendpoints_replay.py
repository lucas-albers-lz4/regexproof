"""Replay AutoAR's pinned JavaScript endpoint extractor under Go 1.25.7."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from regexproof.groundtruth.autoar_html_escape_replay import source_root

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
SOURCE_FILE = "internal/scanner/jsendpoints/jsendpoints.go"
SOURCE_SHA256 = "e9c03be11f7aab2a4310ea4944de5620e500f2400b13e22a3e1ea5b16745c549"
GO_TOOLCHAIN = "go1.25.7"
_URL_ASSIGNMENT_PREFIX = b"(?:url|href|endpoint|baseURL|apiUrl|apiBase|API_URL|BASE_URL)"
_OLD_CAPTURE = rb"""([^"'\x60\s]{4,200})"""
_WEAK_CAPTURE = rb"""([^'\x60\s]{4,200})"""


def _source_bytes() -> tuple[Path, bytes]:
    root = source_root()
    path = root / SOURCE_FILE
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned AutoAR source is missing or a symlink: {path}")
    source = path.read_bytes()
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{SOURCE_FILE}"],
        capture_output=True,
        check=True,
        timeout=30,
        shell=False,
    ).stdout
    if source != committed:
        raise RuntimeError("AutoAR jsendpoints source bytes differ from the pinned commit")
    digest = hashlib.sha256(source).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"AutoAR jsendpoints digest is {digest}, expected {SOURCE_SHA256}")
    return root, source


def _declaration(source: bytes, *, allow_quote: bool) -> bytes:
    start = source.find(b"var endpointRegexes = []*regexp.Regexp{")
    end_marker = b"\n}\n\n// Run extracts API endpoints"
    end = source.find(end_marker, start)
    if start < 0 or end < 0:
        raise RuntimeError("pinned source no longer has the endpointRegexes declaration")
    declaration = source[start : end + len(b"\n}")]
    matching = [
        line
        for line in declaration.splitlines()
        if _URL_ASSIGNMENT_PREFIX in line
    ]
    if len(matching) != 1 or matching[0].count(_OLD_CAPTURE) != 1:
        raise RuntimeError("cannot uniquely locate the pinned URL-assignment capture class")
    if not allow_quote:
        return declaration
    mutated_line = matching[0].replace(_OLD_CAPTURE, _WEAK_CAPTURE, 1)
    return declaration.replace(matching[0], mutated_line, 1)


def _function(source: bytes, name: str, next_marker: bytes) -> bytes:
    start = source.find(f"func {name}(".encode("ascii"))
    if start < 0:
        raise RuntimeError(f"pinned source is missing {name}")
    end = source.find(next_marker, start)
    if end < 0:
        raise RuntimeError(f"cannot bound pinned function {name}")
    return source[start : end + len(b"\n}")]


def _wrapper(source: bytes, *, allow_quote: bool) -> str:
    declaration = _declaration(source, allow_quote=allow_quote).decode("utf-8")
    extract = _function(source, "extractEndpoints", b"\n}\n\n// isNoise").decode("utf-8")
    noise = _function(source, "isNoise", b"\n}\n\nfunc downloadFile").decode("utf-8")
    return f'''package main

import (
    "encoding/json"
    "os"
    "regexp"
    "runtime"
    "strings"
)

{declaration}

{extract}

{noise}

type request struct {{
    Contents []string `json:"contents"`
    SourceURL string `json:"source_url"`
}}

type response struct {{
    GoVersion string `json:"go_version"`
    Outputs [][]string `json:"outputs"`
}}

func main() {{
    var input request
    if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {{
        panic(err)
    }}
    output := response{{GoVersion: runtime.Version(), Outputs: make([][]string, 0, len(input.Contents))}}
    for _, content := range input.Contents {{
        row := extractEndpoints(content, input.SourceURL)
        if row == nil {{
            row = []string{{}}
        }}
        output.Outputs = append(output.Outputs, row)
    }}
    if err := json.NewEncoder(os.Stdout).Encode(output); err != nil {{
        panic(err)
    }}
}}
'''


def run_extractor(
    contents: list[str], *, allow_quote: bool = False
) -> tuple[list[list[str]], str]:
    """Compile the exact pinned declarations/functions with their Go runtime."""
    if not shutil.which("go"):
        raise RuntimeError("Go is required for AutoAR's RE2 product replay")
    _root, source = _source_bytes()
    with tempfile.TemporaryDirectory(prefix="regexproof-autoar-jsendpoints-") as temp:
        work = Path(temp)
        (work / "go.mod").write_text(
            "module regexproof-autoar-jsendpoints-replay\n\ngo 1.25.7\n",
            encoding="utf-8",
        )
        (work / "main.go").write_text(
            _wrapper(source, allow_quote=allow_quote), encoding="utf-8"
        )
        env = os.environ.copy()
        env["GOTOOLCHAIN"] = GO_TOOLCHAIN
        try:
            proc = subprocess.run(
                ["go", "run", "."],
                cwd=work,
                input=json.dumps(
                    {
                        "contents": contents,
                        "source_url": "https://autotarget.invalid/app.js",
                    },
                    ensure_ascii=True,
                ),
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
                shell=False,
                env=env,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("AutoAR Go endpoint replay timed out") from exc
        if proc.returncode != 0:
            raise RuntimeError(
                f"AutoAR Go endpoint replay failed ({proc.returncode}): "
                f"{proc.stderr.strip()[-2000:]}"
            )
        try:
            result = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("AutoAR Go endpoint replay returned invalid JSON") from exc
    outputs = result.get("outputs")
    version = result.get("go_version")
    if (
        not isinstance(outputs, list)
        or len(outputs) != len(contents)
        or any(
            not isinstance(row, list)
            or any(not isinstance(value, str) for value in row)
            for row in outputs
        )
    ):
        raise RuntimeError("AutoAR Go endpoint replay returned an invalid output vector")
    if version != GO_TOOLCHAIN:
        raise RuntimeError(f"AutoAR replay used {version!r}, expected {GO_TOOLCHAIN}")
    return outputs, version


def mutation_reproduces_quote(witness: dict) -> bool:
    """A real weakened-source replay must leak its closing quote into a result."""
    if witness.get("capture_character") != '"':
        return False
    outputs, _ = run_extractor(
        ['const apiUrl = "service/v1/users";'], allow_quote=True
    )
    return len(outputs) == 1 and any('"' in endpoint for endpoint in outputs[0])


__all__ = ["GO_TOOLCHAIN", "PIN", "SOURCE_FILE", "SOURCE_SHA256", "run_extractor"]
