# yara_rules corpus

Pinned YARA-Rules corpus for Corpus Wave 2 Phase 2 (issue #97).

## Materialize the corpus

The full YARA-Rules repository is not committed here (third-party). Point this
directory at a pinned clone before running the scanner:

```bash
# shallow-clone the pinned commit into the repo tree:
git clone --depth 1 https://github.com/YARA-Rules/rules.git rules
# pin: 0f93570194a80d2f2032869055808b0ddcdfb360 (2024-07-29)

# or symlink an existing clone:
ln -s /path/to/yara-rules rules
```

The manifest entry (`regexproof/batch/runner.py`, corpus `yara_rules`) reads
`rules/**/*.yar` and `rules/**/*.yara`. Provenance: YARA-Rules/rules commit
`ccd1f0f` (2024-07-29).

## Sample fallback

When the `rules/` directory is absent, batch falls back to
`batch/corpora/yara_rules/sample/` which contains a small subset of rules
for CI smoke tests. The sample is NOT the measurement corpus — full-corpus
measurement requires the materialized clone and will hard-error if it cannot
find the `rules/` path when `measure_scope != "sample"`.

## Extractor + dialect

- Extractor: `yara` (`regexproof/extractors/yara.py`)
- Dialect: `yara`
- Domain variants: `ascii`, `wide` (per-variant records emitted)

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus yara_rules --assert-determinism
```
