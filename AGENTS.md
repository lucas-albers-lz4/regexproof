# regexproof — AGENTS.md

Instructions for **coding agents** (Hermes, Claude Code, Codex, opencode) that
want to use this repo to improve the security of regex-based code. Read
`docs/` only as needed — this file is the decision tree.

## When to use this repo

Use it when the code you are working on (or reviewing) has **regexes on
security boundaries**:

- input validators / whitelists / deny-lists (usernames, actors, IP-shaped
  gates, allowed-charset checks)
- sanitizers / escapers (JSON escaping, shell quoting, audit-line shaping)
- parsers with regex fallbacks (sed/awk capture groups, classifier patterns)
- anything where the question is **"is there ANY string that, after this
  regex runs, violates the boundary?"**

Do NOT use Z3 for:

- **ReDoS / catastrophic backtracking** — that is complexity analysis of the
  *matching engine*, not language membership. Use `recheck`,
  `safe-regex2`, or `vuln-regex-detector` (see `docs/REDOS.md`).
- **Lookaheads / lookbehinds / backreferences as written** — not expressible
  in Z3's regular-language theory. Rewrite to string ops, or route JS patterns
  through Z3-Noodler's `re.from_ecma2020` (`docs/BACKENDS.md`).
  Variable-width lookbehinds (`(?<=^)` under `re.MULTILINE`) get the
  IndexOf/SubString/CharAt rewrite in `docs/LOOKBEHIND_REWRITE.md`.
- **Dynamic compiles** (`re.compile` with interpolated values) — cannot be
  proven as written. Classify the site (constant / escaped / raw-config)
  and prove the right thing per `docs/DYNAMIC.md`; an unescaped
  config-supplied pattern is a finding, not a proof.
- Cosmetic/internal patterns with no untrusted input — skip them; low value.

## Property-contract precondition

Do not count an UNSAT (or a synthesized SAT) as a **product** result unless
the site has a contract: the guarantee you actually care about, the input
source and trust class, declared domain, and provenance
([`docs/CONTRACTS.md`](docs/CONTRACTS.md)). Untargeted
shape-1/2 synthesis ("does this class contain a space?") is compiler smoke.
Shape-5 `rule_diff` still needs an independent spec or a
`version_diff` / `cross_engine` pair with a `family_contract` — sibling-family
pairing is not a contract.

Phase 0 search-semantics inventory of the ten SAT candidates that looked like
third-party findings: **2 remain filing candidates** (CRS 942220 version-diff,
cross-engine 920210). The other eight are spec-gap or collapse under search.

## The 5-step workflow (follow in order)

### 1. Inventory the regex surface
Find every regex on the boundary. Classify by input trust:
`untrusted-input > config > internal`. Only boundary regexes get properties.
Record each with: file:line, the pattern, what input feeds it, and the
*property you actually care about* (for example, "no `;` can reach the shell",
"the capture never truncates an escaped quote").

### 2. Classify the property, pick the shape
From `scripts/z3-property-template.py`, the canonical shapes:

| Shape | Question | Encoding | Expect |
|---|---|---|---|
| 1. Alphabet disjointness | "accepted strings contain no char X" | single-char `InRe(c, class) ∧ c == bad` | instant, no length bound — **prefer this** |
| 2. Whitelist exclusion | "a whitelisted string (len-bounded) contains no X" | `InRe(s, wl) ∧ len(s) ∈ [a,b] → ¬Contains(s, X)` | length bound is load-bearing (≤16 instant, ≤64 times out) |
| 3. Counterexample finder | "is there a value where capture ≠ true value?" | string ops: `IndexOf`/`SubString` | SAT + witness = the bug repro — cheapest, most valuable |
| 4. Per-token image | "escape output has no raw control chars" | one token per tiny solver query | monolithic image-regex TIMEOUTs — decompose |
| 5. Rule diff (`rule_diff`) | "does R2 accept anything R1 misses?" | `InRe(s, R2) ∧ Not(InRe(s, R1))` (no regex Complement) | SAT = gap; UNSAT = no gap in bound; TIMEOUT ≠ pass |

Shape-5 registry/`kind`/`family`/mutation-guard contract:
[`docs/examples/shape5-rule_diff.md`](docs/examples/shape5-rule_diff.md).
Dialect/`call_kind`/fold tables: [`docs/SEMANTICS.md`](docs/SEMANTICS.md).

### 3. Encode — read `docs/TRAPS.md` first
The traps cost real debugging time. Minimum set:
- `Complement()` is **language** complement, not char-class negation.
  `Star(Complement(Re('"')))` ≠ `[^\"]*`. Use `Range`/`Union` or string ops.
- Never set `smt.string_solver=z3str3` for regex work — it returns `unknown`
  instantly on `InRe`. Default `seq` backend is the one that solves.
- Mirror the real code **exactly**: deny-lists verbatim, length checks,
  char classes. "root" matches the username regex; only the deny-list
  excludes it.
- State input-domain assumptions as constraints + comments (for example,
  *POSIX
  shell strings cannot contain NUL*).
