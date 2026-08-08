"""Python ast extractor scaffold for re.compile/match/search/fullmatch/sub."""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

from regexproof.extractors.record import make_record

_CALL_MAP = {
    "compile": "search",  # compile itself is not a match kind — consumer decides;
    # we still record compile as search-shaped default unless fullmatch flags.
    "match": "match",
    "search": "search",
    "fullmatch": "fullmatch",
    "sub": "substitution",
    "subn": "substitution",
    "split": None,  # unencodable multi-match
}


def _flags_to_str(node: ast.AST | None) -> str:
    if node is None:
        return ""
    # re.I | re.M etc.
    names = []

    def walk(n):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "re":
            mapping = {
                "I": "i",
                "IGNORECASE": "i",
                "M": "m",
                "MULTILINE": "m",
                "S": "s",
                "DOTALL": "s",
                "X": "x",
                "VERBOSE": "x",
                "A": "a",
                "ASCII": "a",
            }
            if n.attr in mapping:
                names.append(mapping[n.attr])
        elif isinstance(n, ast.BinOp) and isinstance(n.op, ast.BitOr):
            walk(n.left)
            walk(n.right)

    walk(node)
    return "".join(sorted(set(names)))


def extract_python(source: str, *, repo: str, file: str) -> list[dict[str, Any]]:
    tree = ast.parse(source)
    out: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id == "re":
            method = func.attr
        else:
            continue
        if method == "split":
            # multi-match — emit unencodable
            out.append(
                make_record(
                    repo=repo,
                    pattern="",
                    flags="",
                    dialect="py_re",
                    call_kind="search",
                    file=file,
                    line=node.lineno,
                    column=node.col_offset,
                    unencodable_reason="multi-match",
                )
            )
            continue
        call_kind = _CALL_MAP.get(method)
        if call_kind is None:
            continue
        if method == "compile":
            call_kind = "search"
        if not node.args:
            continue
        pat_node = node.args[0]
        if isinstance(pat_node, ast.Constant) and isinstance(pat_node.value, str):
            pattern = pat_node.value
            reason = None
        elif isinstance(pat_node, ast.JoinedStr) or (
            isinstance(pat_node, ast.BinOp) and isinstance(pat_node.op, ast.Add)
        ):
            pattern = ""
            reason = "composite-pattern"
        else:
            pattern = ""
            reason = "composite-pattern"
        flags = ""
        if method == "compile" and len(node.args) > 1:
            flags = _flags_to_str(node.args[1])
        elif len(node.args) > 2:
            flags = _flags_to_str(node.args[2])
        for kw in node.keywords:
            if kw.arg == "flags":
                flags = _flags_to_str(kw.value)
        snippet = ast.get_source_segment(source, node) or ""
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags=flags,
                dialect="py_re",
                call_kind=call_kind,
                file=file,
                line=node.lineno,
                column=node.col_offset,
                context_snippet=snippet,
                unencodable_reason=reason,
            )
        )
    return out


def extract_python_file(path: Path, *, repo: str) -> list[dict[str, Any]]:
    return extract_python(path.read_text(encoding="utf-8"), repo=repo, file=str(path))
