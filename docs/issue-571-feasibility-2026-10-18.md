# #571 as-written route feasibility — 2026-10-18

Status: investigation in progress; no new harness route or proof result.

Authority: the owner's [option 1 decision](https://github.com/lucas-albers-lz4/regexproof/issues/571#issuecomment-6251434208)
retains the original source/flags goal. The [new investigation comment](https://github.com/lucas-albers-lz4/regexproof/issues/571#issuecomment-6251737316)
provides a pinned Noodler limitation and finite diagnostic baseline; it does not
satisfy the issue or amend U9. This continuation evaluates the remaining route
question rather than relabeling that baseline as a proof.

## Precommitted criteria and time box

Initial spike: at most 60 minutes from the start of this continuation. Compare:
actual source and flags; non-/u ignore-case semantics over UTF-16; original
search and capture/first-match behavior; unsupported-input rejection;
negative-membership reliability; independently justified semantic correspondence;
reproducible pinning; toolchain and maintenance cost. A decided corpus alone is
not correspondence. Backend errors/unknown/timeouts are not proof success.
No automatic fallback to an ASCII mirror or differential-only scope.

Deliver an independently reviewed go/no-go/partial disposition, with the
undischarged obligations named. Current U9 and all consumer gates stay in force
until a separately reviewed policy/implementation change is warranted.

## Frozen source and independent contract inventory

fwlive source SHA-256:
`52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12`;
Git blob `cc77bc663fc1bae0b2cb473eca2f10b2eedc2079`. The source is identical
through the B/E merges; full commit provenance is in each retained baseline.
Node is v26.11.1. `source-inventory.json` records native patterns and original
flags plus **finite observations**, with NUL, isolated UTF-16 surrogates,
non-ASCII boundaries, NBSP/U+2028 and captures/first-match positions.

| Consumer | Required distinction |
| --- | --- |
| ACTION_RE | `/i`, explicit ASCII boundaries; first match/group 2 after `messageForDetectAction` and `stripKvSpans`, not whole-string membership |
| DENY_ACTION | Exported `/i` regex; do not infer the full production deny classifier from this export alone (underscore handling is separate) |
| NON_FIREWALL_PREFIX | Anchored `/i`; trailing class excludes hyphen as well as ASCII alnum/underscore |
| TCP_FLAG_TAIL | Non-exported source literal at `core/fwlive-log.js:159`; `parseFlags` applies it after KV stripping unless KV flags override; group 1, whitespace, optional OPT suffix and final anchor matter |
| FIREWALL_HINT | Optional stretch, `/i` boolean search with explicit boundaries |

The independently specified desired contracts remain provisional, not registered
product results: ACTION must return the earliest eligible verdict token;
prefix recognition must retain the exact daemon boundary; TCP must return the
final eligible captured flag sequence according to the actual preprocessing.
Raw-regex language membership alone does not prove these consumer contracts.
No input restriction to ASCII or a maximum message length has been adopted.

## Current tool comparison

The newly discovered upstream release **v1.8.0 was published 2026-10-18**;
it was investigated separately rather than assuming the 2026-08 U9 measurements
still describe every current result. The production harness pin was not changed. The [upstream release](https://github.com/VeriFIT/z3-noodler/releases/tag/v1.8.0) and its asset digest were read through the GitHub API.

| Research binary | Verified SHA-256 |
| --- | --- |
| Existing v1.6.1 | `22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464` |
| Candidate v1.8.0 | `4a39a2b9e9066a8bfbe8b5363a85de82e43e27688b7dff456f4cd577bb47bab6` |

The v1.8.0 digest was checked against the upstream GitHub release asset before
execution. It reports Z3 5.1.0, build `06e5c132a1a59fb61eaf4e5f7094860b5aec7c21`.
That is also the inspected source revision. The project releases include ECMA
capture/lookaround, whitespace/dot, input-reading and crash fixes; these changes
do not imply support for JavaScript flags.

The inspected source still declares a **one-argument** `re.from_ecma2020`
(`src/ast/seq_decl_plugin.cpp:259`). Its ECMA compiler explicitly says flags are
unsupported (`src/smt/theory_str_noodler/ecma_regex.cpp:1611`); the group lexer
accepts non-capturing/lookaround/named groups but rejects `(?i:...)`. These
observations are about that revision, not all future releases.

| Exact bounded diagnostic | v1.6.1 | v1.8.0 |
| --- | --- | --- |
| Original ACTION source, fixed `ACCEPT` | SAT | SIGABRT / `map::at` |
| Original ACTION source, fixed `aCcEpT` | UNSAT | UNSAT |
| Explicit ASCII rewrite, fixed `aCcEpT` | SAT | SIGABRT / `map::at` |
| Attempt to pass original `i` as a second converter argument | Parser/type error | Parser/type error |
| Inline `(?i)` attempt (not an original-source proof) | unknown | unknown |
| Negated ACTION membership, fixed `ACCEPT` | UNSAT | UNSAT |
| Negated ACTION membership, unconstrained input | 8-second timeout | SAT |
| Difference of ASCII rewrite vs source converter | 8-second timeout | SAT |
| Historical lookahead/negation control (not current source) | SIGABRT | SIGABRT |
| `^\p{L}$`, fixed literal `p{L}`, no flag supplied | SAT | SAT |
| Same pattern, fixed `A`, no flag supplied | UNSAT | UNSAT |
| Attempt to pass `u` as a second converter argument | Parser/type error | Parser/type error |
| `^.$`, fixed astral character, generic capability control | UNSAT | UNSAT |

Native Node accepts both `ACCEPT` and `aCcEpT` under the original `/i` regex.
The fixed-input mismatch is a **backend/flags mismatch**, not a fwlive bug or
a solver-generated application counterexample. The rewrite is explicitly a
mirror control. SAT above is only a diagnostic solver status; no new product
witness or theorem is claimed. Unknown/timeouts/crashes remain not proven.
The unconstrained negation result improved in v1.8.0; the old crash claim is
reproduced only for the separately labeled historical control, not asserted
for every negative query. Core dumps are disabled and subprocess groups have
an eight-second timeout.

The property-escape controls are intentionally mode-aware: native Node without
`u` treats `\p{L}` as the identity-escape/literal form, and both tested converters
agree on those two fixed strings. That agreement is **not** a Unicode-property
proof or evidence of silent miscompilation of a supplied `/u` flag: the API
cannot accept that flag. Node with `u` gives the opposite fixed-string results.
The one astral-dot result agrees with native non-/u Node, but one case does not
establish a complete UTF-16 correspondence. The existing registration guard
against unsupported property escapes is unchanged.

## Faithful alternative survey

We inspected pinned public primary sources, not just generic claims about
verified engines:

- [Warblre, revision 87af3cc](https://github.com/LindenRegex/Warblre/tree/87af3ccaea96015d4104c0b2d9de758fa8d9ee87)
  provides a Rocq mechanization with captures and an explicit ignore-case record.
  Its [README](https://github.com/LindenRegex/Warblre/blob/87af3ccaea96015d4104c0b2d9de758fa8d9ee87/README.md)
  states that parsing is outside the mechanization and character operations
  depend on external parameters. Its
  [abstraction notes](https://github.com/LindenRegex/Warblre/blob/87af3ccaea96015d4104c0b2d9de758fa8d9ee87/doc/Differences.md)
  leave concrete canonicalization outside the proved core. Project-specific
  source-to-AST and UTF-16/case/whitespace parameter correspondence are therefore
  still needed for this issue's claim. Its example proves a matching fact;
  it is not a ready-made fwlive classifier property suite.
- [Linden, revision 8454dcb](https://github.com/LindenRegex/Linden/tree/8454dcb1ae35fc4ec4568fbe511933ccc1b3a09b)
  supplies mechanized semantics/equivalence and a proved engine for a subset.
  This is a plausible foundation for a dedicated proof development, not an
  already checked fwlive source/flags contract or a drop-in SMT backend.

No Rocq/opam toolchain was available on the investigation host. Neither project
was built or adopted; the survey is source inspection, **not** an executed
alternative-backend feasibility claim. No third-party engine correctness claim
is inferred from its test corpus. This alternative would require a separately
pinned proof adapter and kernel-checked fwlive theorems with explicit trust
assumptions; it cannot be promoted merely by translating patterns manually.

## Obligation disposition

| Required obligation | Current status |
| --- | --- |
| Original source and flags reach a faithful backend | **Failed** for both investigated Noodler binaries: `/i` mismatch |
| Search vs full membership and anchors | Source/call sites inventoried; universal correspondence **not discharged** |
| Captures/earliest match and preprocessing | Inventoried and native examples recorded; universal consumer theorem **not discharged** |
| Full non-/u UTF-16, NUL, surrogates, whitespace/case semantics | Finite native observations only; backend correspondence **not discharged** |
| Reliable negated queries / unsupported constructs | Mixed version-specific diagnostics; crashes/timeouts are **not proven** |
| Reproducible tool/source pins and contained diagnostics | Recorded research evidence; **not a product proof** |

**Proposed disposition: NO-GO for implementing a maintained as-written harness
route from this spike.** This decision is narrower than claiming that the goal
is impossible: the specific current route fails an essential flag condition,
and the proof-oriented alternative still lacks the application-specific bridge.
The spike completed within its initial 60-minute limit; it did not stop because
a finite corpus happened to agree.

Keep #571's original goal open and U9 unchanged. No fwlive proof consumer is
introduced. Existing F1–F5 checks remain its current evidence. An ASCII mirror
would require an explicit owner-approved scope change; it has not been adopted.
A further as-written attempt can instead propose a dedicated Rocq development:
freeze source/flags, check the source-to-AST bridge, justify concrete non-/u
character parameters, define independent consumer contracts, and prove the
per-site properties before registering any result. That is a new reviewed
implementation scope, not a backend version bump.

## Reproduction and retained evidence

See [the research snapshot](../sweep/issue-571/2026-10-18/README.md) for explicit
source/binary pins, environment variables, bounded commands, original SMT files,
per-case result JSON containing raw stdout/stderr strings, and the comparison index. All 13 cases
have identical SMT hashes across the two versions. The standalone driver and
bundled prior 28-row diagnostic do not depend on unmerged local files. A failed
pin is rejected before backend execution; every query also verifies source,
binary and runner identity against its initialized baseline. No binary or core
dump is committed, and no research script is wired into the harness or CI.

Independent final-head review: pending. No proof completion is claimed.
