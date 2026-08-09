# Traps — solver gotchas that cost real debugging time

Every entry below was hit (or measured) during the usrmanage/fwlive work on
`z3-solver==5.0.0` (2026-08). Read this before writing constraints.

## 1. `Complement()` is LANGUAGE complement, not char-class negation

<!-- verified-finding: VF-001 -->

`Complement(Re('"'))` = all strings that aren't exactly `"` — so `a"`, `ba`,
`\"` are all "in the complement", and `Star(Complement(Re('"')))` is **NOT**
`[^\"]*`. Controlled tests:

| Query | Result |
|---|---|
| `s == "b"` ∧ `InRe(s, Complement(Re("a")))` | sat |
| `s == "a"` ∧ `InRe(s, Complement(Re("a")))` | unsat |
| `s == 'a"'` ∧ `InRe(s, Complement(Re('"')))` | **sat** ← the trap |
| `s == ""` ∧ `InRe(s, Complement(Re("a")))` | sat |

To exclude a char class, use `Union(Range(...))` of the allowed chars, or
string ops (`IndexOf`, `Contains`).

**✅ Valid use — single-char membership:** `InRe(c, Complement(Re('"')))`
with `Length(c) == 1` DOES correctly exclude `"` (the complement of the
one-char language restricted to one-char strings is the char-class
complement). Verified in the fwlive pilot (word-boundary check:
`Complement([A-Za-z0-9_])` with `Length==1` excludes alnum/underscore and
admits `.`). The trap is exclusively the multi-char / `Star(Complement(...))`
context — restrict to single-char membership and Complement is safe.

## 2. The `seq` backend solves regex; `z3str3` returns `unknown` instantly

<!-- verified-finding: VF-002 -->

Z3 has two string backends. `z3str3` (`smt.string_solver=z3str3`) solves pure
string equations but gives `unknown` (1ms) on `InRe` constraints. Do NOT set
it for regex work. The default `seq` backend solved P2 in 927ms, P3 in 2ms.

| Backend | Regex membership (`InRe`) | String eq |
|---|---|---|
| `seq` (DEFAULT) | ✅ solves | ✅ |
| `z3str3` | ❌ `unknown` instantly | ✅ |

## 3. NUL (0x00) is a real edge — state input-domain assumptions

<!-- verified-finding: VF-003 -->

An escaper with `if (o > 0 && o < 32)` prints NUL raw through its `else`
branch. "No raw C0 controls" is then FALSE as stated. Fix: state the
input-domain assumption explicitly — *POSIX shell strings cannot contain NUL*
(C strings are NUL-terminated) — and encode it as a solver constraint +
comment, or the property is false as stated.

## 4. "Deny-list unreachable" is ambiguous

`root` IS in the username-regex language; only the accept-language
(regex ∧ ¬deny-list) excludes it. Encode as `accept(s) ∧ s == "root"` → unsat,
NOT plain regex membership. Mirror deny-lists verbatim — forget the deny-list
and the proof silently passes for a name that must be rejected.

## 5. `re.replace_re` / `str.replace_all` are NOT supported

The Z3 guide: "currently not supported". Model replacements as string ops or
unroll (for example, `IndexOf`/`SubString`/`Concat` composition).

## 6. Regex unfolding is incomplete with string constraints

The default solver lazily unfolds memberships via symbolic derivatives — it
works for many membership/non-membership queries but "is not a complete
procedure when membership constraints are combined with constraints over
strings." Don't expect a decision procedure for the full combination. This is
the mechanism behind monolithic-image timeouts — decompose (see
DECOMPOSITION.md).

## 7. `SubString` with symbolic indices is expensive

Prefer concrete indices. `SubString(s, 0, IndexOf(...))` is fine; symbolic
offsets into loops are not.

## 8. `FullRe` is NOT exported in z3py 5.0.0

`NameError`. Use `Star(Re("..."))` over an explicit char set instead.

## 9. Length bounds are load-bearing

Same property shape (`InRe` + `Contains` exclusion), different caps:

- Username validator (`^[a-z_][a-z0-9_-]{0,31}$`, 9-name deny-list): all 10
  injection-char exclusions <1s each.
- Actor whitelist (`^[A-Za-z0-9._@-]{1,64}$`): 9/9 instant at `Length ≤ 16`;
  **`Length ≤ 64` timed out at 60s** on the same query.

