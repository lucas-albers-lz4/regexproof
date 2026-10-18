# Issue #571 — proof-route reconciliation (decision required)

## Status and authority

**Plan + finite diagnostic only; #571's as-written formal proof is blocked, not
implemented or satisfied.** No backend routing, harness registration, classifier
runtime, or external repository changes are proposed by this patch.

Read the issue and its latest comment via GitHub on this investigation:
[issue #571](https://github.com/lucas-albers-lz4/regexproof/issues/571), including
the owner's **2026-09-06 scope-conflict comment**. The body requires
`re.from_ecma2020` / Noodler for `/i` patterns **as written**, explicitly excludes
2^n ASCII-case enumeration, and requests solver witnesses for fwlive F3.
The comment correctly distinguishes a running binary from an ECMA proof route.
[Issue #212](https://github.com/lucas-albers-lz4/regexproof/issues/212) was closed
2026-08-12 as **planning complete**, not authority to reverse U9.

[BACKENDS.md U9](BACKENDS.md#u9-scope-note-phase-14-228220--normative) takes
precedence over earlier general recommendations in BACKENDS, SEMANTICS, and
`properties/fwlive-classifier.md` to use `from_ecma2020`. All current harness
routes remain **mirror**. Merely selecting `backend="noodler"` does not satisfy
this issue: `_run_one_noodler` builds stock-z3py constraints, sends `s.sexpr()`
to the CLI, and records `route="mirror"` (`regexproof/harness/core.py:341–377`).
That function's route block was inspected but not edited; unrelated dirty
changes elsewhere in that file were left alone.

There is a legitimate reconciliation question, not just an outright dismissal:
[`u9-decision.md`](../sweep/harness-backends/p1-baseline/u9-decision.md) expressly
allows re-evaluation **when a consumer requests as-written audit output**.
#571 is such a request and challenges historical condition (b), “no consumer
needs ECMA-as-written output.” This warrants a human scope review; it does
**not** authorize implementing the dropped route ahead of that review.

## Current inventory and evidence

Investigation base: regexproof HEAD `af45bfd5b6fca916e3c17a00881b8eb28729c9a9`.
The adjacent fwlive checkout was read only: HEAD
`20c6ef541cfec12bf95f32cd646c0a55178caaac`; source file SHA256
`f48229cf0db6418ff5456efd5d2aa318f87b49160fff628b17764a5569f5860c`.
The checkout contains unrelated dirty files; it is not claimed to be a pristine
release checkout. The diagnostic records the bytes actually loaded.

| Site in `fwlive/core/fwlive-log.js` | Current semantics / risk |
| --- | --- |
| `wordPattern`, lines 41–44; `ACTION_RE`, 58 | `(^|[^A-Za-z0-9_])(ACCEPT|ALLOW|PASS|DROP|REJECT|DENY|BLOCK)([^A-Za-z0-9_]|$)`, `/i`, no `/u`; `detectAction` uses first match group 2 at 98–100 |
| `DENY_ACTION`, 61 | Same explicit boundaries, `DROP|REJECT|DENY|BLOCK`; search membership, not Unicode whole-word matching |
| `NON_FIREWALL_PREFIX`, 52–56 | Anchored daemon alternation; trailing boundary excludes **hyphen** as well as alnum/underscore; `wpad-drop` is not a daemon tag |
| `TCP_FLAG_TAIL`, 74 | `\b`, eight tokens `SYN|ACK|FIN|RST|PSH|URG|ECE|CWR`, repeated flag run, optional trailer KVs, `\s*$`, `/i`; `parseFlags` at 270–280 returns **group 1**, normalized to uppercase comma-separated flags |
| `FIREWALL_HINT`, 57 (stretch) | Explicit word boundaries around `fw4|nft|iptables|kernel|firewall`, `/i` |
| `DENY_ACTION_UNDERSCORE`, 64–67 | Separate current helper: changes underscore treatment; not the requested `DENY_ACTION` proof |
| `NETFILTER_KV_GLUE`, 75 | `/g` lookahead substitution; outside requested `/i` targets; membership is not replacement correctness |

The existing inventory's ECMA-direct routing statements are **historical intent,
not current permission**. Its generic TCP-tail description omits the current
trailer-KV capture requirement. No shared inventory was edited: this issue-local
document supplies the reconciliation without changing another agent's surface.

The historical pilot is not fresh evidence for these current source bytes:

* `sweep/harness-backends/ecma_pilot.py` snapshots 2026-08-11 patterns. Its TCP
  tokens omit **ECE/CWR**, it lacks trailer KVs, and its daemon boundary lacks
  the current hyphen exclusion. Re-running it unchanged would probe stale rules.
* Its R2 route rewrites `/i` words to per-character ASCII classes **before**
  `from_ecma2020` and wraps them with `.*`. This is not parsing the unchanged
  source with its original flag semantics. The historical label “as-written
  diagnostic route” cannot be promoted into the proof requested here.
* `p1-baseline/ecma-pilot.md` reports 937 strings × 6 patterns, 163 ECMA
  abstentions, and zero divergences on decided cases. Those are corpus results,
  not universal equivalence; abstentions must be excluded from decided counts.
* `p1-baseline/u9-decision.md` explicitly says five patterns have **regression
  parity, no solver-level equivalence theorem**. The ASCII E2M theorem is for
  the lookahead pattern only. Negated `from_ecma2020` membership aborts (`rc=-6`)
  in its recorded measurements, so reverse inclusion is regression-only.
* U9 also records no flag representation and silent property-escape
  literalization. `p_gate.py` rejects real `\p{`/`\P{` tokens at registration;
  that policy must survive any future scope revision. Node non-/u identity
  escapes and actual `/u` Unicode properties must not be conflated.

Fresh feasibility check during this continuation: downloaded the SHA-pinned
Noodler v1.6.1 binary to `/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared`
(sha256 `22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464`)
and ran `sweep/harness-backends/preflight.py`. All preflight checks passed:
#316/#325 SAT regressions, #344 timeout containment, version, and determinism.
This verifies binary identity/runtime, **not** ECMA `/i` flag fidelity. Two
SMT probes confirm the gap: `re.from_ecma2020` on the source-shaped ACTION
pattern returned `unsat` for `aCcEpT`; an explicitly ASCII-expanded pattern
returned `sat`. The second query is a rewritten pattern, not an as-written
proof, and cannot be silently promoted as one. No harness route or property
was added. Local Z3 is **5.0.0** and Node is **v26.11.1**.

fwlive `scripts/z3-verify.py:121–137` still constructs `_both_cases` with
original/lower/upper tokens. Its fixed mixed-case corpus is explicitly outside
F2's finite token model and queued for F3. These are complementary gates, not
an arbitrary mixed-case formal proof. F2's space/tab model also does not cover
all real JS `\s` inputs.

## Human decisions: three options, not interchangeable deliverables

1. **Preserve the original goal; formally reconsider U9 first.** Recommended if
   the user continues to require as-written `/i` semantics. Ask the owner to
   authorize a separate, isolated backend feasibility/authority gate. Freeze
   source bytes and properties, specify how original flags are represented,
   then obtain fresh positive/negative membership, exact-boundary, whitespace,
   Unicode, crash/timeout, and property-escape measurements on a SHA-pinned
   binary. Do not manufacture flag support by rewriting the pattern and still
   call it as-written. If original `/i` cannot be represented faithfully,
   record **no-go**, not completion. Fresh measurements alone do not amend U9:
   owner approval plus an explicit normative policy change precede harness work.
2. **Owner explicitly accepts a mirror proof instead.** U9-compatible, but a
   change to #571's goal/non-goals, not an implementation of the current issue.
   Per-character case-fold unions can model arbitrary ASCII mixtures without
   generating every whole-word permutation. The comment calls this “U4 ASCII
   case-expansion”; whichever encoding is chosen remains a mirror, with a
   separately declared domain and independently evidenced equivalence. The
   existing non-/u fold implementation does not by itself prove all JS UTF-16
   semantics, captures, anchors, or whitespace. No such mirror is shipped here.
3. **Owner narrows to differential parity only.** Retain F2 + F3, refresh source
   inventory and extend finite mixed-case/boundary/trailer/Unicode cases. Report
   corpus size and actual JS / shell / BusyBox engines; leave the universal
   formal requirement explicitly deferred. This is useful regression work,
   **not** the as-written proof or solver-generated counterexample deliverable.

## Contract and implementation sequence after a decision

The issue supplies human intent, but not yet an unambiguous per-site theorem.
The following are **agent-derived contract proposals**, not counted products
until the owner adopts them (`CONTRACTS.md`):

* Input source: untrusted firewall log message strings. Separate raw regex
  input from normalized classifier input and declare any preprocessing.
* ACTION/DENY/HINT: search membership iff an allowed case-insensitive token
  exists at the actual explicit boundaries. ACTION capture correctness needs
  the earliest JS match/group 2, not just membership. “Whole-word” must retain
  underscore and non-ASCII behavior of the actual pattern.
* PREFIX: prefix membership iff a listed daemon starts at offset zero and is
  followed by the allowed boundary/end. Include the hyphen exclusion.
* TCP tail: search membership plus correct group-1 final flag run, excluding
  trailer KVs; distinguish `parseFlags` KV overrides from the regex branch.
* Domain: obtain a human choice between unrestricted JS UTF-16 strings and a
  justified restricted domain. ASCII is not an established input restriction
  for untrusted log messages; an ASCII theorem is only an ASCII theorem.
  Explicitly settle NUL, isolated surrogates, NBSP, JS line terminators, max
  length if bounded, and `/i` without `/u`. A solver length bound is proof
  coverage, not evidence that product inputs have that length.

Then: (a) snapshot current source/flags/call sites and contract provenance;
(b) ship the approved route in its own reviewed scope; (c) register invariants,
mutation guards per family, and counterexample finders with real Node replay;
(d) fail hard on unknown, crashes, missing proof engine, or non-reproducing SAT;
(e) preserve record domains, engine versions, route/authority, and `not_proven`;
(f) only replay-validated solver witnesses go to a separately authorized fwlive
F3 change under both real shell and BusyBox. No foreign repository changes here.
Do not label this diagnostic's fixed strings as Z3-generated witnesses.

Relevant traps: #1 single-character complements vs language complements;
#3 domain/NUL; #9 length bounds; #10 unknown is not SAT; #16 narrower `/i`
mirrors; #17/#25 word alphabets; #18 search-wrapped differences; #22 flags;
#26 whitespace; the escape-input and signal-death appendices. `SEMANTICS.md`
requires the actual `search`/`exec` call semantics: bare `InRe` is whole-string
membership, and language membership does not prove capture position/greediness.

## Shipped bounded diagnostic and verification

New files only:

* `scripts/issue571-diagnostic.js`: 28 fixed strings, each shorter than 64 JS
  code units, on the actual exported four regexes and `parseFlags(input, {})`.
  No pattern rewriting, ASCII-case enumeration, SMT, shell parity, or backend
  invocation. Prints JSON with source hash, Node version, actual pattern/flags,
  expected/observed results, `formal_proof:false` and `product:false`. Exit 1
  on mismatch or missing/wrong exports. TCP regex is not exported: its consumer
  is observed, not replaced by a synthetic copy.
* `tests/issue571-diagnostic.test.js`: mechanics tests using explicitly synthetic
  APIs; includes sensitivity to an always-accept boundary mutation, changed flags,
  missing exports, and CLI failure. These tests do not prove source fidelity.

The path is **trusted operator code**: `require()` executes the supplied module.
The diagnostic itself writes no files, but cannot guarantee that arbitrary
supplied code is read-only. Use the known fwlive core and an external wall bound:

```sh
node --test tests/issue571-diagnostic.test.js
timeout 10s node scripts/issue571-diagnostic.js ../fwlive/core/fwlive-log.js
.venv/bin/python -c 'import z3; print(z3.get_version_string())'
```

Observed after live replay: the initial diagnostic expectations for
`sYn window=1` and `ſsYn` were wrong; real `parseFlags` rejects both because the
regex requires a flag run ending at the tail and starts at `^` or whitespace.
The fixture was corrected to the actual source behavior (not to make the product
pass): `node scripts/issue571-diagnostic.js` now reports **28/28** observations
matching at current source hash
`52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12`, fwlive
HEAD `098f866155fb396a8c3dea855696374e8d45ea03`, Node **v26.11.1**. The four
synthetic mechanics tests pass. Examples: `aCcEpT` and `DrOp` match;
embedded/underscore variants do not; `wPaD-drop` is not a daemon;
`sYn eCe cWr` produces `SYN,ECE,CWR`; NBSP/U+2028 separate flags; lowercase
trailer keys are accepted under `/i`. U+017F is a boundary for the explicit
ASCII boundary class, but is not itself accepted as an ASCII flag letter.
These are finite observations, not proof of arbitrary mixed-case strings.

Refuted claims: the historical pilot is current inventory; enabling Noodler
makes the route ECMA-direct; zero corpus divergences proves equivalence;
original/lower/upper covers arbitrary `/i`; all JS whitespace is space/tab;
and the user-requested proof may silently be replaced with ASCII expansion.
**Remaining blockers:** human scope/contract decision, a faithful `/i` route
(or explicit owner-approved goal change), required contract/domain, proof of
search and capture semantics, and property/mutation/real-Node gates. Preflight
and direct probes are feasibility evidence only. No formal property result or
solver counterexample is reported; #571 remains not implemented/not satisfied.
