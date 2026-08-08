# regexproof pilot — tested against usrmanage, fwlive, happycow

Date: 2026-08-06. Purpose: dogfood regexproof (playbook + toolkit) against
real repos. **Test-only — nothing in the target repos was modified.** Follow-up
findings were filed in the target repos (links below) for a later fixing pass.

Candidate selection (regex-surface survey across 6 cloned repos): fwlive
(47 files, JS+shell classifier on untrusted log input), usrmanage (17 files,
shell security boundaries, known-answer for the issue #6 plan), happycow
(33 files, Python scrape + JS frontend, data-cleaning trust profile).
Rejected: housekeeping (1 file), sre-ai-llm-work (docs-heavy),
mattermost-plugin-community-admin (TS/Go RE2 — lower SMT value).

## Results

| Repo | Checks | Result | What it tested |
|---|---|---|---|
| usrmanage (known-answer) | 24 | ALL PASS | Reproduces the issue #6 P1–P4 suite against current code; migration-hook path |
| fwlive (ECMA frontier) | 15 | ALL PASS | Anchored finite alternation, word-boundary complement, KV extraction, lookahead classification |
| happycow (classification) | 2 + inventory | ALL PASS | "When NOT to use Z3" path: skip cosmetic, flag ReDoS-tooling items |

## Dogfooding wave — OWASP CRS + validator.js (2026-08-08)

Tracking: issue [#35](https://github.com/lucas-albers-lz4/regexproof/issues/35) /
[#36](https://github.com/lucas-albers-lz4/regexproof/issues/36).

| Corpus | Surface | Encodable | Result |
|---|---|---|---|
| OWASP CRS v4.28.0 (`55b09f5`) | 318 `@rx` (modsec extractor) | **206/318 ≈ 64.8%** → **GO** (≥30%; was 39.3% pre toolkit-fix) | shape-5 gaps + ReDoS + dialect triage |
| validator.js (7-file verified domain) | pilots/validatorjs/src subset | shapes 1–3 + `ci()` mutation | PASS under `--require-ground-truth` |

**CRS lessons (machine-verified):**

- ModSecurity `\"`-escape + multi-line `SecRule` joining are load-bearing for
  inventory (TRAPS #19). Naive quote capture produced 102 false parse-errors.
- Shape-5 version-diff (v4.27.0→v4.28.0) with **rule-derived R1 adapter**:
  e.g. rule `942220` SAT witness `JSon.1e309` — R2 accepts optional `json.`
  prefix that R1 misses; PCRE2 ground-truth PASS.
  Artifacts: `properties/generated/crs_rule_diff_report.json`,
  `properties/triage/coreruleset_rule_diff.ndjson`.
- Unencodable routing after toolkit-fix (#45): pattern-too-long **73**
  (TRAPS #21 — keep 256 interactive cap; ReDoS/manual for long patterns),
  word-boundary **34**, internal-anchor **2**, negated-shorthand **2**,
  inline-flag **1**. Negated-class, hex ranges in classes, and most
  lazy/`\x`/scoped-`(?i:)` rejects cleared by encode paths.
- Noodler `re.from_ecma2020` still unavailable on stock z3-solver 5.0.0
  (fixture unchanged; CRS `@rx` has zero lookarounds).
- Uncapped ReDoS (recheck) on encodable subset:
  `properties/generated/crs_redos_report.json`.

**validator.js lessons:**

- Declared verified domain: the 7-file pilot subset (not full upstream
  `src/lib`). Inventory questions hard-fail if left `planned`.
- `{1}`/`{1,1}` exact-single quantifier crashed `lower.py` / `py_re`
  (`Concat` arity) — fixed as identity (TRAPS #20).
- Gap-1 `ci()` + naive-mirror mutation guard flips UNSAT→SAT as required.

Findings are `disclosure: private_first` for CRS (security-tool corpus).
Toolkit-fix (#45): lazy strip, `\xNN`/`\x{}`, negated-class, scoped
`(?i:...)`, pattern-too-long policy, ECMA flag reject-list (TRAPS #21–#22).

## Findings filed (fix-later phase)

- **usrmanage** — comment on [#6](https://github.com/lucas-albers-lz4/usrmanage/issues/6)
  (the Z3-verification plan): P2 temporal-coupling gate resolved (whitelist now
  in code), P3 target gone (rpcd uses `jsonfilter`; whole-word `sed` count 0),
  new P2b surface (audit-token whitelist), audit-line `[^ ]*` captures
  domain-gated (document, no fix).
- **fwlive** — comment on [#120](https://github.com/lucas-albers-lz4/fwlive/issues/120)
  (the F1–F4 umbrella): verified encodings seed F2's property suite;
  `NETFILTER_KV_GLUE` lookahead confirmed not stock-Z3 expressible; the pilot
  itself re-hit the Contains-vs-membership timeout trap.
- **happycow** — new issue [#115](https://github.com/lucas-albers-lz4/happycow/issues/115):
  regex robustness pass. Item 1 **verified safe** (the interpolated
  `re.search(name, …)` was already `re.escape`'d — see correction below);
  item 2 real (backreference `\b(\w+)\s+\1\b` needs a recheck verification).

## Findings for the later fixing pass (per repo)

### usrmanage — code evolved past the issue #6 plan (validation, no new bugs)
- **P2 actor whitelist is now IN THE CODE** (`um_actor_resolve`, lib:96-107,
  `[A-Za-z0-9._@-]` len 1..64) — issue #6's temporal-coupling gate is
  resolved; P2 is verifiable today (UNSAT confirmed).
- **P3's sed JSON fallback is GONE** — rpcd `json_get` now uses
  `jsonfilter -e "@.key"` (rpcd/usrmanage:21-24). The truncation bug target
  no longer exists; the finder flips to "path absent" (migration hook fired).
  Fix-later: update issue #6 / close P3 as fixed, re-scope the suite.
- New surface found: `um_audit_token` whitelist `[A-Za-z0-9._@:=-]` (lib:118)
  — verified UNSAT, worth adding to the suite.
- Audit-line sed captures `[^ ]*` (lib:1041-1045) truncate at spaces (finder
  SAT, witness `"A "`) but the domain is post-whitelist (no spaces in
  actor/src) — document the abstraction, no fix needed.

### fwlive — classifier verified on the ECMA frontier (issue #120 scope)
- F1 `TCP_FLAG_TAIL` token alphabet excludes `=`/digits — UNSAT. The pilot's
  Contains-vs-membership probe itself TIMED OUT (30s), re-confirming the
  TRAPS.md guidance; alphabet form solves instantly.
- F2 `wordPattern` boundary: single-char `Complement` form works as documented
  (excludes alnum/underscore, admits `.`). This validated the Length==1
  Complement nuance now recorded in TRAPS.md #1.
- F3 KV extraction `\b([A-Z]+)=([^\s]+)`: key alphabet clean (UNSAT); value
  capture keeps embedded `=` whole (finder SAT — `[^\s]+` does not truncate,
  unlike sed `[^ ]*`).
- F4 `NETFILTER_KV_GLUE` lookahead: classified NOT expressible in stock Z3 —
  the documented route stands (string-ops rewrite or Z3-Noodler
  `re.from_ecma2020`). No stock-Z3 change needed.
- Fix-later: nothing new beyond issue #120's own F1–F4 plan; the verified
  encodings above can seed F2's property suite.

### happycow — correct classification (mostly nothing to prove)
- All regexes are data-cleaning (hours, addresses, HTML strip, slug) — skip
  per playbook. Slug alphabet proof done as the cheap win (UNSAT).
- **Correction to the pilot's own finding:** item 1 (`check_venue_status.py:109`
  `re.search(name, window, re.I)`) was flagged as an un-escaped interpolated
  pattern — but `name = re.escape(...)` was already applied at :105 (added in
  #92). Escaped literals match in linear time: no injection, no ReDoS.
  **Verified safe; regression note only.** Lesson recorded in PLAYBOOK.md /
  AGENTS.md: read the surrounding code before filing.
- Fix-later (real item): `common.py:103` `re.sub(r"\b(\w+)\s+\1\b", ...)` —
  backreference, not SMT-expressible. Verify complexity with recheck (bounded
  input lengths make risk low); tracked in happycow#115.

## How regexproof performed (dogfooding lessons)

1. **Known-answer reproduction with 0 drift** — the P1–P4 encodings from
   issue #6 reproduce exactly on current code; the toolkit is faithful to the
   original spike.
2. **Migration hook + GATE worked as designed** — and caught me: my first
   gate grep matched the word "pas**sed**" in a comment (count 1) and I
   nearly reported "sed fallback absent" from a buggy pattern. Whole-word
   grep + honest verdict fixed it. Now TRAPS.md #12.
3. **Trap re-confirmed in the wild** — the Contains-vs-membership probe on a
   Star-language timed out at 30s (fwlive F1); the alphabet form is instant.
   The single-char Complement form (F2) behaves exactly as now documented in
   TRAPS.md #1.
4. **Code drifts past plans** — usrmanage's verification targets moved since
   issue #6 (jsonfilter landed, whitelist landed). Re-inventory before
   verifying is now workflow step 2 in PLAYBOOK.md.
5. **Ground-truth discipline applies to your own findings** — the happycow
   "un-escaped pattern" flag was already fixed in code. Read surrounding code
   before filing; PLAYBOOK.md step 3 / AGENTS.md step 4 now say so.
6. **Classification is half the value** — happycow's "skip cosmetic, flag
   ReDoS-tooling items" output is the decision tree doing its job.
7. **CRS at scale** — encodable fraction is compiler-bound (~39%), not
   pattern-quality-bound; language-transparent strip (lazy quantifiers) is
   the largest fix lever; shape-5 version diffs find real acceptance deltas
   with PCRE2-reproduced witnesses.

## Artifacts

Pilot scripts (scratch, not committed to any target repo):
`/tmp/regexproof-pilot/{usrmanage,fwlive,happycow}_pilot.py` — each a
copy-adapt of regexproof's template shapes, run with pinned `z3-solver==5.0.0`.

CRS / validator.js wave artifacts (in-repo):

- `properties/generated/coreruleset_encodable_fraction.json` (full corpus)
- `properties/generated/crs-inventory.ndjson`
- `properties/generated/crs_rule_diff_report.json` / `crs_rule_diff.md`
- `properties/generated/crs_redos_report.json` / `crs_unencodable_triage.json`
- `properties/generated/validatorjs_complete_report.json`
- `properties/triage/coreruleset_rule_diff.ndjson` / `validatorjs.ndjson`
