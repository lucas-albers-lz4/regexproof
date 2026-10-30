"""Native Java Pattern compiler and replay helper tests (#150)."""

from __future__ import annotations

import subprocess
import sys

import pytest
import z3

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


def test_java_rejects_known_semantic_gaps():
    assert compile_pattern(r"^foo$", dialect="java").unencodable_reason == "java-dollar-anchor"
    intersection = compile_pattern(r"[a-z&&[^aeiou]]", dialect="java")
    assert intersection.unencodable_reason == "class-intersection"
    assert compile_pattern(r"\p{L}+", dialect="java").unencodable_reason == "java-escape"
    assert compile_pattern("foo", "m", "java").unencodable_reason == "java-flag"


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
