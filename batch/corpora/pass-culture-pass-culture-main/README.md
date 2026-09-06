# pass-culture-pass-culture-main corpus

Pinned `pass-culture/pass-culture-main` at
`14917fd0f8753933083fd379a7f9a0cc90bcc473` for Smith after admission
`pass-culture-pass-culture-main_gate_decision.json` (GO admit —
cultural-pass app suite, NOT security → public-first capable). Issue
[#391](https://github.com/lucas-albers-lz4/regexproof/issues/391).

## Decision: go

Measured **1526/1589 = 0.9604** encodable on a first-party
`**/*.{js,ts,tsx}` allowlist (`complete_run`, deterministic). Probe had
2056 sites (ecma 1914 + shell 35 + py_re 107); Smith measures ECMA
after dropping tests / e2e / fixtures / storybook / i18n inflation
(1589 sites / 361 files).

75 scanner rows (28 usage_mismatch + 43 intent_mismatch + 4 planned
inventory), none private (not a security tool). Dry-run opens no public
upstream issue (`publish` false until an explicit disclosure gate).

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/pass-culture-pass-culture-main.ndjson` (63 records;
1526 encodable + 63 unencodable = 1589):

| Bucket | Count |
|---|---|
| `stateful` | 39 |
| `composite-pattern` | 21 |
| `lookaround` | 1 |
| `pattern-too-long` | 1 |
| `per-alternative-anchor` | 1 |
| **Total unencodable** | **63** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/pass-culture-pass-culture-main_gate_decision.json` |
| Smith | `properties/generated/pass-culture-pass-culture-main_smith_decision.json` |
| Fraction | `properties/generated/pass-culture-pass-culture-main_encodable_fraction.json` |

## Materialize

```bash
# first-party ecma only (tests/e2e/fixtures/storybook/i18n excluded)
python scripts/materialize-corpus.py --gate \
  properties/generated/pass-culture-pass-culture-main_gate_decision.json \
  --allowlist-file /tmp/passculture-allowlist.txt --link-name rules
# then: mv batch/corpora/pass-culture-main/rules \
#   batch/corpora/pass-culture-pass-culture-main/rules
```

Manifest `files=` is the committed allowlist (361 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus pass-culture-pass-culture-main \
  --assert-determinism
python -m regexproof.batch --corpus pass-culture-pass-culture-main
```

## Notes

- Shell (35) and py_re (107) remain `additional_surface_outside_probe_scope`
  relative to this ecma Smith slice.
- Highest ecma fraction measured to date (0.9604) — prime conversion-slice
  candidate per the #619 ROI plan (Phase 2).
- No conversion contracts in this PR — Smith measure only.
