"""Scaffold emitters — Extract Class from scaffold.py render methods.

Templates are copied verbatim so generated gate/fuzz/ci text stays
byte-stable (filenames, flags, REGISTRY.clear order, emitted builders).
"""

from __future__ import annotations

from dataclasses import dataclass

from regexproof.newgate.emit_builders import EMITTED_BUILD_ALPHABET, EMITTED_FLAG_BITS


@dataclass(frozen=True)
class FuzzBounds:
    runs: int
    exhaust_max_len: int
    fuzz_max_len: int


@dataclass(frozen=True)
class ScaffoldContext:
    pattern: str
    flags: str
    dialect: str
    call_kind: str
    family: str
    slug: str
    ci_workdir: str
    regexproof_ref: str
    site: str
    source: str
    forbidden: list[tuple[str, str]]
    alphabet_chars: str
    mutation_ch: str
    mutation_label: str
    mirror_expr: str
    fuzz_alphabet: str
    mutations: str
    fuzz: FuzzBounds
    input_domain: str = "ascii"

    @property
    def pattern_repr(self) -> str:
        return repr(self.pattern)

    @property
    def flags_repr(self) -> str:
        return repr(self.flags)

    @property
    def site_repr(self) -> str:
        return repr(self.site)

    @property
    def alphabet_chars_repr(self) -> str:
        return repr(self.alphabet_chars)

    @property
    def mutation_ch_repr(self) -> str:
        return repr(self.mutation_ch)

    @property
    def mirror_expr_repr(self) -> str:
        return repr(self.mirror_expr)

    @property
    def fuzz_alphabet_repr(self) -> str:
        return repr(self.fuzz_alphabet)

    @property
    def mutations_repr(self) -> str:
        return repr(self.mutations)


class ScaffoldEmitter:
    """Five emitters for the five scaffold files."""

    def gate(self, ctx: ScaffoldContext) -> str:
        pairs = ",\n    ".join(
            f"({label!r}, {ch!r})" for label, ch in ctx.forbidden
        )
        # Builders are final source (single braces); splice outside f-string
        # so set-comprehensions are not re-interpreted.
        head = f'''"""Scaffolded regexproof gate — Wave 12 cookie-cutter.

Dialect: {ctx.dialect} (Python ``re``). Call kind: {ctx.call_kind}.
Site: {ctx.source}
Pattern: {ctx.pattern_repr}
Flags: {ctx.flags_repr}

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

PATTERN = {ctx.pattern_repr}
FLAGS = {ctx.flags_repr}
DIALECT = {ctx.dialect!r}
CALL_KIND = {ctx.call_kind!r}
FAMILY = {ctx.family!r}
SITE = {ctx.site_repr}
INPUT_DOMAIN = {ctx.input_domain!r}
# Singleton leaves from the Z3 mirror (charset whitelist). Not the full language.
ALPHABET_CHARS = {ctx.alphabet_chars_repr}
MUTATION_CH = {ctx.mutation_ch_repr}

'''
        mid = f'''
_BITS = 0
for _ch in FLAGS:
    if _ch not in _FLAG_BITS:
        raise SystemExit(f"newgate gate: unknown flag {{_ch!r}}")
    _BITS |= _FLAG_BITS[_ch]

_RX = re.compile(PATTERN, _BITS)


'''
        tail = f'''


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
    f"{{FAMILY}}-mutated-{ctx.mutation_label}",
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
        return head + EMITTED_FLAG_BITS + mid + EMITTED_BUILD_ALPHABET + tail

    def fuzz(self, ctx: ScaffoldContext) -> str:
        return f'''"""Argv-only differential fuzz vs Python ``re`` (helpers/python/match.py).

Invokes scripts/differential-fuzz.py with subprocess.run(..., shell=False).
REGEXPROOF_ROOT or an editable checkout locates the script. Dialect: {ctx.dialect}.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

PATTERN = {ctx.pattern_repr}
FLAGS = {ctx.flags_repr}
CALL_KIND = {ctx.call_kind!r}
MIRROR_EXPR = {ctx.mirror_expr_repr}
ALPHABET = {ctx.fuzz_alphabet_repr}
MUTATIONS = {ctx.mutations_repr}
RUNS = {ctx.fuzz.runs}
EXHAUST_MAX_LEN = {ctx.fuzz.exhaust_max_len}
MAX_LEN = {ctx.fuzz.fuzz_max_len}


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

    def readme(self, ctx: ScaffoldContext) -> str:
        return f"""# regexproof gate `{ctx.slug}`

Scaffolded by `regexproof newgate` (Wave 12 / #581). **Dialect: `{ctx.dialect}`**
(Python `re`). Call kind: `{ctx.call_kind}`. Flags: `{ctx.flags or "(none)"}`.

This is the **consumer adoption** path: one regex in your repo → a runnable
property gate. It is not the operator corpus funnel (`docs/PIPELINE.md`).

## Site

- File: `{ctx.source}`
- Pattern: `{ctx.pattern}`
- Family: `{ctx.family}`
- Alphabet chars (scaffold-time): `{ctx.alphabet_chars}`
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
`{ctx.regexproof_ref}` into `regexproof-src`, installs that tree editable
(so `regexproof.newgate.runner` matches the fuzz scripts), sets
`REGEXPROOF_ROOT`, and runs the gate under `{ctx.ci_workdir}`.

Walkthrough: regexproof `docs/NEWGATE.md`.
"""

    def ci(self, ctx: ScaffoldContext) -> str:
        slug = ctx.slug
        workdir = ctx.ci_workdir
        pin = ctx.regexproof_ref
        return f"""# STUB — copy into .github/workflows/ and pin actions/python yourself.
# regexproof newgate scaffold ({slug} / family {ctx.family})
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

    def run_sh(self) -> str:
        return """#!/bin/sh
set -e
here=$(dirname "$0")
python3 "$here/gate.py" --all --require-ground-truth --fail-on-property-failure
python3 "$here/gate.py" --check-mutation-coverage
python3 "$here/fuzz.py"
"""