Timing caveat: these numbers were measured on one machine (z3-solver 5.0.0,
2026-08, single-threaded). They are **order-of-magnitude guides**, not
portable benchmarks — a different CPU/container can shift the exact cutoffs
(16 vs 64) by a factor of 2-3. Use the shapes, not the raw milliseconds.

Mitigation for real bounds > ~16: prove the alphabet-level property
(single-char `InRe(c, class) ∧ c == bad` → unsat, instant, length-independent),
and/or length-slice with incremental push/pop (16, 32, 48, 64).

## 10. `unknown` is NOT sat

<!-- verified-finding: VF-010 -->

Treating solver timeout as SAT produced "FAIL ... SAT (counterexample!)" with
no model. Always check `r == sat` before reading a model. Report `unknown`
honestly — it is a hard failure in CI (**not proven**), never a pass.
Harness JSON sets `result="timeout"` and `not_proven=true`.

## 11. Lookaheads/lookbehinds are not expressible in stock Z3

The regex theory is the *regular-language* theory — no `(?=...)` constructors.
Patterns with lookahead must be rewritten to equivalent non-lookahead forms
(string-ops prefix checks work for most) or routed through Z3-Noodler's
`re.from_ecma2020` (JS only). See BACKENDS.md and the fwlive classifier note
in properties/.

## 12. Presence-gates must use whole-word grep — substring matches lie

Gating a property on code presence ("is the fallback still there?", the
temporal-coupling gate) with a naive `grep -c sed file` matched the word
"pas**sed**" inside a comment and nearly produced a false "fallback absent"
verdict (count 1 instead of 0). Use whole-word or anchored patterns and
derive the verdict from the count explicitly:

```bash
grep -wc "sed" file           # whole-word count — 0 = truly absent
grep -cE "(^|[^A-Za-z])sed([^A-Za-z]|$)" file   # or anchored alternative
```

