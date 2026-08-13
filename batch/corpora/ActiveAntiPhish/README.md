# ActiveAntiPhish corpus

Pinned mrcbax/ActiveAntiPhish yara pack for Smith GO admit
[#341](https://github.com/lucas-albers-lz4/regexproof/issues/341)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Anti-phishing yara pack (single phishkit.yar). Measured **207/207 =
1.0000 encodable** (complete, deterministic) — perfect.

## Materialize

```bash
PIN=6148bb167ebe641901fc468157b640a03ee4e388
git clone --filter=blob:none https://github.com/mrcbax/ActiveAntiPhish.git /tmp/ActiveAntiPhish
git -C /tmp/ActiveAntiPhish fetch --depth 1 origin "$PIN"
git -C /tmp/ActiveAntiPhish checkout "$PIN"
ln -sfn /tmp/ActiveAntiPhish batch/corpora/ActiveAntiPhish/rules
test "$(git -C /tmp/ActiveAntiPhish rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/ActiveAntiPhish_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/ActiveAntiPhish_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.
