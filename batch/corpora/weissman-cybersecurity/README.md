# weissman-cybersecurity corpus

Pinned israel12132/weissman-cybersecurity ecma allowlist for Smith GO admit
[#310](https://github.com/lucas-albers-lz4/regexproof/issues/310)
under umbrella [#305](https://github.com/lucas-albers-lz4/regexproof/issues/305).

Security dashboard frontend. Top-60 ecma files measured **298/388 =
0.7680 encodable** (complete, deterministic).

## Materialize

```bash
PIN=74de1d9d45b17c602040cbde82e2d7623a2d379d
git clone --filter=blob:none https://github.com/israel12132/weissman-cybersecurity.git /tmp/weissman
git -C /tmp/weissman fetch --depth 1 origin "$PIN"
git -C /tmp/weissman checkout "$PIN"
ln -sfn /tmp/weissman batch/corpora/weissman-cybersecurity/rules
test "$(git -C /tmp/weissman rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/weissman-cybersecurity_gate_decision.json` (triage-trial).
Smith: `properties/generated/weissman-cybersecurity_smith_decision.json` (go).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
