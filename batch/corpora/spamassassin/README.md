# spamassassin corpus

Pinned Apache SpamAssassin rules corpus for Corpus Wave 3 Phase 2 (issue #113).

## Materialize the corpus

The full SpamAssassin rules tree is not committed here (third-party). Point this
directory at the **pinned** clone before measuring:

```bash
PIN=17e7842caa629d032589458f86d2f5ce8e7306a4
git clone https://github.com/apache/spamassassin.git /tmp/spamassassin
git -C /tmp/spamassassin fetch --depth 1 origin "$PIN"
git -C /tmp/spamassassin checkout "$PIN"
# Rules live under rules/ in the upstream tree.
ln -sfn /tmp/spamassassin/rules batch/corpora/spamassassin/rules
test "$(git -C /tmp/spamassassin rev-parse HEAD)" = "$PIN"
```

Manifest pin (`regexproof/batch/runner.py` corpus `spamassassin`):
`17e7842caa629d032589458f86d2f5ce8e7306a4`. Provenance: apache/spamassassin.

## Sample vs full

`spamassassin` is a wave corpus without `measure_scope: sample`. If `rules/` is
missing/empty, measure/batch **hard-error** (no silent sample fallback).
Use `batch/corpora/spamassassin/sample/` only for local smoke by pointing the
manifest path at it explicitly. Committed artifact
`properties/generated/spamassassin_encodable_fraction.json` was measured on
the pinned full clone (`scope=full_corpus`).

## Extractor + dialect

- Extractor: `spamassassin` (`regexproof/extractors/spamassassin.py`)
- Dialect: `perl`
- Rule kinds: `body`, `header`, `uri`, `rawbody` (eval: forms skipped)

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus spamassassin --assert-determinism
```
