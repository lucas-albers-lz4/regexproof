# SveltyCMS-SveltyCMS corpus

Pinned `SveltyCMS/SveltyCMS` at `c48326afe2a9d429f105af9aa786738d970af848`
for Smith after admission `SveltyCMS-SveltyCMS_gate_decision.json` (GO admit —
headless CMS, primarily ECMA). Issue
[#396](https://github.com/lucas-albers-lz4/regexproof/issues/396).

## Decision: go

Measured **701/1275 = 0.5498** encodable on a first-party
`**/*.{js,mjs,cjs,ts,tsx}` allowlist (`complete_run`, deterministic). Probe
had 2238 sites (ecma 2226 + shell 12); Smith measures ECMA after dropping
tests/benchmarks/e2e inflation (1275 sites / 231 files).

242 scanner rows. Not a security tool → default disclosure. Dry-run will not
open public upstream issues.

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/SveltyCMS-SveltyCMS.ndjson` (574 records; 701 encodable +
574 unencodable = 1275):

| Bucket | Count |
|---|---|
| `stateful` | 500 |
| `composite-pattern` | 31 |
| `per-alternative-anchor` | 14 |
| `word-boundary` | 11 |
| `negated-shorthand` | 7 |
| `lookaround` | 7 |
| `u-flag` | 2 |
| `m-flag` | 1 |
| `pattern-too-long` | 1 |
| **Total unencodable** | **574** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/SveltyCMS-SveltyCMS_gate_decision.json` |
| Smith | `properties/generated/SveltyCMS-SveltyCMS_smith_decision.json` |
| Fraction | `properties/generated/SveltyCMS-SveltyCMS_encodable_fraction.json` |

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/SveltyCMS-SveltyCMS_gate_decision.json \
  --allowlist-file /tmp/svelty-allowlist.txt
```

Manifest `files=` is the committed allowlist (231 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus SveltyCMS-SveltyCMS \
  --assert-determinism
python -m regexproof.batch --corpus SveltyCMS-SveltyCMS
```

## Notes

- Shell (12) remains `additional_surface_outside_probe_scope` relative to this
  ECMA Smith slice.
- No conversion contracts — Smith measure only (mid-tier ECMA after
  [#390](https://github.com/lucas-albers-lz4/regexproof/issues/390)).
