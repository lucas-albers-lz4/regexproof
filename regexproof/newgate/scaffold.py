"""Emit a consumer property gate under ``--out`` (default ``gates/<slug>/``)."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

from regexproof.compiler import compile_pattern
from regexproof.io_atomic import atomic_write_text
from regexproof.kinds import CALL_KINDS, validate_call_kind, validate_dialect
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
    ctx = {
        "pattern": req.pattern,
        "pattern_repr": repr(req.pattern),
        "flags": req.flags,
        "flags_repr": repr(req.flags),
        "dialect": dialect,
        "call_kind": call_kind,
        "family": req.family,
        "slug": req.slug,
        "ci_workdir": workdir,
        "regexproof_ref": pin_ref,
        "site": site,
        "site_repr": repr(site),
        "source": src.as_posix(),
        "forbidden": forbidden,
        "alphabet_chars": alphabet_chars,
        "alphabet_chars_repr": repr(alphabet_chars),
        "mutation_ch": mutation_ch,
        "mutation_ch_repr": repr(mutation_ch),
        "mutation_label": char_label(mutation_ch),
        "mirror_expr": mirror_expr,
        "mirror_expr_repr": repr(mirror_expr),
        "fuzz_alphabet": fuzz_alpha,
        "fuzz_alphabet_repr": repr(fuzz_alpha),
        "mutations": req.mutations,
        "mutations_repr": repr(req.mutations),
        "fuzz_runs": req.fuzz_runs,
        "exhaust_max_len": req.exhaust_max_len,
        "fuzz_max_len": req.fuzz_max_len,
        # Charset shape-1 assumes an ASCII input domain; edit if the real
        # boundary is Unicode-exposed (TRAPS #17).
        "input_domain": "ascii",
    }

    atomic_write_text(out / "gate.py", _render_gate(ctx))
    atomic_write_text(out / "fuzz.py", _render_fuzz(ctx))
    atomic_write_text(out / "README.md", _render_readme(ctx))
    atomic_write_text(out / "ci.yml", _render_ci(ctx))
    atomic_write_text(out / "run.sh", _render_run())
    (out / "run.sh").chmod((out / "run.sh").stat().st_mode | 0o111)

    return ScaffoldResult(
        out=out,
        files=_SCAFFOLD_FILES,
        family=req.family,
        dialect=dialect,
        mirror_expr=mirror_expr,
    )


def _render_gate(ctx: dict) -> str:
    pairs = ",\n    ".join(
        f"({label!r}, {ch!r})" for label, ch in ctx["forbidden"]
    )
    return f'''"""Scaffolded regexproof gate — Wave 12 cookie-cutter.

Dialect: {ctx["dialect"]} (Python ``re``). Call kind: {ctx["call_kind"]}.
Site: {ctx["source"]}
Pattern: {ctx["pattern_repr"]}
Flags: {ctx["flags_repr"]}

