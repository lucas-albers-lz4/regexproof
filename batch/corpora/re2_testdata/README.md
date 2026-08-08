# re2_testdata corpus (Phase 1b)

Pinned reference: **google/re2** (date pin `2024-07-02`).

Default path is the committed TOML sample (`sample/patterns.toml`) so CI
does not need a full RE2 checkout. Patterns use the gitleaks-style
`[[rules]]` / `regex =` shape via `extract_rule_file`.

## Materialize (optional)

```bash
git clone --depth 1 https://github.com/google/re2.git /tmp/corpus-wave/re2
# Copy or adapt interesting `re2/testdata` rows into sample/patterns.toml
```

```bash
python scripts/measure-corpus-fraction.py --corpus re2_testdata --assert-determinism
```
