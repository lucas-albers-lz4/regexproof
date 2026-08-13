# mcp-for-splunk corpus

Pinned deslicer/mcp-for-splunk posix-shell allowlist for Smith GO admit
[#298](https://github.com/lucas-albers-lz4/regexproof/issues/298)
under umbrella [#294](https://github.com/lucas-albers-lz4/regexproof/issues/294).

Splunk MCP server. posix-shell surface measured **42/44 = 0.9545
encodable** (complete, deterministic) — consistent with the shell
family's high encodability.

## Materialize

```bash
PIN=697f92649f5f1c9f77958d874e5ce2de1b43bd90
git clone --filter=blob:none https://github.com/deslicer/mcp-for-splunk.git /tmp/mcp-for-splunk
git -C /tmp/mcp-for-splunk fetch --depth 1 origin "$PIN"
git -C /tmp/mcp-for-splunk checkout "$PIN"
ln -sfn /tmp/mcp-for-splunk batch/corpora/mcp-for-splunk/rules
test "$(git -C /tmp/mcp-for-splunk rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/mcp-for-splunk_gate_decision.json` (triage-trial).
Smith: `properties/generated/mcp-for-splunk_smith_decision.json` (go).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
