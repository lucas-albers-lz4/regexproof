# coreruleset corpus

Pinned OWASP CRS corpus for the dogfooding wave (issue #35 / #37).

## Materialize the corpus

The full CRS rules are not committed here (third-party, ~7.6 MB). Point this
directory at a pinned clone before running the scanner:

```bash
# either clone the pinned release into the repo tree:
git clone --depth 1 --branch v4.28.0 https://github.com/coreruleset/coreruleset.git rules
# or symlink an existing pinned clone:
ln -s /path/to/coreruleset/rules rules
```

The manifest entry (`regexproof/batch/runner.py`, corpus `coreruleset`) reads
`rules/*.conf`. Provenance: coreruleset v4.28.0 (commit `55b09f5`),
2026-08-08. The `sample.rules` file in this directory is the 13-line
encodable-fraction go/no-go gate from Phase 2 — it is not the corpus.

## Expected surface (measured 2026-08-08)

- 750 `SecRule` directives; 310 `@rx` sites (21 negated); 28 variable-selector regexes
- 119/310 = 38.4% encodable via the PCRE compiler (gate ≥30% → GO)
- See issue #37 comment (2026-08-08) for the full inventory + reject breakdown
