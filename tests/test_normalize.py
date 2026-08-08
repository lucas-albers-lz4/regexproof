from regexproof.compiler.normalize import normalize_inline_flags


def test_lift_leading_i():
    pat, flags = normalize_inline_flags("(?i)abc", "")
    assert pat == "abc"
    assert flags == "i"


def test_lift_preserves_existing_flags():
    pat, flags = normalize_inline_flags("(?i)x", "s")
    assert pat == "x"
    assert flags == "is"
