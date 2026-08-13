# XPR-dump corpus

Pinned ald3ns/XPR-dump yara pack for Smith GO admit
[#339](https://github.com/lucas-albers-lz4/regexproof/issues/339)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Apple XProtect yara extraction tool (16 files). Measured **394/402 =
0.9801 encodable** (complete, deterministic) — XProtect-derived families
are novel vs the admitted yara packs.

## Materialize

```bash
PIN=510bf67808d018cbbaa51b7e66282da965917c95
git clone --filter=blob:none https://github.com/ald3ns/XPR-dump.git /tmp/XPR-dump
git -C /tmp/XPR-dump fetch --depth 1 origin "$PIN"
git -C /tmp/XPR-dump checkout "$PIN"
ln -sfn /tmp/XPR-dump batch/corpora/XPR-dump/rules
test "$(git -C /tmp/XPR-dump rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/XPR-dump_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/XPR-dump_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
