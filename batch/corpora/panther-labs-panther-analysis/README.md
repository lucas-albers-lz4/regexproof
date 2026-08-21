# panther-labs-panther-analysis corpus

Pinned `panther-labs/panther-analysis` at
`0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a` for Smith after admission
`panther-labs-panther-analysis_gate_decision.json` (triage-trial, escape
hatch — SIEM detection-as-code, 57 py_re). Issue
[#387](https://github.com/lucas-albers-lz4/regexproof/issues/387).

## Decision: go

Measured **37/57 = 0.6491** encodable (`complete_run`, deterministic).
22 scanner findings, all `private_first` (security tool). Dry-run will not
open public upstream issues.

Security tool → `SECURITY_TOOL_CORPORA` → `private_first`. Not in
`WAVE_CORPORA`.

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
