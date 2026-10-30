"""Native Java Pattern compiler and replay helper tests (#150)."""

from __future__ import annotations

import subprocess
import sys

import pytest
import z3

from regexproof.batch.compile_records import compile_records
from regexproof.compiler import compile_pattern
from regexproof.compiler.java import HELPER, replay_argv
from regexproof.groundtruth.adapters import ReplayVerdict
from regexproof.groundtruth.adapters import replay as ground_truth_replay


@pytest.fixture(autouse=True)
def require_jdk():
    if subprocess.run(["java", "-version"], capture_output=True, check=False).returncode:
        pytest.skip("JDK with source-file mode is unavailable")


def test_java_dialect_is_registered_and_compiles_subset():
    result = compile_pattern(r"^[A-Z0-9]+", dialect="java", call_kind="fullmatch")
    assert result.encodable
    assert result.dialect == "java"
    assert result.declared_domain == "ascii"
    assert result.meta["engine_versions"]["java"]


def test_java_compile_records_preserve_engine_version(tmp_path):
    records = [
        {
            "regex_id": "a" * 32,
            "pattern": "a+",
            "flags": "",
            "dialect": "java",
            "call_kind": "fullmatch",
            "domain": "ascii",
        }
    ]
    rows = compile_records(
        records,
        lift_inline=False,
        corpus_slug="java-fixture",
        jobs=1,
        cache_dir=tmp_path,
    )
    row, mirror, meta = rows[0]
    assert mirror is not None
    assert row["engine_versions"]["java"] == meta["engine_versions"]["java"]


def test_java_rejects_known_semantic_gaps():
    assert compile_pattern(r"^foo$", dialect="java").unencodable_reason == "java-dollar-anchor"
    intersection = compile_pattern(r"[a-z&&[^aeiou]]", dialect="java")
    assert intersection.unencodable_reason == "class-intersection"
    assert compile_pattern(r"\p{L}+", dialect="java").unencodable_reason == "java-escape"
    assert compile_pattern(r"[\b]", dialect="java").unencodable_reason == "java-escape"
    assert compile_pattern("foo", "m", "java").unencodable_reason == "java-flag"


@pytest.mark.parametrize(
    ("pattern", "accepted", "rejected"),
    [
        (r"[a[b]]", {"a", "b"}, {"]", "e", "q", "_"}),
        (r"[a-d[m-p]]", {"a", "b", "c", "d", "m", "n", "o", "p"}, {"]", "e", "q", "_"}),
        (r"[\d[a-z]]", {"0", "7", "a", "z", "e", "q"}, {"]", "_"}),
    ],
)
def test_java_nested_character_class_union_is_rejected_with_jvm_examples(
    pattern, accepted, rejected
):
    compiled = compile_pattern(pattern, dialect="java", call_kind="fullmatch")
    assert compiled.unencodable_reason == "nested-class"

    # The real Java engine treats nested classes as union; these values make
    # the original parser/mirror discrepancy explicit in the regression.
    for value in accepted | rejected:
        proc = subprocess.run(
            replay_argv(pattern, "", "fullmatch"),
            input=value,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        assert proc.returncode == (0 if value in accepted else 1), (pattern, value)


def test_java_helper_parses_and_replays_with_jdk():
    parse = subprocess.run(
        [sys.executable, str(HELPER), "parse", r"(?i:foo)", ""],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert parse.returncode == 0, parse.stdout + parse.stderr
    assert '"helper":"java-pattern"' in parse.stdout
    parsed = __import__("json").loads(parse.stdout)
    assert parsed["version"]

    replay = subprocess.run(
        replay_argv(r"(?i:foo)", "", "fullmatch"),
        input="FoO",
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert replay.returncode == 0

    rejected = subprocess.run(
        replay_argv(r"(?i:foo)", "", "fullmatch"),
        input="FoO!",
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert rejected.returncode == 1

    gt = ground_truth_replay(r"(?i:foo)", "", "java", "fullmatch", "FoO")
    assert gt.verdict is ReplayVerdict.ACCEPTED
    assert "17." in gt.engine_versions["java"]
    invalid = ground_truth_replay("[", "", "java", "search", "foo")
    assert invalid.verdict is ReplayVerdict.ENGINE_ERROR


@pytest.mark.parametrize(
    ("pattern", "flags", "values"),
    [
        (r"^[A-Z0-9]+", "", ["", "A", "a", "A1", "A!", "A\n"]),
        (r"(?i:foo)", "", ["foo", "FoO", "FOO", "food", "foo\r"]),
        (r"\d{1,2}", "", ["", "0", "12", "123", "²"]),
        (r"\w+", "", ["a", "_", "0", "a!", "é"]),
        (r".", "", ["a", "\n", "\r", "ab"]),
    ],
)
def test_java_mirror_agrees_with_jvm_on_declared_ascii_subset(pattern, flags, values):
    compiled = compile_pattern(pattern, flags, "java", "fullmatch")
    assert compiled.encodable, compiled.unencodable_reason
    for value in values:
        if not value.isascii():
            continue  # outside this compiler's declared ASCII domain
        solver = z3.Solver()
        solver.add(z3.InRe(z3.StringVal(value), compiled.mirror))
        mirror_accepts = solver.check() == z3.sat
        proc = subprocess.run(
            replay_argv(pattern, flags, "fullmatch"),
            input=value,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        assert proc.returncode in (0, 1), proc.stderr
        assert mirror_accepts == (proc.returncode == 0), (pattern, value)
