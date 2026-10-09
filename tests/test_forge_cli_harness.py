"""Forge CLI conversion-wave registration and sensitivity checks."""

from __future__ import annotations

import json
import re
from itertools import product
from pathlib import Path

import jsonschema
from z3 import AllChar, Concat, InRe, Length, Re, Solver, Star, String, StringVal, sat

from regexproof.harness import REGISTRY, check_mutation_coverage, run_one
from regexproof.harness.contract import product_reportable
from regexproof.harness.forge_cli import (
    DMM_VALUE_CHAR,
    DMM_VALUE_PATTERN,
    ENV_API_POLICY_KEYS,
    ENV_MATCH,
    ENV_PATTERN,
    ENV_POLICY_KEYS,
    ENV_PRODUCT,
    ENV_WEAKENED_PATTERN,
    JAAS_MATCH,
    JAAS_PATTERN,
    JAAS_PRODUCT,
    LLM_USERINFO_CHAR,
    LLM_USERINFO_PATTERN,
    URL_PASSWORD_CHAR,
    URL_PASSWORD_PATTERN,
)
from regexproof.schemas import load_schema


FAMILY = "FC-forge-cli"
ROOT = Path(__file__).resolve().parents[1]
PRODUCT_NAMES = (
    "FC-forge-cli-url-password-no-space",
    "FC-forge-cli-dmm-value-no-semicolon",
    "FC-forge-cli-llm-userinfo-no-at",
    "FC-forge-cli-jaas-escaped-quote-covered",
    "FC-forge-cli-sensitive-env-key-covered",
)


def test_forge_cli_product_contracts_are_registered():
    entries = [entry for entry in REGISTRY.values() if entry["family"] == FAMILY]
    assert len(entries) == 7
    properties = [entry for entry in entries if entry["kind"] == "property"]
    assert len(properties) == 5
    assert all(entry["contract"]["provenance"] == "human" for entry in properties)
    assert all(entry["input_domain"] == "ascii" for entry in entries)
    schema = load_schema("property_contract.schema.json")
    for entry in properties:
        jsonschema.validate(instance=entry["contract"], schema=schema)
        assert product_reportable(entry) is True
    assert REGISTRY["FC-forge-cli-llm-userinfo-no-at"]["contract"]["site"].endswith(
        "providers.py:287:LlmConfig.redacted_endpoint"
    )
    assert "FC-forge-cli-sensitive-env-helper-redacts" not in REGISTRY


def test_forge_cli_properties_hold_and_mutation_guard_flips():
    for name in sorted(REGISTRY):
        if REGISTRY[name]["family"] != FAMILY:
            continue
        result = run_one(name, REGISTRY[name], require_ground_truth=True)
        assert result["result"] == (
            "sat" if REGISTRY[name]["kind"] == "mutation_guard" else "unsat"
        )
        assert result["not_proven"] is False
        if REGISTRY[name]["kind"] == "mutation_guard":
            if REGISTRY[name]["ground_truth"] is None:
                assert result["ground_truth"] == "mutation-guard-sat-expected"
                if name == "FC-forge-cli-mutated-sensitive-env-api-key":
                    from regexproof.groundtruth.forge_cli_replay import (
                        redaction_mutation_reproduces,
                    )

                    assert result["witness"]["s"].lower() in ENV_API_POLICY_KEYS
                    assert redaction_mutation_reproduces(
                        result["witness"]["s"], ENV_WEAKENED_PATTERN
                    )
            else:
                assert result["ground_truth"] == "reproduced"
                assert result["witness"]["s"].lower() in ENV_API_POLICY_KEYS


def test_forge_cli_family_has_mutation_coverage():
    assert check_mutation_coverage() == 0


def test_product_match_are_not_aliases():
    assert JAAS_PRODUCT is not JAAS_MATCH
    assert ENV_PRODUCT is not ENV_MATCH


def test_source_alphabets_agree_with_cpython_re():
    cases = (
        (URL_PASSWORD_PATTERN, URL_PASSWORD_CHAR, " "),
        (DMM_VALUE_PATTERN, DMM_VALUE_CHAR, ";"),
        (LLM_USERINFO_PATTERN, LLM_USERINFO_CHAR, "@"),
    )
    for pattern, alphabet, forbidden in cases:
        compiled = re.compile(pattern)
        for code in range(0x20, 0x7F):
            token = chr(code)
            source_ok = compiled.fullmatch(token) is not None
            solver = Solver()
            char = String("c")
            solver.add(InRe(char, alphabet), Length(char) == 1, char == StringVal(token))
            in_mirror = solver.check() == sat
            assert in_mirror is source_ok, (pattern, repr(token), in_mirror, source_ok)
            if token == forbidden:
                assert source_ok is False


def _case_variants(text: str):
    choices = [(char.lower(), char.upper()) for char in text if char.isalpha()]
    positions = [i for i, char in enumerate(text) if char.isalpha()]
    for variant in product(*choices):
        chars = list(text)
        for index, char in zip(positions, variant):
            chars[index] = char
        yield "".join(chars)


def _env_mirror_search():
    any_char = AllChar(Re("").sort())
    return Concat(Star(any_char), ENV_MATCH, Star(any_char))


