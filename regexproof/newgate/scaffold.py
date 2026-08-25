"""Emit a consumer property gate under ``--out`` (default ``gates/<slug>/``)."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

from regexproof.compiler import compile_pattern
from regexproof.io_atomic import atomic_write_text
from regexproof.kinds import CALL_KINDS, validate_call_kind, validate_dialect
from regexproof.newgate.emitters import FuzzBounds, ScaffoldContext, ScaffoldEmitter
from regexproof.newgate.mirror_expr import (
    collect_singleton_alphabet,
    fuzz_alphabet,
    mirror_to_py,
)
from regexproof.z3_pin import assert_z3_pinned

DEFAULT_FORBIDDEN = " \t\n;=|$`&"
DEFAULT_MUTATIONS = r""" ;="`$|&"""
_SLUG_RE = re.compile(r"[^a-zA-Z0-9]+")
_IDENT_RE = re.compile(r"[^A-Za-z0-9_]+")

_CHAR_LABELS = {
    " ": "space",
    "=": "equals",
    "\n": "newline",
    "\t": "tab",
    ";": "semicolon",
    "|": "pipe",
    "$": "dollar",
    "`": "backtick",
    "&": "ampersand",
    "*": "star",
    "\x7f": "del",
    "\x00": "nul",
}

_SCAFFOLD_FILES = ("gate.py", "fuzz.py", "README.md", "ci.yml", "run.sh")
_SAFE_SLUG_RE = re.compile(r"^[A-Za-z0-9_]{1,40}$")
_SAFE_WORKDIR_RE = re.compile(r"^[A-Za-z0-9._/-]+$")
_MUTATION_CANDIDATES = ("*", ";", "|", "$", "`", "\x7f", "\x00", "!", "#")


@dataclass(frozen=True)
class ScaffoldRequest:
    source_file: Path
    pattern: str
    out: Path
    slug: str
    family: str
    dialect: str
    call_kind: str
    flags: str
    forbidden: str
    fuzz_runs: int
    exhaust_max_len: int
    fuzz_max_len: int
    mutations: str
    force: bool
    regexproof_ref: str = ""

    @property
    def fuzz_bounds(self) -> FuzzBounds:
        return FuzzBounds(
            runs=self.fuzz_runs,
            exhaust_max_len=self.exhaust_max_len,
            fuzz_max_len=self.fuzz_max_len,
        )


@dataclass(frozen=True)
class ScaffoldResult:
    out: Path
    files: tuple[str, ...]
    family: str
    dialect: str
    mirror_expr: str


def char_label(ch: str) -> str:
    if ch in _CHAR_LABELS:
        return _CHAR_LABELS[ch]
    if ch.isascii() and ch.isalnum():
        return ch
    return f"chr{ord(ch)}"


def default_slug(source_file: Path, pattern: str) -> str:
    stem = _SLUG_RE.sub("_", source_file.stem).strip("_").lower() or "gate"
    digest = hashlib.sha256(pattern.encode("utf-8")).hexdigest()[:8]
    slug = f"{stem}_{digest}"
    return slug[:40].rstrip("_")


def family_ident(slug: str) -> str:
    ident = _IDENT_RE.sub("_", slug).strip("_") or "gate"
    if ident[0].isdigit():
        ident = f"g_{ident}"
    return f"NG_{ident}"


def validate_slug(slug: str) -> str:
    """Fail-closed: slug is interpolated into generated CI YAML paths."""
    if not _SAFE_SLUG_RE.fullmatch(slug):
        raise SystemExit(
            f"newgate: --slug must match [A-Za-z0-9_]{{1,40}} (got {slug!r})"
        )
    return slug


def ci_workdir_for(out: Path, slug: str) -> str:
    """POSIX path for generated ``working-directory`` (YAML-safe).

    Relative ``--out`` is preferred. Absolute temp paths (tests / ad-hoc) fall
    back to ``gates/<slug>`` so the CI stub stays a portable copy-paste.
    """
    text = out.as_posix()
    if (
        not out.is_absolute()
        and ".." not in out.parts
        and _SAFE_WORKDIR_RE.fullmatch(text)
        and "\n" not in text
        and ":" not in text
    ):
        return text
    fallback = f"gates/{slug}"
    if not _SAFE_WORKDIR_RE.fullmatch(fallback):
        raise SystemExit(
            f"newgate: cannot derive YAML-safe CI working-directory from "
            f"--out {text!r} / slug {slug!r}"
        )
    return fallback


def pick_mutation_sentinel(alphabet: set[str]) -> str:
    for ch in _MUTATION_CANDIDATES:
        if ch not in alphabet:
            return ch
    for code in range(0x80, 0x100):
        ch = chr(code)
        if ch not in alphabet:
            return ch
    raise SystemExit(
        "newgate: cannot pick a mutation sentinel outside the alphabet"
    )


