# Harness backend support: Noodler escalation + cvc5 cross-check (planning ticket)

**Filed:** regexproof#212 (OPEN) — https://github.com/lucas-albers-lz4/regexproof/issues/212
**Status:** PLANNING ONLY — brainstorm/review NOT started, no work scheduled (banner in
the issue body). This file is the working copy of the issue body; keep in sync.
**Targets:** `regexproof/harness/` (post-#192 refactor; `scripts/z3-verify.py` is gone at
origin/main — local main is behind and must be updated before any implementation).

## Objective

Encode the backend rule-of-thumb from `docs/BACKENDS.md` into the harness instead of
leaving it as prose a human/agent must remember:

1. **Noodler escalation** for properties stock `seq` cannot solve: ECMA/JS-sourced
   properties (via `re.from_ecma2020`) and `unknown` results that decomposition could
   not fix.
2. **cvc5 cross-check** (`--cross-check=cvc5`) for high-stakes SAT results — a second
   implementation of the string/regex theory before an exploitable witness is trusted.
3. **Backend disagreement = hard fail**, extending the existing `unknown` = hard-fail
   policy to "solvers disagree = hard fail requiring manual triage".

Origin: conversation with Claude (2026-08-10) reviewing `docs/BACKENDS.md`; its reading
of the doc is line-accurate (verified below). This ticket corrects the two things that
conversation got wrong: (a) the real cost is not a cmake CI build — Noodler ships
prebuilt release assets; (b) the "trigger after decomposition" rule is **not
machine-detectable** as stated and needs an explicit per-property opt-in.

## Context (what exists today — all verified 2026-08-10)

- `docs/BACKENDS.md` is the authoritative playbook: decision table (`seq` ✅ / `z3str3`
  ❌ unknown-instantly, VF-002), Noodler triggers (word eq + regular + length timeouts;
  `re.from_ecma2020` for JS-as-written; extra string fns), cvc5 as soundness second
  opinion (Z3Prover/z3#10379 precedent), S3P/Norn/HAMPI/Kaluza/Stranger consciously
  excluded (symbolic-execution tooling), rule of thumb: escalate only when (a) JS/ECMA
  as-written or (b) stock Z3 times out **on a property decomposition couldn't fix**.
- The harness is **stock-z3-only with zero backend machinery**: `Solver() + timeout →
  check()`; `unknown` = HARD FAILURE (`regexproof/harness/core.py`, same shape as the
  old `scripts/z3-verify.py`). No `smt.string_solver` anywhere, no `--backend`,
  no `--cross-check`, no SMT2 dump path, no dialect/backend field in the `prop()`
  registry or the NDJSON record (schema_version 1: result/witness/ground-truth/domain/
  wall_ms/engine_versions/not_proven — an additive `backend` field is backward-compatible).
- **Already exists (proposal's blind spot):** `tests/test_noodler_probe.py` +
  `tests/fixtures/noodler_probe.json` — auditable probe recording `re.from_ecma2020`
  **absent on stock z3-solver 5.0.0** (`available: false`, `triage_fallback: true`);
  `scripts/crs-redos-dialect.py` re-confirms availability each run and records
  `changed`; `properties/fwlive-classifier.md` (from **fwlive repo** umbrella #120,
  OPEN) is a complete routing plan for the LuCI JS classifier — lookahead pattern
  `NETFILTER_KV_GLUE` is the only non-regular-language-expressible pattern, two valid
  paths (string-ops rewrite vs `re.from_ecma2020`), F2/F3 scope commits to Noodler for
  ECMA-direct properties and names the CI build cost. **fwlive #120 is a scan of fwlive
  using regexproof tooling — this ticket is regexproof-side infrastructure that #120
  consumes; nothing is built into fwlive.**
- Recent audit-wave context that constrains the design: #171 (all subprocess calls need
  `timeout=` — Noodler/cvc5 invocations must inherit), #186 (not-proven results must
  exit non-zero across all pilots), #192 (harness refactored into the package).

## Verified probe facts (2026-08-10, measured)

