"""Doberman-Core Python command-boundary conversion wave."""

from __future__ import annotations

import json
import re
from pathlib import Path

import jsonschema
import pytest

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage, run_one
import regexproof.harness.doberman as doberman  # noqa: F401 — register family
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
FAMILY = "PY-doberman-command-exec"
PRODUCT_NAMES = (
    "PY-doberman-windows-root-token",
    "PY-doberman-disk-wipe-token",
)


def test_doberman_family_is_registered_and_guarded():
    assert all(name in REGISTRY for name in PRODUCT_NAMES)
    assert all(REGISTRY[name]["family"] == FAMILY for name in PRODUCT_NAMES)
    assert all(product_reportable(REGISTRY[name]) for name in PRODUCT_NAMES)
    guards = [
        name
        for name, entry in REGISTRY.items()
        if entry["family"] == FAMILY and entry["kind"] == "mutation_guard"
    ]
    assert len(guards) == 2
    assert check_mutation_coverage() == 0


def test_doberman_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"


def test_doberman_proofs_and_mutation_guards_pass():
    for name in PRODUCT_NAMES:
        result = run_one(name, REGISTRY[name], require_ground_truth=True)
        assert result["ok"] is True, result
        assert result["result"] == "unsat"
    for name in (
        "PY-doberman-mutated-windows-root-token",
        "PY-doberman-mutated-disk-wipe-token",
    ):
        result = run_one(name, REGISTRY[name], require_ground_truth=True)
        assert result["ok"] is True, result
        assert result["result"] == "sat"


@pytest.mark.parametrize(
    "value,expected",
    [
        ("C:", True),
        ("C:/", True),
        ("C:\\", True),
        ("C:*", True),
        ("C:/*", True),
        ("C:\\*", True),
        ("C:/tmp", False),
        ("C:;", False),
        ("/", False),
    ],
)
def test_windows_root_replay_uses_python_engine(value: str, expected: bool):
    source = re.compile(r"^[A-Za-z]:[/\\]?(\*)?$")
    assert bool(source.match(value)) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ("format", True),
        ("FORMAT-VOLUME", True),
        ("mkfs.ext4", True),
        ("mkfs.", False),
        ("xformat", False),
        ("format;rm", False),
        ("format extra", False),
    ],
)
def test_disk_wipe_replay_uses_python_engine(value: str, expected: bool):
    source = re.compile(
        r"^(?:mkfs(?:\.\w+)?|shred|wipefs|format-volume|clear-disk|format)$",
        re.IGNORECASE,
    )
    assert bool(source.match(value)) is expected


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "Doberman-Core_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert {row["name"] for row in rows} == set(PRODUCT_NAMES)
    for row in rows:
        assert row["family"] == FAMILY
        assert row["corpus"] == "Doberman-Core"
        assert row["wave_id"] == "doberman_w1"
        assert row["idiom_bucket"] == "command-execution"
        assert row["product_reportable"] is True


def test_wave_closeout_records_deferred_candidates():
    path = ROOT / "properties" / "generated" / "Doberman-Core_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "15 read → 2 asked" in text
    assert "_SUBSTITUTION" in text
    assert "_SUSPECTED_EGRESS_VERB" in text
