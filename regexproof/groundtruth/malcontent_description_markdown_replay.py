"""Exact-pin replay for third-party YARA descriptions entering Markdown."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from regexproof.groundtruth.malcontent_replay import PIN, source_root

REPOSITORY = "https://github.com/chainguard-dev/malcontent"
SOURCE_FILE = "pkg/report/report.go"
SOURCE_SHA256 = "bb3ab2bc50fb835f4add14d8c1f6b71140335313c016575bd55eef224fe690de"
RENDER_SOURCE_FILE = "pkg/render/markdown.go"
RENDER_SOURCE_SHA256 = "77b3123a08f5a3e73f1cbe303278067cb05b8e5ee14643726824d26bce8f4035"
PATTERN = r"Detection patterns for the tool '(.*)' taken from the ThreatHunting-Keywords github project"
WITNESS = (
    "Detection patterns for the tool 'Benign' | "
    "[click](https://attacker.invalid)' taken from the ThreatHunting-Keywords github project"
)
EXPECTED_DESCRIPTION = "references 'Benign' | [click](https://attacker.invalid)' tool"
EXPECTED_LINK = "[click](https://attacker.invalid)"
GO_REPLAY = Path(__file__).with_name("malcontent_description_markdown_replay.go")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True,
        text=not binary, timeout=30, shell=False,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_source(root: Path) -> None:
    if _git(root, "rev-parse", "HEAD") != PIN:
        raise RuntimeError(f"Malcontent source must be checked out at {PIN}")
    if _git(root, "status", "--porcelain"):
        raise RuntimeError("Malcontent source must be a clean pinned checkout")
    for relative, expected in (
        (SOURCE_FILE, SOURCE_SHA256),
        (RENDER_SOURCE_FILE, RENDER_SOURCE_SHA256),
    ):
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"pinned source file is missing or a symlink: {path}")
        committed = _git(root, "show", f"{PIN}:{relative}", binary=True)
        if not isinstance(committed, bytes) or path.read_bytes() != committed:
            raise RuntimeError(f"working source differs from {PIN}:{relative}")
        if _sha256(committed) != expected:
            raise RuntimeError(f"source digest changed for {relative}")
    report_source = (root / SOURCE_FILE).read_text(encoding="utf-8")
    if "threatHuntingKeywordRe = regexp.MustCompile(`" + PATTERN + "`)" not in report_source:
        raise RuntimeError("pinned threatHuntingKeywordRe construction was not found")
    if "desc := mungeDescription(v)" not in report_source:
        raise RuntimeError("pinned YARA description metadata call path changed")
    if "return fmt.Sprintf(\"references '%s' tool\", m[1])" not in report_source:
        raise RuntimeError("pinned description interpolation changed")
    render_source = (root / RENDER_SOURCE_FILE).read_text(encoding="utf-8")
    if "// sanitizeMarkdown escapes characters that could be used for markdown injection." not in render_source:
        raise RuntimeError("pinned Markdown sanitizer documentation changed")
    if "desc := k.Behavior.Description" not in render_source or "table.Bulk(data)" not in render_source:
        raise RuntimeError("pinned Markdown description-to-table path changed")


def _pkg_config_value(option: str) -> str:
    executable = shutil.which("pkg-config")
    if not executable:
        raise RuntimeError("pkg-config is required to link the YARA-X Go binding")
    flag = "--modversion" if option == "version" else "--variable=libdir"
    result = subprocess.run(
        [executable, flag, "yara_x_capi"], check=True, capture_output=True,
        text=True, timeout=10, shell=False,
    )
    return result.stdout.strip()


def run_description_replay(description: str) -> dict[str, Any]:
    """Run YARA-X → report.Generate → the pinned Markdown renderer."""
    if description != WITNESS:
        raise ValueError("replay input differs from the frozen description witness")
    if not description.isascii() or "\n" in description or "\r" in description:
        raise ValueError("description is outside the declared one-line ASCII domain")
    root = source_root()
    _verify_source(root)
    if _pkg_config_value("version") != "1.19.0":
        raise RuntimeError("YARA-X C API version is not the pinned 1.19.0")
    go_version = subprocess.run(
        ["go", "version"], check=True, capture_output=True, text=True,
        timeout=10, shell=False,
    ).stdout.strip()
    go_mod = (root / "go.mod").read_text(encoding="utf-8")
    if not re.search(r"github\.com/VirusTotal/yara-x/go v1\.19\.0(?:\s|$)", go_mod):
        raise RuntimeError("pinned go.mod no longer selects YARA-X Go v1.19.0")
    env = os.environ.copy()
    env["MALCONTENT_DESCRIPTION_METADATA"] = description
    result = subprocess.run(
        ["go", "run", str(GO_REPLAY)], cwd=root, env=env, check=False,
        capture_output=True, text=True, timeout=180, shell=False,
    )
    if result.returncode:
        raise RuntimeError(f"pinned product description replay failed: {result.stderr.strip()}")
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Go description replay did not emit one JSON object") from exc
    markdown = output.get("markdown", "") if isinstance(output, dict) else ""
    if (
        output.get("rule_name") != "regexproof_description_metadata_replay"
        or output.get("description") != EXPECTED_DESCRIPTION
        or EXPECTED_LINK not in markdown
        or " | [click](https://attacker.invalid)' tool |" not in markdown
        or output.get("input_sha256") != _sha256(description.encode("ascii"))
    ):
        raise RuntimeError("pinned product output did not reproduce the Markdown link and raw table delimiter")
    return {
        **output,
        "checkout_root": str(root),
        "source_pin": PIN,
        "repository_url": REPOSITORY,
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_SHA256,
        "renderer_source_file": RENDER_SOURCE_FILE,
        "renderer_source_file_sha256": RENDER_SOURCE_SHA256,
        "go_version": go_version,
        "yara_x_go_binding_version": "1.19.0",
        "yara_x_c_api_version": _pkg_config_value("version"),
        "replay_source_sha256": _sha256(GO_REPLAY.read_bytes()),
    }


def ground_truth_reproduces(witness: dict[str, Any]) -> bool:
    try:
        run_description_replay(str(witness.get("description_metadata") or ""))
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError):
        return False
    return True


__all__ = [
    "EXPECTED_DESCRIPTION", "EXPECTED_LINK", "PATTERN", "PIN", "REPOSITORY",
    "SOURCE_FILE", "SOURCE_SHA256", "WITNESS", "ground_truth_reproduces",
    "run_description_replay",
]
