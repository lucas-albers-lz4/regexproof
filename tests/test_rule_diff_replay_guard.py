"""Guard test for issue #542: no in-process unbounded re-* replay in rule_diff.

The shape-5 search/pad gate runs untrusted corpus patterns in a TIMED
subprocess (scripts/shape5-pad-gate.py, issue #524). The unbounded in-process
replay (regexproof/rule_diff/search_replay.py) was removed in #542; this test
fails if a bare in-process re.search/re.fullmatch (the catastrophic-
backtracking sinks) is reintroduced, or if re.match/re.sub/re.compile is
called with a non-literal pattern (i.e. an interpolated untrusted pattern).

Robustness (CodeRabbit fold, #542): scans recursively (rglob) so nested
modules cannot escape, and resolves `re` bindings — `import re`,
`import re as regex`, and `from re import search` — before checking calls.
"""

from __future__ import annotations

import ast
from pathlib import Path

_RULE_DIFF = Path(__file__).resolve().parents[1] / "regexproof" / "rule_diff"


def _re_bindings(tree: ast.Module) -> set[str]:
    """Names bound to the stdlib ``re`` module anywhere in this module.

    Walks the whole tree (not just module top level) so a function-scoped
    ``import re as regex`` / ``from re import search`` cannot evade the guard.
    Over-approximation is fine for a guard: a local binding applying to the
    whole module only makes it stricter.
    """
    bindings: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "re":
                    bindings.add(alias.asname or "re")
        elif isinstance(node, ast.ImportFrom) and node.module == "re":
            for alias in node.names:
                bindings.add(alias.asname or alias.name)
    return bindings


def test_no_inprocess_unbounded_replay_in_rule_diff() -> None:
    offenders: list[str] = []
    for py in sorted(_RULE_DIFF.rglob("*.py")):
        tree = ast.parse(py.read_text(encoding="utf-8"))
        bindings = _re_bindings(tree)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            name = None
            if (
                isinstance(fn, ast.Attribute)
                and isinstance(fn.value, ast.Name)
                and fn.value.id in bindings
            ):
                name = fn.attr
            elif isinstance(fn, ast.Name) and fn.id in bindings:
                name = fn.id
            if name is None:
                continue
            if name in ("search", "fullmatch"):
                offenders.append(
                    f"{py.relative_to(_RULE_DIFF)}:{node.lineno}: re.{name}() in-process"
                )
            elif name in ("match", "sub", "compile"):
                if not (
                    node.args
                    and isinstance(node.args[0], ast.Constant)
                    and isinstance(node.args[0].value, str)
                ):
                    offenders.append(
                        f"{py.relative_to(_RULE_DIFF)}:{node.lineno}: "
                        f"re.{name}() with non-literal pattern"
                    )
    assert not offenders, (
        "unbounded in-process re-* replay detected in rule_diff/"
        + " (untrusted patterns must go through the timed pad-gate subprocess):\n"
        + "\n".join(offenders)
    )
