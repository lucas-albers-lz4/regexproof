# gadievron-raptor corpus

Pinned `gadievron/raptor` at `d81cada060a5e7b61938445da021ed0b33236cbb`
for Smith after admission `gadievron-raptor_gate_decision.json` (GO admit —
Claude Code offensive/defensive security agent, primarily py_re). Issue
[#384](https://github.com/lucas-albers-lz4/regexproof/issues/384).

## Decision: go

Measured **894/1879 = 0.4758** encodable on a first-party `**/*.py`
allowlist (`complete_run`, deterministic). Probe had 1951 sites (py_re
1908 + shell 42 + ecma 1); Smith measures py_re only after dropping
tests/fixtures inflation (1879 sites / 304 files).

428 scanner rows, all `private_first`. Dry-run will not open public
upstream issues.

Security tool → `SECURITY_TOOL_CORPORA` → `private_first`. Not in
`WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/gadievron-raptor.ndjson` (985 records; 894 encodable +
985 unencodable = 1879):

| Bucket | Count |
|---|---|
| `word-boundary` | 477 |
| `composite-pattern` | 235 |
| `unicode-not-literal` | 88 |
| `m-flag` | 80 |
| `per-alternative-anchor` | 28 |
| `pattern-too-long` | 23 |
| `negated-shorthand` | 18 |
| `lookaround` | 16 |
| `multi-match` | 15 |
| `backref` | 5 |
| **Total unencodable** | **985** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/gadievron-raptor_gate_decision.json` |
| Smith | `properties/generated/gadievron-raptor_smith_decision.json` |
| Fraction | `properties/generated/gadievron-raptor_encodable_fraction.json` |

## Materialize

```bash
# first-party .py only (exclude tests/fixtures); regenerate from gate probe if needed
python scripts/materialize-corpus.py --gate \
  properties/generated/gadievron-raptor_gate_decision.json \
  --allowlist-file /tmp/raptor-allowlist.txt
```

Manifest `files=` is the committed allowlist (304 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus gadievron-raptor \
  --assert-determinism
python -m regexproof.batch --corpus gadievron-raptor
```

## Notes

- Shell (42) and ecma (1) remain `additional_surface_outside_probe_scope`
  relative to this py_re Smith slice.
- No conversion contracts in this PR — Smith measure only (cheap-later after
  [#533](https://github.com/lucas-albers-lz4/regexproof/issues/533) /
  [#387](https://github.com/lucas-albers-lz4/regexproof/issues/387)).
