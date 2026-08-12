# regexproof — Dogfooding measurement, shell dialect, OpenWrt feed probe

> **For Hermes:** execution via standard-development with per-PR luna gates
> (implementation wave in the regexproof repo).

**Goal:** Convert the dogfooding singleton analysis from a one-off script into a
committed measurement primitive, add a POSIX shell extractor with a scoped
compiler backend (dialect `posix-shell`), and run the OpenWrt feed admission
probe that the shell gap justifies. **End state (user decision 2026-08-12):
MULTIPLE mining streams — the existing GitHub-repo stream plus new
source-specific streams (OpenWrt feeds first) — running the same intent chain:
mine for novel findings, then convert findings into real bugs. This wave
builds the measurement + dialect foundations that any new stream stands on
(stream-generic by design); the OpenWrt probe decides whether the first new
stream opens and validates the pattern for later ones.**

**Architecture:** Three phases with a dependency reorder that keeps the probe's
novelty claim honest. P1 lands the measurement script (PR #259) with tests, a
frozen novelty snapshot, and the `[[ =~ ]]`/fgrep extraction fixes. P2 adds a
real shell extractor (dialect `posix-shell`, ONE dialect — user decision) plus
a scoped BRE→ERE normalize + pcre compiler backend, so shell records actually
compile and the findings→bugs intent chain runs. P3's probe evidence is
captured BEFORE P2 merges (while shell is still novel — the admission
condition requires it), with the gate artifact authored from that evidence;
post-P2, the feed processing cross-checks against the registered extractor.

**Tech Stack:** Python, the repo's existing extractor framework
(`regexproof/extractors/record.py` make_record contract,
`regexproof/batch/extractor_registry.py`, `regexproof/batch/manifests.py`),
the compiler dispatch (`regexproof/compiler/__init__.py` `_compile_dialect`),
pcre backend as the BRE→ERE target, the existing probe/author tooling
(`scripts/probe-corpus-admission.py`, `scripts/author-gate-decision.py`).

## Artifact contract (cross-phase)

| Artifact | Produced-by | Consumed-by | Schema owner |
|---|---|---|---|
| `dogfooding_novelty_2026-08-12.json` | P1 | P2 AC1 denominator, docs/why.md, P2.5 | P1 |
| `probe_records.ndjson` (P1 script `--dir --ndjson` export) | P1 | merge-probe-draft.py, reconcile_probe.py | P1 |
| `extractor_records.ndjson` (registered-extractor output) | P2a | reconcile_probe.py (P3-B), P2 AC3 validation | P2a |
| `dogfooding_novelty_2026-08-12_POST_P2.json` | P2.5 | P3-B wave review, docs/why.md | P2 |
| `dogfood_shell_gate_decision.json` | P2c (author-gate-decision.py) | check_admission_gates | admission schema |
| `openwrt_packages_probe_decision.json` | P3-B (probe evidence from P3-A; merge → author) | test_probe_decision_artifacts.py, wave review, follow-on stream kickoff | admission schema |
| `prediction_vocabulary.json` shell entries | P3 | predict_buckets | admission vocabulary |

The two NDJSON artifact names are DISTINCT and never shared: P1's lightweight
`probe_records.ndjson` (fields: pattern, flags, dialect, shell_flags, file,
line) vs P2a's schema-valid `extractor_records.ndjson` (full extractor schema
with regex_id/site/column/schema_version).

---

## Context (measured 2026-08-12)

- Dogfooding universe = usrmanage, fwlive, happycow, hermes-agent-fork (user
  code = the P(compiles) distribution). 2,878 regex sites / 2,025 distinct
  (exact) / 2,004 (canonicalized) at first measure; a re-run showed 2,876 /
  2,023 — a 2-site drift from working-tree changes in the dogfooding repos,
  which is evidence that snapshots must PIN state (see P1 AC2).
- Singleton fraction 0.984 (convenience-sample estimate — pooled distinct
  singleton fraction, NOT a formal Good-Turing estimator; see P1 Step 4) —
  the P(compiles) curve is still deep in the steep region at n=4; the ~20–50
  repo knee is NOT refuted. Trailing-window novel-rate is the stopping rule
  (window = last 2 repos, threshold <3% novel rate to stop), measured and
  reported (not gated).
- Per-family idiom recurrence is visible: `^RW[A-Za-z0-9+/=]+$`,
  `untrusted comment:`, `listen_https` shared between fwlive + usrmanage
  (both OpenWrt); nothing shared with happycow/hermes-agent. Closure holds
  only within a dialect family, matching the corpus-side finding.
- Shell surface: 292 sites (10% of dogfooding) extracted by a LABELED
  heuristic scanner because no shell extractor exists. The OpenWrt admission
  argument has a number attached.
