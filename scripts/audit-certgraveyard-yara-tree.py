#!/usr/bin/env python3
"""Inventory YARA rule files and regex literals at the pinned intake commit."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

EXPECTED_PIN = "d965ff32860bef8010f7eb1e7df7b9ea1762d2d4"
RULE_SUFFIXES = {".yar", ".yara"}
# YARA regex literals appear in string assignments (``= /.../``) and in
# conditions using ``matches /.../``. Scan both forms across every pinned
# rule file; whitespace in the second form may include newlines.
REGEX_ASSIGNMENT = re.compile(rb"=\s*/")
REGEX_MATCHES = re.compile(rb"\bmatches\s*/", re.IGNORECASE)


def _git(repo: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
    )
    return result.stdout


def _assert_tracked_files_match_head(repo: Path) -> None:
    result = subprocess.run(
        ["git", "-C", str(repo), "diff", "--quiet", "HEAD", "--"],
        capture_output=True,
        timeout=30,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit("candidate checkout has tracked changes from its pinned HEAD")


def audit(repo: Path) -> dict[str, Any]:
    repo = repo.expanduser().resolve()
    pin = str(_git(repo, "rev-parse", "HEAD")).strip()
    if pin != EXPECTED_PIN:
        raise SystemExit(f"source pin mismatch: expected {EXPECTED_PIN}, found {pin}")
    _assert_tracked_files_match_head(repo)

    paths_raw = _git(
        repo,
        "ls-tree",
        "-r",
        "-t",
        "-z",
        "--format=%(objecttype) %(path)",
        "HEAD",
        binary=True,
    )
    assert isinstance(paths_raw, bytes)
    entries = [item for item in paths_raw.split(b"\0") if item]
    decoded = [item.decode("utf-8", errors="surrogateescape") for item in entries]
    objects = [line.split(" ", 1) for line in decoded]
    blobs = [Path(path) for kind, path in objects if kind == "blob"]
    tree_nodes = sum(kind == "tree" for kind, _ in objects)
    rule_paths = sorted(path for path in blobs if path.suffix.lower() in RULE_SUFFIXES)
    bytes_total = 0
    assignment_hits: list[str] = []
    matches_hits: list[str] = []
    for relative in rule_paths:
        content = (repo / relative).read_bytes()
        bytes_total += len(content)
        for pattern, hits in (
            (REGEX_ASSIGNMENT, assignment_hits),
            (REGEX_MATCHES, matches_hits),
        ):
            for match in pattern.finditer(content):
                line = content.count(b"\n", 0, match.start()) + 1
                hits.append(f"{relative.as_posix()}:{line}")

    license_file = next(
        (path for path in blobs if path.name.lower() in {"license", "license.md", "license.txt"}),
        None,
    )
    license_text = (
        (repo / license_file).read_text(encoding="utf-8")
        if license_file
        else ""
    )
    return {
        "schema_version": "1",
        "corpus": "tjnel/certgraveyard_yara",
        "pin": pin,
        "tree_files": len(blobs),
        "tree_nodes": tree_nodes,
        "recursive_entries": len(objects),
        "rule_files": len(rule_paths),
        "yar_files": sum(path.suffix.lower() == ".yar" for path in rule_paths),
        "yara_files": sum(path.suffix.lower() == ".yara" for path in rule_paths),
        "rule_bytes": bytes_total,
        "regex_assignment_pattern": REGEX_ASSIGNMENT.pattern.decode("ascii"),
        "regex_assignment_hits": len(assignment_hits),
        "regex_assignment_hit_sites": assignment_hits,
        "regex_matches_pattern": REGEX_MATCHES.pattern.decode("ascii"),
        "regex_matches_hits": len(matches_hits),
        "regex_matches_hit_sites": matches_hits,
        "regex_literal_hits": len(assignment_hits) + len(matches_hits),
        "license_file": license_file.as_posix() if license_file else None,
        "license_summary": "MIT" if license_text.startswith("MIT License") else "not confirmed",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="exact-pin candidate checkout")
    parser.add_argument("--output", type=Path, help="write inventory JSON to this path")
    args = parser.parse_args(argv)
    result = audit(args.repo)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
