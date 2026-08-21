# ajohnsonnow-vet-rate-org corpus

Pinned `ajohnsonnow/vet-rate-org` at
`1e9b252ca541f7a6b7f9eff7f82a99a4a055b8a7` for Smith after admission
`ajohnsonnow-vet-rate-org_gate_decision.json` (GO admit — veterans benefits
site, primarily ECMA). Issue
[#408](https://github.com/lucas-albers-lz4/regexproof/issues/408).

## Decision: go

Measured **1408/2342 = 0.6012** encodable on a first-party
`**/*.{js,mjs,cjs,ts,tsx}` allowlist (`complete_run`, deterministic). Probe
had 2800 sites (ecma 2659 + py_re 126 + shell 15); Smith measures ECMA after
dropping tests/fixtures/i18n/e2e inflation (2342 sites / 214 files).

246 scanner rows. Not a security tool → default disclosure (not
`private_first`). Dry-run will not open public upstream issues.

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/ajohnsonnow-vet-rate-org.ndjson` (934 records; 1408
encodable + 934 unencodable = 2342):

| Bucket | Count |
|---|---|
| `stateful` | 830 |
| `lookaround` | 31 |
| `m-flag` | 29 |
| `composite-pattern` | 17 |
| `negated-shorthand` | 12 |
| `backref` | 4 |
| `per-alternative-anchor` | 4 |
| `word-boundary` | 3 |
| `u-flag` | 2 |
| `unclosed-group` | 1 |
| `empty-class` | 1 |
| **Total unencodable** | **934** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/ajohnsonnow-vet-rate-org_gate_decision.json` |
| Smith | `properties/generated/ajohnsonnow-vet-rate-org_smith_decision.json` |
| Fraction | `properties/generated/ajohnsonnow-vet-rate-org_encodable_fraction.json` |

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/ajohnsonnow-vet-rate-org_gate_decision.json \
  --allowlist-file /tmp/vet-rate-allowlist.txt
```

Manifest `files=` is the committed allowlist (214 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus ajohnsonnow-vet-rate-org \
  --assert-determinism
python -m regexproof.batch --corpus ajohnsonnow-vet-rate-org
```

## Notes

- Shell (15) and py_re (126) remain `additional_surface_outside_probe_scope`
  relative to this ECMA Smith slice.
- No conversion contracts in this PR — Smith measure only (mid-tier ECMA after
  [#398](https://github.com/lucas-albers-lz4/regexproof/issues/398)).
