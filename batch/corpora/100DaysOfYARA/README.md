# 100DaysOfYARA corpus

Pinned 3vangel1st/100DaysOfYARA yara pack for Smith GO admit
[#342](https://github.com/lucas-albers-lz4/regexproof/issues/342)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Yara learning pack (19 files, day-by-day teaching rules). Measured
**98/100 = 0.9800 encodable** (complete, deterministic).

## Materialize

```bash
PIN=50c8516ecb73db2a7b44e0bf42a99b0eaf94155d
git clone --filter=blob:none https://github.com/3vangel1st/100DaysOfYARA.git /tmp/100DaysOfYARA
git -C /tmp/100DaysOfYARA fetch --depth 1 origin "$PIN"
git -C /tmp/100DaysOfYARA checkout "$PIN"
ln -sfn /tmp/100DaysOfYARA batch/corpora/100DaysOfYARA/rules
test "$(git -C /tmp/100DaysOfYARA rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/100DaysOfYARA_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/100DaysOfYARA_smith_decision.json` (`go`).
Security-adjacent → `private_first` via `SECURITY_TOOL_CORPORA`.