def pick_forbidden(alphabet: set[str], requested: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    seen_labels: set[str] = set()
    for ch in requested:
        if ch in alphabet:
            continue
        label = char_label(ch)
        if label in seen_labels:
            continue
        seen_labels.add(label)
        pairs.append((label, ch))
    if pairs:
        return pairs
    for ch in (";", " ", "|", "\x7f", "\x00"):
        if ch not in alphabet:
            return [(char_label(ch), ch)]
    raise SystemExit(
        "newgate: every candidate forbidden char is inside the pattern "
        "alphabet; shape-1 disjointness has nothing to prove (pass --chars)"
    )

def scaffold(req: ScaffoldRequest) -> ScaffoldResult:
    """Write the gate tree. Fail-closed: missing file, unencodable pattern, clash."""
    assert_z3_pinned()
    src = req.source_file
    if not src.is_file():
        raise SystemExit(f"newgate: not a file: {src}")
    if not req.pattern:
        raise SystemExit("newgate: empty pattern")
    if req.fuzz_runs < 1:
        raise SystemExit("newgate: --fuzz-runs must be >= 1")
    if req.exhaust_max_len < 0:
        raise SystemExit("newgate: --exhaust-max-len must be >= 0")
    if req.fuzz_max_len < 1:
        raise SystemExit("newgate: --fuzz-max-len must be >= 1")
    if req.exhaust_max_len >= req.fuzz_max_len:
        raise SystemExit(
            "newgate: --exhaust-max-len must be < --fuzz-max-len "
            "(differential-fuzz randint(exhaust+1, max_len))"
        )
    validate_slug(req.slug)
    workdir = ci_workdir_for(req.out, req.slug)
    try:
        dialect = validate_dialect(req.dialect)
    except ValueError as exc:
        raise SystemExit(f"newgate: {exc}") from exc
    if dialect != "py_re":
        raise SystemExit(
            f"newgate: dialect {dialect!r} is not supported in v1 "
            "(first cut is Python re / py_re)"
        )
    try:
        call_kind = validate_call_kind(req.call_kind)
    except ValueError as exc:
        raise SystemExit(f"newgate: {exc}") from exc
    if call_kind is None or call_kind not in CALL_KINDS:
        raise SystemExit(f"newgate: invalid call_kind {req.call_kind!r}")
    if call_kind == "substitution":
        raise SystemExit("newgate: substitution call_kind has no v1 replay adapter")

    compiled = compile_pattern(
        req.pattern,
        flags=req.flags,
        dialect=dialect,
        call_kind=call_kind,
    )
    if not compiled.encodable or compiled.mirror is None:
        reason = compiled.unencodable_reason or "unencodable"
        raise SystemExit(
            f"newgate: pattern is not encodable as a Z3 mirror ({reason})"
        )
    if compiled.mirror_exact is not True:
        raise SystemExit(
            "newgate: pattern mirror is approximate (mirror_exact=False); "
            "v1 refuses Unicode-default shorthand like \\w/\\d/\\s without "
            "re.ASCII — pass flags 'a' or use an explicit charset class"
        )
    try:
        mirror_expr = mirror_to_py(compiled.mirror)
    except ValueError as exc:
        raise SystemExit(f"newgate: {exc}") from exc

    try:
        alphabet_chars = collect_singleton_alphabet(compiled.mirror)
    except ValueError as exc:
        raise SystemExit(f"newgate: {exc}") from exc
    alphabet = set(alphabet_chars)
    if not alphabet_chars:
        raise SystemExit(
            "newgate: pattern has no singleton char alphabet for shape-1 "
            "(v1 needs a charset whitelist like [A-Za-z0-9._-]+, not fixed "
            "multi-char literals alone)"
        )
    forbidden = pick_forbidden(alphabet, req.forbidden)
    mutation_ch = pick_mutation_sentinel(alphabet)
    fuzz_alpha = fuzz_alphabet(compiled.mirror)
    out = req.out
    if out.exists() and not out.is_dir():
        raise SystemExit(f"newgate: --out is not a directory: {out}")
    if not req.force:
        clashes = [name for name in _SCAFFOLD_FILES if (out / name).exists()]
        if clashes:
            raise SystemExit(
                f"newgate: refusing to overwrite {clashes} under {out} "
                "(pass --force)"
            )
    out.mkdir(parents=True, exist_ok=True)

    pin_ref = (req.regexproof_ref or "").strip()
    if not pin_ref:
        raise SystemExit(
            "newgate: missing --regexproof-ref (pin the CI checkout SHA/tag)"
        )
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", pin_ref) or ".." in pin_ref:
        raise SystemExit(f"newgate: unsafe --regexproof-ref {pin_ref!r}")

    site = f"{src.as_posix()}:{req.pattern}"
    ctx = ScaffoldContext(
        pattern=req.pattern,
        flags=req.flags,
        dialect=dialect,
        call_kind=call_kind,
        family=req.family,
        slug=req.slug,
        ci_workdir=workdir,
        regexproof_ref=pin_ref,
        site=site,
        source=src.as_posix(),
        forbidden=forbidden,
        alphabet_chars=alphabet_chars,
        mutation_ch=mutation_ch,
        mutation_label=char_label(mutation_ch),
        mirror_expr=mirror_expr,
        fuzz_alphabet=fuzz_alpha,
        mutations=req.mutations,
        fuzz=req.fuzz_bounds,
        # Charset shape-1 assumes an ASCII input domain; edit if the real
        # boundary is Unicode-exposed (TRAPS #17).
        input_domain="ascii",
    )
    emitter = ScaffoldEmitter()
    atomic_write_text(out / "gate.py", emitter.gate(ctx))
    atomic_write_text(out / "fuzz.py", emitter.fuzz(ctx))
    atomic_write_text(out / "README.md", emitter.readme(ctx))
    atomic_write_text(out / "ci.yml", emitter.ci(ctx))
    atomic_write_text(out / "run.sh", emitter.run_sh())
    (out / "run.sh").chmod((out / "run.sh").stat().st_mode | 0o111)

    return ScaffoldResult(
        out=out,
        files=_SCAFFOLD_FILES,
        family=req.family,
        dialect=dialect,
        mirror_expr=mirror_expr,
    )

