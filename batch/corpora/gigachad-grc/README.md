# gigachad-grc corpus

Pinned grcengineering/gigachad-grc first-party services/mcp-servers ecma
surface for Smith triage-trial [#243](https://github.com/lucas-albers-lz4/regexproof/issues/243)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Allowlist focuses on sanitizers, validators, security-scanner, phishing/SCIM,
policy-validator, and evidence collectors — excludes tests, frontend UI pages,
and vendor trees.

## Materialize

```bash
PIN=d4a39726cad8d8e27e4c0502d1843c3b4180ffbc
git clone --filter=blob:none https://github.com/grcengineering/gigachad-grc.git /tmp/gigachad-grc
git -C /tmp/gigachad-grc fetch --depth 1 origin "$PIN"
git -C /tmp/gigachad-grc checkout "$PIN"
ln -sfn /tmp/gigachad-grc batch/corpora/gigachad-grc/rules
test "$(git -C /tmp/gigachad-grc rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/gigachad-grc_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus gigachad-grc --assert-determinism
python -m regexproof.batch --corpus gigachad-grc
```
