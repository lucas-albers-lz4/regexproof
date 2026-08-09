# Perl-dialect feature survey (Corpus Wave 3 / P1)

Pinned helper: `helpers/perl/match.py` (`PERL_VERSION` pin, presence gate, no Python `re` fallback).
Sample surface: SpamAssassin ~249 regex rules across 14 `.cf` files (`body`/`header`/`uri`/`rawbody`).

## Construct decisions (for P2 compiler)

| Construct | Sample role | Decision |
|---|---|---|
| Plain / `(?i)` | common | Encode via perl dialect → Z3 (re2-like core + flag fold) |
| POSIX `[[:alpha:]]` etc. | present in spam rules | **Map** `[[:alpha:]]`→`[a-zA-Z]`, `[[:digit:]]`→`[0-9]`, `[[:space:]]`→`[\s]`, `[[:punct:]]`→`[\p{Punct}]` with perl-helper ground truth — **or** reject `[:` in-class. Never silent `{:aplh}` |
| `\K` | reset start | **STRIP candidate** (membership-unchanged; mirrors `pcre_strip.py` `(?>` precedent); hard-reject only as fallback |
| `\x{…}` | hex escapes | Lower to codepoint ranges (spike-verified encodable) |
| Trailing `(?:…\|$)` / `\|$` | common A1B shape | Already lowered post-#87/#89 |
| `(?{code})`, `(?(?{…}))`, recursion `(?R)`, `\g{-1}` | rare / dangerous | Reject; bucket a/b/c |
| Markers `\g{`, `\N{`, `\p`, `\P`, `\h`, `\v`, `\Q` | perl-specific | `_local_reject`-style gate (never silent `Lit`) |

## Helper pre-gate

```bash
python helpers/perl/match.py version   # ok + version ≥ 5.38
python helpers/perl/match.py parse 'a+'
printf 'aaa' | python helpers/perl/match.py match 'a+' ''
```

No perl-corpus witness verification until this is green (Wave-1 pcre2 lesson).

## Fixture replay

`sweep/corpus-wave3/fixtures/{spamassassin,perl_re}.json` — perl helper dual-replay vs Z3 literal/re2-encodable spike mirrors.

## Handoff

P2 ships `extractors/spamassassin.py`, `perl` in `DIALECTS` + dispatch, fraction + gate decision, goldens per construct class. Differential-fuzz vs this helper is load-bearing.
