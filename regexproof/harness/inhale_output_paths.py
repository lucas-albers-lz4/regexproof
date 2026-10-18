"""Inhale's URL-derived download paths must stay within the configured output root."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Contains, Length, Not, PrefixOf, String, StringVal, SubString

from regexproof.groundtruth.inhale_directory_replay import (
    MUTATED_PATH_PATTERN,
    directory_url_output_escapes_configured_root,
    file_url_output_escapes_configured_root,
    widened_file_path_mutation_replays,
)
from regexproof.harness.core import prop

PIN = "889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8"
FAMILY = "IH-inhale-output-path-confinement"
PATTERN = r"https?://"
MUTATED_PATTERN = MUTATED_PATH_PATTERN
FILE_SITE = (
    f"netspooky/inhale@{PIN}:"
    "iModules/rDownload.py:111:url"
)
DIRECTORY_SITE = (
    f"netspooky/inhale@{PIN}:"
    "iModules/rDownload.py:129:url"
)
_CALIBRATION = Path(__file__).resolve().parents[2] / "properties/calibration/2026-10-15-p2-inhale-source-review"
FILE_CONTRACT = json.loads((_CALIBRATION / "file-contract.json").read_text(encoding="utf-8"))
DIRECTORY_CONTRACT = json.loads((_CALIBRATION / "directory-contract.json").read_text(encoding="utf-8"))


@prop(
    "IH-inhale-file-url-output-root-confinement",
    "The concrete printable-ASCII HTTPS URL witness; stripping the exact "
    "https?:// prefix leaves a URL-derived relative path containing /../../. "
    "Ground truth resolves the pinned getSingleFile destination against a "
    "temporary -o output directory.",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    ground_truth=file_url_output_escapes_configured_root,
    contract=FILE_CONTRACT,
)
def inhale_file_url_output_root_confinement():
    url = String("file_url")
    stripped = SubString(url, 8, Length(url) - 8)
    witness = StringVal("https://downloads.example/../../escape.bin")
    return [url == witness], And(
        PrefixOf(StringVal("https://"), url),
        Contains(stripped, StringVal("/../../")),
    )


@prop(
    "IH-inhale-directory-url-output-root-confinement",
    "The concrete printable-ASCII HTTPS URL witness; stripping the exact "
    "https?:// prefix leaves a URL-derived relative path containing /../../. "
    "Ground truth resolves the pinned parseDir destination against a "
    "temporary -o output directory.",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    ground_truth=directory_url_output_escapes_configured_root,
    contract=DIRECTORY_CONTRACT,
)
def inhale_directory_url_output_root_confinement():
    url = String("directory_url")
    stripped = SubString(url, 8, Length(url) - 8)
    witness = StringVal("https://downloads.example/../../directory.bin")
    return [url == witness], And(
        PrefixOf(StringVal("https://"), url),
        Contains(stripped, StringVal("/../../")),
    )


@prop(
    "IH-inhale-weakened-url-strip-traversal-mutation",
    "MUTATION GUARD: weakening the scheme-only substitution to strip the "
    "authority as well changes the one-parent URL from an in-root destination "
    "to a destination outside -o.",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=MUTATED_PATTERN,
    pattern_flags="",
    ground_truth=widened_file_path_mutation_replays,
)
def inhale_weakened_url_strip_exposes_parent_traversal():
    url = String("url")
    witness = StringVal("https://downloads.example/../escape.bin")
    original_tail = SubString(url, 8, Length(url) - 8)
    weakened_tail = SubString(url, 26, Length(url) - 26)
    return [url == witness], And(
        Not(PrefixOf(StringVal("../"), original_tail)),
        PrefixOf(StringVal("../"), weakened_tail),
    )


__all__ = [
    "DIRECTORY_CONTRACT", "DIRECTORY_SITE", "FAMILY", "FILE_CONTRACT",
    "FILE_SITE", "MUTATED_PATTERN", "PATTERN", "PIN",
]
