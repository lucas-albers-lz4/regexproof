# yara_rules corpus

Pinned YARA-Rules corpus for Corpus Wave 2 Phase 2 (issue #97).

## Materialize the corpus

The full YARA-Rules repository is not committed here (third-party). Point this
directory at the **pinned** clone before measuring:

```bash
PIN=0f93570194a80d2f2032869055808b0ddcdfb360
git clone https://github.com/YARA-Rules/rules.git /tmp/yara-rules
git -C /tmp/yara-rules fetch --depth 1 origin "$PIN"
git -C /tmp/yara-rules checkout "$PIN"
ln -sfn /tmp/yara-rules batch/corpora/yara_rules/rules
test "$(git -C batch/corpora/yara_rules/rules rev-parse HEAD)" = "$PIN"
```

Manifest pin (`regexproof/batch/runner.py` corpus `yara_rules`):
`0f93570194a80d2f2032869055808b0ddcdfb360`. Provenance: YARA-Rules/rules.

## Sample fallback

When `rules/` is absent, `measure-corpus-fraction.py` / batch currently fall
back to `batch/corpora/yara_rules/sample/` and rewrite `scope` to `sample`
(stderr NOTE). The sample is for CI smoke only — **do not treat a sample
run as the Wave-2 fraction**. Committed artifact
`properties/generated/yara_rules_encodable_fraction.json` was measured on
the pinned full clone (`scope=full_corpus`, `complete_run=true`).

## Extractor + dialect

- Extractor: `yara` (`regexproof/extractors/yara.py`)
- Dialect: `yara`
- Domain variants: `ascii`, `wide` (per-variant records; domain passed to compile)

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus yara_rules --assert-determinism
```
