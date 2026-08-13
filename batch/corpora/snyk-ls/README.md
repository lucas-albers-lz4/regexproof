# snyk-ls corpus

Pinned snyk/snyk-ls go re2 allowlist for Smith GO admit
[#281](https://github.com/lucas-albers-lz4/regexproof/issues/281)
under umbrella [#277](https://github.com/lucas-albers-lz4/regexproof/issues/277).

Snyk SAST language server. Go re2 surface (13 files) measured **21/35 =
0.6000 encodable** (complete, deterministic).

## Materialize

```bash
PIN=68dc3ee1a1d3cc31820daa762475292675464799
git clone --filter=blob:none https://github.com/snyk/snyk-ls.git /tmp/snyk-ls
git -C /tmp/snyk-ls fetch --depth 1 origin "$PIN"
git -C /tmp/snyk-ls checkout "$PIN"
ln -sfn /tmp/snyk-ls batch/corpora/snyk-ls/rules
test "$(git -C /tmp/snyk-ls rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/snyk-ls_gate_decision.json` (triage-trial).
Smith: `properties/generated/snyk-ls_smith_decision.json` (go).
SAST security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