| # | Fact | Evidence |
|---|---|---|
| 1 | z3str3 returns `unknown` in <5ms on every shape this repo encodes (P1 star+range+len+Contains, P2 star+len+Contains, shape-5 gap) while `seq` solves within the 30s budget | live z3-solver 5.0.0.0 experiment, this session |
| 2 | …but z3str3 *does* decide fully-grounded `InRe ∧ equality` queries (unsat, 0.3ms) — the doc's blanket "unknown on InRe" overstates; VF-002 holds operationally, not literally | same experiment |
| 3 | `Solver().sexpr()` emits clean SMT-LIB2 (`(assert (str.in_re u (str.to_re "abc")))`) — a Noodler-CLI dump→`./z3 file.smt2` path is technically viable | live experiment |
| 4 | **z3-noodler v1.6.1 ships prebuilt `z3-noodler-ubuntu-24.04-x86_64-shared` + `-static-libz3` release assets** (13 releases, updated 2026-07-25) — CI cost is a pinned asset download + sha256, **not** a cmake build; BACKENDS.md L44-47 is stale on this point | GitHub API, this session |
| 5 | cvc5 is not in requirements.txt / pyproject deps (`z3-solver==5.0.0`, pytest, jsonschema only); pip-wheel feasibility on py3.13/ubuntu-latest unverified | repo state |
| 6 | No open or closed regexproof issue has ever filed Noodler/cvc5 harness work — novel to the tracker | `gh issue list --search` |
| 7 | Upstream main (62bf4b8) is far ahead of local main (47dcc40): waves 5–7 landed (#202, #209, #211 audit waves incl. #192 harness refactor) | `git fetch + log` |

## Proposed scoped design (for discussion — not final)

1. **Registry additions** (`regexproof/harness/`): `backend="seq"` (default) and
   `dialect=None|"ecma"` fields on `prop()`; a new per-property flag
   `decomposition_exhausted: true` set ONLY after the documented decomposition
   ceiling (alphabet form, fullmatch+bounds, per-alternative) has been tried.
2. **Noodler escalation is opt-in per property, never blanket-auto**: a property with
   `backend="noodler"` (or `dialect="ecma"` with a passed from_ecma2020 subset check)
   runs through the Noodler CLI when the binary is present; `unknown` under stock seq
   only escalates for properties marked `decomposition_exhausted`. Absent binary →
   documented triage fallback (probe-fixture pattern), **not** hard fail, **not**
   silent skip.
3. **`--cross-check=cvc5`**: runs the same satisfiability query in cvc5 for
   `counterexample_finder` / `bug_demo` / high-stakes SAT results only. Disagreement
   protocol (well-defined, cheap):
   | seq | cvc5 | verdict |
   |---|---|---|
   | sat | sat | cross-checked (report witness) |
   | sat | unsat | **HARD FAIL** — solver disagreement, manual triage |
   | unsat | sat | **HARD FAIL** — solver disagreement, manual triage |
   | either | unknown | no verdict from cvc5 — seq result stands (cvc5 is also incomplete) |
   | n/a | absent | cross-check skipped (recorded in report) |
   Absence ≠ disagreement: probe fixtures / `triage_fallback` semantics keep stock
   environments green.
4. **NDJSON**: additive `backend` (+ `cross_check` verdict) field per record;
   schema_version stays 1 (additive = backward compatible).
5. **CI**: optional job downloading pinned z3-noodler release asset + sha256 pin; cvc5
   wheel in a separate job; availability failures degrade to probe-fixture state.

## Open questions — the investigation agenda (spike before design finalization)

- **Q1 SMT2 round-trip parity:** does a `sexpr()` dump fed to the Noodler CLI reproduce
  stock-z3's sat/unsat/unknown on a matrix of the 5 canonical shapes? Does the dump need
  `(set-logic ...)` / option wrappers Noodler's CLI requires? (Parity matrix = P1/P2/P3/
  P4/shape-5 shapes, both outcomes + one known-timeout.)
- **Q2 Model/witness round-trip:** parse Noodler's `(model ...)` output back into the
  harness `witness` dict with `z3_str` escape-decoding so `--require-ground-truth`
  replay still works on Noodler-sat witnesses.