- `re.replace_re` / `str.replace_all` are unsupported — model with string ops.

### 4. Ground-truth every witness
A Z3 model is a *mirror*; SAT means "the mirror says there's a counterexample".
Before reporting it:
1. Run the **real implementation** on the witness (real `sed`, real JS, real
   Python `re`) and confirm behavior matches the model byte-for-byte.
2. If the target runs BusyBox (OpenWrt), verify under `busybox sed` too —
   pin `busybox` in CI for device fidelity.
3. **Presence-gates use whole-word grep** (`grep -wc`) — substring matches
   lie ("sed" matches "passed"). See TRAPS.md #12.
4. Enumerate refuted reviewer/model claims in your report — a digest that
   says what was checked and what was disproven is what makes a proof
   trustworthy. This includes your own claims: read the surrounding code
   before filing a finding (the pilot flagged an interpolated regex as
   un-escaped when `re.escape` was already two lines above).

### 5. Make it a regression gate
- Ship as a runnable script + CI job (`pip install z3-solver`; **TIMEOUT
  (`unknown`) = hard failure / not proven**, never a silent skip).
- Add **mutation guards**: a tagged property that weakens the regex and
  asserts the result flips UNSAT→SAT. A harness that can't fail proves
  nothing. Run them in `--all`, always. The harness enforces coverage: every
  family with a security property must have at least one mutation guard
  (`check_mutation_coverage()` warns and exits non-zero otherwise).
- Add **differential fuzz** for transformation properties: random inputs →
  mirror accept/reject vs real implementation accept/reject must agree.
  Mutation guards prove the mirror is sensitive; differential fuzz proves
  mirror ≡ real code. **`scripts/differential-fuzz.py` implements this**:
  give it a Z3 mirror expression + a real command (`grep -qE`, `sed`,
  `busybox`, …) and it fuzzes exhaustive short strings, random strings, and
  dangerous-char mutations, failing on any disagreement. The mirror is a Z3
  **expression**, not a pattern string — `z3.Re("...")` is a literal match.
- **Ground-truth every SAT witness in code, not just in prose**: give each
  counterexample-finding property a `ground_truth=` callback that runs the
  real implementation on the witness, and run the harness with
  `--require-ground-truth`. An unverified (or non-reproducing) witness is a
  hard failure — an unverified counterexample is never reported as a
  vulnerability. (The P3 sed-capture and P4-NUL properties ship real
  replay callbacks.)
- **Tag every property with `kind=`**: `property` (invariant must hold),
  `counterexample_finder` (SAT is the finding), `mutation_guard` (SAT proves
  sensitivity), `bug_demo` (SAT demonstrates a known bug), `rule_diff`
  (shape-5 gap query). The `kind` field is what makes `expect_unsat=False`
  unambiguous and lets the coverage check reason about the registry.
  Scanner NDJSON also uses finding kinds `redos`, `usage_mismatch`,
  `intent_mismatch`, `triage` — see `docs/REPORTING.md`.
- Pin `z3-solver==5.0.0` — the `Re()`/regex API changed across 4.x/5.x.
  The harness refuses to run (exit 3) on any non-5.0.x solver.
- **Machine-readable output (NDJSON contract — must match CLI help):**
  `z3-verify.py --json` emits one NDJSON object per property
  (`schema_version`, result, witness, ground-truth, domain, wall_ms,
  `engine_versions`, `not_proven`). Same facts as the human report — the two
  reports can never disagree. Partial streams remain valid if a later
  property fails. Mutually exclusive with `--json-legacy`.
  `--json-legacy` emits a single JSON array of the same records (one-release
  compat). Mutually exclusive with `--json`.
- **Triage / batch reports:** `properties/triage/<repo>.ndjson` and
  `properties/generated/<repo>.ndjson` (+ `*_batch.md`). Field contracts:
  [`docs/REPORTING.md`](docs/REPORTING.md). Deterministic sort by `regex_id`.
- **Disclosure:** security-tool findings are `private_first` — see
  [`SECURITY.md`](SECURITY.md).

## Report shape

For each property report: the pattern (file:line), the property, the declared
domain (what exactly was proven — a length bound means "proven up to this
length", not "inputs are this length"), result (UNSAT=holds / SAT=witness /
TIMEOUT=not proven / hard fail), ground-truth evidence, and engine versions.

Prefer **alphabet-level, length-independent proofs** wherever the property
allows: they cover ALL strings with no bound at all. Use length bounds only
for genuinely length-sensitive properties, and document the declared domain
in the harness output so a reader knows exactly what was proven.

## Worked examples in this repo

- `scripts/z3-property-template.py` — runnable shapes 1–5 (incl. complement-free
  shape-5 `rule_diff`) PASS against a pinned z3-solver
- `docs/examples/shape5-rule_diff.md` — shape-5 `kind`/`family`/mutation guards
- `scripts/rule-diff-pilot.py` — Phase 3 gitleaks encodable-subset shape-5 pilot
  (independent-spec R1, admitted_pairs≥20, timeout gate)
