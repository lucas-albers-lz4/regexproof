# SentryShield corpus

Pinned Rizzy1857/SentryShield yara pack for Smith GO admit
[#325](https://github.com/lucas-albers-lz4/regexproof/issues/325)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

Malware yara pack (single malware.yar). Measured **180/180 = 1.0000
encodable** (complete, deterministic) — perfect.

## Materialize

```bash
PIN=4f43015c80fde0cb1bd3f001a7551c40eed2682c
git clone --filter=blob:none https://github.com/Rizzy1857/SentryShield.git /tmp/SentryShield
git -C /tmp/SentryShield fetch --depth 1 origin "$PIN"
git -C /tmp/SentryShield checkout "$PIN"
ln -sfn /tmp/SentryShield batch/corpora/SentryShield/rules
test "$(git -C /tmp/SentryShield rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/SentryShield_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/SentryShield_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
