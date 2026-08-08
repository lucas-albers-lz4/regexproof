# The Playbook — proving regex security properties with Z3

Prove properties of regex-based sanitation (whitelists, validators, parsers)
with Microsoft's Z3 SMT solver (`z3-solver` pip package), and generate
machine-checked counterexamples for parser bugs.

**Validated:** empirically measured on `z3-solver==5.0.0` (2026-08) against
real security boundaries in usrmanage (#6) and fwlive (#120): OpenWrt POSIX-sh
audit-actor whitelists, username validators, JSON escaping, sed JSON-parsing
fallbacks, and LuCI (JS) log-classifier regexes.

## Core strategy (the mindset)

1. **Define the sanitized state as a regex** — that regex is the security
   boundary.
2. **Ask the critical question**: "Is there ANY input that, after sanitation,
   violates the boundary?"
   - `unsat` → property **proven**: no string in the declared domain violates it
   - `sat` → **counterexample** found: print the model — it's the bug witness
   - `unknown` → solver timeout: **hard failure**, never a pass
3. Start small: one critical function at a time. Be precise. Expect trade-offs.

## Verified API surface (z3-solver 5.0.0)

```python
from z3 import *
s = String('s')
a, b = String('a'), String('b')

# Regex construction
Re("abc")                      # literal string -> regex. Re(".") IS the literal dot
Range('a','z')                 # char range (inclusive)
Union(r1, r2)                  # alternation
Concat(r1, r2)                 # sequence
Star(r), Plus(r), Opt(r)       # *, +, ?
Loop(Re("a"), 2, 3)            # a{2,3} — VERIFIED works
Complement(r)                  # LANGUAGE complement — see TRAPS
InRe(s, r)                     # membership
Intersect(r1, r2)              # regex intersection (works, can be slow)

# String ops (prefer over regex where possible)
Length(s), Contains(s, sub), PrefixOf(pre, s), SuffixOf(suf, s)
IndexOf(s, sub, 0)             # first position; -1 if absent
SubString(s, offset, len)      # NOTE: len<0 -> empty string
Concat(s, t)                   # string concat (same as regex Concat)
s != StringVal("x")            # inequality
```

## Performance rules (empirically measured, 5.0.0)

| Rule | Evidence |
|---|---|
| **Bound lengths.** `Length ≤ 16` solves ~instant; `≤ 64` **times out** (60s+). | P2 whitelist: 9/9 UNSAT ≤16; both 64-char queries TIMEOUT |
| **Containment is alphabet-trivial.** "No space in whitelisted strings" is decided by `space ∉ alphabet` — no length bound, no solver search. Prove alphabet disjointness + ONE membership query; drop length-slicing loops. | Caught in review. Confirmed by re-measurement. |
| **Prefer string ops over monolithic regex** for extraction/contains reasoning. Regexes fine for membership, expensive for transformation. | P3 sed model: string-ops version solves in **2ms** |
| **Decompose big properties.** One giant regex-image proof times out. ⚠️ Encoding matters: `Contains` against the `Star(...)` image times out even per-token (30s measured); the equivalent instant form is single-char membership over the TOKEN ALPHABET (0.4ms) — star-language containment ≡ alphabet disjointness. | P4: monolithic TIMEOUT; per-token `Contains`-vs-`Star` TIMEOUT (30s); alphabet form 0.4ms |
| **Set `solver.set("timeout", N)` per property.** TIMEOUT must be a hard CI failure — never silently skip. | — |
| **Per-property wall-time logging** — needed to tune slice bounds empirically. | — |

## Workflow (what makes a proof trustworthy)

1. **Spike first, plan second.** Prove the core properties in a throwaway
   script before writing any plan. Costs minutes, converts speculation into
   evidence.
2. **Re-inventory before verifying — code drifts past plans.** A plan (or a
   skill note) written against an older revision can gate on things that no
   longer exist. The regexproof pilot found usrmanage's planned P3 target
   (rpcd sed JSON fallback) replaced by `jsonfilter` and the P2 whitelist
   already landed — both since the plan was written. Grep the actual code
   before encoding, and treat "known from a previous session" as suspect.
3. **Ground-truth digest.** Manually verify every strong claim against the
   real code before synthesis/CI. Refute confidently — reviewers and LLMs
   produce plausible-but-wrong claims (a "TOCTOU" that's serialized by a lock;
   a byte-fidelity claim that `od` disproves). Enumerate refuted claims in the
   digest. This includes your own pilot findings: the happycow pilot flagged
   an interpolated regex as "un-escaped" without reading line 105 — the
   `re.escape` was already there. Read the surrounding code before filing.
4. **Differential fuzz.** The Z3 model is a *mirror* of the shell/JS logic.
   Mutation guards prove the mirror is sensitive; differential fuzz proves
   mirror ↔ real code agree. Source the real shell under a fake env
   (`USRMANAGE_DRY_RUN=1` pattern) and assert agreement on random inputs.
5. **Automated mutation guards.** Tagged tests (`P1-mutated`) that weaken the
   regex and assert `expect_sat=True`. The harness MUST be able to fail — a
   proof harness that can't fail proves nothing.
6. **Device fidelity.** On OpenWrt targets, run ground-truth subprocess tests
   through `busybox sed` (behavior was identical on tested repros, but pin for
   device fidelity — CI runs GNU tools).
7. **Pin the version.** `z3-solver==5.0.0` — the `Re()`/Regex API changed
   across 4.x/5.x. Unpinned installs break non-deterministically.
8. **Counterexample mode is the cheap win.** A "finder" property (expect SAT +
   witness) is far easier than full verification and still guards regressions.
   Include a **migration hook**: when the underlying bug is fixed, flip the
   property from finder to "path absent" (trivial proof) — and gate the flip
   on a whole-word presence check (see TRAPS.md #12).

## Scope guidance

For a whole repo: count regexes per file, classify by input trust
(untrusted-log-input > config > internal/cosmetic), then split into
per-boundary properties. Skip cosmetic patterns (for example, CSS color
parsing) — low value. Verify one critical function at a time; expect
trade-offs.

**CRS / ModSecurity:** extract with `regexproof.extractors.modsec` (handles
`\"` escapes + multi-line `SecRule`). Shape-5 version-diff pairs use the
**CRS rule-derived R1 adapter** (`regexproof.rule_diff.crs_pairs`) — do not
apply `reject_rule_derived_r1` (that gate is for independent-spec corpora
like gitleaks). Ground-truth witnesses with the PCRE2 helper, not Python
`re`.

**Pattern length / ECMA flags:** keep the interactive **256-char** encode cap
(`pattern-too-long` — TRAPS #21); long patterns go to ReDoS/manual triage.
ECMA `m`/`u`/`v`/`g`/`y`/`d` are explicit rejects (TRAPS #22) — never silent
ASCII approximations.

## Corpus-wave loop (minimal repro)

1. Inventory → `scripts/measure-corpus-fraction.py --corpus NAME --assert-determinism`
2. Matrix → `scripts/build-cross-corpus-matrix.py`
3. Toolkit closeout → `properties/generated/phase2_toolkit_fix_closeout.md`
4. Freeze IDs → `scripts/remeasure-frozen-ids.py --corpus gitleaks --write-baseline`
5. Delta / residual → `scripts/build-phase3-delta.py`
6. Shape-5 families → `scripts/phase4-rule-diff-families.py`
7. Report → `docs/final-report.md`
