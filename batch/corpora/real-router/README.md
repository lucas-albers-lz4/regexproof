# real-router corpus

Pinned greydragon888/real-router ecma allowlist for Smith GO admit
[#295](https://github.com/lucas-albers-lz4/regexproof/issues/295)
under umbrella [#294](https://github.com/lucas-albers-lz4/regexproof/issues/294).

Router framework monorepo. Top-60 first-party ecma files measured
**1,225/1,249 = 0.9808 encodable** (complete, deterministic).

## Materialize

```bash
PIN=55aa7ef43a9c129beba90823cd8a4db10bb01211
git clone --filter=blob:none https://github.com/greydragon888/real-router.git /tmp/real-router
git -C /tmp/real-router fetch --depth 1 origin "$PIN"
git -C /tmp/real-router checkout "$PIN"
ln -sfn /tmp/real-router batch/corpora/real-router/rules
test "$(git -C /tmp/real-router rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/real-router_gate_decision.json` (`go`).
Smith: `properties/generated/real-router_smith_decision.json` (`go`).
Non-security framework → public-first.