Shape-1 alphabet-disjointness (template style): query single-char membership
against the pattern's singleton alphabet, not ``InRe(s, full_mirror) ∧
Length(s)==1``. The latter is vacuous for quantifiers like ``{{8,}}`` that
admit no length-1 strings. Mutation guard widens the alphabet with a
sentinel outside the charset. Provenance is ``agent_derived`` until a human
edits the contract (docs/CONTRACTS.md / docs/NEWGATE.md).
"""
from __future__ import annotations

import re

from z3 import InRe, Length, Range, Re, String, StringVal, Union

from regexproof.harness.core import REGISTRY, prop
from regexproof.newgate.runner import main
from regexproof.z3_pin import assert_z3_pinned

# ``import regexproof.harness.core`` still runs harness/__init__.py, which
# registers the built-in P1-P6 / OpenWrt suites. Isolate this gate.
REGISTRY.clear()

assert_z3_pinned()

PATTERN = {ctx["pattern_repr"]}
FLAGS = {ctx["flags_repr"]}
DIALECT = {ctx["dialect"]!r}
CALL_KIND = {ctx["call_kind"]!r}
FAMILY = {ctx["family"]!r}
SITE = {ctx["site_repr"]}
INPUT_DOMAIN = {ctx["input_domain"]!r}
# Singleton leaves from the Z3 mirror (charset whitelist). Not the full language.
ALPHABET_CHARS = {ctx["alphabet_chars_repr"]}
MUTATION_CH = {ctx["mutation_ch_repr"]}

_FLAG_BITS = {{
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
    "a": re.ASCII,
    "u": re.UNICODE,
}}
_BITS = 0
for _ch in FLAGS:
    if _ch not in _FLAG_BITS:
        raise SystemExit(f"newgate gate: unknown flag {{_ch!r}}")
    _BITS |= _FLAG_BITS[_ch]

_RX = re.compile(PATTERN, _BITS)


def _build_alphabet():
    """Collapse contiguous code points into Range (Union of 39 Re() is slow)."""
    if not ALPHABET_CHARS:
        raise SystemExit("newgate gate: empty ALPHABET_CHARS")
    codes = sorted({{ord(ch) for ch in ALPHABET_CHARS}})
    parts = []
    start = prev = codes[0]
    for code in codes[1:]:
        if code == prev + 1:
            prev = code
            continue
        parts.append(
            Range(chr(start), chr(prev)) if start != prev else Re(chr(start))
        )
        start = prev = code
    parts.append(Range(chr(start), chr(prev)) if start != prev else Re(chr(start)))
    if len(parts) == 1:
        return parts[0]
    return Union(*parts)


ALPHABET = _build_alphabet()


def _ground_truth(witness: dict) -> bool:
    """Replay SAT witnesses against Python ``re`` (dialect=py_re).

    Shape-1 witnesses are length-1 chars. For quantifiers like ``{{8,}}``,
    probe ``ch*n`` for n in 1..32 so the real engine confirms the char can
    appear in an accepted string.
    """
    text = witness.get("s")
    if not isinstance(text, str) or len(text) != 1:
        return False
    for n in range(1, 33):
        cand = text * n
        if CALL_KIND == "fullmatch":
            if _RX.fullmatch(cand) is not None:
                return True
        elif CALL_KIND == "match":
            if _RX.match(cand) is not None:
                return True
        elif _RX.search(cand) is not None:
            return True
    return False


def _contract(guarantee: str) -> dict:
    return {{
        "schema_version": "1",
        "site": SITE,
        "guarantee": guarantee,
        "input_source": "consumer-supplied (edit me)",
        "trust": "untrusted-input",
        "declared_domain": (
            f"length-1 strings over the singleton alphabet of {{PATTERN!r}} "
            f"({{DIALECT}}/{{CALL_KIND}}; not the full pattern language)"
        ),
        "provenance": "agent_derived",
    }}


FORBIDDEN = [
    {pairs},
]

for _label, _ch in FORBIDDEN:
    def _fn(ch=_ch):
        s = String("s")
        return [InRe(s, ALPHABET), Length(s) == 1], s == StringVal(ch)

    prop(
        f"{{FAMILY}}-excludes-{{_label}}",
        f"singleton alphabet of {{PATTERN!r}} excludes {{_label}}",
        expect_unsat=True,
        ground_truth=_ground_truth,
        kind="property",
        family=FAMILY,
        input_domain=INPUT_DOMAIN,
        call_kind=CALL_KIND,
        contract=_contract(
            f"singleton alphabet of {{PATTERN!r}} contains no {{_label}}"
        ),
    )(_fn)


@prop(
    f"{{FAMILY}}-mutated-{ctx['mutation_label']}",
    "MUTATION GUARD: Union(alphabet, Re(sentinel)) must admit the sentinel "
    "(UNSAT→SAT). Sentinel is outside the charset so the guard is not tautological.",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain=INPUT_DOMAIN,
    call_kind=CALL_KIND,
)
def _mutated():
    s = String("s")
    weakened = Union(ALPHABET, Re(MUTATION_CH))
    return [InRe(s, weakened), Length(s) == 1], s == StringVal(MUTATION_CH)


if __name__ == "__main__":
    raise SystemExit(main())
'''


def _render_fuzz(ctx: dict) -> str:
    return f'''"""Argv-only differential fuzz vs Python ``re`` (helpers/python/match.py).

Invokes scripts/differential-fuzz.py with subprocess.run(..., shell=False).
REGEXPROOF_ROOT or an editable checkout locates the script. Dialect: {ctx["dialect"]}.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

PATTERN = {ctx["pattern_repr"]}
FLAGS = {ctx["flags_repr"]}
CALL_KIND = {ctx["call_kind"]!r}
MIRROR_EXPR = {ctx["mirror_expr_repr"]}
ALPHABET = {ctx["fuzz_alphabet_repr"]}
MUTATIONS = {ctx["mutations_repr"]}
RUNS = {ctx["fuzz_runs"]}
EXHAUST_MAX_LEN = {ctx["exhaust_max_len"]}
MAX_LEN = {ctx["fuzz_max_len"]}


def _root() -> Path:
    env = os.environ.get("REGEXPROOF_ROOT")
    if env:
        path = Path(env)
        if (path / "scripts" / "differential-fuzz.py").is_file():
            return path
        raise SystemExit(
            f"newgate fuzz: REGEXPROOF_ROOT={{env!r}} has no scripts/differential-fuzz.py"
        )
    import regexproof

    cand = Path(regexproof.__file__).resolve().parent.parent
    if (cand / "scripts" / "differential-fuzz.py").is_file():
        return cand
    raise SystemExit(
        "newgate fuzz: set REGEXPROOF_ROOT to the regexproof checkout "
        "(needed for scripts/differential-fuzz.py)"
    )