- `python -m regexproof.batch` — Phase 5 batch (inventory, triage NDJSON, intent-vs-actual,
  scanner NDJSON/MD, ReDoS join optional, PR dry-run / disclosure gate)
- `scripts/z3-verify.py --all --require-ground-truth --fail-on-property-failure` — harness skeleton run (CI overlay #360): P1 injection chars,
  P2 actor whitelist, P3 sed-capture counterexample (SAT + witness), P4
  per-token escape image + the NUL-passthrough bug demo, and the
  `P1-mutated-star` mutation guard
- `properties/usrmanage-p1-p6.md` — full property suite (username validator,
  actor whitelist, sed-fallback truncation, JSON escaper image, audit-line
  integrity, password policy) with encoded forms and spike timings
- `properties/fwlive-classifier.md` — classifier regex inventory incl. the
  `NETFILTER_KV_GLUE` lookahead blocker and the decomposition route per pattern
- `docs/final-report.md` — corpus-wave (#51–#57) fraction table + gap closure
- `docs/verified-findings.jsonl` — machine-readable implementation findings
  keyed into TRAPS/BACKENDS/SEMANTICS
- `scripts/conversion-ledger.py` — product funnel (sites → properties asked →
  SAT → ground-truth → accepted upstream). Artifact:
  `properties/generated/conversion-ledger.md`. Curated last mile:
  `docs/conversion-upstream.jsonl`. Heap's-law novelty saturates the compiler;
  this ledger saturates the claim that we find real bugs.

## Auditing regexproof itself

The workflow above is for proving properties of *someone else's* regexes. When
the task is instead **"audit this repo's own security"**, read
[`docs/SECURITY-AUDIT.md`](docs/SECURITY-AUDIT.md) first — it exists so each
audit does not re-derive the same context. It carries:

- the **trust-boundary map** (which inputs are attacker-supplied vs
  operator-supplied — this is the input to almost every severity call here)
- an inventory of **controls that already exist**, so a covered finding is
  recognized as a false positive without reading the call site
- a **settled-decisions registry** of items already examined and declined
  (floating action tags, the `match.mjs` RegExp construction, `--mirror-expr`
  `eval`) — re-filing these wastes a review cycle
- copy-paste **machine-checkable sweeps** (untimed `subprocess` calls, CI gates
  with no `sys.exit`, fail-open `except` handlers, symlink-following reads)
- **severity calibration for this repo**: a CI gate that cannot fail outranks a
  conventional injection finding, because the product is trust in a proof

Two rules from step 4 of the workflow apply unchanged to self-audits: ground-truth
every finding against the surrounding code before filing, and report what you
*disproved* alongside what you found.

## Related tooling

- Daily corpus mine (GHA + ledger, live): [`docs/MINE-SETUP.md`](docs/MINE-SETUP.md)
  — `PROJECT_PAT` classic PAT with `repo`; ledger/queue commit-back to `main`;
  score-v1 allocator + `scripts/rank-mine-candidates.py` for next-to-probe
- Cluster conversion (OpenWrt, OpenClaw, …): [`docs/CLUSTER-CONVERSION.md`](docs/CLUSTER-CONVERSION.md)
  — rank 15 / write ≤5 human contracts **per idiom slice** (close-out is
  the deny-list; later waves reuse emit + product-engine checker). First
  application [`sweep/openwrt-conversion/plan.md`](sweep/openwrt-conversion/plan.md);
  packages waves 1–3 close-outs under `properties/generated/openwrt_packages_conversion_wave*.md`
  (packages **stopped** 2026-08-20). Next cluster: LuCI
  [`sweep/openwrt-luci-conversion/plan.md`](sweep/openwrt-luci-conversion/plan.md)
  (probe GO, 895 ECMA sites @ `77dad3f`).
  Heap saturates the compiler; this SOP saturates `properties_asked`.
  Cursor: `.cursor/rules/cluster-conversion-waves.mdc`.
- Auditing this repo's own security: [`docs/SECURITY-AUDIT.md`](docs/SECURITY-AUDIT.md)

## CodeRabbit (review bot)

Draft PRs are **not automatically** reviewed (`auto_review.drafts: false`);
manual `@coderabbitai review` can still trigger on drafts. Review limits are
**plan-specific** (e.g. Free 1/hr, Pro 5/hr, Pro+ 10/hr — check remaining
quota with `@coderabbitai rate limit`), not a fixed ~3/hr cap. Marking Ready
makes the PR *eligible* for automatic review. CodeRabbit takes ~5–10 min to
write a round; **wait for the round to complete before pushing fixes** (new
`COMMENTED` submission from `coderabbitai[bot]` with `commit_id` = your head;
a rate-limit comment means the head was NOT reviewed), batch all fixes into
one push, and never declare the gate green while a round is still in flight.
Full protocol: [`docs/CODERABBIT.md`](docs/CODERABBIT.md).

## Related skills (Hermes)

If running under Hermes, the `z3-regex-verification`, `z3-string-verification`,
and `z3-verification` skills carry the same knowledge with the full evidence
base. This repo is the distributable, language-agnostic version.
