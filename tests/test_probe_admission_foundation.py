"""Foundation tests for admission probe (P1 A0–A2)."""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.admission.boundary import BoundarySignals, classify_boundary, load_signal_lists
from regexproof.admission.dialect_aliases import normalize_dialect_counts
from regexproof.admission.serialize import dumps_pinned
from regexproof.admission.vocabulary import DEFAULT_VOCAB_PATH, load_vocabulary, predict_buckets

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "admission"


def test_vocabulary_artifact_exists_and_loads():
    assert DEFAULT_VOCAB_PATH.is_file()
    vocab = load_vocabulary()
    assert "_meta" in vocab
    assert "construct_to_bucket" in vocab
    assert "lookaround" in vocab["construct_to_bucket"]
    # Explicit gap note vs inventory cardinality
    note = vocab["_meta"]["note"]
    assert "57" in note or "compile_reason" in note


def test_predict_buckets_maps_and_skips_unknown():
    vocab = load_vocabulary()
    out = predict_buckets(
        {"(?x)": 136, "(?i)": 69, "lookaround": 3, "not-a-construct": 9},
        vocabulary=vocab,
    )
    assert out["inline-flag"] == 136 + 69
    assert out["lookaround"] == 3
    assert "not-a-construct" not in out


def test_dumps_pinned_byte_identical():
    obj = {"b": 2, "a": {"z": 1, "m": 0}, "list": [3, 1]}
    a = dumps_pinned(obj)
    b = dumps_pinned(obj)
    assert a == b
    assert a.endswith("\n")
    assert '"a"' in a and a.index('"a"') < a.index('"b"')


def test_normalize_dialect_aliases_py_to_py_re():
    assert normalize_dialect_counts({"py": 2}) == {"py_re": 2}
    assert normalize_dialect_counts({"py": 1, "py_re": 4}) == {"py_re": 5}
    assert normalize_dialect_counts({"java": 22, "rust-regex": 1, "shell": 0}) == {
        "java": 22,
        "rust-regex": 1,
        "shell": 0,
    }


def test_boundary_rule_positive_negative_neither_and_priority():
    lists = load_signal_lists()
    assert (
        classify_boundary(BoundarySignals(extra_positive=True), signal_lists=lists)
        == "deterministic-true"
    )
    assert (
        classify_boundary(
            BoundarySignals(extra_negative_category="form-library"),
            signal_lists=lists,
        )
        == "deterministic-false"
    )
    assert classify_boundary(BoundarySignals(repo_name="plain-lib"), signal_lists=lists) == "unknown"
    # positive beats negative
    assert (
        classify_boundary(
            BoundarySignals(extra_positive=True, extra_negative_category="form-library"),
            signal_lists=lists,
        )
        == "deterministic-true"
    )


@pytest.mark.parametrize(
    "name,expected",
    [
        ("gitleaks", {"deterministic-true", "unknown"}),
        ("DOMPurify", {"deterministic-true", "unknown"}),
        ("java-html-sanitizer", {"deterministic-true", "unknown"}),
        ("wtforms", {"deterministic-false"}),
        ("url-regex", {"deterministic-false"}),
        ("git-secrets", {"unknown"}),
    ],
)
def test_boundary_golden_fixtures(name: str, expected: set[str]):
    lists = load_signal_lists()
    verdict = classify_boundary(BoundarySignals(repo_name=name), signal_lists=lists)
    assert verdict in expected
    if name in {"gitleaks", "DOMPurify", "java-html-sanitizer"}:
        assert verdict != "deterministic-false"
    if name in {"wtforms", "url-regex"}:
        assert verdict == "deterministic-false"


def test_boundary_avoids_short_keyword_false_positives():
    lists = load_signal_lists()
    assert (
        classify_boundary(
            BoundarySignals(description="Belgian waffle recipes"),
            signal_lists=lists,
        )
        == "unknown"
    )
    assert (
        classify_boundary(
            BoundarySignals(repo_name="secretariat-helpers"),
            signal_lists=lists,
        )
        == "unknown"
    )


def test_boundary_prefix_needles_still_match():
    lists = load_signal_lists()
    assert (
        classify_boundary(
            BoundarySignals(repo_name="awesome-regex-list"),
            signal_lists=lists,
        )
        == "deterministic-false"
    )
    assert (
        classify_boundary(
            BoundarySignals(paths=("src/secrets/scanner.go",)),
            signal_lists=lists,
        )
        == "deterministic-true"
    )


def test_vocabulary_maps_k_reset_to_reset_bucket():
    vocab = load_vocabulary()
    assert vocab["construct_to_bucket"]["\\K"] == "reset"
    assert predict_buckets({"\\K": 3}, vocabulary=vocab) == {"reset": 3}


def test_signal_lists_not_security_tool_corpora():
    lists = load_signal_lists()
    # Must not reuse the closed admitted-name frozenset from disclose.py
    from regexproof.batch.disclose import SECURITY_TOOL_CORPORA

    assert lists.get("positive", {}).get("name_substrings") != sorted(SECURITY_TOOL_CORPORA)
    assert "negative_categories" in lists
    assert "form-library" in lists["negative_categories"]
    # Classifier module must not import SECURITY_TOOL_CORPORA
    import inspect

    import regexproof.admission.boundary as boundary_mod

    src = inspect.getsource(boundary_mod)
    assert "SECURITY_TOOL_CORPORA" not in src
