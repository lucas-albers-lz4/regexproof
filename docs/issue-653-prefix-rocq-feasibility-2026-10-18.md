# #653: prefix-guard Rocq feasibility

## Decision

**PARTIAL feasibility; NO-GO for an as-written proof claim, backend registration
or fwlive consumer gate from this spike.** A pinned Warblre/Rocq build is
practical here, and small kernel-checked facts and negative controls work.
The checked source parser and concrete full-UTF-16 semantic correspondence
required by [#653](https://github.com/lucas-albers-lz4/regexproof/issues/653)
are not delivered. No mirror substitute is adopted. The original
[#571](https://github.com/lucas-albers-lz4/regexproof/issues/571) goal remains
unresolved; U9, production pins, harness and fwlive checks are unchanged.

This is the authorized initial feasibility deliverable, not the universal
prefix theorem or an implementation of the remaining application properties.
The first boundary is the string **already supplied to NON_FIREWALL_PREFIX**;
raw-log normalization/classifyTrim and the full classifier remain outside it.
The snapshot and reproduction commands are in
[`sweep/issue-653/2026-10-18/`](../sweep/issue-653/2026-10-18/README.md).

## What ran

| Layer | Measured result | Limit |
| --- | --- | --- |
| Upstream Warblre proof example | Unmodified example built with Rocq 9.1.1 / Stdlib 9.0.0; independently rechecked by `rocqchk` | Parametric matching theorem, not concrete JavaScript correctness |
| Current fwlive source inventory | Frozen commit `aa1554730999de8cf3660f959c8ffd1e554b8992`, core and LuCI byte hashes, spec-derived source and original `i` flags agree | Identity and finite native observations, not source-to-AST proof |
| Native guard observations | 21 finite cases, actual core/LuCI regexes; two native mutation discriminators | Not exhaustive, not solver-generated witnesses; diagnostic reproduces the small trim loop |
| Hand-built prefix AST | Four computational facts: `WpAd[`, `wpad[`, `wpad-drop`, `xwpad[`; kernel checked and `rocqchk` rechecked | Upstream ASCII-oriented NaiveEngine, manually constructed AST; no original-source/full-UTF16 theorem |
| Canonicalize return logic | Non-ASCII input cannot yield ASCII; ASCII output requires ASCII input; two concrete examples; kernel checked and `rocqchk` rechecked | Abstract uppercase-UTF16-output function; not an implementation/correspondence proof of Unicode case conversion |
| Negative controls | Removing AST start anchor or hyphen continuation rejects the corresponding original equality; removing canonicalization guard rejects the 383→383 equality because it computes 83 | Controls show sensitivity of these particular artifacts, not completeness of a consumer proof |

`Print Assumptions` reports the four named research facts closed under the
global context. The canonicalization lemmas quantify over arbitrary
`upper_units`; they do not assume a correct Unicode implementation. Closed
facts about this definition do not establish that definition's external
specification correspondence. The upstream example quantifies over a parameter
record containing operations and their interface laws; its theorem is not an
instantiation of those laws with JavaScript operations.

## Source, domain and build provenance

The current native regex is:

```text
/^(dnsmasq|procd|ubusd|netifd|odhcpd|logd|dropbear|uhttpd|hostapd|wpad)([^A-Za-z0-9_-]|$)/i
```

The source hash remains `52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12`
for core and `efddb7eab758c5c86038248274fddf4ce1b2d7b6003e5d81cb423f1c151cc336`
for the LuCI mirror. The native script checks both before loading their code.
The guard accepts JavaScript strings, with no new ASCII restriction or length
bound. Examples retain NUL, lone surrogates, a supplementary pair, non-ASCII
boundaries, whitespace and mixed case as UTF-16 code units. The measured native runtime is Node 26.11.1, V8 14.6.202.34-node.37,
ICU 78.3 / Unicode 17.0. Its finite long-s-in-`dnsmasq` example is rejected
under the actual non-/u regex; it does not establish a Unicode-version bridge
to the Rocq model. These selected examples cannot establish full-domain correctness.

Foundation: [Warblre `87af3cc`](https://github.com/LindenRegex/Warblre/tree/87af3ccaea96015d4104c0b2d9de758fa8d9ee87),
confirmed current upstream HEAD at pilot start. Executed image:
`rocq/rocq-prover@sha256:9a1e969649a3cc3c6f310d5be5a842e2187384560337c6c0807aba9f8565efba`
(linux/amd64, Rocq 9.1.1, OCaml 4.14.2, Stdlib 9.0.0). Docker Hub release
metadata binds that image digest; it does not attest a reproducible compiler
build. The image's bundled Dune 3.21.1 initially rejected Warblre's 3.23 language
version. Bootstrapping [Dune 3.23.1, `6f6eee6`](https://github.com/ocaml/dune/tree/6f6eee69eda59e355bae2ca4e3ad1af678271883)
from pinned source resolved that without modifying Warblre. Proof invocations
have no network, four CPUs, 8 GiB and per-process timeouts. Source trees,
selected hashes, installed image packages, raw logs and all final command
statuses are retained in the snapshot; binaries/build trees are not committed.
No npm dependencies, OCaml/JavaScript extracted engine, or Linden engine was
built or adopted in this pilot.

## Missing bridges

### Parsing and generated source

Warblre's mechanization explicitly starts **after parsing**. Its
[JavaScript adapter](https://github.com/LindenRegex/Warblre/blob/87af3ccaea96015d4104c0b2d9de758fa8d9ee87/engines/js/Parser.ml)
uses external `@eslint-community/regexpp`, maps nodes to its AST and is not a
kernel-checked source parser. We inspected this adapter; we did not build or
execute it. Our AST explicitly transcribes the daemon vocabulary, two groups,
anchor, alternatives and boundary class. It does not certify its relation to
the exact source, including parse-tree association, redundant empty nodes,
generator inputs and supported syntax. Hashes bind bytes, not that relation.

A future route needs a checked bridge for this small generated grammar,
including rejection on source/spec/flag drift and a reviewed argument that
its admitted grammar and AST interpretation implement the ECMAScript syntax.
Running the existing generator, pretty-printing an AST, or having a parser
agree on examples alone is insufficient.

### Character parameters and mode

Warblre's [parameter interface](https://github.com/LindenRegex/Warblre/blob/87af3ccaea96015d4104c0b2d9de758fa8d9ee87/mechanization/spec/Parameters.v)
leaves character representation, canonicalization and set operations abstract.
Its [difference notes](https://github.com/LindenRegex/Warblre/blob/87af3ccaea96015d4104c0b2d9de758fa8d9ee87/doc/Differences.md)
explicitly describe minimal safety/termination laws, not complete
canonicalization correctness. The JavaScript adapter calls runtime
`toUpperCase` for non-Unicode-mode handling; that external code is not a proved
concrete parameter instantiation.

The existing Rocq `NaiveEngine` is ASCII-oriented and represents characters by
`nat`; it lowercases ASCII uppercase letters. The actual non-/u
[ECMA-262 2023 Canonicalize algorithm](https://tc39.es/ecma262/2023/multipage/text-processing.html#sec-runtime-semantics-canonicalize-ch)
uses Unicode uppercase plus length/non-ASCII return guards. These are different
functions. The AST's flag record has `i=true` and other represented booleans
false; the Unicode field is erased to `unit`, so `tt` does not prove a concrete
non-/u mode. **The AST probe and return-logic lemmas are not connected by a
proved refinement theorem.** No concrete UTF-16 type/range/case/character-set
parameter proof or specific Unicode table-version correspondence is supplied.
The adapter's separate `/u` SimpleFold table is not evidence for this goal.

There is a promising reduction, but it is not yet a result: this regex's
literals and excluded boundary characters are ASCII, and the return-logic
lemma rules out non-ASCII-to-ASCII conversion for an arbitrary uppercase
function. A future proof may avoid enumerating every non-ASCII uppercase
mapping by proving that only ASCII canonicalization classes are observable
by this grammar. It must still prove the ASCII cases, character-set operations,
valid UTF-16 representation and matching/refinement argument. A manually
expanded ASCII case mirror without that argument remains outside the approved
goal.

## Criteria disposition and next decision

| Initial criterion | Disposition |
| --- | --- |
| Pinned foundation/toolchain and built upstream example | Pass for the isolated research build; compiler/image trust explicit |
| Frozen actual source/spec/flags/call site | Pass as inventory and finite native evidence |
| Checked source-to-AST correspondence | Not delivered; no as-written claim |
| Concrete full non-/u UTF-16/canonicalization correspondence | Not delivered; one independent return-logic sublemma only |
| Faithful application matching fact under original semantics | Partial only: finite hand-built AST/ASCII-engine facts; not a pass for the requested concrete bridge |
| Reviewed report with limits/cost/disposition | This report; exact-head review recorded on its PR |

The useful next scope is **bridge development**, not another backend version
bump or automatic consumer registration: implement a restricted source checker,
prove its AST mapping, and construct a concrete or proved observational
character refinement for this one grammar before attempting its universal
boolean-guard theorem. This is several proof-development tasks, not a
configuration change; no measured implementation estimate is justified by the
small computational examples. Maintenance includes source-drift rejection,
Rocq/library compatibility and any admitted semantics/Unicode-version contract.
A separate reviewed implementation plan is required before that expansion.

The pilot does not reopen fwlive's closed prefix-model finding or change its
wontfix disposition. It produces no new product counterexample or vulnerability
claim. If bridge cost is not justified, stopping at this reviewed partial
research outcome is valid; #571 remains unresolved.
