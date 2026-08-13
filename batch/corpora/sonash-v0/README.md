# sonash-v0 corpus

Pinned jasonmichaelbell78-creator/sonash-v0 ecma allowlist for Smith GO
admit [#321](https://github.com/lucas-albers-lz4/regexproof/issues/321)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

Sobriety journal app monorepo. Top-60 first-party ecma files measured
**1,344/1,990 = 0.6754 encodable** (complete, deterministic) with **481
findings — highest yield in the matrix**.

## Materialize

```bash
PIN=3eda2a06b917e0ed9bbf83658e68643e249c646e
git clone --filter=blob:none https://github.com/jasonmichaelbell78-creator/sonash-v0.git /tmp/sonash-v0
git -C /tmp/sonash-v0 fetch --depth 1 origin "$PIN"
git -C /tmp/sonash-v0 checkout "$PIN"
ln -sfn /tmp/sonash-v0 batch/corpora/sonash-v0/rules
test "$(git -C /tmp/sonash-v0 rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/sonash-v0_gate_decision.json` (`go`).
Smith: `properties/generated/sonash-v0_smith_decision.json` (`go`).
Non-security app → public-first.
