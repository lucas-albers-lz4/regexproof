# perl_tre corpus (Wave-3 Phase 5 / #116)

Pinned **Perl/perl5** `t/re` regex test suite (full — not sample).

## Materialize

```bash
PIN=6aef1e87c1ea274e225828cbc1a6044b54feec44
git clone --filter=blob:none --sparse https://github.com/Perl/perl5.git /tmp/perl5
git -C /tmp/perl5 sparse-checkout set t/re
git -C /tmp/perl5 fetch --depth 1 origin "$PIN"
git -C /tmp/perl5 checkout "$PIN"
ln -sfn /tmp/perl5/t/re batch/corpora/perl_tre/rules
test "$(git -C /tmp/perl5 rev-parse HEAD)" = "$PIN"
test -f batch/corpora/perl_tre/rules/re_tests
```

Manifest pin: `6aef1e87c1ea274e225828cbc1a6044b54feec44`.
Expected files: **81** (80 `*.t` + `re_tests`).

## Sample vs full

Wave testdata corpus (full pin required for measure). `sample/` holds a
tiny `re_tests` slice + one `.t` for local smoke. Missing/empty `rules/`
→ measure **hard-error** (no silent sample fallback).

## Extractor + dialect

- Extractor: `perl_re_tests` (`regexproof/extractors/perl_re_tests.py`)
- Dialect: `perl` (helpers/perl ground truth)
- `corpus_type: testdata` — admission gate_decision **not** required

## Measure

```bash
.venv/bin/python scripts/measure-corpus-fraction.py --corpus perl_tre --assert-determinism
```
