# lintendo-Axhub-Make corpus

Pinned `lintendo/Axhub-Make` at `bc10e311028d5e72752de97187ff690b2095f466`
for Smith after admission `lintendo-Axhub-Make_gate_decision.json` (GO admit —
AI workbench, ECMA-only). Issue
[#390](https://github.com/lucas-albers-lz4/regexproof/issues/390).

## Decision: go

Measured **759/2473 = 0.3069** encodable on a first-party
`**/*.{js,mjs,cjs,ts,tsx}` allowlist (`complete_run`, deterministic). Probe
had 2994 ECMA sites; Smith measures after dropping tests/fixtures/examples
and `*.test.*` / `*.spec.*` files (2473 sites / 302 files). Fraction clears
the informational 0.30 bar; `smith_decision=go` is explicit (not inferred).

557 scanner rows. Not a security tool → default disclosure. Dry-run will not
open public upstream issues.

Not in `SECURITY_TOOL_CORPORA`. Not in `WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/lintendo-Axhub-Make.ndjson` (1714 records; 759 encodable +
1714 unencodable = 2473):

| Bucket | Count |
|---|---|
| `stateful` | 870 |
| `u-flag` | 745 |
| `composite-pattern` | 35 |
| `per-alternative-anchor` | 21 |
| `word-boundary` | 14 |
| `lookaround` | 11 |
| `m-flag` | 8 |
| `negated-shorthand` | 8 |
| `backref` | 2 |
| **Total unencodable** | **1714** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/lintendo-Axhub-Make_gate_decision.json` |
| Smith | `properties/generated/lintendo-Axhub-Make_smith_decision.json` |
| Fraction | `properties/generated/lintendo-Axhub-Make_encodable_fraction.json` |

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/lintendo-Axhub-Make_gate_decision.json \
  --allowlist-file /tmp/axhub-allowlist.txt
```

Manifest `files=` is the committed allowlist (302 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus lintendo-Axhub-Make \
  --assert-determinism
python -m regexproof.batch --corpus lintendo-Axhub-Make
```

## Notes

- Probe dialect is ECMA-only (2994); no additional shell/py_re surface.
- Heavy `u-flag` / `stateful` rejects dominate unencodable (not inflation).
- No conversion contracts — Smith measure only (mid-tier ECMA after
  [#408](https://github.com/lucas-albers-lz4/regexproof/issues/408)).
