# stateset-icommerce corpus

Pinned stateset/stateset-icommerce ecma allowlist for Smith GO admit
[#293](https://github.com/lucas-albers-lz4/regexproof/issues/293)
under umbrella [#291](https://github.com/lucas-albers-lz4/regexproof/issues/291).

Commerce platform. Top-60 first-party ecma files measured **288/409 =
0.7042 encodable** (complete, deterministic) with 104 findings.

## Materialize

```bash
PIN=06a61c4fa83b902f9f436daa29289323011d99cd
git clone --filter=blob:none https://github.com/stateset/stateset-icommerce.git /tmp/stateset-icommerce
git -C /tmp/stateset-icommerce fetch --depth 1 origin "$PIN"
git -C /tmp/stateset-icommerce checkout "$PIN"
ln -sfn /tmp/stateset-icommerce batch/corpora/stateset-icommerce/rules
test "$(git -C /tmp/stateset-icommerce rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/stateset-icommerce_gate_decision.json` (`go`).
Smith: `properties/generated/stateset-icommerce_smith_decision.json` (`go`).
Non-security → public-first.
