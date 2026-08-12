# volatility3-mcp corpus

Pinned Kirandawadi/volatility3-mcp yara pack for Smith GO admit
[#329](https://github.com/lucas-albers-lz4/regexproof/issues/329)
under umbrella [#328](https://github.com/lucas-albers-lz4/regexproof/issues/328).

Volatility3 memory-forensics MCP server. **Largest yara corpus in the matrix**
(29,364 probe sites; 17,574 measured after MAX_FILE_BYTES). Measured
**11,534/17,574 = 0.6563 encodable** (complete, deterministic) with **71
findings** and 6,040 triage.

## Materialize

```bash
PIN=edc50f35005032c940bf6260ca791dab700eaabc
git clone --filter=blob:none https://github.com/Kirandawadi/volatility3-mcp.git /tmp/volatility3-mcp
git -C /tmp/volatility3-mcp fetch --depth 1 origin "$PIN"
git -C /tmp/volatility3-mcp checkout "$PIN"
ln -sfn /tmp/volatility3-mcp/rules batch/corpora/volatility3-mcp/rules
test "$(git -C /tmp/volatility3-mcp rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/volatility3-mcp_gate_decision.json` (`go`).
Smith: `properties/generated/volatility3-mcp_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus volatility3-mcp --assert-determinism
python -m regexproof.batch --corpus volatility3-mcp
```

## Notes

- 566 yara files: webshell / stealer / evilginx / antidebug_antivm /
  capabilities / crypto / packers packs. One file >2MB skipped per
  MAX_FILE_BYTES (policy, not a bug).
- The 0.6563 fraction is the yara-family norm (yara_rules 0.656, malcontent
  0.6993) — fullword-boundary-heavy rules dominate the rejects.