- **Q3 `from_ecma2020` subset boundary:** which JS features convert (lookahead yes —
  the fwlive blocker; backrefs/named groups/`m`/`u`/`g`/`y`/`d` flags?). The repo
  rejects `m/u/v/g/y/d` for its own ecma compiler (TRAPS #22) and caps pattern length
  at 256 (TRAPS #21) — does the Noodler route bypass or inherit those gates? Auto-route
  must be **fail-explicit** per pattern (subset check), never silent.
- **Q4 Does Noodler actually rescue the repo's known timeouts?** PLAYBOOK's measured
  timeouts (len≤64 whitelist queries, monolithic image proofs) through the Noodler
  binary — if it doesn't beat `seq` on these, the escalation's value is ECMA-only and
  the ticket shrinks to the fwlive path.
- **Q5 cvc5 feasibility:** pip wheel on py3.13/ubuntu-latest? Version? Theory surface
  overlap for the ops the harness uses (`IndexOf`, `SubString`, `Contains`, `Loop`,
  `Intersect`, `Star(AllChar)` prefix mirrors) — determines dual-encoding cost vs a
  shared-encoding path. cvc5 regex+length is itself incomplete: confirm its `unknown`
  behavior on the repo's shapes so the protocol row is real, not aspirational.
- **Q6 Effort calibration:** asset download size, binary runtime per query (startup
  overhead × per-property invocation vs batch reuse), CI wall-clock impact.

## Non-goals

- **No blanket auto-escalation on any `unknown`** — it would mask the decomposition
  discipline (P4 measured: monolithic 30s timeout → alphabet form 0.4ms; a bigger
  solver is not the fix for an un-decomposed encoding). Escalation only on
  `decomposition_exhausted` opt-in.
- No z3str3 revival of any kind (VF-002).
- No solver integration into fwlive — fwlive #120 remains a scan; this ticket only
  equips the scanner.
- No vendoring of the Noodler binary into the repo (license + size); pinned download
  only.
- No change to the `unknown` = hard-fail contract for stock `seq` results.
- No new theory (this is two implementations of one SMT-LIB theory, not a second theory).

## Proposed phases (effort S/M/L, to be calibrated by the spike)

| Phase | Scope | Depends | Effort |
|---|---|---|---|
| P1 | Spike: Q1–Q6 (SMT2 parity matrix, model parsing, from_ecma2020 subset, Noodler-vs-timeout measurements, cvc5 wheel + surface, asset size/runtime) | — | M |
| P2 | Harness plumbing: `backend`/`dialect`/`decomposition_exhausted` registry fields, Noodler CLI runner (subprocess `timeout=` per #171), fail-explicit absence, NDJSON `backend` field | P1 | M |
| P3 | cvc5 `--cross-check` for finding kinds + disagreement protocol + report field | P1 | M |
| P4 | CI jobs (pinned Noodler asset + sha256; cvc5 wheel), probe-fixture refresh, BACKENDS.md update (prebuilt-asset fact, z3str3 precision fix, "two implementations" framing), TRAPS/CHANGELOG | P2, P3 | S |
| P5 | fwlive handoff: ECMA-direct properties for the fwlive #120 scan use the new path (separate from #120's own work) | P2–P4 | S |

## Draft falsifiable ACs (per-phase, to be finalized at plan review)

- **P1:** parity matrix committed: every shape reproduces stock-z3's verdict through the
  Noodler CLI (or a committed list of documented divergences with reasons); Q3 subset
  table committed; Q4 wall-clock table committed; Q5 wheel+surface verdict committed.
- **P2:** a `backend="noodler"` property runs the real binary and reports a verdict
  through the normal result path; binary absent → `triage_fallback` recorded, exit code
  unchanged from stock behavior; NDJSON records carry `backend`; no subprocess without
  `timeout=` (grep-checked like #171).
- **P3:** disagreement protocol unit-tested with a synthetic disagreement (two solvers
  forced to differ on a fixture) → HARD FAIL + non-zero exit; cvc5-absent runs skip
  cleanly; report field present in `--json`.
- **P4:** CI job downloads pinned asset with sha256 verification; stock-only CI job
  stays green without Noodler/cvc5 (probe fixture `available: false` path intact);
  BACKENDS.md updated (prebuilt assets + z3str3 precision + implementations framing).
- **P5:** fwlive classifier's ECMA-direct properties (or a faithful fixture subset)
  run through the Noodler path in a committed pilot; results land in the #120 scan
  pipeline, not in fwlive.

## Cross-cutting gates

- Ground-truth every SAT witness — **including Noodler-sat and cvc5-cross-checked
  ones** (`--require-ground-truth` applies to every backend).
- TIMEOUT/not-proven = hard failure, non-zero exit, every backend and every pilot (#186).
- Every backend invocation: subprocess `timeout=` (#171), sha256-pinned binary,
  version recorded in `engine_versions`.
- Backend absence is recorded state (probe fixture), never a failure and never a skip.
- Disagreement = hard fail requiring manual triage (the extension of the existing
  unknown-policy that this ticket's proposal #3 rests on).
