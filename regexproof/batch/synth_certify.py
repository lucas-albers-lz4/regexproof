"""Certify phase: eligibility, selectors, and shape-1 alphabet certificates."""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass
from pathlib import PurePath
from typing import Any

import z3
from z3 import Re

from regexproof.compiler import CompileResult
from regexproof.compiler.simple_parse import (
    Alt,
    Anchor,
    Cls,
    Folded,
    Lit,
    Repeat,
    Seq,
    parse_pattern,
)

KNOWN_DIALECTS = frozenset({"py_re", "ecma", "re2", "pcre", "perl", "yara", "posix-shell"})
REPLAYABLE_MATCH_DIALECTS = frozenset({"py_re", "ecma", "re2", "pcre", "perl"})
SKIP_BUCKETS = (
    "synth_skipped_no_gt_adapter",
    "synth_skipped_unanchored_search",
    "synth_skipped_substitution_call_kind",
    "synth_skipped_approximate_mirror",
    "synth_skipped_witness_replay",
)


@dataclass(frozen=True)
class AlphabetCertification:
    """Syntactic shape-1 certificate and its known positive member."""

    known_char: str
    ast_chars: tuple[str, ...]
    charclass: Any | None = None
    repeat_kind: str | None = None
    has_shorthand: bool = False
    member_checker: Any | None = None

    def __bool__(self) -> bool:
        return bool(self.ast_chars) and self.charclass is not None


def _strip_edge_anchors(node: Any) -> Any:
    """Return the simple-parse body after removing only edge anchors."""
    if isinstance(node, Seq):
        items = list(node.items)
        if items and isinstance(items[0], Anchor) and items[0].kind == "start":
            items.pop(0)
        if items and isinstance(items[-1], Anchor) and items[-1].kind == "end":
            items.pop()
        if len(items) == 1:
            return _strip_edge_anchors(items[0])
        return Seq(items)
    return node


def _alphabet_atoms(node: Any) -> set[str] | None:
    """Extract a union of single-character AST atoms, or return ``None``."""
    if isinstance(node, Folded):
        return _alphabet_atoms(node.item)
    if isinstance(node, Lit):
        return {node.ch} if len(node.ch) == 1 else None
    if isinstance(node, Cls):
        if node.negate or not node.chars:
            return None
        chars: set[str] = set()
        for ch in node.chars:
            if len(ch) == 1:
                chars.add(ch)
            else:
                return None
        return chars
    if isinstance(node, Alt):
        chars: set[str] = set()
        for item in node.items:
            child = _alphabet_atoms(item)
            if child is None:
                return None
            chars.update(child)
        return chars or None
    return None


def _repeat_body(mirror: Any) -> tuple[Any, str] | None:
    mirror = _strip_epsilon_concat(mirror)
    if mirror is None or not hasattr(mirror, "decl"):
        return None
    kind = mirror.decl().kind()
    if kind == z3.Z3_OP_RE_STAR:
        return mirror.arg(0), "star"
    if kind == z3.Z3_OP_RE_PLUS:
        return mirror.arg(0), "plus"
    return None


def _strip_epsilon_concat(regex: Any) -> Any:
    """Drop parser-generated empty anchor atoms around the lowered body."""
    if regex is None or not hasattr(regex, "decl"):
        return regex
    if regex.decl().kind() != z3.Z3_OP_RE_CONCAT:
        return regex
    parts = [
        _strip_epsilon_concat(regex.arg(index))
        for index in range(regex.num_args())
        if not regex.arg(index).eq(Re(""))
    ]
    if len(parts) == 1:
        return parts[0]
    return z3.Concat(*parts) if parts else Re("")


def _certify_alphabet_union(ast: Any, mirror: Any | None = None) -> AlphabetCertification | None:
    """Certify ``Star``/``Plus`` over a union of literal/range AST nodes.

    ``simple_parse.Cls`` has already expanded ranges into literal members. A
    concatenation of two language-bearing nodes is intentionally rejected.
    The optional mirror supplies the exact lowered character-class expression
    used by the solver; the AST alone is enough to decide the syntax shape.
    """
    body = _strip_edge_anchors(ast)
    if not isinstance(body, Repeat) or body.lo not in (0, 1) or body.hi is not None:
        return None
    chars = _alphabet_atoms(body.item)
    if not chars:
        return None
    repeated = _repeat_body(mirror)
    if mirror is not None and repeated is None:
        return None
    charclass = repeated[0] if repeated else None
    repeat_kind = repeated[1] if repeated else None
    has_shorthand = _contains_shorthand(body)
    member_checker = _build_charclass_checker(charclass) if charclass is not None else None
    return AlphabetCertification(
        known_char=sorted(chars, key=ord)[0],
        ast_chars=tuple(sorted(chars, key=ord)),
        charclass=charclass,
        repeat_kind=repeat_kind,
        has_shorthand=has_shorthand,
        member_checker=member_checker,
    )


