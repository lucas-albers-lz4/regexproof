# Point regexproof at one regex and get a gate

This is the **consumer adoption** path: you have a regex on a security
boundary in *your* product, and you want a CI-ready Z3 property gate
(mirror, ground-truth, differential fuzz, mutation guard).

It is **not** a second onboarding story for corpus work. Operators who
discover and admit third-party repos still use
[`PIPELINE.md`](PIPELINE.md) (mine → rank → probe → gate → conversion
wave). `newgate` does not mine, probe, or write `*_gate_decision.json`.

## What you get

From `file` + `pattern`, `regexproof newgate` writes `gates/<slug>/`
(or `--out`):

| File | Role |
|---|---|
| `gate.py` | Shape-1 alphabet-disjointness properties + mutation-guard sibling, runnable with `--require-ground-truth` |
| `fuzz.py` | Argv-only call to `scripts/differential-fuzz.py` vs Python `re` (`helpers/python/match.py`) |
| `ci.yml` | GitHub Actions stub (same CI overlay: ground-truth + mutation coverage; TIMEOUT is a hard fail) |
| `run.sh` / `README.md` | How to run it |

First cut dialect is **Python `re` (`py_re`)**. Documented in the
generated README. Other dialects stay on the operator funnel + compiler
until a later newgate wave.

## Quickstart

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"   # in a regexproof checkout; or pip install regexproof

# FILE + PATTERN
.venv/bin/python -m regexproof.newgate path/to/validators.py '^[a-z0-9._-]+$'

# Same thing as one token (longest existing-file prefix before ':')
.venv/bin/python -m regexproof.newgate path/to/validators.py:^[a-z0-9._-]+$

# After install:
regexproof newgate --out gates/username --slug username \
  path/to/validators.py '^[a-z0-9._-]+$'
```

(`--slug` must match `[A-Za-z0-9_]`; when using `--out gates/username`, set
`--slug username` so the workflow `name:` matches the directory. The CI
`working-directory` always follows `--out`.)

Then:

```bash
python3 gates/<slug>/gate.py --all --require-ground-truth --fail-on-property-failure
python3 gates/<slug>/gate.py --check-mutation-coverage
REGEXPROOF_ROOT=/path/to/regexproof python3 gates/<slug>/fuzz.py
```

`REGEXPROOF_ROOT` is required when regexproof is not an editable checkout
(fuzz locates `scripts/differential-fuzz.py` and the Python match helper).
A PyPI wheel does **not** ship those paths — the generated `ci.yml` clones
`lucas-albers-lz4/regexproof` at a **pinned** `ref:` (from
`--regexproof-ref`, defaulting to this checkout's `HEAD`), installs that
tree with `pip install -e`, and points `REGEXPROOF_ROOT` there. Fuzz never
uses `shell=True`.

## What the mirror proves

The cookie-cutter encodes **shape 1** from
`scripts/z3-property-template.py`: for each injection character that is
*not* already in the pattern's singleton alphabet, "a length-1 string over
that alphabet equals the forbidden character" must be UNSAT. That is
alphabet disjointness — cheap, length-independent for the charset question.

It queries `InRe(s, ALPHABET)` where `ALPHABET` is the singleton char leaves
of the Z3 mirror (e.g. `[a-z0-9._-]`), **not** `InRe(s, full_pattern) ∧
Length(s)==1`. The full-pattern form is vacuous for quantifiers like
`{8,}` that admit no length-1 strings — newgate refuses to claim a
charset proof that way.

A **mutation guard** widens the alphabet with `Union(alphabet, Re('*'))`
and expects SAT. A harness that cannot fail proves nothing.

Ground-truth replay for SAT witnesses runs Python `re` on `ch*n` for
`n` in 1..32 (so `{8,}` still shows that the char is in the real language).
Differential fuzz compares the **full** mirror language to Python `re`
via `helpers/python/match.py`.

Contracts are `provenance: agent_derived` until you read the surrounding
code and adopt them as `human` ([`CONTRACTS.md`](CONTRACTS.md)). UNSAT
is not product without that.

## Fail-closed

- Missing file, empty pattern, unknown dialect/call-kind → `SystemExit` with a message
- Pattern the compiler cannot encode → `SystemExit` with the unencodable reason
- Mirror too wide to emit as `--mirror-expr` (e.g. `.` expanded to a BMP union) → refuse; use a charset whitelist
- Pattern with no singleton char alphabet (fixed multi-char literals only) → refuse
- Wide `re.range` (≥128 code points) → refuse (partial extraction → false UNSAT)
- Approximate mirrors (`mirror_exact=False`, e.g. Unicode-default `\w`) → refuse;
  use `flags=a` / `re.ASCII` or an explicit charset
- `--slug` outside `[A-Za-z0-9_]{1,40}` → refuse (YAML injection)
- `--exhaust-max-len >= --fuzz-max-len` → refuse
- Existing scaffold files → refuse unless `--force`
- v1 dialect is `py_re` only

## Scaffolded gate exit codes (§10)

`python3 gates/<slug>/gate.py …` uses the same operator contract as the
stock harness (`regexproof.harness.cli`):

| Exit | Meaning |
|------|---------|
| 0 | Result recorded (proven, finding, or recorded fallback) |
| 1 | Not-proven (`unknown`/abstain), mutation/domain/contract coverage failure, or `--fail-on-property-failure` with `ok=False` |
| 2 | D15 disagreement hard fail (`disagreement` on any result record) |

Consumer CI that copies `ci.yml` should treat exit 2 as a hard fail, not a
soft skip. TIMEOUT / not-proven is never a silent pass.

## After the scaffold

1. Read 50–150 lines around the site. Edit the contract (`trust`,
   `input_source`, `guarantee`). Change `provenance` to `human` if you
   stand behind the question.
2. Drop injection chars that are *supposed* to match (`--chars` on the
   next scaffold, or edit `FORBIDDEN` in `gate.py`).
3. Copy `ci.yml` into your workflows and pin actions/python the way
   that repo already does.
4. If the property is not "this charset excludes `;`", do not pretend
   the cookie-cutter answered it — encode shape 3/4/5 by hand from
   `scripts/z3-property-template.py` and [`AGENTS.md`](../AGENTS.md).

Pinned solver: `z3-solver==5.0.0` (`regexproof.z3_pin`).
