# semgrep_rules corpus (Phase 1a)

Pinned: **semgrep/semgrep-rules** commit
`40b8c63f75dc7c22c8a77482d73bfb864b146f7e`.

## Materialize

```bash
git clone --depth 1 https://github.com/semgrep/semgrep-rules.git /tmp/semgrep-rules
# optionally: git -C /tmp/semgrep-rules checkout 40b8c63f75dc7c22c8a77482d73bfb864b146f7e
ln -sfn /tmp/semgrep-rules batch/corpora/semgrep_rules/rules
```

Extractor: `semgrep_yaml` via `extract_rule_file` (includes `pattern-regex:`).
Dialect: `py_re` (stock Python `re` mirror). Accepted: `**/*.{yml,yaml}`.
Block-scalar `pattern-regex: |` rows are `composite-pattern` (not truncated).

```bash
python scripts/measure-corpus-fraction.py --corpus semgrep_rules --assert-determinism
```
