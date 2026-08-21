"""Guard test for issue #542: no in-process unbounded re-* replay in rule_diff.

The shape-5 search/pad gate runs untrusted corpus patterns in a TIMED
subprocess (scripts/shape5-pad-gate.py, issue #524). The unbounded in-process
replay (regexproof/rule_diff/search_replay.py) was removed in #542; this test
fails if a bare in-process re.search/re.fullmatch (the catastrophic-
backtracking sinks) is reintroduced, or if re.match/re.sub/re.compile is
called with a non-literal pattern (i.e. an interpolated untrusted pattern).
"""

from __future__ import annotations

import ast
from pathlib import Path

_RULE_DIFF = Path(__file__).resolve().parents[1] / "regexproof" / "rule_diff"


def test_no_inprocess_unbounded_replay_in_rule_diff() -> None:
    offenders: list[str] = []
    for py in sorted(_RULE_DIFF.glob("*.py")):
        tree = ast.parse(py.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            if not (
                isinstance(fn, ast.Attribute)
                and isinstance(fn.value, ast.Name)
                and fn.value.id == "re"
            ):
                continue
            if fn.attr in ("search", "fullmatch"):
                offenders.append(f"{py.name}:{node.lineno}: re.{fn.attr}() in-process")
            elif fn.attr in ("match", "sub", "compile"):
                if not (
                    node.args
                    and isinstance(node.args[0], ast.Constant)
                    and isinstance(node.args[0].value, str)
                ):
                    offenders.append(
                        f"{py.name}:{node.lineno}: re.{fn.attr}() with non-literal pattern"
                    )
    assert not offenders, (
        "unbounded in-process re-* replay detected in rule_diff/"
        + " (untrusted patterns must go through the timed pad-gate subprocess):\n"
        + "\n".join(offenders)
    )
