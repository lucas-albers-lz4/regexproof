# v8_mjsunit corpus (Wave-3 Phase 5 / #116)

Pinned **v8/v8** `test/mjsunit/**/regexp*.js` (91 files at pin).

## Materialize

```bash
PIN=15ce9d47586c47d1e44c9ddc49366cf4edc509a2
git clone --filter=blob:none --sparse https://github.com/v8/v8.git /tmp/v8
git -C /tmp/v8 sparse-checkout set test/mjsunit
git -C /tmp/v8 fetch --depth 1 origin "$PIN"
git -C /tmp/v8 checkout "$PIN"
ln -sfn /tmp/v8/test/mjsunit batch/corpora/v8_mjsunit/rules
test "$(git -C /tmp/v8 rev-parse HEAD)" = "$PIN"
test "$(find batch/corpora/v8_mjsunit/rules -name 'regexp*.js' | wc -l)" = "91"
```

Manifest pin: `15ce9d47586c47d1e44c9ddc49366cf4edc509a2`.
Expected files: **91**.

## Sample vs full

Wave testdata corpus (full pin required). `sample/regexp.js` is a tiny
literal/`new RegExp` smoke. Missing `rules/` → hard-error.

## Extractor + dialect

- Extractor: `v8_mjsunit` → `extract_js_precise`
- Dialect: `ecma` (node helper ground truth)
- `corpus_type: testdata` — admission gate_decision **not** required
- Mirror-fidelity mjsunit surface remains deferred (P1 `perl_re` /
  `go_regexp` fixtures untouched)

## Measure

```bash
.venv/bin/python scripts/measure-corpus-fraction.py --corpus v8_mjsunit --assert-determinism
```
