"""Synthesize validator properties from compiled, replayable regex sites.

The compiler remains the source of truth for wrapper shape and mirror
exactness.  This module only inspects the already-lowered metadata and uses
the parser AST to certify the small shape-1 subset.
"""

from __future__ import annotations

import fnmatch
import hashlib
import itertools
import platform
import random
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import PurePath
from typing import Any

import z3
from z3 import Contains, InRe, Length, Plus, Re, Solver, Star, String, StringVal, Union

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
from regexproof.groundtruth.adapters import (
    Replayability,
    ReplayVerdict,
    classify_replayability,
    replay,
    replay_batch,
    require_replayable,
    status_for_claim,
)
SYNTHESIZER_VERSION = "1"
DEFAULT_SYNTH_MAX_SITES = 200
DEFAULT_SYNTH_LEN_BOUND = 16
DEFAULT_SYNTH_DIFF_FUZZ_SAMPLE = 5
SOLVER_TIMEOUT_MS = 5000
EXHAUSTIVE_ALPHABET_CAP = 32
KNOWN_DIALECTS = frozenset({"py_re", "ecma", "re2", "pcre", "perl", "yara", "posix-shell"})
REPLAYABLE_MATCH_DIALECTS = frozenset({"py_re", "ecma", "re2", "pcre", "perl"})
SKIP_BUCKETS = (
    "synth_skipped_no_gt_adapter",
    "synth_skipped_unanchored_search",
    "synth_skipped_substitution_call_kind",
    "synth_skipped_approximate_mirror",
    "synth_skipped_witness_replay",
    # #423 Luna follow-up: selected sites that never reached a query, plus
    # pre-measure AST parse failures (those still may emit shape-2 rows).
    "synth_skipped_unencodable",
    "synth_skipped_missing_compile",
    "synth_skipped_certification_parse",
)


class SynthesisError(RuntimeError):
    """A synthesis gate failed and the batch must fail closed."""


def _record_skip(
    stats: dict[str, Any],
    counted_skips: set[tuple[str, str]],
    regex_id: str,
    bucket: str,
) -> None:
    """Count a named skip once per (site, bucket). Unknown buckets fail closed."""
    key = (regex_id, bucket)
    if key in counted_skips:
        return
    counted_skips.add(key)
    stats["skip_reasons"][bucket] = int(stats["skip_reasons"].get(bucket, 0)) + 1
    if bucket not in stats["skip_buckets"]:
        raise SynthesisError(f"unregistered skip bucket: {bucket}")
    stats["skip_buckets"][bucket] += 1


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


@dataclass
class SynthesisResult:
    findings: list[dict[str, Any]]
    stats: dict[str, Any]
    executed_questions: set[str]


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


def _solver_check(formula: Any, *, want_model: bool = False) -> tuple[str, Any | None]:
    solver = Solver()
    solver.set(timeout=SOLVER_TIMEOUT_MS)
    solver.add(formula)
    outcome = solver.check()
    if outcome == z3.sat:
        return "sat", solver.model() if want_model else None
    if outcome == z3.unsat:
        return "unsat", None
    raise SynthesisError("Z3 returned unknown/timeout during synthesis")


def _check_formula(formula: Any, *, want_model: bool = False) -> tuple[str, Any | None]:
    """Decide concrete membership before invoking the bounded string solver."""
    simplified = z3.simplify(formula)
    if z3.is_true(simplified):
        return "sat", None
    if z3.is_false(simplified):
        return "unsat", None
    return _solver_check(formula, want_model=want_model)


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


def _model_string(model: Any, variable: Any) -> str:
    value = model.eval(variable, model_completion=True).as_string()
    return _decode_z3_string(value)