- Heuristic scanner bugs found during development and review (all fixed in
  this plan's P1): re.VERBOSE stripped literal spaces in flag runs; `[[ =~ ]]`
  matched only QUOTED RHS while bash 3.2+ treats unquoted RHS as the regex
  (0 of 3 real sites extracted); `fgrep` and `grep -F` literals were extracted
  as regexes; `sed -n '1,20p'` line addresses were treated as regexes.
- Compiler gap: `DIALECTS` (kinds.py:60) and `_compile_dialect`
  (compiler/__init__.py:60) support py_re/ecma/re2/pcre/yara/perl only —
  `posix-shell` currently raises `ValueError`. P2 scopes the backend.
- Dialect semantics (verified on GNU grep 3.11 + busybox 1.37): BRE
  `a\+b` = one-or-more (needs unescape to ERE `a+b`); BRE bare `a+b` =
  literal (needs `\+` escape); ERE `a+b` = one-or-more (pass-through); ERE
  `a\+b` = LITERAL `a+b` (pass-through — pcre agrees; NO reject).
- Schema gaps: `extractor_record.schema.json:28` dialect enum omits
  `posix-shell`; `make_record` (record.py:11-43) has a fixed signature with no
  field-extensibility; `compile_pattern` has no per-record syntax-flag param;
  `regexproof/batch/compile_records.py:72-80` is the only record→compile
  route in batch and passes no syntax flags; `regexproof/admission/walk.py`
  (`_extractors_for`, :82) has NO shell extractor — the probe's counter
  skips all `.sh`/`.init` files today.
- Existing tooling: `scripts/probe-corpus-admission.py` (emits probe draft
  with regex_sites/dialect/flags/predicted_buckets/security_boundary) and
  `scripts/author-gate-decision.py` (writes `properties/generated/<corpus>_gate_decision.json`)
  exist. `author-gate-decision.py` `--human` mode hard-requires `--decision`
  and, for a met condition, `--evidence <id>=<text>`; the draft is a
  positional arg. `gate_decision.schema.json` top-level `required` =
  [schema_version, corpus, candidate_url, decision, probe, conditions,
  rationale]; `probe.required` = [regex_sites, dialect, flags,
  predicted_buckets]; probe has NO per-package field.
- Prior dogfooding wave (hermes_agent_delta.json): 1,100 sites (frozen
  SAMPLE), encodable fraction 0.42 → 0.55 after lazy-strip /
  scoped-(?i:) / hex-soundness fixes. Full-tree re-measure = 2,347 sites.

## Non-goals

- NO Java dialect work (#150 stays deferred).
- NO compiler changes outside the scoped posix-shell backend (P2):
  BRE→ERE normalize + pcre route + `DIALECTS`/schema enum entries. Existing
  dialect compilers are untouched.
- NO mining-scanner changes (#149 stays separate; P2's manifest is extractor
  registration only, not the automation pipeline).
- NO new stopping-rule enforcement in CI — measured and reported, not gated.
- NO bulk OpenWrt scan — the probe decides admission; the funnel applies.
- NO global budget gate in `run_batch` this wave — the budget partition is
  DOCUMENTED in the probe artifact; runner-level enforcement is follow-on.
- NO gate_decision.schema.json change this wave (no per-package field added
  to the schema — the distribution lives in the probe doc; a schema
  extension is follow-on work if the OpenWrt stream graduates).

---

## Phase 1 — Land the measurement primitive (PR #259)

**Owner:** Hermes agent (work profile), standard-development.

**Objective:** Make `scripts/dogfood-singleton-analysis.py` merge-ready: fixes,
tests, lint-clean, frozen novelty snapshot, and a `--dir` argument so it can
count ANY repo (the probe's pre-P2 counting tool).

**Files:**
- Modify: `scripts/dogfood-singleton-analysis.py` (PR #259, already pushed)
- Create: `tests/test_dogfood_singleton_analysis.py`
- Create: `properties/generated/dogfooding_novelty_2026-08-12.json` (frozen snapshot)
- Modify: `docs/why.md` (snapshot stats refresh; the refresh recipe lives in
  the Hermes regexproof skill at `references/doc-stats-refresh.md` — inline
  the commands in the plan issue body rather than citing the skill path)

**Step 1: Fix the heuristic scanner (review findings).**
- `[[ =~ ]]`: match UNQUOTED RHS as the ERE (bash 3.2+ semantics); treat
  quoted RHS as literal match and SKIP. Emit a `bash_ksh` provenance field
  (the 3 known sites are `^[Yy]$` x2, `^[0-9]+$`).
- `fgrep` / `grep -F`: args are LITERALS, not regexes — do NOT extract as
  `posix-shell` patterns (skip, or record with a literal marker).
- `grep -i`: map into the record `flags` field (`flags="i"`) — do not
  hardcode `flags=""` (case-insensitive greps must compile case-folded).
- Keep the existing correct handling: no VERBOSE, sed `s///`-search-part +
  `/re/`-address forms only (numeric addresses rejected), awk program text
  skipped (`awk '/re/'` and `awk -F` ERE forms only), empty patterns
  dropped, `$var` greps kept.
- Known false-negative to document: `-qE'pat'` (no space between flags and
  pattern) is not matched by the flag-run regex.
- Performance: precompute newline offsets once per file and bisect for
  line-number lookup (not `count` per match — the OpenWrt walk is the hot
  path).

**Step 2: Add the `--dir` argument with shell-adjacent file selection.**
The script's `DOGFOOD` mapping becomes the default when no `--dir` is passed;
with `--dir <path> --name <label>` it extracts a single arbitrary repo.
File selection in `--dir` mode covers the shell surface OpenWrt actually
uses: `*.sh`, `*.bash`, `*.init`, files under `init.d/`, plus shebang sniff
(first line `#!/bin/sh`, `#!/bin/bash`, `#!/usr/bin/env bash`). Add a
`MAX_FILE_BYTES` guard (reuse `manifests.py:12` = 2MB), a `--ext` filter, and
a `--dry-run` mode (per-file counts, no extraction). **`--ndjson` exports the
FULL extraction records** (one NDJSON object per site: pattern, flags,
dialect, shell_flags, file, line — the records the extractor already
produces internally), NOT aggregated per-file counts: per-file counts are
derived by aggregating the records, and the pattern text is REQUIRED by
`merge-probe-draft.py` (P3) to derive construct counts for `predict_buckets`
— a counts-only export cannot produce non-empty `predicted_buckets`. The
export schema (field names + one-record-per-line) is documented in the
script's `--help` and covered by a fixture test. Default repos remain pinned
by commit (see Step 4).

**Step 3: Unit-test the pure functions** — `canon()`, `_sed_search()`
(including alternate delimiter `s#foo#bar#`), flag-run matching (`grep -q`,
`grep -i -q`), bash `=~` unquoted/quoted, awk forms, fgrep/-F rejection,
`-i`→flags mapping, empty-pattern drop, length-2 filter. Name the helper
split explicitly: `scan_shell()` keeps its `list[dict]` record contract; add
`extract_bash_ere(src) -> list[str]` and `extract_shell_patterns(src) ->
list[str]` as thin wrappers the tests exercise.

```python
def test_canon_vars_and_digits():
    assert canon(r"option syn_flood '1'") == r"option syn_flood '#'"
    assert canon(r"${index_url}") == "$V"
    assert canon(r"$_u") == "$V"

def test_sed_search_rejects_numeric_address():
    assert _sed_search("1,20p") is None   # line address, not a regex
    assert _sed_search("s/foo/bar/") == "foo"
    assert _sed_search("s#foo#bar#") == "foo"
    assert _sed_search("/listen_https/d") == "listen_https"

def test_bash_ere_unquoted_only():
    assert extract_bash_ere("[[ $x =~ ^[0-9]+$ ]]") == ["^[0-9]+$"]
    assert extract_bash_ere('[[ $x =~ "^[0-9]+$" ]]') == []

def test_fgrep_and_F_are_literal():
    assert extract_shell_patterns("fgrep 'a.b' f") == []
    assert extract_shell_patterns("grep -F 'a.b' f") == []
    assert extract_shell_patterns("grep 'a.b' f") == ["a.b"]

def test_grep_i_maps_to_flags():
    recs = scan_shell("grep -i 'foo' f", repo="t", file="x.sh")
    assert recs[0]["flags"] == "i"
```

**Step 4: Freeze the snapshot.** Run the script against PINNED commits of the
four dogfooding repos (record the commit SHA per repo in the snapshot JSON —
the dogfooding repos are moving targets; see Context). The script VERIFIES
each repo HEAD == recorded SHA and refuses to snapshot on mismatch (no
operator-dependent pinning). Save per-corpus site/distinct/singleton counts +
global GT estimate + dialect surface. Report the GT figure honestly:
per-observation singleton fraction (n1/N over sites) AND per-repo joint
novelty, labeled as a convenience-sample estimate — do not present the pooled
distinct-singleton fraction as a formal estimator. Also freeze the FILE LIST
per repo under an explicit snapshot key (`file_lists: {repo: [paths]}`) —
this is the recall/precision denominator for P2 ACs and the probe surface
(three file universes collapse into one). The snapshot ALSO freezes per-file
site counts (`site_counts_per_file: {repo: {path: count}}`) — the P2a recall
AC is measured per FILE against this frozen count table, not against a bare
path list. Shell identity includes the
`shell_flags` syntax selector (BRE `a+b` literal vs ERE `a+b` one-or-more
must not collapse into one distinct pattern).

**Step 5: Update `docs/why.md`** snapshot numbers (corpus count, this analysis
exists, shell gap quantified).

**Verification:** `pytest tests/test_dogfood_singleton_analysis.py -v` all
green; script rerun on pinned commits produces byte-identical snapshot;
`--dir` extraction on a scratch repo produces sane counts; `--dry-run` and
`--ndjson` work on the scratch repo; `gh pr checks 259` (or the repo's
standard gates) pass.

**ACs (falsifiable):**
1. `tests/test_dogfood_singleton_analysis.py` exists, covering all listed
   edge cases (canon, sed-forms incl. alternate delimiter, flag-runs,
   bash =~ unquoted/quoted, awk forms, fgrep/-F rejection, `-i`→flags,
   empty-pattern drop, length-2 filter) — the listed set, not an arbitrary
   count.
2. Snapshot JSON committed with per-repo commit pins AND per-repo file list
   under the `file_lists` key; byte-identical on rerun against the same
   pins (verifiable: rerun + sha256 diff); script refuses to snapshot when
   a repo HEAD != recorded SHA.
3. `docs/why.md` carries the shell-gap finding with the 292-site number and
   the GT figures labeled as convenience-sample estimates.
4. The 3 known `[[ =~ ]]` sites (`^[Yy]$` x2, `^[0-9]+$`) appear in the
   extraction output with the `bash_ksh` provenance field.
5. `--dir <path>` extraction works on a scratch repo (incl. a `*.init` and
   an extensionless shebang file); `--dry-run` and `--ndjson` covered by
   tests.
6. `MAX_FILE_BYTES` guard + `--ext` filter are tested (oversized file
   skipped with documented count, not OOM); line-number lookup uses
   precomputed offsets (no per-match `count`).

---

## Phase 2 — POSIX shell extractor + scoped compiler backend

**Owner:** Hermes agent (work profile), standard-development.

**Objective:** Replace the heuristic scanner with a registered extractor
producing schema-valid records that COMPILE (dialect `posix-shell`, one
dialect — user decision; BRE→ERE normalize + pcre backend — user decision
2026-08-12, LOCKED: the backend is in P2, keeping the findings→bugs intent
chain intact).

**Files:**
- Create: `regexproof/extractors/shell_posix.py` —
  `extract_shell_posix(src, *, repo, file, dialect)`
- Create: `regexproof/compiler/posix_shell.py` — BRE→ERE normalize + pcre
  backend mapping into the existing pcre compile path
- Modify: `regexproof/compiler/__init__.py` — `_compile_dialect` gains a
  `posix-shell` branch; `compile_pattern` gains `shell_flags: dict | None =
  None` param; normalize runs at `compile_pattern` ENTRY (before the
  special-case hooks caret_in_x / trailing_alt_dollar, which then operate on
  normalized ERE text). **Explicit guard: the posix-shell branch calls the
  pcre compile directly on already-normalized text; normalize is entry-only,
  NEVER re-run in `compile_bare` (a re-normalize would round-trip BRE
  `\+`→`+`→`\+` and cancel the fix).**
- Modify: `regexproof/kinds.py` — `DIALECTS` gains `posix-shell`
- Modify: `regexproof/schemas/extractor_record.schema.json` — dialect enum
  gains `"posix-shell"` (line 28)
- Modify: `regexproof/extractors/record.py` — `make_record` gains a typed
  `extra_fields: dict | None = None` param merged into the returned dict
  **BEFORE the fixed fields (fixed fields win — an `extra_fields` attempt
  to override `pattern`/`dialect`/`regex_id` is ignored; add a test
  asserting the override is dropped)**; typed, NOT bare `**kwargs` (no
  silent typo corruption from the 33 existing callers); documented as the
  field-extensibility contract
- Modify: `regexproof/batch/compile_records.py` — the record→compile route
  reads `rec.get("shell_flags")` and threads it into `compile_pattern`
  (the `compile_pattern` try-block call, referenced by function not line
  number)
- Modify: `regexproof/batch/extractor_registry.py` — register
  `"shell_posix"` with `dialect_kw=True` (the default wrapper passes
  `dialect` — the extractor signature MUST accept it; verify the
  `**/init.d/**` glob against a fixture), glob
  `"**/*.sh,**/*.bash,**/*.init,**/init.d/**"`
- Modify: `regexproof/batch/manifests.py` — corpus manifest for the shell
  corpus (extractor registration ONLY — does not touch the #149 automation
  pipeline): key `dogfood_shell`, `corpus_type` set, `path` pointing at a
  committed/cloned tree (NOT an uncommitted local checkout),
  `dialect: "posix-shell"`, **`lift_inline: false`** (grep has NO inline
  modifiers: BRE treats a leading `(?i)` as literal text; GNU grep ERE
  warns `? at start of expression` and matches nothing — verified GNU grep
  3.11 + busybox 1.37, 2026-08-12. `normalize_inline_flags` must not strip
  it; the literal-(?i) semantics are handled by the P2b normalize +
  inline-flag guard, NOT by inline-flag stripping), `corpus_type:
  "rule_corpus"` (NON-EXEMPT — `check_admission_gates` requires the
  decision artifact for every corpus except testdata/inventory_only)
- Modify: `scripts/dogfood-singleton-analysis.py` — use the registered
  extractor instead of `scan_shell`
- Modify: `regexproof/admission/walk.py` — add shell dispatch to
  `_extractors_for` (`*.sh`/`*.bash`/`*.init`/`init.d/` + shebang sniff)
  so the PROBE path counts shell surface (this is the tooling that feeds
  `probe.regex_sites`; without it the authored artifact reports ~0 shell
  sites). This is a P2 deliverable — the P3 probe runs against the P1
  script's `--dir` counter for its authoritative count (P3 Step 2), and the
  walk_repo dispatch lands with the extractor so the tooling and the batch
  agree.
- Create: `tests/test_extract_shell_posix.py`
- Create: `tests/test_compile_posix_shell.py`
- Create: `properties/generated/shell_precision_seed.bin` +
  `properties/generated/shell_precision_spotcheck_seed.bin` (random-source
  files sized per AC2) + `properties/generated/shell_precision_sample_50.txt`
  (chosen-50 path list) + `properties/generated/shell_precision_sample.json`
  (labels + draw records) — the committed precision evidence (P2 AC2)
- Create: `properties/generated/dogfood_shell_gate_decision.json` (admission
  artifact for the shell corpus itself; GO-class on condition id
  `new-surface` — authored via `author-gate-decision.py` FROM A DRAFT: the
  tooling hard-requires a positional draft + `--decision` + `--evidence`
  per met condition. The draft is produced by running
  `scripts/probe-corpus-admission.py` against the `dogfood_shell` corpus
  tree AFTER P2c's walk_repo shell dispatch lands (so `probe.regex_sites`
  counts shell files), then authored from the repo ROOT with the complete
  invocation:
  `python scripts/author-gate-decision.py <draft.json> --human --decision go
  --met new-surface --evidence "new-surface=<text>" --template new-surface
  -o properties/generated/dogfood_shell_gate_decision.json`.
  Authoring is a P2c deliverable (depends on walk dispatch; verified
  machine fact: `check_admission_gates` at runner.py:550 skips only
  `testdata`/`inventory_only` corpus_types and requires the
  `{manifest_key}_gate_decision.json` for every other corpus). The manifest
  `corpus_type` must therefore be NON-EXEMPT (`rule_corpus` — consumes
  `batch/inventories/rule_corpus.json` like the other rule corpora; NOT a
  testdata/inventory-only corpus). NOTE: this artifact is intentionally
  manifest-gated (consumed by `check_admission_gates` via the `dogfood_shell`
  key) — it is the shell corpus's own admission, distinct from the
  OpenWrt probe decision in P3)
- Create: `properties/generated/dogfooding_novelty_2026-08-12_POST_P2.json`
  (the P2.5 re-freeze snapshot — listed HERE as a Create)
- Modify: `tests/test_dogfood_singleton_analysis.py` — migrate tests from
  `scan_shell` to the registered extractor (P2 AC4 deletes `scan_shell`; the
  migration is a named P2 deliverable)

**Key design points:**
- **Extractor** follows `make_record` via the typed `extra_fields` param and
  accepts `dialect` (registry wrapper passes it). `column` = line-relative
  match offset (`match.start() - line_start`, matching peer extractors'
  convention — `site` is `file:line:column` and feeds `regex_id`).
  `call_kind`: `search` for grep/[[, `substitution` for sed s///. Dialect
  value: `posix-shell` for all; carry the syntax selector (`-E`/`-G`/`-F`,
  bare grep = BRE, sed = BRE, `[[ =~ ]]` = bash/ksh ERE) in the
  `shell_flags` record field (a dict of selectors + a `bash_ksh` provenance
  boolean); `-i` maps to the record `flags` field. NOT in `call_kind` and
  NOT as a dialect split — preserves the one-dialect decision while making
  syntax visible to the compiler.
- **Compiler backend** (LOCKED decision: in P2): normalize then route
  through the existing pcre compile path. The normalize handles BOTH
  directions for BRE-syntax records:
  - unescape BRE escapes: `\(` `\)` `\{` `\}` `\|` `\+` `\?` → `(` `)` `{`
    `}` `|` `+` `?`
  - literal-escape direction: bare `+` `?` `{` `|` `(` `)` in a
    BRE-syntax record are LITERALS (BRE has no unescaped group syntax) and
    must be escaped (`\+` `\?` `\{` `\|` `\(` `\)`) so the ERE/pcre
    compile does not widen or re-parse them
  - BRE = GNU/busybox flavor (documented in module docstring; `\+` `\?`
    `\|` are POSIX-undefined but GNU/busybox-supported — the OpenWrt target)
  - reject GNU extensions `\<` `\>` as Unencodable (documented, not silent)
  - BRE backrefs `\(...\)\1` are Unencodable("backref") regardless
    (simple_parse.py:184 / pcre `_local_reject` precedent)
  For ERE-syntax records (`grep -E`, `[[ =~ ]]`): PASS-THROUGH, no
  normalization and NO reject — ERE backslash-metas (`\+` `\?` `\{n\}`)
  are LITERALS in GNU/busybox ERE (verified: `grep -E 'a\+b'` matches
  literal `a+b` on GNU grep 3.11 + busybox 1.37) and pcre reads them
  identically. No silent corruption exists in this direction.
  **ONE ERE exception — the inline-flag guard:** a `(?` sequence in an
  ERE-syntax record is rejected as Unencodable("inline-flag-like")
  (documented, not silent). GNU grep ERE does NOT support inline modifiers:
  `grep -E '(?i)foo'` emits `? at start of expression` and matches nothing;
  BRE `grep '(?i)foo'` matches the LITERAL text `(?i)foo` (both verified on
  GNU grep 3.11 + busybox 1.37, 2026-08-12). Routed unguarded to pcre, `(?i)`
  would be read as a case-insensitive flag and diverge from real grep, so
  the guard is mandatory — and `normalize_inline_flags` must never strip it
  (`lift_inline: false` in the manifest). For BRE-syntax records the
  literal-escape direction handles it: `(` `?` are escaped to `\(` `\?`, so
  `(?i)foo` compiles as literal text.
  Fixture tests must cover the 4-way distinction: `a+b` (BRE literal → needs
  `\+` escape) vs `a\+b` (BRE one-or-more → unescape to `a+b`) vs
  `grep -E 'a+b'` (ERE one-or-more → pass-through) vs `grep -E 'a\+b'`
  (ERE literal `a+b` → pass-through, compile-success). PLUS the inline-flag
  guard pair: BRE `(?i)foo` compiles to a LITERAL match and ERE `(?i)foo`
  → Unencodable("inline-flag-like") — both asserted against a GNU grep /
  busybox ground-truth differential fixture (`grep -E '(?i)foo'` warns +
  matches nothing; `grep '(?i)foo'` matches literal).
- **Heuristic-by-nature labeling:** module docstring documents the
  false-positive/negative profile — numeric addresses rejected, awk program
  text skipped (`awk '/re/'` and `awk -F` ERE forms extracted),
  `grep -P` rejected/rebranched (PCRE-in-shell), `-qE'pat'` whitespace gap,
  fgrep/-F literal handling, `[[ =~ ]]` unquoted-ERE semantics, `init.d/`
  symlinks and extensionless files covered by the glob + shebang sniff.
- **Precision guard:** the extractor must not pollute the corpus with
  phantom patterns — false positives distort the P(compiles) distribution
  and the singleton measurement.

**Verification:** `pytest tests/test_extract_shell_posix.py -v` green;
`pytest tests/test_compile_posix_shell.py -v` green (BRE + ERE patterns
compile per the 4-way fixture set, backrefs and GNU `\<` `\>` → Unencodable,
no ValueError, ERE `\+` compiles as literal); extractor output on the
usrmanage+fwlive shell slice matches the P1 heuristic surface within
documented tolerance; `compile_pattern("...", dialect="posix-shell",
shell_flags=...)` succeeds for representative ERE + normalized BRE;
`make_record` caller audit: `grep -rn "make_record(" regexproof/ scripts/ |
wc -l` recorded and every caller's args checked against the typed signature
(no silent typos); `walk_repo` shell dispatch tested (a scratch tree with
`.sh`/`.init` files yields non-zero `regex_sites`).

**ACs (falsifiable):**
1. **Recall:** registered extractor extracts ≥280 of the 292 heuristic shell
   sites on the usrmanage+fwlive slice. Denominator = the frozen per-file
   site counts (`site_counts_per_file`) in the P1 snapshot, measured per
   file; gaps documented per file.
2. **Precision:** on a hand-labeled 50-file sample drawn from the frozen P1
   `file_lists`, precision ≥ 90%. The draw is REPRODUCIBLE: GNU `shuf`
   takes `--random-source=FILE`, not a bare seed, and FAILS with
   `end of file` on an undersized source — size both seed files to the
   input (`bytes >= 4*N + 64` for N input lines; record byte counts in the
   sample JSON). Commit `properties/generated/shell_precision_seed.bin`
   (50-draw) and `properties/generated/shell_precision_spotcheck_seed.bin`
   (10-draw), plus the chosen-50 path list as
   `properties/generated/shell_precision_sample_50.txt` (sorted, one per
   line). Draws:
   `shuf -n 50 --random-source=properties/generated/shell_precision_seed.bin <properties/generated/shell_precision_sample_50.txt`
   and
   `shuf -n 10 --random-source=properties/generated/shell_precision_spotcheck_seed.bin <properties/generated/shell_precision_sample_50.txt`.
   The per-record TP/FP labels are COMMITTED with the P2a PR as
   `properties/generated/shell_precision_sample.json` (schema: seed files +
   byte counts, draw commands, files, records with label; zero-record files
   excluded from the denominator and counted separately). Definition: a true positive is an extracted
   pattern that is a regex used in a grep/sed/awk/`[[ =~ ]]` context (not a
   literal, assignment, or comment). Numerator/denominator = TP/(TP+FP)
   over the 50 files. Independent spot-check: a DIFFERENT human labeler
   reviews the 10-file subset produced by the spot-check draw (distinct
   seed file;
   disagreement = fraction of records where the two labelers disagree on
   TP/FP classification, over the union of records in the subset;
   disagreement > 10% → relabel the full 50 files; AC fails if relabeled
   precision < 90%.
3. All records schema-valid. Exact validator:
   `python -c "import json,jsonschema,regexproof.schemas as s; [jsonschema.validate(json.loads(l), s.extractor_schema()) for l in open('extractor_records.ndjson')]"`
   (per-line validation — `json.loads`, not `json.load`; `extractor_schema()`
   is the exported accessor). Requires the `posix-shell` enum entry from
   this phase's Files list.
4. Singleton analysis script uses the registered extractor; no `scan_shell`
   remains; `tests/test_dogfood_singleton_analysis.py` migrated (P2 Files).
5. VERBOSE-space regression test exists and passes (flag runs with separate
   `-i -q`).
6. Compiler smoke test: `compile_pattern` accepts `posix-shell` for ERE and
   normalized-BRE inputs; BRE backrefs and GNU `\<` `\>` produce
   Unencodable; ERE-syntax `\+` compiles as literal (no reject); existing
   dialects' tests stay green; normalize is entry-only (no re-normalize in
   the branch — the double-normalize test asserts a BRE `a\+b` record
   compiles to one-or-more, not literal).
7. **P2.5 re-freeze (mandatory, within P2):** after extractor registration
   and BEFORE P3-B begins (P3-A evidence capture runs pre-P2 and is the
   exception — see AC7 and P3 Step 7), re-run the singleton analysis via the registered
   extractor; commit
   `properties/generated/dogfooding_novelty_2026-08-12_POST_P2.json`
   (Create entry in this phase's Files) with a delta report (site count,
   singleton fraction, dialect surface changes); update `docs/why.md` with
   both snapshots. P3-B (artifact authoring + reconciliation) cannot start
   without this commit. **P3-A (probe evidence capture) is the explicit
   exception**: it must COMPLETE before P2 merges (shell still novel —
   condition `new-surface` requires the evidence to be captured while the
   dialect is unadmitted) and runs against the PR #259 branch counter per
   P3 Step 1. The P2.5 gate applies to P3-B only.
8. `make_record` caller audit recorded (caller count + arg check); typed
   `extra_fields` merged BEFORE fixed fields; override-attempt test passes;
   no bare `**kwargs` in the diff.
9. `walk_repo` shell dispatch test: probe path yields non-zero `regex_sites`
   on a scratch tree with `.sh`/`.init` files.
10. `lift_inline: false` pinned in the `dogfood_shell` manifest; a fixture
    with a literal `(?i)`-leading pattern compiles as literal (not stripped).

---

## Phase 3 — OpenWrt feed admission probe

**Owner:** Hermes agent (work profile), standard-development.

**Objective:** Run the admission gate's probe stage against an OpenWrt feed at
FEED level, producing a committed, schema-valid gate decision artifact via
the existing probe/author tooling. The probe evidence is captured BEFORE P2
merges (shell still novel — condition id `new-surface` requires it); the gate
artifact is authored from that evidence. Post-P2 feed processing is
follow-on, not this wave.

**Files:**
- Create: `sweep/corpus-wave5/openwrt-feed-probe.md`
- Create: `properties/generated/openwrt_packages_probe_decision.json`
  (the probe decision artifact — see Step 7 for its consumer story)
- Create: `tests/test_probe_decision_artifacts.py` — globs
  `properties/generated/*_probe_decision.json` and schema-validates each
  (THE probe artifact's validator)
- Modify: `scripts/author-gate-decision.py` — **go/new-surface guard** (the
  under-report rule's ENFORCEMENT point, not just workflow convention):
  for `--decision go` with `--met new-surface`, refuse (exit non-zero,
  clear message) when the draft's `probe.predicted_buckets` is EMPTY.
  Regression test: a draft with `new-surface` met + empty
  `predicted_buckets` fails authoring; the same draft with a non-empty
  `predicted_buckets` authors cleanly. (The merge-probe-draft.py preflight
  is the first line; this guard closes the direct-draft bypass at
  author.py:118-153, where `assemble_decision` would otherwise emit `go`
  for a hand-supplied empty-bucket draft.)
- Create: `scripts/reconcile_probe.py` — probe-count vs extractor-output
  reconciliation: per-file delta, `--tolerance-pct` flag, tolerance report.
  Input contract: probe side = per-file counts AGGREGATED from the P1
  script's `--dir --ndjson` record export; extractor side = extractor NDJSON
  records aggregated per file; tolerance =
  |probe_count - extractor_count| / probe_count per file.
- Create: `scripts/merge-probe-draft.py` — THE pre-P2 shell-evidence merge
  step: takes (a) the P1 `--dir --ndjson` export (FULL extraction records —
  pattern, flags, dialect, shell_flags, file, line; per-file counts are
  derived by aggregation) and (b) the probe draft emitted by
  `probe-corpus-admission.py` (whose `walk_repo` path cannot see shell
  files pre-P2), and populates the draft's `probe.regex_sites` (aggregated
  from records) and `probe.predicted_buckets`. **The construct-counting
  step is DEFINED to match walk.py EXACTLY (walk.py:186-199): the merge
  calls `regexproof.admission.constructs.accumulate_constructs(patterns)`
  on the shell record pattern texts, then FOLDS the record `flags` through
  `_FLAG_LETTER_TO_CONSTRUCT` (walk.py:34 — `i`→`(?i)`, `x`→`(?x)`,
  `s`→`(?s)`, `m`→`(?m)`, `u`→`u-flag`, `v`→`v-flag`, `g`→`stateful`)
  into a merged Counter — so shell `grep -i` records land in the
  `(?i)`/inline-flag bucket, not silently dropped — and only THEN feeds the
  merged Counter through `regexproof.admission.vocabulary.predict_buckets`
  (the same path as walk.py:199). **Preflight enforcement: if the merged
  draft's `probe.predicted_buckets` is EMPTY, `merge-probe-draft.py` exits
  NON-ZERO before any authoring can proceed** — the AC4 "under-report
  forces triage-trial/no-go" rule is thereby enforced by the merge tool,
  not by human review: an empty-bucket draft cannot reach
  `author-gate-decision.py --decision go`. The shell construct keys it emits MUST be
  present as `construct_to_bucket` entries in `prediction_vocabulary.json`
  (P3 deliverable — see Files), keyed to the constructs `count_constructs`
  actually emits for shell patterns (add a shell fixture to
  `tests/test_constructs.py` or the merge's own fixture asserting the
  emitted keys, including a `grep -i` record asserting the `(?i)` bucket).** Without this merge, the authored artifact's shell
  evidence is ~0 and the `new-surface` GO is internally incoherent
  (verified: `walk_repo` `_extractors_for` has no shell dispatch until P2's
  AC9 lands, which is AFTER the pre-P2 probe runs).
- Modify: `properties/generated/prediction_vocabulary.json` — shell
  construct→bucket entries (the LOADED artifact — `vocabulary.py`
  `predict_buckets` reads `construct_to_bucket` from this JSON at
  vocabulary.py:11/34; editing the loader module adds nothing)

**Steps:**
1. Clone `openwrt/packages.git` (depth 1) to a scratch dir — feed-level unit,
   NOT 8,000 individual package repos. **Record the feed clone SHA** in the
   probe doc (reproducibility), plus commit message/date (branch may be
   deleted after merge — the SHA alone can become unresolvable). PR #259
   dependency: the probe runs against the PR #259 BRANCH (P1 merge NOT
   required — the `--dir` counter exists on the branch); probe doc records
   the PR branch commit SHA used, and the probe is run from a detached
   checkout of that recorded commit (fail on SHA mismatch).
2. **Counting tool is named and scaled:** the P1 script with `--dir` (P1
   Step 2) IS the probe counter — it inherits the P1-fixed extraction
   semantics (`=~` unquoted, fgrep/-F literal, `-i`→flags, sed forms,
   `*.init` + shebang selection) and the `MAX_FILE_BYTES`/`--ext` bounds;
   use `--dry-run` for the per-file spot-check and `--ndjson` for the
   reconciliation input. Raw `grep -rhcE` may be used for the
   admission-and-returns recipe's cross-check, but the authoritative count
   comes from the script. The probe doc records expected runtime (<5 min on
   a defined hardware class: 4-core/8GB), expected disk (<500MB clone +
   walk — mirror `probe-corpus-admission.py`'s `--max-disk-mb=500` default),
   and the ACTUAL runtime + file counts + disk from the run.
3. **Aggregation defined up front** (the gate's <200-site scale red flag was
   designed for repo-level corpora; an 8k-package monorepo breaks its
   assumptions): count regex sites PER PACKAGE DIRECTORY via the `--dir`
   counter; report min/median/max/total across packages in the PROBE DOC
   (the gate schema has no per-package field — the distribution is a probe
   artifact, not a schema field; a schema extension is follow-on if the
   stream graduates). GO requires total sites ≥ 1 AND at least one package
   with novel dialect surface (init scripts with grep -E/sed/BRE/awk -F
   patterns, busybox-ash constructs). The <200 scale red flag is explicitly
   OVERRIDDEN and justified in the artifact's `rationale` (a feed is not a
   repo; the scale signal is meaningless at this granularity).
4. Probe mechanics, documented in the probe doc: exact command sequence with
   `LC_ALL=C`, `grep -a` for binary files, CRLF-tolerant counting,
   busybox-ash `[[` vs `[` vs `test` handling, Makefile `pattern = value`
   false-positive avoidance (Makefile assignments are not regex sites).
5. **Timing/novelty honesty:** capture the probe site counts and the
   dialect-surface evidence BEFORE P2 merges (or explicitly target a
   DIFFERENT novel surface if post-P2 — busybox-ash quoting, Makefile
   pattern syntax — and say so in the artifact). The artifact's
   `decision_basis` must match the evidence: `admission_conditions` with
   condition id `new-surface` met + real evidence, or `escape_hatch` with a
   security-boundary classification of init scripts (config parsing — weak
   leg, evidence required; do not default to escape_hatch).
6. Bucket-overlap prediction uses the EXTENDED vocabulary — the shell
   construct→bucket entries added to `prediction_vocabulary.json` (the
   loaded artifact — see Files) — so `predicted_buckets` reflects shell
   constructs. AC4 requires `predicted_buckets` NON-EMPTY for a `go` with
   condition `new-surface`; the under-report escape forces
   `triage-trial`/`no-go` (no soft OR).
7. **Author the gate decision artifact via existing tooling, with the
   shell-evidence merge — SPLIT INTO P3-A and P3-B with an explicit
   handoff:**
   **P3-A (pre-P2, evidence + merge):** (a) run
   `scripts/probe-corpus-admission.py` to emit the probe draft scaffold
   (its `walk_repo` path sees only non-shell files pre-P2 — expected);
   (b) run `scripts/merge-probe-draft.py` to populate the draft's
   `probe.regex_sites` (aggregated from records) and
   `probe.predicted_buckets` (constructs derived from record pattern text)
   from the P1 `--dir --ndjson` FULL-RECORD export — this is the step that
   makes the artifact's shell novelty evidence real. **The MERGED DRAFT is
   the P3-A → P3-B handoff artifact** (committed at the P3-A evidence
   freeze); authoring does NOT run in the same step.
   **P3-B (post-P2.5, authoring):** (c) author with the
   COMPLETE invocation, run from the REPO ROOT (the `-o` path is
   CWD-relative and
   `_resolve_output` refuses paths outside `properties/generated`):
   `python scripts/author-gate-decision.py <merged-draft.json> --human --decision go --met new-surface --evidence "new-surface=<evidence text>" --template new-surface -o properties/generated/openwrt_packages_probe_decision.json`
   (the draft positional, `--decision go`, and `--evidence <id>=<text>` are
   all REQUIRED — `--human` without `--decision` errors at
   author-gate-decision.py:301; a met condition without `--evidence` errors
   at author.py:79-81). The artifact must include every schema-required
   field: top-level `required` = [schema_version, corpus, candidate_url,
   decision, probe, conditions, rationale] and nested `probe.required` =
   [regex_sites, dialect, flags, predicted_buckets]. **Consumer story:**
   the probe artifact is a PLAN-TIME admission decision — `check_admission_gates`
   only reads `{manifest_key}_gate_decision.json` for manifest corpora, so
   the OpenWrt decision is consumed by (a) `test_probe_decision_artifacts.py`
   (schema validation), (b) the wave-close review, and (c) the follow-on
   stream kickoff that registers OpenWrt as a manifest corpus (next wave).
   This is stated explicitly so the artifact's role is not confused with a
   runtime gate artifact. Validate with `pytest tests/test_probe_decision_artifacts.py`.
8. **Budget partition documented** (no runner change this wave): the probe
   artifact records the shared compile-budget partition — a reserved
   pattern/wall budget for the GitHub stream before any OpenWrt
   extraction/compile is admitted; the partition is the decision record for
   the follow-on global gate.
9. **Reconciliation:** after P2 lands, run `scripts/reconcile_probe.py`
   (P1 `--dir --ndjson` output vs extractor NDJSON, `--tolerance-pct 10`)
   and commit the tolerance report to the probe doc — this is the defined
   procedure for comparing the pre-P2 probe counts with the P2 extractor
   output.

**Verification:** `pytest tests/test_probe_decision_artifacts.py -v` green
(globs + validates `*_probe_decision.json`); artifact committed; probe
counts reproducible (commands + `--dry-run` output + clone SHA + PR-branch
SHA + actual runtime/disk recorded in the probe doc).

**ACs (falsifiable):**
1. Probe doc records real clone + clone SHA + PR-branch SHA + real
   per-package site counts with the aggregation distribution
   (min/median/max/total) + actual runtime/disk — no plan-doc claims; counts
   produced by the P1 script `--dir` invocation, command recorded.
2. Gate decision artifact exists, schema-valid (validator:
   `test_probe_decision_artifacts.py`), authored via
   `probe-corpus-admission.py` → `author-gate-decision.py` with the complete
   invocation (draft positional + `--decision go` + `--evidence
   new-surface=<text>`), `decision` + `decision_basis` + condition id
   (`new-surface`) consistent with the schema enum and the capture timing,
   all schema-required fields present (top-level + nested `probe.required`;
   `corpus_pin` is optional and NOT claimed required).
3. No per-package scanning performed — verified by the probe doc's recorded
   commands (clone feed + count via `--dir`, no loop over individual
   package repos) and the absence of per-package artifacts.
4. `prediction_vocabulary.json` shell construct→bucket entries exist (P3
   deliverable — the loaded artifact, not `vocabulary.py`), keyed to the
   constructs `count_constructs` (constructs.py:25) actually emits for
   shell patterns (fixture-verified); `predicted_buckets`
   in the artifact is NON-EMPTY for a `go` with condition `new-surface`;
   the under-report escape forces `triage-trial`/`no-go` (enforced by the
   merge-probe-draft.py preflight — P3 Files).
5. `scripts/reconcile_probe.py` exists, `--tolerance-pct` tested with the
   defined input contract (per-file counts aggregated from `--dir --ndjson`
   records vs extractor NDJSON), and the tolerance report committed to the
   probe doc.
6. `scripts/merge-probe-draft.py` exists and is tested: given a
   `probe-corpus-admission.py` draft + a P1 `--dir --ndjson` record export,
   the merged draft's `probe.regex_sites` equals the aggregated record
   count and `probe.predicted_buckets` is non-empty — derived via
   `accumulate_constructs(patterns)` + `_FLAG_LETTER_TO_CONSTRUCT` flag
   folding → `predict_buckets` (the same path walk_repo uses at
   walk.py:186-199) — when the vocabulary has shell entries (unit test with
   a fixture draft + fixture ndjson records; the fixture asserts the
   construct keys `count_constructs` emits for the shell patterns match the
   `prediction_vocabulary.json` keys, AND that a `grep -i` record with
   `flags="i"` produces the `(?i)` bucket).

---

## Risks / tradeoffs / open questions

- **Compiler backend scope (P2):** DECIDED 2026-08-12 — the BRE→ERE
  normalize + pcre backend is IN P2 (keeps findings→bugs intact). The
  inventory-only alternative is REJECTED; no residual branch language in
  this plan. (Branch impact, for the record: had inventory-only been
  chosen, P2 ACs 1/3/5/6 + the P3 findings→bugs chain would have needed
  rewriting — cross-phase, not a one-line edit.)
- **Dialect granularity:** DECIDED — one `posix-shell` dialect. The BRE/ERE
  semantics fork is real and handled via the `shell_flags` record field +
  compiler normalize, not a dialect split. Normalize handles BOTH directions
  for BRE records; ERE records pass through untouched (verified: ERE `\+`
  is literal on GNU + busybox, pcre agrees — no reject needed). BRE
  backrefs and GNU `\<` `\>` are Unencodable. BRE = GNU/busybox flavor.
- **shell_flags plumbing:** the full chain is specified and file-listed:
  extractor emits `shell_flags` via typed `extra_fields` → record carries it
  → `compile_records.py` threads `rec.get("shell_flags")` →
  `compile_pattern(shell_flags=...)` normalizes at entry (entry-only, never
  re-normalized in the branch) → hooks see normalized ERE text →
  posix-shell→pcre.
- **Probe counter consistency:** THREE counters exist but their roles are
  now defined: the P1 script `--dir` is authoritative for the probe;
  `walk_repo` gains shell dispatch in P2 so the tooling path agrees;
  `scripts/merge-probe-draft.py` (P3) is the DEFINED bridge that populates
  the pre-P2 probe draft's shell evidence from the P1 counter — without it
  the artifact's `probe.regex_sites`/`predicted_buckets` cannot carry shell
  surface pre-P2 (walk_repo's dispatch lands in P2, after the probe runs);
  `scripts/reconcile_probe.py` (P3) is the post-P2 reconciliation procedure
  with a tolerance threshold and defined input contract.
- **Probe artifact role:** the OpenWrt probe decision is a PLAN-TIME
  artifact (validated by `test_probe_decision_artifacts.py`, consumed by
  wave review + follow-on stream kickoff) — NOT a runtime gate artifact
  (`check_admission_gates` only reads manifest-corpus decisions). The
  follow-on wave registers OpenWrt as a manifest corpus, at which point the
  runtime path engages.
- **Probe timing vs P2:** the probe's novelty evidence must be captured
  before P2 merges, or the artifact must claim a different novel surface.
  This reorder (P3 evidence pre-P2) is load-bearing — do not let P2 land
  before the probe counts are frozen. The probe runs against a detached
  checkout of the recorded PR #259 commit; P1 merge is NOT a precondition.
- **P2 scope (luna):** P2 is large (extractor, record API, compiler,
  batch plumbing, registry, manifest, admission-walk, migration, re-freeze).
  For the wave carve, split P2 into ordered child issues with a tested
  extractor/record seam BEFORE compiler + manifest work (see carving).
  Execution remains one owner (Hermes agent) but review is incremental.
- **Multi-stream operations (post-probe):** if the probe goes, the OpenWrt
  stream is a NEW mining pipeline, not a fork of the GitHub one — and the
  architecture stays stream-generic (the pattern repeats for later sources,
  e.g. other distro feeds). Same intent chain (novel findings → real bugs)
  but source-native extraction (init scripts, UCI config parsing,
  busybox-ash) and its own admission artifacts. Sequencing, allocation
  (compile budget is shared — the super-linear Z3 cost binds ALL streams),
  and stream handoff rules are follow-on work, deliberately out of scope
  here; the P3 artifact documents the budget partition as the handoff record.
- **Snapshot freshness:** `dogfooding_novelty_2026-08-12.json` is
  point-in-time; the script is the primitive, the snapshot is evidence.
  Refresh cadence = per batch; re-freeze after any extractor change (P2.5).
- **hermes-agent dominates the pool (~10:1 sites):** the global singleton
  fraction is mostly its tail; per-family views (OpenWrt family vs
  hermes/happycow) are the more informative numbers going forward.
- **Owners:** P1/P2/P3 each have an explicit owner (Hermes agent, work
  profile, standard-development) — no unowned deliverables.

## Suggested issue carving (after review pass)

- Umbrella: dogfooding measurement + shell dialect + OpenWrt probe
  (phase map, artifact contract, cross-cutting gates: ground-truth-or-
  it-didn't-happen, precision guard, probe-timing rule, budget partition,
  shell_flags plumbing contract, normalize-entry-only rule)
- P1 issue: measurement primitive land (PR #259) — owner Hermes
- P2 issue: POSIX shell extractor + scoped compiler backend — owner Hermes.
  **Carve within P2 (ordered child issues, tested seam before next):**
  P2a extractor + record `extra_fields` + schema enum + tests (the tested
  seam), P2b compiler backend (posix_shell.py + dispatch + normalize +
  fixtures), P2c registry + manifest + admission-walk dispatch + migration
  + P2.5 re-freeze. Merge order P2a → P2b → P2c; each merges independently.
- P3 issue: OpenWrt feed admission probe (evidence pre-P2) — owner Hermes
