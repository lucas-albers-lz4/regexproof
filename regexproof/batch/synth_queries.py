"""Query phase: shape-1/shape-2 solver queries, mutation guards, and diff-fuzz."""

from __future__ import annotations

import hashlib
import itertools
import random
from collections.abc import Iterable
from typing import Any

import z3
from z3 import Contains, InRe, Length, Plus, Re, Solver, Star, String, StringVal, Union

from regexproof.batch.synth_certify import (
    AlphabetCertification,
    _certified_contains,
    _decode_z3_string,
)
from regexproof.groundtruth.adapters import replay_batch, require_replayable

SOLVER_TIMEOUT_MS = 5000
EXHAUSTIVE_ALPHABET_CAP = 32


class SynthesisError(RuntimeError):
    """A synthesis gate failed and the batch must fail closed."""


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
