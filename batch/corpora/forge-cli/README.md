# forge-cli corpus

Pinned Agenticstiger/forge-cli py_re allowlist for Smith GO admit
[#296](https://github.com/lucas-albers-lz4/regexproof/issues/296)
under umbrella [#294](https://github.com/lucas-albers-lz4/regexproof/issues/294).

CLI tool. Top-60 .py files measured **171/314 = 0.5446 encodable**
(complete, deterministic).

## Materialize

```bash
PIN=efcf8e4c0087def553a737dc1c4eebda5d8a90cd
git clone --filter=blob:none https://github.com/Agenticstiger/forge-cli.git /tmp/forge-cli
git -C /tmp/forge-cli fetch --depth 1 origin "$PIN"
git -C /tmp/forge-cli checkout "$PIN"
ln -sfn /tmp/forge-cli batch/corpora/forge-cli/rules
test "$(git -C /tmp/forge-cli rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/forge-cli_gate_decision.json` (triage-trial).
Smith: `properties/generated/forge-cli_smith_decision.json` (go).
`private_first` via `SECURITY_TOOL_CORPORA`.

## Notes

- The admission-time 42 extractor_errors were outside the top-60 allowlist
  files — the measured surface is clean.
