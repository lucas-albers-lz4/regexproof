# semgrep-semgrep corpus

Pinned `semgrep/semgrep` at `cc97b5c47dacabe76be343ef981204b8c1f60e07`
for Smith after admission `semgrep-semgrep_gate_decision.json`
(triage-trial via escape hatch — SAST engine below the 1000-site scale
bar, distinct from the admitted `semgrep_rules` repo). Issue
[#386](https://github.com/lucas-albers-lz4/regexproof/issues/386).

## Decision: go (triage-trial superseded)

Measured **5/12 = 0.4167** encodable on a first-party ecma allowlist
(`complete_run`, deterministic). Probe had 597 sites (ecma 493 + shell
11 + py_re 93); the ecma count was tests/perf + vendored-bundle
inflation (`swagger-ui-bundle.js` alone contributed 399) — Smith
measures 10 first-party files under `tests/rules/` +
`tests/patterns/js|ts/` (12 sites).

4 scanner rows (planned inventory questions rc-shape1-4), all
`private_first`. Dry-run will not open public upstream issues.

Security tool → `SECURITY_TOOL_CORPORA` → `private_first`. Not in
`WAVE_CORPORA`.

## Triage buckets

Per-`unencodable_reason` from
`properties/triage/semgrep-semgrep.ndjson` (7 records; 5 encodable + 7
unencodable = 12):

| Bucket | Count |
|---|---|
| `stateful` | 6 |
| `composite-pattern` | 1 |
| **Total unencodable** | **7** |

| Artifact | Path |
|---|---|
| Gate | `properties/generated/semgrep-semgrep_gate_decision.json` |
| Smith | `properties/generated/semgrep-semgrep_smith_decision.json` |
| Fraction | `properties/generated/semgrep-semgrep_encodable_fraction.json` |

## Materialize

```bash
# first-party ecma only (tests/perf + vendored bundles excluded)
python scripts/materialize-corpus.py --gate \
  properties/generated/semgrep-semgrep_gate_decision.json \
  --allowlist-file /tmp/semgrep-allowlist.txt --link-name rules
# then: mv batch/corpora/semgrep/rules batch/corpora/semgrep-semgrep/rules
```

Manifest `files=` is the committed allowlist (10 paths).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus semgrep-semgrep \
  --assert-determinism
python -m regexproof.batch --corpus semgrep-semgrep
```

## Notes

- Shell (11) and py_re (93) remain `additional_surface_outside_probe_scope`
  relative to this ecma Smith slice.
- No conversion contracts in this PR — Smith measure only (triage-trial;
  findings decide next steps per #386).
