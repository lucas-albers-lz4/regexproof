"""Z3 regex AST → compact z3py expression for ``--mirror-expr``.

``scripts/differential-fuzz.py`` evals Concat/Union/Range/Re/Star/Plus/Loop
(Complement). Huge encodings (Python ``.`` as a BMP union) fail closed —
newgate v1 is a charset-whitelist cookie-cutter, not a general pretty-printer.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

_MAX_EXPR = 8000
_MAX_UNION = 64

_OP = {
    "re.++": "Concat",
    "re.union": "Union",
    "re.*": "Star",
    "re.+": "Plus",
    "re.comp": "Complement",
    "re.complement": "Complement",
}

# Visitor: (node_name, children) → True if handled (do not recurse into kids).
RegexVisitor = Callable[[str, list[Any]], bool]


def walk_z3_regex(node, visitor: RegexVisitor) -> None:
    """Dispatch-only walk over a Z3 regex AST.

    ``visitor(name, kids)`` returns True when it handled the node (no default
    child recursion). Returns False to recurse into children. Callers keep
    their own range / newline / printable policies — do not unify handlers.
    """
    name = node.decl().name()
    kids = list(node.children())
    if visitor(name, kids):
        return
    for child in kids:
        walk_z3_regex(child, visitor)


def mirror_to_py(expr, *, max_len: int = _MAX_EXPR) -> str:
    """Return a MIRROR_NS-evalable Python expression, or raise ValueError."""
    text = _pp(expr)
    if len(text) > max_len:
        raise ValueError(
            f"mirror pretty-print is {len(text)} chars (cap {max_len}); "
            "newgate v1 needs a compact charset-shaped pattern, not '.' / [^...]"
        )
    return text


def collect_singleton_alphabet(expr) -> str:
    """Single-char leaves from the mirror (ranges expanded).

    Includes ``\\n`` when present (including ``$`` trailing-newline artifacts)
    so shape-1 cannot claim a false ``excludes-newline`` UNSAT. Fail-closed on
    wide ranges (≥128 code points): silently skipping them would omit accepted
    chars and yield false UNSAT properties.
    """
    found: list[str] = []
    seen: set[str] = set()

    def add(ch: str) -> None:
        if ch and ch not in seen:
            seen.add(ch)
            found.append(ch)

    def visitor(name: str, kids: list) -> bool:
        if name == "re.range" and len(kids) == 2:
            lo = kids[0].as_string()
            hi = kids[1].as_string()
            if len(lo) != 1 or len(hi) != 1:
                raise ValueError("re.range bounds must be single characters")
            a, b = ord(lo), ord(hi)
            if not (0 <= a <= b <= 0x10FFFF):
                raise ValueError(
                    f"re.range out of order or out of Unicode: {lo!r}-{hi!r}"
                )
            span = b - a
            if span >= 128:
                raise ValueError(
                    f"re.range {lo!r}-{hi!r} spans {span + 1} chars (≥128); "
                    "newgate v1 refuses partial alphabet extraction "
                    "(false UNSAT risk)"
                )
            for code in range(a, b + 1):
                add(chr(code))
            return True
        if name == "str.to_re":
            s = kids[0].as_string() if kids else ""
            # Include ``\n`` when present. Skipping it (for ``$`` trailing-newline
            # artifacts) omitted real charset newlines and allowed false
            # ``excludes-newline`` UNSAT proofs.
            if len(s) == 1:
                add(s)
            return True
        return False

    walk_z3_regex(expr, visitor)
    return "".join(found)


def fuzz_alphabet(expr, *, fallback: str = "ab01._-") -> str:
    """Short fuzz alphabet: first/last of each ASCII range plus literal chars."""
    sample: list[str] = []
    seen: set[str] = set()

    def add(ch: str) -> None:
        if ch and ch not in seen and ch.isprintable() and ch != "\n":
            seen.add(ch)
            sample.append(ch)

    def visitor(name: str, kids: list) -> bool:
        if name == "re.range" and len(kids) == 2:
            lo = kids[0].as_string()
            hi = kids[1].as_string()
            if len(lo) == 1 and len(hi) == 1:
                add(lo)
                add(hi)
            return True
        if name == "str.to_re":
            s = kids[0].as_string() if kids else ""
            if len(s) == 1:
                add(s)
            return True
        return False

    walk_z3_regex(expr, visitor)
    text = "".join(sample)
    return text if text else fallback


def _pp(expr) -> str:
    name = expr.decl().name()
    kids = list(expr.children())
    if name == "str.to_re":
        s = kids[0].as_string() if kids else ""
        return f"Re({s!r})"
    if name == "re.range":
        if len(kids) != 2:
            raise ValueError("re.range without two bounds")
        return f"Range({kids[0].as_string()!r}, {kids[1].as_string()!r})"
    if name == "re.loop":
        params = list(expr.params() or [])
        if len(params) != 2 or len(kids) != 1:
            raise ValueError("re.loop: expected (body, lo, hi)")
        lo, hi = params
        return f"Loop({_pp(kids[0])}, {int(lo)}, {int(hi)})"
    if name == "re.allchar":
        raise ValueError("re.allchar cannot be emitted as compact --mirror-expr")
    if name in {"re.++", "re.union"}:
        flat = _flatten(expr, name)
        if name == "re.union" and len(flat) > _MAX_UNION:
            raise ValueError(
                f"union arity {len(flat)} exceeds {_MAX_UNION} — pattern is too "
                "wide for a compact mirror (try a charset whitelist)"
            )
        op = _OP[name]
        if len(flat) == 1:
            return _pp(flat[0])
        if len(flat) < 2:
            raise ValueError(f"{name} with no children")
        return f"{op}({', '.join(_pp(k) for k in flat)})"
    if name in {"re.*", "re.+", "re.comp", "re.complement"}:
        if len(kids) != 1:
            raise ValueError(f"{name} expected one child")
        return f"{_OP[name]}({_pp(kids[0])})"
    raise ValueError(f"unsupported Z3 regex node {name!r} for --mirror-expr")


def _flatten(expr, name: str) -> list:
    out: list = []

    def walk(node) -> None:
        if node.decl().name() == name:
            for child in node.children():
                walk(child)
        else:
            out.append(node)

    walk(expr)
    return out
