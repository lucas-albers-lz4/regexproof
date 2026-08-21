# visulima-visulima corpus

Pinned `visulima/visulima` at `50ce4889c75d82b4d7ad5f54a0fdf5142b06c710`
for Smith after admission `visulima-visulima_gate_decision.json` (GO admit —
dev-tools/libraries monorepo, primarily ECMA). Issue
[#398](https://github.com/lucas-albers-lz4/regexproof/issues/398).

## Decision: go

Measured **950/1617 = 0.5875** encodable on a first-party
`**/*.{js,mjs,cjs,ts,tsx}` allowlist (`complete_run`, deterministic). Probe
had 2668 sites (ecma 2662 + shell 6); Smith measures ECMA after dropping
tests / `__tests__` / fixtures / `__fixtures__` / `__bench__` / examples /
i18n / storybook inflation (1617 sites / 506 files).

576 scanner rows. Not a security tool → default disclosure (not
`private_first`). Dry-run will not open public upstream issues (`publish`
false until an explicit disclosure gate).

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/visulima-visulima.ndjson` (667 records; 950 encodable +
667 unencodable = 1617):

| Bucket | Count |
|---|---|
| `stateful` | 356 |
| `u-flag` | 133 |
| `composite-pattern` | 59 |
| `m-flag` | 45 |
| `per-alternative-anchor` | 33 |
| `lookaround` | 15 |
| `backref` | 12 |
| `negated-shorthand` | 7 |
| `word-boundary` | 4 |
| `unclosed-group` | 1 |
| `internal-anchor` | 1 |
| `pattern-too-long` | 1 |
| **Total unencodable** | **667** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/visulima-visulima_gate_decision.json` |
| Smith | `properties/generated/visulima-visulima_smith_decision.json` |
| Fraction | `properties/generated/visulima-visulima_encodable_fraction.json` |

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/visulima-visulima_gate_decision.json \
  --allowlist-file /tmp/visulima-allowlist.txt
```

Manifest `files=` is the committed allowlist (506 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus visulima-visulima \
  --assert-determinism
python -m regexproof.batch --corpus visulima-visulima
```

## Notes

- Shell (6) remains `additional_surface_outside_probe_scope` relative to this
  ECMA Smith slice.
- No conversion contracts in this PR — Smith measure only (mid-tier ECMA after
  [#384](https://github.com/lucas-albers-lz4/regexproof/issues/384)).
