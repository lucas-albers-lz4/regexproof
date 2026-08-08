"""Join contract + argv-only static checks for ReDoS paths."""

from __future__ import annotations

from pathlib import Path

from regexproof.fuzz.adapters import reject_shell_subprocess_usage
from regexproof.redos.join import join_findings
from regexproof.regex_id import make_regex_id


def test_join_keeps_sections_separate():
    rid = make_regex_id("r", "a+", "", "ecma", "search", "a.js:1:0")
    z3 = [{"regex_id": rid, "result": "unsat", "shape": 1}]
    redos = [
        {
            "regex_id": rid,
            "result": "vulnerable",
            "tool": "recheck",
            "tool_version": "4.5.0",
        }
    ]
    report = join_findings(z3, redos)
    assert "verdict" not in report
    assert "combined" not in report
    assert report["z3_findings"][rid][0]["result"] == "unsat"
    assert report["redos_findings"][rid][0]["result"] == "vulnerable"
    # Same id, different sections — not collapsed
    assert report["z3_findings"][rid] is not report["redos_findings"][rid]


def test_no_shell_true_in_redos_paths():
    root = Path(__file__).resolve().parents[1]
    paths = [
        root / "regexproof" / "redos",
        root / "helpers" / "redos",
    ]
    violations = reject_shell_subprocess_usage(paths)
    assert violations == [], "\n".join(violations)