def _regex_alphabet_contains(regex: Any, value: str) -> bool | None:
    """Return exact alphabet membership for a finite regex expression.

    ``None`` means the expression contains a predicate/full character set (or
    an unknown node), so the caller must retain the solver query.  Ranges are
    checked symbolically instead of expanded, which matters for Unicode
    validator classes.

    Iterative walk with a depth cap: a pathological expression (a deep or
    self-referential union tree) must not blow the Python stack — beyond
    the cap we return ``None`` (fail closed to the solver query).
    """

    # P3 (luna re-gate 2): the recursive version overflowed the stack on a
    # 20k-deep union tree (RecursionError surfaced through z3's ctypes arg
    # conversion). The iterative walk is bounded; the solver remains the
    # final authority for anything the walk cannot decide exactly.
    _MAX_WALK_DEPTH = 4096
    stack: list[tuple[Any, int]] = [(regex, 0)]
    unknown = False
    while stack:
        node, depth = stack.pop()
        if node is None or not hasattr(node, "decl"):
            unknown = True
            continue
        if depth > _MAX_WALK_DEPTH:
            unknown = True
            continue
        kind = node.decl().kind()
        if kind == z3.Z3_OP_RE_RANGE:
            lo = _decode_z3_string(node.arg(0).as_string())
            hi = _decode_z3_string(node.arg(1).as_string())
            if len(lo) == len(hi) == len(value) == 1 and ord(lo) <= ord(value) <= ord(hi):
                return True
            continue
        if kind in (z3.Z3_OP_SEQ_TO_RE, z3.Z3_OP_SEQ_UNIT):
            if value in _decode_z3_string(node.arg(0).as_string()):
                return True
            continue
        if kind in (z3.Z3_OP_RE_EMPTY_SET, z3.Z3_OP_SEQ_EMPTY):
            continue
        if kind in (
            z3.Z3_OP_RE_UNION,
            z3.Z3_OP_RE_CONCAT,
            z3.Z3_OP_RE_STAR,
            z3.Z3_OP_RE_PLUS,
            z3.Z3_OP_RE_OPTION,
            z3.Z3_OP_RE_LOOP,
        ):
            unary = kind in (
                z3.Z3_OP_RE_STAR,
                z3.Z3_OP_RE_PLUS,
                z3.Z3_OP_RE_OPTION,
                z3.Z3_OP_RE_LOOP,
            )
            if unary:
                stack.append((node.arg(0), depth + 1))
            else:
                for index in range(node.num_args()):
                    stack.append((node.arg(index), depth + 1))
            continue
        if kind in (z3.Z3_OP_RE_FULL_SET, z3.Z3_OP_RE_FULL_CHAR_SET, z3.Z3_OP_RE_OF_PRED):
            unknown = True
            continue
        # Unrecognized node kind: fail closed (solver query decides).
        unknown = True
    return None if unknown else False


def _shape2_query(
    mirror: Any, bad_char: str, bound: int, *, want_model: bool
) -> tuple[str, str | None]:
    # A finite alphabet is load-bearing here: asking Z3 to prove that a
    # bounded regex language excludes a character can otherwise hit the
    # 5-second gate even when the character is absent from every atom.  This
    # is the same language query, discharged by a syntactic consequence of the
    # exact mirror rather than by an approximation.
    if _regex_alphabet_contains(mirror, bad_char) is False:
        return "unsat", None
    variable = String("synth_s")
    result, model = _solver_check(
        [
            InRe(variable, mirror),
            Length(variable) <= bound,
            Contains(variable, StringVal(bad_char)),
        ],
        want_model=want_model,
    )
    witness = _model_string(model, variable) if model is not None else None
    if result == "sat" and (witness is None or bad_char not in witness):
        raise SynthesisError("Z3 returned a shape-2 witness without the bad character")
    return result, witness


def _widened_guard(
    mirror: Any,
    bad_char: str,
    *,
    shape: int,
    certification: AlphabetCertification | None,
    bound: int,
) -> tuple[str, str | None]:
    if shape == 1:
        if certification is None or certification.charclass is None:
            raise SynthesisError("shape-1 guard lacks a certified character class")
        widened_class = Union(certification.charclass, Re(bad_char))
        widened_language = (
            Plus(widened_class)
            if certification.repeat_kind == "plus"
            else Star(widened_class)
        )
        # The guard's SAT must be PROVEN against the real widened structure —
        # a tautological InRe(bad_char, Re(bad_char)) would never detect a
        # widening/class regression (luna gate 1, PR #438). The bad char is in
        # the widened class by construction, so Z3 decides the membership
        # query fast; a regression that drops the union or the repeat flips it
        # to unsat and the gate fails.
        result, _ = _check_formula(InRe(StringVal(bad_char), widened_language))
        return result, bad_char
    widened = Union(mirror, Re(bad_char))
    return _shape2_query(widened, bad_char, bound, want_model=True)


