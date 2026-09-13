"""Doberman-Core Python command-boundary conversion wave."""

from __future__ import annotations

import json
import shlex
from pathlib import Path

import jsonschema
import pytest
from z3 import InRe, Solver, StringVal, sat

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage, run_one
import regexproof.harness.doberman as doberman
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


def test_doberman_findings_and_mutation_guards_pass():
    for name in PRODUCT_NAMES:
        result = run_one(name, REGISTRY[name], require_ground_truth=True)
        assert result["ok"] is True, result
        assert result["result"] == "sat"
        assert result["ground_truth"] == "reproduced"
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
        ("C:*\n", True),
        ("C:/tmp\n", False),
        ("C:;", False),
        ("/", False),
    ],
)
def test_windows_root_replay_uses_python_engine(value: str, expected: bool):
    source_match = bool(doberman._WINDOWS_ROOT_SOURCE.match(value))
    solver = Solver()
    solver.add(InRe(StringVal(value), doberman.WINDOWS_ROOT_RE))
    mirror_match = solver.check() == sat
    assert source_match is expected
    assert mirror_match is source_match


@pytest.mark.parametrize(
    "value,expected",
    [
        ("format", True),
        ("FORMAT-VOLUME", True),
        ("mkfs.ext4", True),
        ("mkfs.", False),
        ("format\n", True),
        ("xformat", False),
        ("format;rm", False),
        ("format extra", False),
    ],
)
def test_disk_wipe_replay_uses_python_engine(value: str, expected: bool):
    source_match = bool(doberman._DISK_WIPE_SOURCE.match(value))
    solver = Solver()
    solver.add(InRe(StringVal(value), doberman.DISK_WIPE_RE))
    mirror_match = solver.check() == sat
    assert source_match is expected
    assert mirror_match is source_match


def test_terminal_newline_survives_doberman_argument_preprocessing():
    root_token = shlex.split('rm -rf "\'C:\n\'"')[2]
    root_token = root_token.strip().strip("'\"")
    assert root_token == "C:\n"
    assert doberman._WINDOWS_ROOT_SOURCE.match(root_token)

    wipe_token = shlex.split("doberman format 'format\n'")[2]
    assert wipe_token == "format\n"
    assert doberman._DISK_WIPE_SOURCE.match(wipe_token)


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
    assert "Both product properties are SAT" in text
    assert "P:*\\n" in text
    assert "mkfs\\n" in text
    assert "_SUBSTITUTION" in text
    assert "_SUSPECTED_EGRESS_VERB" in text
