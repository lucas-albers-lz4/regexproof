# test262 corpus (RegExp built-ins)

Corpus Wave 2 Phase 5 (issue #100): tc39/test262 `test/built-ins/RegExp`.

## Materialize

```bash
PIN=be13516fb6441b950ba8a3df97eb34062c186972   # update if re-pinned
git clone --depth 1 --filter=blob:none --sparse https://github.com/tc39/test262.git /tmp/test262
git -C /tmp/test262 sparse-checkout set test/built-ins/RegExp
# optional: checkout exact PIN
ln -sfn /tmp/test262/test/built-ins/RegExp batch/corpora/test262/RegExp
test "$(find -L batch/corpora/test262/RegExp -name '*.js' | wc -l)" = "1879"
```

Manifest pin: see `corpus_pin` on `test262` in `regexproof/batch/runner.py`.
Expected file count: **1879** (`EXPECTED_REGEXP_FILES`).

## Sample vs full

Default `measure_scope: sample` uses `batch/corpora/test262/sample/` for CI.
Full-tree measure requires the `RegExp/` symlink above; missing full root with
non-sample scope hard-errors (wave corpus).

## Measure

```bash
python scripts/measure-corpus-fraction.py --corpus test262 --assert-determinism
```