def _require_nonvacuous(
    mirror: Any,
    *,
    shape: int,
    certification: AlphabetCertification | None,
    bound: int,
) -> None:
    if shape == 1:
        if certification is None or certification.charclass is None:
            raise SynthesisError("shape-1 certification is missing")
        result = "sat" if _certified_contains(certification, certification.known_char) else "unsat"
    else:
        variable = String("nonvacuous_s")
        result, _ = _solver_check(
            [InRe(variable, mirror), Length(variable) >= 1, Length(variable) <= bound],
            want_model=False,
        )
    if result != "sat":
        raise SynthesisError("certified mirror is vacuous: positive membership is UNSAT")


def _engine_versions() -> dict[str, str]:
    return {"python": platform.python_version(), "z3": z3.get_version_string()}


def _property_row(
    *,
    corpus: str,
    row: dict[str, Any],
    question: dict[str, Any],
    bad_char: str,
    shape: int,
    result: str,
    witness: str | None,
    domain_note: str,
    ground_truth_status: str | None,
) -> dict[str, Any]:
    regex_id = str(row["regex_id"])
    family = f"synth:{corpus}:{regex_id}"
    return {
        "schema_version": "1",
        "regex_id": regex_id,
        "corpus": corpus,
        "kind": "property",
        "family": family,
        "question_id": str(question["id"]),
        "bad_char": bad_char,
        "shape": shape,
        "result": result,
        "domain_note": domain_note,
        "input_domain": str(row.get("domain") or "ascii"),
        "witness": witness,
        "ground_truth_status": ground_truth_status,
        "wall_ms": 0,
        "engine_versions": _engine_versions(),
        "site": row.get("site") or "",
        "pattern": row.get("pattern") or "",
        "dialect": row.get("dialect") or "",
        "call_kind": row.get("call_kind") or "",
        "disclosure": None,
        "synthesized": True,
        "synth": {
            "synthesizer_version": SYNTHESIZER_VERSION,
            "encoding": "shape1-charclass" if shape == 1 else "shape2-bounded-mirror",
        },
        "detail": {
            "question_id": str(question["id"]),
            "threat": question.get("threat"),
            "bad_char": bad_char,
            "domain_note": domain_note,
        },
    }


def _guard_row(
    *,
    corpus: str,
    row: dict[str, Any],
    question_id: str,
    bad_char: str,
    shape: int,
    witness: str | None,
) -> dict[str, Any]:
    regex_id = str(row["regex_id"])
    family = f"synth:{corpus}:{regex_id}"
    return {
        "schema_version": "1",
        "regex_id": regex_id,
        "corpus": corpus,
        "kind": "mutation_guard",
        "family": family,
        "question_id": question_id,
        "bad_char": bad_char,
        "shape": shape,
        "result": "sat",
        "expected_result": "sat",
        "input_domain": str(row.get("domain") or "ascii"),
        "witness": witness,
        "ground_truth_status": "mutation-guard-sat-expected",
        "wall_ms": 0,
        "engine_versions": _engine_versions(),
        "site": row.get("site") or "",
        "pattern": row.get("pattern") or "",
        "dialect": row.get("dialect") or "",
        "call_kind": row.get("call_kind") or "",
        "disclosure": None,
        "synthesized": True,
        "synth": {
            "synthesizer_version": SYNTHESIZER_VERSION,
            "encoding": "widened-mirror",
        },
        "detail": {
            "question_id": question_id,
            "bad_char": bad_char,
            "mutation": "union bad_char into mirror",
        },
    }


