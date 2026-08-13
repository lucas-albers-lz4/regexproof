# remotepower corpus

Pinned tyxak/remotepower py_re allowlist for Smith GO admit
[#279](https://github.com/lucas-albers-lz4/regexproof/issues/279)
under umbrella [#277](https://github.com/lucas-albers-lz4/regexproof/issues/277).

Remote power-management app. Top-60 .py files (34 present) measured
**156/282 = 0.5532 encodable** (complete, deterministic) with 56 findings.

## Materialize

```bash
PIN=4bbe6925652c03b02329c5fb15d34df96faf994c
git clone --filter=blob:none https://github.com/tyxak/remotepower.git /tmp/remotepower
git -C /tmp/remotepower fetch --depth 1 origin "$PIN"
git -C /tmp/remotepower checkout "$PIN"
ln -sfn /tmp/remotepower batch/corpora/remotepower/rules
test "$(git -C /tmp/remotepower rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/remotepower_gate_decision.json` (triage-trial).
Smith: `properties/generated/remotepower_smith_decision.json` (go).
Non-security → public-first.
