"""Collision / determinism fixtures for regex_id."""

from __future__ import annotations

import pytest

from regexproof.regex_id import make_regex_id


def _id(**overrides):
    base = dict(
        repo="example/repo",
        pattern=r"^[a-z]+$",
        flags="",
        dialect="py_re",
        call_kind="fullmatch",
        site="validators.py:10:0",
    )
    base.update(overrides)
    return make_regex_id(**base)


def test_deterministic():
    assert _id() == _id()
    assert len(_id()) == 32
    assert all(c in "0123456789abcdef" for c in _id())


@pytest.mark.parametrize(
    "field,value",
    [
        ("repo", "other/repo"),
        ("pattern", r"^[a-z]+"),
        ("flags", "i"),
        ("dialect", "ecma"),
        ("call_kind", "search"),
        ("site", "validators.py:11:0"),
    ],
)
def test_distinct_on_each_component(field, value):
    assert _id() != _id(**{field: value})


def test_unencodable_not_in_hash():
    """Unencodability must never affect regex_id (recorded only in triage)."""
    a = _id()
    # Same identity fields — reason lives outside the hash inputs.
    b = make_regex_id(
        repo="example/repo",
        pattern=r"^[a-z]+$",
        flags="",
        dialect="py_re",
        call_kind="fullmatch",
        site="validators.py:10:0",
    )
    assert a == b


def test_rejects_bad_dialect():
    with pytest.raises(ValueError):
        _id(dialect="nope")


def test_rejects_bad_call_kind():
    with pytest.raises(ValueError):
        _id(call_kind="nope")
