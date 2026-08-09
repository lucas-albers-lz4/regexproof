# go_regexp_tests corpus (Wave-3 Phase 5 / #116)

Pinned **golang/go** `src/regexp/*_test.go` (incl. `syntax/`). Distinct from
any `go_regexp` / trufflehog rule-corpus path.

## Materialize

```bash
PIN=e5ec1263ca5e1428d233206b99dc21c38ea2a124
git clone --filter=blob:none --sparse https://github.com/golang/go.git /tmp/golang-go
git -C /tmp/golang-go sparse-checkout set src/regexp
git -C /tmp/golang-go fetch --depth 1 origin "$PIN"
git -C /tmp/golang-go checkout "$PIN"
ln -sfn /tmp/golang-go/src/regexp batch/corpora/go_regexp_tests/rules
test "$(git -C /tmp/golang-go rev-parse HEAD)" = "$PIN"
test "$(find batch/corpora/go_regexp_tests/rules -name '*_test.go' | wc -l)" = "9"
```

Manifest pin: `e5ec1263ca5e1428d233206b99dc21c38ea2a124`.
Expected files: **9** `*_test.go`.

## Sample vs full

Wave testdata corpus (full pin required). `sample/` has a minimal `_test.go`
with `MustCompile` + a FindTest-style row. Missing `rules/` → hard-error.

## Extractor + dialect

- Extractor: `go_regexp_tests` (`regexproof/extractors/go_regexp_tests.py`)
- Dialect: `re2` (go-re2 helper ground truth)
- `corpus_type: testdata` — admission gate_decision **not** required

## Measure

```bash
.venv/bin/python scripts/measure-corpus-fraction.py --corpus go_regexp_tests --assert-determinism
```
