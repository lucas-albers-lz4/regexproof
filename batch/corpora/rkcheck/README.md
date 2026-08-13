# rkcheck corpus

Pinned dmknght/rkcheck yara pack for Smith GO admit
[#324](https://github.com/lucas-albers-lz4/regexproof/issues/324)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

Malware scanner yara pack (8 files: botnet/coin_miner/ransomware
families). Measured **186/207 = 0.8986 encodable** (complete,
deterministic).

## Materialize

```bash
PIN=ca4b30b254861b5f76d6cad68c9cc5c9e49a58ac
git clone --filter=blob:none https://github.com/dmknght/rkcheck.git /tmp/rkcheck
git -C /tmp/rkcheck fetch --depth 1 origin "$PIN"
git -C /tmp/rkcheck checkout "$PIN"
ln -sfn /tmp/rkcheck batch/corpora/rkcheck/rules
test "$(git -C /tmp/rkcheck rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/rkcheck_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/rkcheck_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
