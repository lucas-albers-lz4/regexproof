"""Exact-pin replay for YARA author metadata entering Malcontent Markdown."""

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
PATTERN = r"(.*?) \((http.*)\)"
WITNESS = "Name (https://example.invalid/)[click](https://attacker.invalid)"
EXPECTED_CAPTURE_URL = "https://example.invalid/)[click](https://attacker.invalid"
EXPECTED_SECOND_LINK = "[click](https://attacker.invalid)"

GO_REPLAY = Path(__file__).with_name("malcontent_author_markdown_replay.go")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def _verify_reviewed_sources(root: Path) -> None:
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
        actual = _sha256(committed)
        if actual != expected:
            raise RuntimeError(
                f"source digest for {relative} is {actual}, expected {expected}"
            )
    report_source = (root / SOURCE_FILE).read_text(encoding="utf-8")
    expected_pattern_declaration = r"authorWithURLRe        = regexp.MustCompile(`(.*?) \((http.*)\)`)"
    if expected_pattern_declaration not in report_source:
        raise RuntimeError("pinned authorWithURLRe construction was not found")
    if "RuleAuthorURL = m[2]" not in report_source:
        raise RuntimeError("pinned author capture no longer feeds RuleAuthorURL")
    if "if strings.HasPrefix(b.RuleURL, b.ReferenceURL)" not in report_source:
        raise RuntimeError("pinned reference-URL control flow changed")
    render_source = (root / RENDER_SOURCE_FILE).read_text(encoding="utf-8")
    if 'author = fmt.Sprintf("[%s](%s)", author, k.Behavior.RuleAuthorURL)' not in render_source:
        raise RuntimeError("pinned Markdown author-link sink changed")


def _pkg_config_value(name: str) -> str:
    executable = shutil.which("pkg-config")
    if not executable:
        raise RuntimeError("pkg-config is required to link the YARA-X Go binding")
    result = subprocess.run(
        [executable, "--modversion" if name == "version" else "--variable=libdir", "yara_x_capi"],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
        shell=False,
    )
    return result.stdout.strip()


def run_metadata_replay(author_metadata: str) -> dict[str, Any]:
    """Run the actual pinned YARA-X → report.Generate → Markdown path."""
    if author_metadata != WITNESS:
        raise ValueError("replay input differs from the frozen counterexample witness")
    if not author_metadata.isascii() or "\n" in author_metadata or "\r" in author_metadata:
        raise ValueError("replay input is outside the declared one-line ASCII domain")
    root = source_root()
    _verify_reviewed_sources(root)
    binding_version = _pkg_config_value("version")
    if binding_version != "1.19.0":
        raise RuntimeError(f"YARA-X C API is {binding_version}, expected 1.19.0")
    go_version = subprocess.run(
        ["go", "version"], check=True, capture_output=True, text=True,
        timeout=10, shell=False,
    ).stdout.strip()
    if not re.search(r"github\.com/VirusTotal/yara-x/go v1\.19\.0(?:\s|$)", (root / "go.mod").read_text(encoding="utf-8")):
        raise RuntimeError("pinned Malcontent go.mod no longer selects YARA-X Go v1.19.0")

    env = os.environ.copy()
    env["MALCONTENT_AUTHOR_METADATA"] = author_metadata
    result = subprocess.run(
        ["go", "run", str(GO_REPLAY)],
        cwd=root,
        env=env,
        check=False,
        capture_output=True,
        text=True,
        timeout=180,
        shell=False,
    )
    if result.returncode:
        raise RuntimeError(
            "pinned Malcontent metadata replay failed "
            f"({result.returncode}): {result.stderr.strip()}"
        )
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Go replay did not emit a single JSON result") from exc
    if not isinstance(output, dict):
        raise RuntimeError("Go replay result must be an object")
    if (
        output.get("rule_name") != "regexproof_author_metadata_replay"
        or output.get("author") != "Name"
        or output.get("author_url") != EXPECTED_CAPTURE_URL
        or output.get("reference_url") != "https://reference.invalid"
        or EXPECTED_SECOND_LINK not in output.get("markdown", "")
        or output.get("input_sha256") != _sha256(author_metadata.encode("ascii"))
    ):
        raise RuntimeError("pinned product output did not reproduce the authored Markdown link")
    return {
        **output,
        "checkout_root": str(root),
        "source_pin": PIN,
        "repository_url": REPOSITORY,
        "source_file_sha256": SOURCE_SHA256,
        "renderer_source_file_sha256": RENDER_SOURCE_SHA256,
        "go_version": go_version,
        "yara_x_go_binding_version": "1.19.0",
        "yara_x_c_api_version": binding_version,
        "replay_source_sha256": _sha256(GO_REPLAY.read_bytes()),
    }


def ground_truth_reproduces(witness: dict[str, Any]) -> bool:
    """Harness callback; return true only for the fully replayed witness."""
    try:
        run_metadata_replay(str(witness.get("author_metadata") or ""))
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError):
        return False
    return True


__all__ = [
    "EXPECTED_CAPTURE_URL",
    "EXPECTED_SECOND_LINK",
    "PATTERN",
    "PIN",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "WITNESS",
    "ground_truth_reproduces",
    "run_metadata_replay",
]