Print the verdict ("0 hits — path absent, finder flipped" vs "N hits — finder
stays active"), never just the raw count. This bit the regexproof pilot
(usrmanage P3 gate); ground-truthing the gate output caught it before the
false claim shipped.

## 13. `Re("...")` is a LITERAL, not a pattern parse

<!-- verified-finding: VF-004 -->

`z3.Re("[a-z]")` builds the regex matching the 5-character string `[a-z]`
literally — it does NOT compile a regex pattern. Verified:

```
InRe("a", Re("[a-z]"))  → unsat      (the 1-char string "a" is not "[a-z]")
InRe("[", Re("[a-z]"))  → sat        (the literal "[a-z]" contains "[")
```

This silently breaks any "mirror = Re(user_pattern_string)" design: the
mirror accepts a different language than the real regex and differential
fuzz reports mismatches on every input — or worse, a containment property
passes vacuously. The original `differential-fuzz.py --mirror-regex`
design shipped exactly this bug. It was caught in testing and the script
now requires a z3py EXPRESSION (Union/Range/Concat/Star), never a pattern
string. Build mirrors with the API, same as z3-verify.py properties.

## 14. Char-range boundaries are load-bearing — off-by-one silently includes neighbors

Building `[^A-Za-z0-9_]` as `Union(Range("[", "`"), ...)` wrongly includes
`_` (0x5F), which IS alnum: `Range("[","`")` spans 0x5B–0x60. The correct
complement is `Range("[","^")` (0x5B–0x5E) + `Re("`")` (0x60). A Z3
witness (`b = "_"`) exposed the error in the fwlive sweep (property
"trailing boundary rejects alnum" initially PASSED a wrong encoding).
Always write complements as explicit disjoint ranges and probe each
boundary char with a membership query before trusting the class.

## 15. `Opt` is the optimizer class, not regex optional

There is NO regex-optional `Opt`/`ReOpt` in z3py 5.0.0 — `z3.Opt` is the
optimization-solver class. Regex `?` is `Union(r, Re(""))` (verified:
accepts both the token and the empty string). This bit the
differential-fuzz mirror namespace (AttributeError at import). Documented
here so a mirror namespace never advertises `Opt` as regex-optional.

## 16. Case-insensitive flags: the mirror must expand case

<!-- verified-finding: VF-005 -->

`Re("AND")` is case-sensitive. A pattern compiled with `re.I` / `(?i)`
silently accepts a SUPERSET of the naive mirror's language. Verified
(hermes-agent sweep, telegram bot-handle boundary,
`re.fullmatch(r"[a-z0-9_]{2,29}bot", handle, re.IGNORECASE)`):

| handle | real regex | naive mirror `Re("bot")` | ci() mirror |
|--------|-----------|---------------------------|-------------|
| `mybot` | accepts | accepts | accepts |
| `MyBot` | accepts | **rejects** | accepts |
| `MYBOT` | accepts | **rejects** | accepts |

A containment property proven against the naive mirror covers a strict
subset of the real accepted language — the classic silently-narrower
mirror. **Use `ci(word)` / `ci_class(lo, hi)` from `scripts/z3-verify.py`**
(Union of both cases per char) for any pattern compiled with a
case-insensitive flag. Related: `re.match`/`re.sub` with `^` is a PREFIX
match while Z3 `InRe` is whole-string membership — model anchored
matchers with `prefix_match(regex)`, never the bare regex (verified:
`InRe("AND foo", Re("AND"))` is unsat, `re.match(r"AND", "AND foo")`
matches; see P6 properties).

## 17. Unicode classes: the input-domain assumption is load-bearing

<!-- verified-finding: VF-006 -->

Python's `\w \d \s \b` are Unicode-aware by default. Z3's `Range`/`Union`
classes are ASCII. An ASCII mirror of a Unicode class silently diverges —
and the DIVERGENCE DIRECTION determines the danger:

- **Narrower mirror (`\d`): false FINDINGS.** Python `\d` matches
  Arabic-Indic `٣` and fullwidth `１`; an ASCII `[0-9]` mirror misses them.
  A property "phone-shaped strings are redacted" proven on the mirror
  under-reports (noise, safe direction).
- **Wider mirror (`\b`): false SAFETY.** Python `\b` is a Unicode word
  boundary — `中` is `\w`, so `xx中sk-<token>` has NO boundary and is NOT
  redacted by the real regex. An ASCII `\b` mirror treats `中` as a
  boundary and matches — a coverage proof passes while the real layer
  leaks (verified hermes-agent `gateway/run.py:150`).

**Discipline:** declare `input_domain="ascii"` on `@prop` only when the
boundary is genuinely ASCII-constrained; run `--require-domain` to make
unstated domains a hard failure; add non-ASCII chars to differential-fuzz
mutation sets so a Unicode-exposed boundary with an ASCII mirror produces
a mismatch instead of a silent pass.

## 18. Search-wrapped `rule_diff` blows up Z3

<!-- verified-finding: VF-007 -->

Shape-5 gap queries (`InRe(s,R2) ∧ Not(InRe(s,R1))`) under a **search**
wrapper (leading/trailing `Star(any)`) routinely return `unknown` within
budget. The Phase-3 gitleaks pilot compiles R1/R2 as **`fullmatch`** mirrors
with tight length bounds, then ground-truths witnesses with the real
detector `call_kind` (usually `search`). See
`docs/examples/shape5-rule_diff.md` and `scripts/rule-diff-pilot.py`.

## 19. ModSecurity `@rx` strings escape quotes as `\"`

CRS / ModSecurity operator strings are double-quoted with `\"` escapes
inside the pattern. A naive `"..."` capture truncates at the first
embedded quote (102 false parse-errors on CRS v4.28.0 before
`regexproof.extractors.modsec`). Always join `\` continuations before
matching so `id:NNNN` on a later line is captured.

## 20. Exact `{1}` / `{1,1}` must not call Z3 `Concat` with one arg

`lower._repeat` previously did `Concat(*([body] * lo))` for `lo == hi`.
When `lo == 1`, Z3 raises `At least two arguments expected` — a compiler
**crash**, not an encodable reject (19 validator.js sites). Treat `{1}` as
identity (`return body`).

## 21. Pattern-too-long is a capacity policy, not a language limit

`DEFAULT_MAX_LENGTH = 256` on every dialect compiler. Patterns longer than
the cap raise `pattern-too-long`. This is an **interactive Z3 query budget**,
not a claim that the regex is inexpressible:

| Route | What to do |
|---|---|
| Interactive / property suite | Keep the 256 cap; shorten or decompose the pattern |
| Batch inventory | Record `unencodable_reason=pattern-too-long`; do not silent-skip |
| Long security regexes | Prefer **ReDoS-only** analysis (`docs/REDOS.md`) + manual review; optional raise `max_length=` only in controlled batch jobs |

Never treat TIMEOUT/`unknown` as a pass when probing a lengthened cap.

## 22. ECMA flags `m` / `u` / `v` / sticky (`g`/`y`/`d`) — reject, don't approximate

JS RegExp flags beyond `i`/`s` are **explicit rejects** in `compile_ecma`:

| Flag | Reason | Triage |
|---|---|---|
| `m` | `^`/`$` become line-anchored | Rewrite (IndexOf/split) or LOOKBEHIND_REWRITE notes |
| `u` / `v` | Unicode / Unicode-sets mode | Stock Z3 ASCII domain — route to triage, not silent BMP approx |
| `g` / `y` | Stateful `lastIndex` | `stateful` — not a regular language question |
| `d` | `hasIndices` match metadata | `stateful` |

Do not encode these as ASCII-ish mirrors. Report the reject reason in triage
NDJSON (`unencodable_reason`) so batch routing stays honest.

## 23. Hex escapes must lower to the codepoint, not literal text

<!-- verified-finding: VF-HEX-001 -->

`\xNN` / `\x{…}` inside a pattern (including character classes) must become
the corresponding character in the Z3 mirror. A pre-fix bug compiled
`[\x22]` as encodable while the mirror accepted the literal strings `x2` /
`x22` and rejected `"` — the opposite of Python `re`, PCRE2, and ECMA.

**Regression:** `compile_pattern(r"[\x22]", …)` must SAT-admit `"` and
UNSAT-reject `x22`. Same for `\x{22}`. Class ranges `\x21-\x7e` must expand
to the codepoint range (not `x` / `-` / digits as separate atoms).

## 24. ReDoS fan-out uses a wall-clock gate, not a count cap

Batch `--with-redos` walks encodable records through the non-Z3 ReDoS helper.
Truncation is governed by `--redos-timeout-s` or per-corpus
`budget.redos_wall_s` (default **120s** when unset). A count-based
`--redos-cap` was removed: it produced incomplete reports that looked like
“only N findings exist”. Incomplete runs write `{corpus}.ndjson` with
`result=incomplete` then fail the evidence gate. The budget is checked
before and after each `analyze_record` call (a single hung helper call is
still not preemptible — that is a helper-level limit, not a silent skip).

## 25. ASCII-domain `\b` encode — never silent Unicode mirrors

<!-- verified-finding: VF-WORD-BOUNDARY-001 -->

Stock Z3 has no zero-width `\b`. Edge-only `\b` / `\b…\b` (no mid-pattern,
no `\B`) lowers under **ASCII `\w` = `[A-Za-z0-9_]`** as a search-shaped
`(^|\W)inner(\W|$)` union (see `WordBounded` in `simple_parse` / `lower`).

| Dialect | `\b` |
|---|---|
| re2 / pcre / ecma (no `u`) | Encode — engine `\w` is ASCII |
| py_re default | **Reject** `word-boundary` — Unicode `\b` (TRAPS #17 false-safety) |
| py_re + `re.ASCII` / `(?a)` | Future: may encode; still reject until wired |
| Mid-pattern `foo\bbar`, `\B` | Reject `word-boundary` |

Spike evidence: `properties/generated/word_boundary_spike.json` (GO).
Differential-fuzz against `re.ASCII`; Unicode probes must diverge from
Python-default `\b` and must not be used as a silent pass.

## 26. Dialect `\s` on complement / `[^\S]` must use dialect space codes

<!-- verified-finding: VF-SPACE-COMPLEMENT-001 -->

Positive `\s` already uses each dialect's `space()` alphabet (ECMA includes
NBSP / U+2028 / U+2029; RE2 omits `\v`). The negated-class / `\S` path used
to hard-code `_SPACE_CODES` (` \t\n\r\f\v`) — so ECMA `[^\S]` rejected NBSP
while Node accepted it (**false-UNSAT**). Pass `space_codes=` from each
`compile_*` into `lower` / `_member_codes`. Documentation alone does not
eliminate the under-approximation.

## 27. Per-alternative anchors and literal `}+` / `}?`

- `^a|b` must not compile as `^(a|b)`. Shared `at_start`/`meta` across `Alt`
  branches caused search under-approx (`xb` accepted by real engines,
  rejected by the mirror). Reject `per-alternative-anchor` (parity with
  `py_re`) until per-alt wraps exist.
- `strip_atomic_and_possessive("a}+")` must preserve `a}+` — `}` is a
  possessive closer only after a real `{n,m}` brace, not after a literal
  `}`. Same guard for lazy `}?`.

## 28. Pattern-final `(?:…|$)` — A1B lowering (accept-class boundary)

<!-- verified-finding: VF-TRAILING-ALT-DOLLAR-A1B-001 -->

Stock lowering rejects `$` inside an alternation as `per-alternative-anchor`
(trap 27). That is sound for mid-pattern and caret-branch shapes, but many
secret-detector rules end with a **pattern-final** non-capturing
`(?:R|$)` / `(?:…|$)`. Those are encodable via A1B
(`regexproof/compiler/trailing_alt_dollar.py`, wave #81 / P2 #87).

**Minimal repro (encode):**

```text
pattern:  foo(?:bar|$)
call:     search
mirror ≈  Union( Star(any)·foo·bar·Star(any) , Star(any)·foo )
domain:   ascii;a1b_suffix_bound=128
```

Membership: `"foo"` and `"foobar"` accept; `"bar"` / `"fooba"` reject.
Bare X/R sub-mirrors must use `fullmatch` (search wrappers in sub-position
are unsound — #86).

**Accept condition (do not widen casually):**

| In class | Out of class (still `per-alternative-anchor`) |
|---|---|
| Pattern ends with `(?:…|$)` | Mid-pattern `$`: `a(?:$|b)c` |
| Prefix X top-level anchor-free | Leading `^` in X → **caret-in-X** (§33), not A1B |
| `\b` in X allowed | Capturing / bare `(|$)`: `(&|$)` |
| | Caret-boundary wrap: `(?:^|…)(…)(?:$|…)` |

**Word-boundary suffix:** stock `WordBounded` + `$` false-SATs mid-string
junk after a non-suffix X. Use `wb_leading_suffix_mirror` (`(^|\W) INNER $`,
no trailing `Star(any)`).

**Sat-find note:** prefer case-split `Or` branches; declare
`Length(q) ≤ a1b_suffix_bound` (default 128) on the suffix witness. Fuzz
membership timeouts should be ≥15s for these mirrors.

## 29. YARA encoding-domain declaration (ascii vs wide)

<!-- verified-finding: VF-YARA-DOMAIN-001 -->

YARA `$s` modifiers are **not** regex flags. `ascii` and `wide` are distinct
encoding domains: the same pattern text yields different matches (and must
not share a `regex_id`). Schema v2 puts `domain` on the record and as the
optional 7th `regex_id` component (`ascii` default omitted for v1 compat).

**Trap:** compiling once and claiming “encodable” while `wide` is undeclared
(or colliding ascii/wide IDs) silently under-proves the rule.

**Minimal repro:**

```text
rule:   $a = /abc/ ascii wide
wrong:  one regex_id, one mirror
right:  two records — domain=ascii and domain=wide (UTF-16LE code-unit mirror)
        wide non-literals → wide-non-literal reject (not silent accept)
```

`fullword` ≠ `\b`. See `regexproof/compiler/yara.py` / Wave-2 P2 (#97/#105).

## 30. Semgrep denominator precision (`pattern:` vs `pattern-regex:`)

<!-- verified-finding: VF-SEMGREP-DENOM-001 -->

Semgrep YAML `pattern:` is a **code-pattern** DSL, not a regex site.
Counting every `pattern:` line as a regex inflates the denominator
(~9k “sites”, fraction ~0.28 no-go). Real regex surfaces are
`pattern-regex:` / `metavariable-regex:` (incl. block scalars).

**Minimal repro:**

```yaml
# NOT a regex site — exclude from denom
- pattern: foo($X)
# IS a regex site
- pattern-regex: |
    (?i)password\s*=
```

After the dedicated extractor (`regexproof/extractors/semgrep_yaml.py`),
Wave-2 P3 measured **707/1431 = 0.4941 go**. Semantics are
`ascii_approx_rust_regex` (rust `regex` crate), not stock `py_re` parity.

## 31. Testdata sample vs full (`complete_run` / silent fallback)

<!-- verified-finding: VF-SAMPLE-SCOPE-001 -->

A `scope=sample` fraction with `complete_run=true` is a lie. Wave corpora
must either:

1. declare `measure_scope: sample` → `complete_run=false`, or
2. materialize the full root → measure with `complete_run=true`.

Missing full roots without `measure_scope=sample` **hard-error** (no silent
fallback). Budget breaches also force `complete_run=false` and clear stale
inventory.

**Minimal repro:**

```text
manifest: path=…/testdata (missing), measure_scope unset, WAVE_CORPORA
wrong:    fall back to sample/, write complete_run=true
right:    SystemExit HARD ERROR  OR  measure_scope=sample → complete_run=false
```

See `scripts/measure-corpus-fraction.py` / Wave-2 P4 (#99/#107).

## 32. Cross-engine parity discipline (re2 vs pcre)

<!-- verified-finding: VF-CROSS-ENGINE-001 -->

Same rule text under Coraza (go-re2) and ModSecurity (pcre) is **not** a
single-engine property. Result classes:

| Class | Meaning |
|---|---|
| `gap` / `no-gap` | Both encodable; shape-5 SAT/UNSAT |
| `non-comparable-re2` | re2 rejects at parse; pcre ok |
| `non-comparable-both` | Both reject — counted, not a finding |

Engine-semantic divergences (e.g. `\s` / `$`-before-newline) are **findings**,
not measurement artifacts. Gap witnesses need **per-engine** ground truth
(`ground_truth.pcre2` + `ground_truth.go_re2`), not one generic status.

**Minimal repro:**

```text
pattern:  ^(?:GET|HEAD)$
R1:       re2 fullmatch mirror (Coraza)
R2:       pcre fullmatch mirror (ModSecurity)
witness:  "GET\n"  → pcre may match, re2 may not  → class=gap + dual GT
lookaround pattern → class=non-comparable-re2 (not a gap)
```

Pilot: `scripts/cross-engine-rule-diff-pilot.py` / Wave-2 P5 (#100/#108).

## 33. Caret-in-X vs A1B (do not widen A1B)

<!-- verified-finding: VF-CARET-IN-X-001 -->

Pattern-final `^X(?:R|$)` is **not** A1B. A1B rejects leading `^` in X
because mid-string `Star·X` suffix semantics are wrong under a BOS caret.

Caret-in-X (`regexproof/compiler/caret_in_x.py`, domain `ascii;caret_in_x`):

- `$` branch ≈ strings equal to X' (X without the leading `^`)
- `R` branch ≈ strings with prefix X'R (no leading `Star(any)`)
- Dispatcher tries caret-in-X **before** A1B

**Minimal repro:**

```text
pattern:  ^0+(?:&|$)
wrong:    A1B Union(Star·0+&·Star, Star·0+)   # mid-string "0+" over-accepts
right:    Union(Concat(0+&, Star), fullmatch(0+))
reject:   ^a|b , a(?:$|b)c , (?:^|a)  # still per-alternative-anchor
```

Never silently remove A1B’s caret check — that is a false-UNSAT hazard
(TRAPS §27). Mid-pattern / `$`-first alts remain out of both shapes (#103).

## 34. Perl dialect frontier (`\K`, code assertions, POSIX, `\x{…}`)

<!-- verified-finding: VF-PERL-FRONTIER-001 -->

Perl is not “PCRE with a different helper.” Membership mirrors must route
through the `perl` dialect + `helpers/perl/match.py`, never Python `re`.
Construct classes diverge:

| Construct | Correct handling |
|---|---|
| `\K` | strip candidate (membership-preserving) or named reject — never silent Lit |
| `(?{…})` / `(?(?{…}))` / recursion | reject (`code-assertion` / related) |
| POSIX `[[:alpha:]]` | map with helper GT **or** reject `[:` — never silent `{` |
| `\x{…}` | lower to codepoint (same soundness as TRAPS #23) |
| perl-vs-pcre edges | findings under declared perl domain, not measurement noise |

**Minimal repro:**

```text
pattern:  a\Kb
wrong:    compile as py_re / pcre without strip → wrong membership or Lit("\K")
right:    perl dialect → strip \K (or reject) + replay via helpers/perl/match.py
```

See `sweep/corpus-wave3/perl-features.md` / Wave-3 P1–P2 (#112/#113).

## 35. `(?x)` whitespace/comment strip (class-aware)

<!-- verified-finding: VF-XFLAG-STRIP-001 -->

`(?x)` is insignificant whitespace + `#`-to-EOL comments. Strip **before**
flag lifting / lowering. `#` and spaces inside `[…]` stay literal. Residual
`x` after strip must **reject** (`x-flag-unstripped`) — never silent
literal-whitespace mirrors. Combined `(?xi)` / `(?sx)`: consume the group;
body strips only while `x` is on. Interaction with `i`/`s`/`m` is flag
folding after strip, not a reason to skip strip.

**Minimal repro:**

```text
pattern:  (?x) a b   # comment
          [ #]       # '#' inside class is literal
wrong:    Re("a b") / leave x in flags → go-re2 parse-error or space Lit
right:    strip → "ab" (+ class unchanged); residual x → reject
probe:    "a b" must NOT match stripped mirror (wrong_xflag_caught)
```

See `sweep/corpus-wave3/xflag-semantics.md` / Wave-3 P3 (#114).

## 36. Secret-detector pack (`pattern:` vs `regex:`)

<!-- verified-finding: VF-SECRET-PACK-001 -->

Nosey Parker YAML uses `pattern:`; shhgit uses `regex:`. Extractors must
key off the right field — sharing a generic YAML regex scrape conflates
detectors and under/over-counts. Filename-selection regexes are
**boundary-adjacent** (path filters), not the secret-on-untrusted-input
boundary; still inventory them, but do not treat them as the sole
security-boundary justification.

**Minimal repro:**

```yaml
# noseyparker rules/*.yml
pattern: (?x) AKIA[0-9A-Z]{16}
# shhgit config.yaml
regex: AKIA[0-9A-Z]{16}
wrong:  one extractor regex for both keys / skip filename rules silently
right:  extract_noseyparker vs extract_shhgit; declare filename rules adjacent
```

See `sweep/corpus-wave3/noseyparker-dialect.md` / Wave-3 P3 (#114).

## 37. ECMA sanitizer / validator boundary (DOMPurify + email)

<!-- verified-finding: VF-ECMA-SANITIZER-001 -->

DOMPurify URI/script gates (`IS_ALLOWED_URI`, `IS_SCRIPT_OR_DATA`) are the
security-boundary regex shapes — not every `/…/` in comments or docs.
Email validators (isemail / email-addresses) often carry lookarounds;
those rows go on the **reject-list** (typed reason), never silent
approx. Plan site-count greps that ignore comments inflate denominators
(wave-3 P4 corrected 146→16 / 121→5 / 71→4).

**Minimal repro:**

```text
wrong:  comment/URL grep → ~146 “sites”; lookaround encoded as Re(…)
right:  string-aware scan → 16 DOMPurify literals; lookaround → reject reason
        fraction gate ≠ admission gate (isemail/email_addresses NO-GO admit)
```

See `sweep/corpus-wave3/ecma-frontier-nogo.md` / Wave-3 P4 (#115).

## 38. Testdata full-suite vs sample (expected-file manifests)

<!-- verified-finding: VF-TESTDATA-FULL-001 -->

Wave-3 perl `t/re`, Go `regexp` tests, and V8 mjsunit are **full-suite**
testdata (`complete_run=true`), not sample stand-ins. Expected-vs-actual
file counts fail closed (wave-1 under-extraction lesson). Sample trees
under `batch/corpora/*/sample/` are unit fixtures only — never write
`complete_run=true` from them. Measure large suites under mem/wall budgets
(+ guarded single-flight) so OOM/`parse-error` zeros stay honest.

**Minimal repro:**

```text
manifest: expected_files=91, path=…/v8_mjsunit/rules (mjsunit pin)
wrong:    measure sample/regexp.js → complete_run=true, fraction “green”
right:    full tree file count == expected; budget breach → complete_run=false
```

See `sweep/corpus-wave3/testdata-p5.md` / Wave-3 P5 (#116); TRAPS §31.
