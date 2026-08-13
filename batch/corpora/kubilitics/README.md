# kubilitics corpus

Pinned kubilitics/kubilitics ecma allowlist for Smith GO admit
[#309](https://github.com/lucas-albers-lz4/regexproof/issues/309)
under umbrella [#305](https://github.com/lucas-albers-lz4/regexproof/issues/305).

K8s observability suite. Top-60 first-party ecma files measured **505/567
= 0.8907 encodable** (complete, deterministic).

## Materialize

```bash
PIN=788d4d0760dfaec214bd1fd4b363391ac6c5a7a7
git clone --filter=blob:none https://github.com/kubilitics/kubilitics.git /tmp/kubilitics
git -C /tmp/kubilitics fetch --depth 1 origin "$PIN"
git -C /tmp/kubilitics checkout "$PIN"
ln -sfn /tmp/kubilitics batch/corpora/kubilitics/rules
test "$(git -C /tmp/kubilitics rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/kubilitics_gate_decision.json` (`go`).
Smith: `properties/generated/kubilitics_smith_decision.json` (`go`).
Non-security → public-first.