def test_env_policy_keys_match_source_regex():
    compiled = re.compile(ENV_PATTERN)
    for key in ENV_POLICY_KEYS:
        assert compiled.search(key), key
        assert compiled.search(key.upper()), key


def test_pinned_env_renderer_redacts_every_documented_case_variant():
    from regexproof.groundtruth.forge_cli_replay import (
        product_regex_pattern,
        render_command,
        renderer_source,
        source_root,
    )

    assert renderer_source().is_relative_to(source_root())
    assert source_root().is_dir()  # source_root validates HEAD against PIN
    assert product_regex_pattern() == ENV_PATTERN
    source = re.compile(product_regex_pattern())
    key_symbol = String("key")
    solver = Solver()
    solver.add(InRe(key_symbol, _env_mirror_search()))

    checked = set()
    for base_key in ENV_POLICY_KEYS:
        for key in _case_variants(base_key):
            if key in checked:
                continue
            checked.add(key)
            assert source.search(key), key
            solver.push()
            solver.add(key_symbol == StringVal(key))
            mirror_matches = solver.check() == sat
            solver.pop()
            assert mirror_matches, key
            for flag in ("-e", "--env"):
                command = ["dbt", "run", flag, f"{key}=CLEAR_SENTINEL"]
                expected = f"dbt run {flag} {key}=<redacted>"
                actual = render_command(command)
                assert actual == expected, (key, flag, actual, expected)
                assert "CLEAR_SENTINEL" not in actual
    assert len(checked) == 5680


def test_env_search_differential_and_exact_helper_images():
    from regexproof.groundtruth.forge_cli_replay import render_command

    source = re.compile(ENV_PATTERN)
    solver = Solver()
    key_symbol = String("key")
    solver.add(InRe(key_symbol, _env_mirror_search()))
    # Expected sensitivity is hand-labeled, independent of both regex mirrors.
    cases = (
        ("ordinary", "plain", False),
        ("API--KEY", "empty", False),
        ("api.key", "delimiter", False),
        ("xApI_KeY_suffix", "left=right;tail", True),
        ("passwordless", "value", True),
        ("AUTHORIZATION", "value", True),
        ("API_KEY", "", True),
        ("Secret", "left=middle;right\n", True),
        ("TOKEN\n", "terminal\n", True),
        ("\nprivate-key", "value", True),
    )
    for key, value, sensitive in cases:
        source_matches = source.search(key) is not None
        solver.push()
        solver.add(key_symbol == StringVal(key))
        mirror_matches = solver.check() == sat
        solver.pop()
        assert mirror_matches is source_matches, key
        assert source_matches is sensitive, key
        rendered = render_command(["dbt", "run", "-e", f"{key}={value}"])
        expected_value = "<redacted>" if sensitive else value
        expected = f"dbt run -e {key}={expected_value}"
        assert rendered == expected, (key, rendered, expected)
        if sensitive and value:
            assert value not in rendered

    repeated = [
        "dbt", "run", "-e", "TOKEN=first", "--env", "token=second",
        "-e", "ordinary=plain",
    ]
    assert render_command(repeated) == (
        "dbt run -e TOKEN=<redacted> --env token=<redacted> -e ordinary=plain"
    )


def test_api_key_mutation_replays_cleartext_against_pinned_helper():
    from regexproof.groundtruth.forge_cli_replay import redaction_mutation_reproduces

    for key in ENV_API_POLICY_KEYS:
        assert redaction_mutation_reproduces(key, ENV_WEAKENED_PATTERN), key


def test_jaas_escaped_quote_product_matches_source_and_not_naive():
    sample = 'sasl.jaas.config="secret\\"value"'
    assert re.compile(JAAS_PATTERN).search(sample)
    naive = re.compile(
        r'(?i)([\w.]{,64}sasl\.jaas\.config"?\s{,8}[:=]\s{,8}")([^"]{,2048})(")\Z'
    )
    assert naive.search(sample) is None


def test_committed_conversion_rows_match_registry():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    schema = load_schema("scanner_finding.schema.json")
    assert [row["name"] for row in rows] == sorted(PRODUCT_NAMES)
    for row in rows:
        jsonschema.validate(instance=row, schema=schema)
        assert row["family"] == FAMILY
        assert row["corpus"] == "forge-cli"
        assert row["wave_id"] == "forge-cli_w1"
        assert row["idiom_bucket"] == "secret-redaction"
        assert row["product_reportable"] is True
        assert row["result"] == "unsat"
        assert row["ground_truth_status"] is None
        assert row["engine_versions"]["z3"].startswith("5.0.")
        assert row["name"] in REGISTRY
        fresh = run_one(row["name"], REGISTRY[row["name"]])
        assert fresh["result"] == row["result"]


def test_wave_closeout_records_scope_and_next_step():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "FC-forge-cli" in text
    assert "secret-redaction" in text
    assert "0 SAT" in text
    assert "providers.py:280" in text
    assert "Concat-identity" in text
    assert "#648 helper-image replay" in text
    assert "all 5,680 ASCII case assignments" in text
    assert "shape 2 proves only" in text
    assert "does not prove the renderer's output image" in text
    assert "exact-witness mutation replay" in text
    assert "no claim is made for arbitrary values" in text.lower()
