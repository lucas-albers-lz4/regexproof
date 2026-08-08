# trufflehog corpus (Phase 1a)

Pinned: **trufflesecurity/trufflehog** `v3.88.29`
(`90190deac64289cb10bb694894be8db9ead8790b`).

## Materialize

```bash
git clone --depth 1 --branch v3.88.29 \
  https://github.com/trufflesecurity/trufflehog.git /tmp/trufflehog
ln -sfn /tmp/trufflehog/pkg/detectors batch/corpora/trufflehog/detectors
```

Extractor: `go_regexp` over `**/*.go` (`regexp.MustCompile` / `Compile`).
Dialect: `re2`. Accepted: `.go`. Skipped: non-Go sources.

```bash
python scripts/measure-corpus-fraction.py --corpus trufflehog --assert-determinism
```