def _contains_shorthand(node: Any) -> bool:
    if isinstance(node, Cls):
        return any(value in {"\\d", "\\s", "\\w"} for value in node.chars)
    if isinstance(node, Folded):
        return _contains_shorthand(node.item)
    if isinstance(node, (Alt, Seq)):
        return any(_contains_shorthand(item) for item in node.items)
    if isinstance(node, Repeat):
        return _contains_shorthand(node.item)
    return False


def _parse_for_certification(pattern: str) -> Any | None:
    try:
        # P3 fold (luna gate 1): the synthesizer's patterns are ECMAScript
        # (validatorjs); \uXXXX/\u{...} escapes must parse as codepoints, not
        # as literal 'u' sequences. With the dialect-blind default, the
        # Gurmukhi class [\u0A00-\u0A7F] parsed as [u0A00-u0A7F] — the range
        # 0->u (0x30-0x75) contains ';', producing a wrong SAT verdict that
        # that the witness replay then (correctly) rejected.
        # Braced escapes are allowed: the compiler already rejected
        # non-u/v-mode braced forms, so only u/v-mode patterns reach here.
        return parse_pattern(pattern, unicode_escapes=True, allow_braced=True)
    except Exception:
        return None


def _compile_view(row: dict[str, Any], mirror: Any, meta: dict[str, Any]) -> CompileResult:
    """Build a CompileResult view so eligibility uses C1 accessors."""
    return CompileResult(
        mirror=mirror,
        unencodable_reason=None,
        dialect=str(row.get("dialect") or ""),
        call_kind=str(row.get("call_kind") or ""),
        flags=str(row.get("flags") or ""),
        pattern=str(row.get("pattern") or ""),
        declared_domain=str(row.get("domain") or "ascii"),
        meta=meta,
    )


def _eligibility(cr: CompileResult) -> str | None:
    """Return a skip reason, or ``None`` when the lowered shape is eligible."""
    call_kind = cr.call_kind
    if call_kind in ("search", "exec"):
        if cr.leading_caret is not True or cr.trailing_dollar is not True:
            return "synth_skipped_unanchored_search"
    elif call_kind == "match":
        if cr.trailing_dollar is not True:
            return "synth_skipped_match_without_dollar"
        if cr.dialect not in REPLAYABLE_MATCH_DIALECTS:
            return "synth_skipped_non_start_anchored_match"
    elif call_kind != "fullmatch":
        return "synth_skipped_unsupported_call_kind"
    if cr.meta is None or cr.fullmatch_shaped is not True:
        return "synth_skipped_not_fullmatch_shaped"
    if "m" in cr.flags:
        return "synth_skipped_multiline"
    if cr.word_boundary_wrap:
        return "synth_skipped_word_boundary_wrap"
    return None


def _selector_support(selector: Any) -> tuple[bool, str | None]:
    if selector is None:
        return True, None
    if not isinstance(selector, dict):
        return False, "selector must be an object"
    if set(selector) - {"file_globs", "context_regex", "dialects"}:
        return False, "unknown selector field"
    for key in ("file_globs", "context_regex", "dialects"):
        value = selector.get(key)
        if value is None:
            continue
        if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
            return False, f"{key} must be a string list"
        if key == "context_regex":
            try:
                for regex in value:
                    re.compile(regex)
            except re.error as exc:
                return False, f"invalid context regex: {exc}"
        if key == "dialects" and any(v not in KNOWN_DIALECTS for v in value):
            return False, "unknown dialect selector"
    return True, None


def selector_matches(row: dict[str, Any], selector: dict[str, Any] | None) -> bool:
    """Apply a structured selector; path/context alternatives are ORed."""
    if not selector:
        return True
    dialects = selector.get("dialects") or []
    if dialects and row.get("dialect") not in dialects:
        return False
    path = str(row.get("file") or row.get("site") or "")
    # P3 fold (luna re-gate 2): the validator.js family is camelCase
    # (isAscii.js, isFQDN.js) — globs match case-insensitively.
    path_l = path.lower()
    path_hits = any(
        fnmatch.fnmatchcase(path_l, glob.lower()) or PurePath(path).match(glob)
        for glob in selector.get("file_globs") or []
    )
    context = " ".join(
        str(row.get(key) or "") for key in ("context_snippet", "name", "file", "site")
    )
    context_hits = any(
        re.search(regex, context) is not None
        for regex in selector.get("context_regex") or []
    )
    # P3 fold (luna re-gate 2): file_globs and context_regex are
    # ALTERNATIVES (OR) — the previous code ANDed them, so isAscii.js
    # (glob `**/*ascii*` missed the camelCase name) was silently excluded
    # even when the context regex matched, and its NUL-accepting class was
    # never synthesized.
    if not selector.get("file_globs") and not selector.get("context_regex"):
        return True
    return path_hits or context_hits


