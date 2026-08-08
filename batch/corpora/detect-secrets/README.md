# detect-secrets corpus (P4 / #84)

Pinned: **Yelp/detect-secrets** `v1.5.0`
(`01886c8a910c64595c47f186ca1ffc0b77fa5458`).

## Materialize

```bash
git clone --depth 1 --branch v1.5.0 \
  https://github.com/Yelp/detect-secrets.git /tmp/detect-secrets
ln -sfn /tmp/detect-secrets/detect_secrets/plugins \
  batch/corpora/detect-secrets/plugins
```

Extractor: `python_dir` over `**/*.py` (`re.compile` / `search` / …).
Dialect: `py_re`. When `plugins/` is missing, `measure-corpus-fraction.py`
falls back to `sample/` (the Phase-5 mini pilot).

```bash
python scripts/measure-corpus-fraction.py --corpus detect-secrets --assert-determinism
```
