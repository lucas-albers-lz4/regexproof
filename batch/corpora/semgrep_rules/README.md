# semgrep_rules corpus (Phase 1a)

Pinned: **semgrep/semgrep-rules** commit
`40b8c63f75dc7c22c8a77482d73bfb864b146f7e`.

## Materialize

Fetch the **pinned commit** (required — do not use tip-of-default):

```bash
git clone https://github.com/semgrep/semgrep-rules.git /tmp/semgrep-rules
git -C /tmp/semgrep-rules fetch --depth 1 origin 40b8c63f75dc7c22c8a77482d73bfb864b146f7e
git -C /tmp/semgrep-rules checkout 40b8c63f75dc7c22c8a77482d73bfb864b146f7e
ln -sfn /tmp/semgrep-rules batch/corpora/semgrep_rules/rules
```

Extractor: dedicated `extract_semgrep_yaml` (only `pattern-regex:` + `metavariable-regex:`, incl. block scalars).
Dialect: `py_re` with `declared_semantics=ascii_approx_rust_regex`.
Code-pattern `pattern:` sites are excluded from the denominator.

```bash
python scripts/measure-corpus-fraction.py --corpus semgrep_rules --assert-determinism
```
