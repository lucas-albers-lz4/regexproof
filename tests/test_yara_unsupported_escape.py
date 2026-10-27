"""YARA rejects PCRE escapes the RE2 mirror cannot represent."""

from __future__ import annotations

import pytest

from regexproof.compiler import compile_pattern
from regexproof.compiler.yara import _has_unsupported_upper_v_escape


def test_upper_v_escape_is_classified_before_the_re2_helper():
    pattern = r"\\AppData\\Roaming\\[0-9]{9,12}\VMwareCplLauncher\.exe"
    result = compile_pattern(pattern, "", "yara", "search")
    assert not result.encodable
    assert result.unencodable_reason == "unsupported-escape"


@pytest.mark.parametrize(
    "pattern, expected",
    [
        (r"\V", True),
        (r"\\V", False),
        (r"[\V]", False),
        (r"[]\V]", False),
    ],
)
def test_upper_v_detector_ignores_escaped_literals_and_classes(pattern, expected):
    assert _has_unsupported_upper_v_escape(pattern) is expected