def _expression_alphabet(
    regex: Any, cap: int = EXHAUSTIVE_ALPHABET_CAP + 1
) -> tuple[set[str], bool]:
    """Collect a deterministic small alphabet and whether the expression is wide."""
    chars: set[str] = set()
    wide = False
    pending = [regex]
    while pending:
        node = pending.pop()
        if not hasattr(node, "decl"):
            continue
        kind = node.decl().kind()
        if kind == z3.Z3_OP_RE_RANGE:
            lo = _decode_z3_string(node.arg(0).as_string())
            hi = _decode_z3_string(node.arg(1).as_string())
            if len(lo) != 1 or len(hi) != 1:
                wide = True
                continue
            count = ord(hi) - ord(lo) + 1
            if count > cap or len(chars) + count > cap:
                wide = True
                chars.update({lo, hi})
                if count > 2:
                    chars.add(chr((ord(lo) + ord(hi)) // 2))
                continue
            chars.update(chr(code) for code in range(ord(lo), ord(hi) + 1))
            continue
        if kind == z3.Z3_OP_RE_OF_PRED:
            wide = True
            continue
        if kind in (z3.Z3_OP_RE_FULL_SET, z3.Z3_OP_RE_FULL_CHAR_SET):
            wide = True
            chars.update("a0 _-\n")
            continue
        if kind == z3.Z3_OP_RE_EMPTY_SET:
            continue
        if kind == z3.Z3_OP_RE_UNION or kind == z3.Z3_OP_RE_CONCAT:
            pending.extend(node.arg(index) for index in range(node.num_args()))
            continue
        if kind in (z3.Z3_OP_RE_STAR, z3.Z3_OP_RE_PLUS, z3.Z3_OP_RE_OPTION, z3.Z3_OP_RE_LOOP):
            pending.append(node.arg(0))
            continue
        if kind == z3.Z3_OP_SEQ_TO_RE:
            value = _decode_z3_string(node.arg(0).as_string())
            if value:
                chars.update(value[:cap])
                if len(value) > cap:
                    wide = True
            continue
        if kind == z3.Z3_OP_SEQ_EMPTY:
            continue
        if kind == z3.Z3_OP_SEQ_UNIT:
            value = _decode_z3_string(node.arg(0).as_string())
            if len(value) == 1:
                chars.add(value)
            continue
        # Do not generically walk unknown declarations: Z3 string constants
        # are internal applications whose declaration arguments are not a
        # regex tree and can recurse back into the context.
    return chars, wide or len(chars) > EXHAUSTIVE_ALPHABET_CAP


def _fuzz_witnesses(
    regex_id: str,
    alphabet: set[str],
    bad_chars: Iterable[str],
    sample: int,
    *,
    wide: bool = False,
) -> list[str]:
    dangerous = sorted(set(bad_chars), key=ord)
    base = sorted(alphabet, key=ord)
    all_chars = list(dict.fromkeys(base + dangerous))
    if not all_chars:
        all_chars = ["a"]
    # P3 fold (luna re-gate 3): a WIDE mirror (large range) whose sampled
    # alphabet happens to be small must still take the seeded wide path —
    # the exhaustive path would otherwise explode over a wide language's
    # representatives.
    if not wide and len(all_chars) <= EXHAUSTIVE_ALPHABET_CAP:
        witnesses = [""]
        for length in range(1, 4):
            witnesses.extend(
                "".join(parts) for parts in itertools.product(all_chars, repeat=length)
            )
        return witnesses

    # Wide alphabets get a bounded deterministic sample plus explicit
    # dangerous-character splices.  The seed is stable across processes.
    witnesses: list[str] = [""]
    for ch in dangerous:
        witnesses.extend((ch, "a" + ch, ch + "a"))
    seed = int(hashlib.sha256(regex_id.encode("ascii", "replace")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    for _ in range(max(0, sample)):
        length = rng.randrange(1, 4)
        witnesses.append("".join(rng.choice(all_chars) for _ in range(length)))
    return list(dict.fromkeys(witnesses))


def _mirror_accepts(mirror: Any, witness: str) -> bool:
    concrete = z3.simplify(InRe(StringVal(witness), mirror))
    if z3.is_true(concrete):
        return True
    if z3.is_false(concrete):
        return False
    result, _ = _solver_check(InRe(StringVal(witness), mirror), want_model=False)
    return result == "sat"


def _diff_fuzz_site(
    row: dict[str, Any],
    mirror: Any,
    bad_chars: Iterable[str],
    sample: int,
    *,
    shape: int,
    certification: AlphabetCertification | None,
) -> int:
    alphabet, wide = _expression_alphabet(mirror)
    witnesses = _fuzz_witnesses(
        str(row["regex_id"]), alphabet, bad_chars, sample, wide=wide
    )
    if shape == 1 and certification is not None and certification.charclass is not None:
        # P3 fold (luna re-gate 3): compute membership DIRECTLY per witness
        # char — the sampled-alphabet dict missed chars the wide fuzz path
        # introduces (e.g. the 'a' splice anchor), defaulting them to False
        # and manufacturing mirror=False/engine=True disagreements.
        expected = [
            (
                all(_certified_contains(certification, char) for char in witness)
                if witness
                else certification.repeat_kind == "star"
            )
            for witness in witnesses
        ]
    else:
        expected = [_mirror_accepts(mirror, witness) for witness in witnesses]
    actual = replay_batch(
        str(row.get("pattern") or ""),
        str(row.get("flags") or ""),
        str(row.get("dialect") or ""),
        str(row.get("call_kind") or ""),
        witnesses,
    )
    for witness, expected_accept, result in zip(witnesses, expected, actual):
        require_replayable(result)
        if result.verdict.value not in ("accepted", "rejected"):
            raise SynthesisError(
                f"diff-fuzz engine failure for {row['regex_id']}: {result.verdict.value}"
            )
        if result.accepted != expected_accept:
            raise SynthesisError(
                f"diff-fuzz disagreement for {row['regex_id']} witness={witness!r}: "
                f"mirror={expected_accept} engine={result.accepted}"
            )
    return len(witnesses)


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


def synthesize_compiled(
    corpus: str,
    compiled: list[tuple[dict[str, Any], Any, dict[str, Any] | None]],
    inventory: dict[str, Any],
    manifest: dict[str, Any] | None = None,
    *,
    diff_fuzz_sample: int | None = None,
) -> SynthesisResult:
    """Synthesize properties/guards from the compiled stream."""
    manifest = manifest or {}
    all_rows = sorted(
        (item[0] for item in compiled),
        key=lambda row: str(row.get("regex_id") or ""),
    )
    max_sites = int(manifest.get("synth_max_sites", DEFAULT_SYNTH_MAX_SITES))
    rows = all_rows[:max_sites]
    questions = list(inventory.get("questions") or [])
    selected, selector_outcomes = _selected_questions(rows, questions)
    bound = int(manifest.get("synth_len_bound", DEFAULT_SYNTH_LEN_BOUND))
    fuzz_sample = (
        int(diff_fuzz_sample)
        if diff_fuzz_sample is not None
        else int(manifest.get("synth_diff_fuzz_sample", DEFAULT_SYNTH_DIFF_FUZZ_SAMPLE))
    )
    stats: dict[str, Any] = {
        "synth_max_sites": max_sites,
        "synth_len_bound": bound,
        "synth_diff_fuzz_sample": fuzz_sample,
        "selector_outcomes": selector_outcomes,
        "skip_buckets": {bucket: 0 for bucket in SKIP_BUCKETS},
        "skip_reasons": {},
        "selected_sites": len(
            {str(r.get("regex_id")) for values in selected.values() for r in values}
        ),
        "selected_sites_after_cap": len(
            {str(r.get("regex_id")) for values in selected.values() for r in values}
        ),
        "encodable_sites": sum(1 for row, _mirror, _meta in compiled if row.get("encodable")),
    }
    stats["shape1_certification_count"] = 0
    stats["shape1_certification_parse_failures"] = 0
    counted_skips: set[tuple[str, str]] = set()
    for row, mirror, meta in compiled:
        if not row.get("encodable") or mirror is None:
            continue
        if _compile_view(row, mirror, meta).mirror_exact is not True:
            continue
        ast = _parse_for_certification(str(row.get("pattern") or ""))
        if ast is None:
            stats["shape1_certification_parse_failures"] += 1
            _record_skip(
                stats,
                counted_skips,
                str(row.get("regex_id") or ""),
                "synth_skipped_certification_parse",
            )
            continue
        if _certify_alphabet_union(ast, mirror) is not None:
            stats["shape1_certification_count"] += 1

    item_by_id = {str(row.get("regex_id")): (row, mirror, meta) for row, mirror, meta in compiled}
    property_rows: list[dict[str, Any]] = []
    guard_inputs: dict[
        tuple[str, str],
        tuple[dict[str, Any], Any, int, AlphabetCertification | None, str],
    ] = {}
    executed_questions: set[str] = set()
    premeasure_sites: set[str] = set()
    premeasure_certified: set[str] = set()

    for question in questions:
        if not _question_payload(question):
            continue
        qid = str(question["id"])
        for row in selected.get(qid, []):
            regex_id = str(row.get("regex_id") or "")
            mirror_meta = item_by_id.get(regex_id)
            if mirror_meta is None:
                _record_skip(stats, counted_skips, regex_id, "synth_skipped_missing_compile")
                continue
            _row, mirror, meta = mirror_meta
            replayability = classify_replayability(
                str(row.get("dialect") or ""), str(row.get("call_kind") or "")
            )
            if replayability is Replayability.SKIPPED_NO_GT_ADAPTER:
                _record_skip(stats, counted_skips, regex_id, "synth_skipped_no_gt_adapter")
                continue
            if replayability is Replayability.SKIPPED_SUBSTITUTION:
                _record_skip(
                    stats, counted_skips, regex_id, "synth_skipped_substitution_call_kind"
                )
                continue
            if not row.get("encodable") or mirror is None or meta is None:
                _record_skip(stats, counted_skips, regex_id, "synth_skipped_unencodable")
                continue
            cr = _compile_view(row, mirror, meta)
            skip = _eligibility(cr)
            if skip is not None:
                stats["skip_reasons"][skip] = int(stats["skip_reasons"].get(skip, 0)) + 1
                if skip == "synth_skipped_unanchored_search":
                    stats["skip_buckets"][skip] += 1
                continue
            premeasure_sites.add(regex_id)
            if cr.mirror_exact is not True:
                _record_skip(
                    stats, counted_skips, regex_id, "synth_skipped_approximate_mirror"
                )
                continue
            ast = _parse_for_certification(str(row.get("pattern") or ""))
            certification = _certify_alphabet_union(ast, mirror) if ast is not None else None
            if certification is not None:
                premeasure_certified.add(regex_id)
                effective_shape = 1
            else:
                effective_shape = 2
            if question.get("shape") == 2:
                effective_shape = 2
            for bad_char in question.get("bad_chars") or []:
                if not isinstance(bad_char, str) or len(bad_char) != 1:
                    raise SynthesisError(f"{qid}: bad_chars must contain one-character strings")
                domain_note = "all-lengths" if effective_shape == 1 else f"len<={bound}"
                if effective_shape == 1:
                    assert certification is not None
                    result = (
                        "sat"
                        if _certified_contains(certification, bad_char)
                        else "unsat"
                    )
                    witness = bad_char if result == "sat" else None
                else:
                    result, witness = _shape2_query(mirror, bad_char, bound, want_model=True)
                gt_status = None
                if result == "sat":
                    assert witness is not None
                    gt_result = replay(
                        str(row.get("pattern") or ""),
                        str(row.get("flags") or ""),
                        str(row.get("dialect") or ""),
                        str(row.get("call_kind") or ""),
                        witness,
                    )
                    require_replayable(gt_result)
                    gt_status = status_for_claim(gt_result, True)
                    if gt_status != "reproduced":
                        if gt_result.verdict is ReplayVerdict.REJECTED:
                            # SEMANTIC disagreement: the real engine rejects
                            # the witness the mirror claims to accept — the
                            # certification/query is wrong. Never skip this
                            # class; it is a soundness violation.
                            raise SynthesisError(
                                f"SAT witness failed replay for {regex_id}/{qid}/{bad_char!r}: "
                                f"{gt_result.verdict.value}"
                            )
                        # INFRA limitation (engine-error/timeout/no-adapter):
                        # the witness cannot be transported or evaluated (e.g.
                        # a NUL byte breaks the P1 NUL-framed batch protocol).
                        # The SAT claim is unverifiable — drop the row
                        # fail-closed and count it; do not crash the run.
                        _record_skip(
                            stats,
                            counted_skips,
                            regex_id,
                            "synth_skipped_witness_replay",
                        )
                        continue
                property_rows.append(
                    _property_row(
                        corpus=corpus,
                        row=row,
                        question=question,
                        bad_char=bad_char,
                        shape=effective_shape,
                        result=result,
                        witness=witness,
                        domain_note=domain_note,
                        ground_truth_status=gt_status,
                    )
                )
                key = (f"synth:{corpus}:{regex_id}", bad_char)
                guard_inputs.setdefault(
                    key, (row, mirror, effective_shape, certification, qid)
                )
            executed_questions.add(qid)

    guard_rows: list[dict[str, Any]] = []
    for (_family, bad_char), (row, mirror, shape, certification, qid) in sorted(
        guard_inputs.items(), key=lambda item: (item[0][0], item[0][1])
    ):
        _require_nonvacuous(
            mirror,
            shape=shape,
            certification=certification,
            bound=bound,
        )
        result, witness = _widened_guard(
            mirror,
            bad_char,
            shape=shape,
            certification=certification,
            bound=bound,
        )
        if result != "sat":
            raise SynthesisError(f"mutation guard is {result}, expected sat")
        guard_rows.append(
            _guard_row(
                corpus=corpus,
                row=row,
                question_id=qid,
                bad_char=bad_char,
                shape=shape,
                witness=witness,
            )
        )

    synth_findings = sorted(
        property_rows + guard_rows,
        key=lambda finding: (
            str(finding.get("regex_id") or ""),
            str(finding.get("question_id") or ""),
            str(finding.get("bad_char") or ""),
            str(finding.get("kind") or ""),
        ),
    )
    stats["synthesized_property_rows"] = len(property_rows)
    stats["mutation_guard_rows"] = len(guard_rows)
    stats["pre_measure"] = {
        "selected_sites": stats["selected_sites"],
        "selected_fullmatch_shaped_encodable_replay_supported": len(premeasure_sites),
        "shape1_certification_count_over_all_encodable_sites": stats["shape1_certification_count"],
        "shape1_certification_count_selected": len(premeasure_certified),
        "shape1_certification_parse_failures": stats["shape1_certification_parse_failures"],
        "encodable_sites": stats["encodable_sites"],
    }

    fuzz_sites: list[
        tuple[dict[str, Any], Any, list[str], int, AlphabetCertification | None]
    ] = []
    seen_sites: set[str] = set()
    for finding in property_rows:
        if finding.get("shape") not in (1, 2):
            continue
        regex_id = str(finding["regex_id"])
        if regex_id in seen_sites:
            continue
        source = item_by_id.get(regex_id)
        if source is None:
            continue
        source_row, source_mirror, _source_meta = source
        dangerous = [
            str(other.get("bad_char"))
            for other in property_rows
            if other.get("regex_id") == regex_id
        ]
        guard_info = next(
            (
                value
                for (family, bad), value in guard_inputs.items()
                if family == f"synth:{corpus}:{regex_id}"
            ),
            None,
        )
        if guard_info is None:
            continue
        _guard_row_source, _guard_mirror, guard_shape, guard_cert, _guard_qid = guard_info
        fuzz_sites.append((source_row, source_mirror, dangerous, guard_shape, guard_cert))
        seen_sites.add(regex_id)
    shape1_sites = [item for item in fuzz_sites if item[3] == 1]
    shape2_sites = [item for item in fuzz_sites if item[3] != 1]
    # Shape-1 sites are all checked. Shape-2 sites are deterministic samples.
    selected_fuzz_sites = shape1_sites + sorted(
        shape2_sites, key=lambda item: str(item[0].get("regex_id"))
    )[:fuzz_sample]
    fuzz_witnesses = 0
    for source_row, source_mirror, dangerous, shape, certification in selected_fuzz_sites:
        fuzz_witnesses += _diff_fuzz_site(
            source_row,
            source_mirror,
            dangerous,
            fuzz_sample,
            shape=shape,
            certification=certification,
        )
    stats["diff_fuzz_sites"] = len(selected_fuzz_sites)
    stats["diff_fuzz_witnesses"] = fuzz_witnesses
    stats["diff_fuzz_disagreements"] = 0
    return SynthesisResult(synth_findings, stats, executed_questions)
