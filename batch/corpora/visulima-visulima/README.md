# visulima-visulima corpus

Pinned `visulima/visulima` at `50ce4889c75d82b4d7ad5f54a0fdf5142b06c710`
for Smith after admission `visulima-visulima_gate_decision.json` (GO admit —
dev-tools/libraries monorepo, primarily ECMA). Issue
[#398](https://github.com/lucas-albers-lz4/regexproof/issues/398).

## Decision: go

Measured **1006/1704 = 0.5904** encodable on a first-party
`**/*.{js,mjs,cjs,ts,tsx}` allowlist (`complete_run`, deterministic). Probe
had 2668 sites (ecma 2662 + shell 6); Smith measures ECMA after dropping
tests/fixtures/i18n inflation (1704 sites / 548 files).

596 scanner rows. Not a security tool → default disclosure (not
`private_first`). Dry-run will not open public upstream issues (`publish`
false until an explicit disclosure gate).

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/visulima-visulima.ndjson` (698 records; 1006 encodable +
698 unencodable = 1704):

| Bucket | Count |
|---|---|
| `stateful` | 368 |
| `u-flag` | 135 |
| `composite-pattern` | 64 |
| `m-flag` | 45 |
| `per-alternative-anchor` | 34 |
| `lookaround` | 17 |
| `backref` | 12 |
| `negated-shorthand` | 8 |
| `word-boundary` | 4 |
| `unclosed-group` | 3 |
| `internal-anchor` | 3 |
| `v-flag` | 3 |
| `unsupported-syntax` | 1 |
| `pattern-too-long` | 1 |
| **Total unencodable** | **698** |

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

Manifest `files=` is the committed allowlist (548 paths).

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
