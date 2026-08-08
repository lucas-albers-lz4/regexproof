# cpython_re corpus (Phase 1b)

Pinned: **python/cpython** tag `v3.12.8` (`Lib/test/re_tests.py`).

Committed `re_tests.py` is a truncated head suitable for CI. Replace with
the full upstream file after materializing for a full-corpus measure.

## Materialize (optional full)

```bash
git clone --depth 1 --branch v3.12.8 \
  https://github.com/python/cpython.git /tmp/corpus-wave/cpython
cp /tmp/corpus-wave/cpython/Lib/test/re_tests.py \
  batch/corpora/cpython_re/re_tests.py
```

Extractor: `cpython_re_tests`. Dialect: `py_re`.

```bash
python scripts/measure-corpus-fraction.py --corpus cpython_re --assert-determinism
```