def _decode_z3_string(value: str) -> str:
    """Decode the Unicode escape spelling used by ``z3.ExprRef.as_string``."""
    return re.sub(
        r"\\u\{([0-9a-fA-F]+)\}",
        lambda match: chr(int(match.group(1), 16)),
        value,
    )


def _build_charclass_checker(charclass: Any):
    """Index one lowered character class for repeated concrete membership."""
    ranges: list[tuple[int, int]] = []
    literals: set[str] = set()
    full = False
    unknown = False
    pending = [charclass]
    while pending:
        node = pending.pop()
        if node is None or not hasattr(node, "decl"):
            unknown = True
            continue
        kind = node.decl().kind()
        if kind == z3.Z3_OP_RE_RANGE:
            lo = _decode_z3_string(node.arg(0).as_string())
            hi = _decode_z3_string(node.arg(1).as_string())
            if len(lo) == len(hi) == 1:
                ranges.append((ord(lo), ord(hi)))
            else:
                unknown = True
        elif kind == z3.Z3_OP_SEQ_TO_RE:
            value = _decode_z3_string(node.arg(0).as_string())
            if len(value) == 1:
                literals.add(value)
            else:
                unknown = True
        elif kind == z3.Z3_OP_RE_UNION:
            pending.extend(node.arg(index) for index in range(node.num_args()))
        elif kind == z3.Z3_OP_RE_FULL_CHAR_SET or kind == z3.Z3_OP_RE_FULL_SET:
            full = True
        else:
            unknown = True

    def contains(value: str) -> bool:
        if len(value) != 1:
            return False
        return (
            full
            or value in literals
            or any(lo <= ord(value) <= hi for lo, hi in ranges)
            or (unknown and _charclass_contains(charclass, value))
        )

    return contains


def _charclass_contains(charclass: Any, value: str) -> bool:
    """Evaluate one literal against a lowered single-character union.

    Shape-1 deliberately decomposes to one-character queries. Walking that
    finite union avoids asking Z3 to normalize a large case-folded union.
    """
    pending = [charclass]
    while pending:
        node = pending.pop()
        if not hasattr(node, "decl"):
            continue
        kind = node.decl().kind()
        if kind == z3.Z3_OP_RE_RANGE:
            lo = _decode_z3_string(node.arg(0).as_string())
            hi = _decode_z3_string(node.arg(1).as_string())
            if len(lo) == len(hi) == len(value) == 1 and ord(lo) <= ord(value) <= ord(hi):
                return True
        elif kind == z3.Z3_OP_RE_UNION:
            pending.extend(node.arg(index) for index in range(node.num_args()))
        elif kind == z3.Z3_OP_SEQ_TO_RE:
            if _decode_z3_string(node.arg(0).as_string()) == value:
                return True
        elif kind == z3.Z3_OP_RE_FULL_CHAR_SET:
            return True
    return False


def _certified_contains(certification: AlphabetCertification, value: str) -> bool:
    if certification.member_checker is not None:
        return bool(certification.member_checker(value))
    return certification.charclass is not None and _charclass_contains(
        certification.charclass, value
    )


def _question_payload(question: dict[str, Any]) -> bool:
    return int(question.get("shape") or 0) in (1, 2) and bool(question.get("bad_chars"))


def _selected_questions(
    rows: list[dict[str, Any]], questions: list[dict[str, Any]]
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, dict[str, int]]]:
    selected: dict[str, list[dict[str, Any]]] = {}
    outcomes: dict[str, dict[str, int]] = {}
    for question in questions:
        if not _question_payload(question):
            continue
        qid = str(question.get("id") or "")
        support, _reason = _selector_support(question.get("selector"))
        counts = {"selected": 0, "rejected-by-selector": 0, "unsupported-selector": 0}
        if not support:
            counts["unsupported-selector"] = len(rows)
            selected[qid] = []
            outcomes[qid] = counts
            continue
        matches = []
        for row in rows:
            if selector_matches(row, question.get("selector")):
                matches.append(row)
                counts["selected"] += 1
            else:
                counts["rejected-by-selector"] += 1
        selected[qid] = matches
        outcomes[qid] = counts
    return selected, outcomes
