# pcre2_testdata corpus (Phase 1b)

Pinned: **PCRE2Project/pcre2** tag `pcre2-10.44`.

Full `testdata/` can OOM the process; the manifest defaults to
`batch/corpora/pcre2_testdata/sample/`.

## Materialize (optional full tree)

```bash
git clone --depth 1 --branch pcre2-10.44 \
  https://github.com/PCRE2Project/pcre2.git /tmp/corpus-wave/pcre2
ln -sfn /tmp/corpus-wave/pcre2/testdata batch/corpora/pcre2_testdata/testdata
# Then point CORPUS path / re-run with an override if measuring full tree.
```

Extractor: `pcre2_testdata` (`/pattern/flags` lines). Dialect: `pcre`.

```bash
python scripts/measure-corpus-fraction.py --corpus pcre2_testdata --assert-determinism
```
