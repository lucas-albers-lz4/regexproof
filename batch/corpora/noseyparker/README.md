# noseyparker corpus

Pinned Praetorian Nosey Parker builtin rules for Corpus Wave 3 Phase 3 (issue #114).

## Materialize the corpus

The full rules tree is not committed here (third-party). Point this directory at
the **pinned** clone before measuring:

```bash
PIN=2e6e7f36ce36619852532bbe698d8cb7a26d2da7
git clone https://github.com/praetorian-inc/noseyparker.git /tmp/noseyparker
git -C /tmp/noseyparker fetch --depth 1 origin "$PIN"
git -C /tmp/noseyparker checkout "$PIN"
ln -sfn /tmp/noseyparker/crates/noseyparker/data/default/builtin/rules \
  batch/corpora/noseyparker/rules
test "$(git -C /tmp/noseyparker rev-parse HEAD)" = "$PIN"
```

Manifest pin (`regexproof/batch/runner.py` corpus `noseyparker`):
`2e6e7f36ce36619852532bbe698d8cb7a26d2da7`.

## Sample vs full

`noseyparker` is a wave corpus without `measure_scope: sample`. If `rules/` is
missing/empty, measure/batch **hard-error** (no silent sample fallback).
Use `batch/corpora/noseyparker/sample/` for local smoke (includes a `(?x)`
pattern). Committed fraction artifacts are measured on the pinned full clone.

## Extractor + dialect

- Extractor: `noseyparker` (`regexproof/extractors/noseyparker.py`)
- Dialect: `re2` (declared ASCII approximation of rust `regex` — see
  `sweep/corpus-wave3/noseyparker-dialect.md`)
- `(?x)` stripped at extraction via `strip_verbose_x`; residual `x` / `s`
  rejected fail-closed in `compile_re2`

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus noseyparker --assert-determinism
```
