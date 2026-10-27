"""F5 (#553 close-out): emit-conversion-ndjson SHAPE fail-closed."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_emit_module():
    spec = importlib.util.spec_from_file_location(
        "emit_conversion_ndjson",
        ROOT / "scripts" / "emit-conversion-ndjson.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_entry() -> dict:
    return {
        "kind": "property",
        "domain": "test domain",
        "family": "OW-packages",
        "contract": {
            "guarantee": "no semicolon in accepted strings",
            "declared_domain": "test domain",
            "provenance": "human",
        },
    }


def test_row_from_run_missing_shape_aborts():
    mod = _load_emit_module()
    name = "OW-packages-not-in-shape-map"
    entry = _minimal_entry()
    result = {
        "result": "unsat",
        "domain": "test domain",
        "ground_truth": "verified",
        "engine_versions": {"python": "3.12.0", "z3": "5.0.0"},
    }
    with pytest.raises(SystemExit, match="missing SHAPE entry"):
        mod.row_from_run(name, entry, result, corpus="openwrt_packages")


def test_row_from_run_missing_engine_versions_aborts():
    mod = _load_emit_module()
    name = "OW-packages-hostname-no-semicolon"
    entry = _minimal_entry()
    result = {
        "result": "unsat",
        "domain": "test domain",
        "ground_truth": "verified",
    }
    with pytest.raises(SystemExit, match="missing engine_versions"):
        mod.row_from_run(name, entry, result, corpus="openwrt_packages")


def test_row_from_run_rejects_placeholder_engine_versions():
    mod = _load_emit_module()
    name = "OW-packages-hostname-no-semicolon"
    entry = _minimal_entry()
    result = {
        "result": "unsat",
        "domain": "test domain",
        "ground_truth": "verified",
        "engine_versions": {"python": "3.12.0", "z3": "?"},
    }
    with pytest.raises(SystemExit, match="missing engine_versions"):
        mod.row_from_run(name, entry, result, corpus="openwrt_packages")


def test_row_context_override_assigns_helper_image_wave():
    """#648: the reclassified property lands in its own wave, not wave 1."""
    mod = _load_emit_module()
    wave, bucket, overridden = mod.resolve_row_context(
        "FC-forge-cli-sensitive-env-helper-redacts",
        "forge-cli_w1",
        "secret-redaction",
    )
    assert (wave, bucket) == ("forge-cli_helper_image", "helper-image")
    assert overridden is True


def test_row_context_override_does_not_leak_to_sibling_properties():
    """A later forge-cli wave must keep the CLI defaults for every other row."""
    mod = _load_emit_module()
    wave, bucket, overridden = mod.resolve_row_context(
        "FC-forge-cli-url-password-no-space",
        "forge-cli_w2",
        "secret-redaction",
    )
    assert (wave, bucket) == ("forge-cli_w2", "secret-redaction")
    assert overridden is False
