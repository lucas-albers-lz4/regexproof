# panther-labs-panther-analysis corpus

Pinned `panther-labs/panther-analysis` at
`0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a` for Smith after admission
`panther-labs-panther-analysis_gate_decision.json` (triage-trial, escape
hatch — SIEM detection-as-code, 57 py_re). Issue
[#387](https://github.com/lucas-albers-lz4/regexproof/issues/387).

## Decision: go

Measured **37/57 = 0.6491** encodable (`complete_run`, deterministic).
22 batch records (18 `usage_mismatch` findings + 4 planned inventory
properties), all `private_first` (security tool). Dry-run will not
open public upstream issues.

Security tool → `SECURITY_TOOL_CORPORA` → `private_first`. Not in
`WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` counts from
`properties/triage/panther-labs-panther-analysis.ndjson` (20 records,
all `reason_kind=unencodable`; 37 encodable + 20 unencodable = 57 sites):

| Bucket | Definition | Count |
|---|---|---|
| `composite-pattern` | `re.compile` argument is an f-string or `+` concatenation (`ast.JoinedStr` / `BinOp`) — dynamic pattern, cannot fold to one literal | 12 |
| `unicode-not-literal` | Complement of a literal over the full Unicode domain (non-ASCII `[^x]`) — over-broad complement rejected unless ASCII-only | 4 |
| `m-flag` | `re.MULTILINE` / inline `(?m)` — per-line `^`/`$` anchors not encodable | 2 |
| `negated-shorthand` | Negated shorthand category (`\D`, `\S`, `\W`) — complement not expressible | 1 |
| `per-alternative-anchor` | `^`/`$` anchors inside alternation branches (branch-local anchors rejected) | 1 |
| **Total unencodable** | | **20** |

The 22 batch rows in `properties/generated/panther-labs-panther-analysis.ndjson`
are a separate view (18 `usage_mismatch` findings + 4 planned inventory
properties); the triage table above is the unencodable view and reconciles the
37/57 ratio (37 encodable + 20 unencodable = 57 sites).

| Artifact | Path |
|---|---|
| Gate | `properties/generated/panther-labs-panther-analysis_gate_decision.json` |
| Smith | `properties/generated/panther-labs-panther-analysis_smith_decision.json` |
| Fraction | `properties/generated/panther-labs-panther-analysis_encodable_fraction.json` |

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/panther-labs-panther-analysis_gate_decision.json
```

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus panther-labs-panther-analysis \
  --assert-determinism
python -m regexproof.batch --corpus panther-labs-panther-analysis
```

## Notes

- Probe listed 32 files with sites; batch `python_dir` `**/*.py` extracted 57
  sites (same probe total).
- Rejects are mostly compiler unencodable (inline-flag / m-flag predicted in
  gate), not inflation.
- No conversion contracts in this PR — Smith measure only (cheap-later after
  [#533](https://github.com/lucas-albers-lz4/regexproof/issues/533)).