def main() -> int:
    root = _root()
    script = root / "scripts" / "differential-fuzz.py"
    helper = root / "helpers" / "python" / "match.py"
    if not helper.is_file():
        raise SystemExit(f"newgate fuzz: missing {{helper}}")
    cmd = [
        sys.executable,
        str(script),
        "--mirror-expr",
        MIRROR_EXPR,
        "--alphabet",
        ALPHABET,
        "--mutations",
        MUTATIONS,
        "--runs",
        str(RUNS),
        "--seed",
        "42",
        "--exhaust-max-len",
        str(EXHAUST_MAX_LEN),
        "--max-len",
        str(MAX_LEN),
        "--real-argv",
        sys.executable,
        str(helper),
        "match",
        CALL_KIND,
        PATTERN,
        FLAGS,
    ]
    proc = subprocess.run(cmd, shell=False, timeout=120, check=False)
    return int(proc.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
'''


def _render_readme(ctx: dict) -> str:
    return f"""# regexproof gate `{ctx["slug"]}`

Scaffolded by `regexproof newgate` (Wave 12 / #581). **Dialect: `{ctx["dialect"]}`**
(Python `re`). Call kind: `{ctx["call_kind"]}`. Flags: `{ctx["flags"] or "(none)"}`.

This is the **consumer adoption** path: one regex in your repo → a runnable
property gate. It is not the operator corpus funnel (`docs/PIPELINE.md`).

## Site

- File: `{ctx["source"]}`
- Pattern: `{ctx["pattern"]}`
- Family: `{ctx["family"]}`
- Alphabet chars (scaffold-time): `{ctx["alphabet_chars"]}`
- Shape: 1 (alphabet disjointness over singleton charset leaves) +
  mutation guard (`Union(alphabet, Re('*'))`)

Shape-1 queries ``InRe(s, ALPHABET) ∧ Length(s)==1`` against the pattern's
singleton char leaves — not the full mirror language. That keeps
``^[a-z]{{8,}}$`` from vacuously passing.

Contracts ship as `provenance: agent_derived`. After you read the surrounding
code, change that to `human` before counting UNSAT as product
(`docs/CONTRACTS.md`).

## Run

From this directory (regexproof + `z3-solver==5.0.0` installed):

```bash
python3 gate.py --all --require-ground-truth --fail-on-property-failure
python3 gate.py --check-mutation-coverage
REGEXPROOF_ROOT=/path/to/regexproof python3 fuzz.py
```

Or `./run.sh` (same three steps; set `REGEXPROOF_ROOT` for fuzz).
`REGEXPROOF_ROOT` must point at a regexproof *source* tree (`scripts/` +
`helpers/`); a PyPI install alone is not enough for fuzz.

TIMEOUT is a hard failure. SAT on a `property` kind is a finding — replay it
against the alphabet domain before filing.

## CI

Copy `ci.yml` into your workflows (pin actions the way your repo already
does). The stub checks out `lucas-albers-lz4/regexproof` at pinned ref
`{ctx["regexproof_ref"]}` into `regexproof-src`, installs that tree editable
(so `regexproof.newgate.runner` matches the fuzz scripts), sets
`REGEXPROOF_ROOT`, and runs the gate under `{ctx["ci_workdir"]}`.

Walkthrough: regexproof `docs/NEWGATE.md`.
"""


def _render_ci(ctx: dict) -> str:
    slug = ctx["slug"]
    workdir = ctx["ci_workdir"]
    pin = ctx["regexproof_ref"]
    return f"""# STUB — copy into .github/workflows/ and pin actions/python yourself.
# regexproof newgate scaffold ({slug} / family {ctx["family"]})
# TIMEOUT is a hard failure. --require-ground-truth + mutation coverage.
# Install from the pinned regexproof *source* checkout (not unpinned PyPI):
# gate.py imports regexproof.newgate.runner; fuzz needs scripts/ + helpers/.
name: regexproof-gate-{slug}
on:
  pull_request:
  push:
jobs:
  regexproof-gate:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - name: Checkout consumer repo
        uses: actions/checkout@v4  # pin this
      - name: Checkout regexproof (pin ref — supply-chain)
        uses: actions/checkout@v4  # pin this
        with:
          repository: lucas-albers-lz4/regexproof
          ref: "{pin}"
          path: regexproof-src
      - uses: actions/setup-python@v5  # pin this
        with:
          python-version: "3.12"
      - name: Install pinned solver + editable regexproof from checkout
        run: pip install "z3-solver==5.0.0" -e ./regexproof-src
      - name: Property gate
        run: python gate.py --all --require-ground-truth --require-domain --fail-on-property-failure
        working-directory: {workdir}
      - name: Mutation coverage
        run: python gate.py --check-mutation-coverage
        working-directory: {workdir}
      - name: Differential fuzz (argv-only)
        run: python fuzz.py
        working-directory: {workdir}
        env:
          REGEXPROOF_ROOT: ${{{{ github.workspace }}}}/regexproof-src
"""


def _render_run() -> str:
    return """#!/bin/sh
set -e
here=$(dirname "$0")
python3 "$here/gate.py" --all --require-ground-truth --fail-on-property-failure
python3 "$here/gate.py" --check-mutation-coverage
python3 "$here/fuzz.py"
"""
