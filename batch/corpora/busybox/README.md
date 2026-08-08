# busybox corpus (Phase 1b)

Pinned: **busybox** `1_36_1` testsuite.

Manifest defaults to `sample/*.tests`. Materialize the full testsuite for
larger measurements.

## Materialize (optional full)

```bash
git clone --depth 1 --branch 1_36_1 \
  https://github.com/mirror/busybox.git /tmp/corpus-wave/busybox
ln -sfn /tmp/corpus-wave/busybox/testsuite batch/corpora/busybox/testsuite
# Override path to testsuite when measuring the full tree.
```

Extractor: `busybox_tests` (`grep -E` / `sed -e` quoted patterns). Dialect: `pcre`.

```bash
python scripts/measure-corpus-fraction.py --corpus busybox --assert-determinism
```
