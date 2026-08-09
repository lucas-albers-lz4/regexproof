# Java-dialect feature survey (Corpus Wave 4 / P4)

Phase of [#133](https://github.com/lucas-albers-lz4/regexproof/issues/133).
Precedent: [`sweep/corpus-wave3/perl-features.md`](../corpus-wave3/perl-features.md).

## Corpus pin

| Field | Value |
|---|---|
| Repo | `https://github.com/OWASP/java-html-sanitizer` |
| Pin (default branch HEAD at survey) | `a979a97e65f3cda1921fe3bb27ff4f9457be5c8d` |
| Probe path | P1 dialect-agnostic `count_java_pattern_compile` (no `validate_dialect`) |

Trial gate artifact ([`properties/generated/java-html-sanitizer_gate_decision.json`](../../properties/generated/java-html-sanitizer_gate_decision.json))
had `corpus_pin: null` (ephemeral `/tmp` clone). This pin supersedes that gap for
graduation work.

## Site inventory

| Surface | Sites | Notes |
|---|---|---|
| Committed fixture `tests/fixtures/admission/java_sites/` | **22** / 2 files | Synthetic `Pattern.compile("patN")` — walker AC |
| Live pin, `src/main` string literals | **20** / 2 example files | `EbayPolicyExample.java` (19) + `SlashdotPolicyExample.java` (1) |
| Live pin, main+test tree | **46** / 6 files | Includes `CssFuzzerTest` (20) etc. |

Trial prose “22 sites / 2 files” matches the **fixture** shape used for P1 ACs;
live main-source literals at this pin are 20. Graduation uses the pinned live
corpus; fixture remains the CI-stable count of 22.

## Construct survey (live main literals + fixture)

| Construct | Seen | Decision (pcre approximation) |
|---|---|---|
| Plain ASCII / `\w` / char classes | common | **Encode** as `pcre` |
| Non-capturing `(?:…)` / alternation / `{n,m}` | common | **Encode** as `pcre` |
| Inline `(?i)` | EbayPolicy (4) | **Encode** — fold via pcre `i` / existing compiler flag path |
| `\Q…\E` quoting | `HISTORY_BACK` | **Reject** `quote` — pcre2 accepts but Z3 ASCII mirror does not lower `\Q` faithfully |
| Unicode `\p{L}` / `\p{N}` | several URL/title patterns | **Reject** for Z3 membership path (outside A1B ASCII-bound encodable subset) unless a later fix-wave adds a declared fold — **no silent widen** |
| Lookaround | not in main 20 | N/A this pin; reject if appears |
| `Pattern.compile(String, int)` flag API | not in main 20 string sites | Out of string-literal extractor scope for v1 |
| Fixture `pat0`… literals | 22 | Trivially encodable as `pcre` |

## Locked dialect decision

**Declared pcre approximation** — do **not** add `java` to `DIALECTS` in this wave.

- Inventory / probe dialect label remains `java` (count-only).
- Compile + ground-truth replay use `helpers/pcre2` with dialect `pcre` and an
  explicit `approximation: java→pcre` note on records / SEMANTICS.
- Encodable subset for triage = patterns that `helpers/pcre2` parses and that
  avoid rejected markers (`\p{`, lookarounds, etc.).

### Differential-fuzz pass criteria (encodable subset)

1. Exhaustive short strings + random + dangerous-char mutations
   (`scripts/differential-fuzz.py` shape).
2. **Zero disagreements** between Z3 mirror accept/reject and `helpers/pcre2`
   on the bounded domain for every pattern in the encodable subset.
3. Patterns that fail parse / hit reject markers are **excluded** from the
   subset (recorded as reject reasons), not silently lowered.

If a security-boundary pattern requires a construct that cannot be approximated
without A1B widening, stop and file a fix-wave — do not invent a silent route.

## Helper pre-gate

```bash
python helpers/pcre2/match.py parse 'a+'
printf 'aaa' | python helpers/pcre2/match.py match 'a+' ''
```

## Handoff (P4 B2) — done

1. Extractor: `regexproof/extractors/java_pattern.py` (`dialect: pcre` +
   `approximation: java→pcre`).
2. Triage script: `scripts/java-html-sanitizer-triage.py` (compile +
   differential vs `helpers/pcre2`; empty-string samples omitted for helper
   quirk on optional patterns).
3. Committed artifacts under `properties/generated/java-html-sanitizer_*`
   (extractor JSONL, triage NDJSON, fraction, batch MD).
4. Gate supersede: `decision=go`, `decision_basis=escape_hatch`,
   `corpus_pin` = pin above; pin `src/main` fraction **14/20 = 0.70** with
   zero differential disagreements on the encodable subset.
