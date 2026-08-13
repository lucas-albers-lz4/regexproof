# OctopusBeak corpus

Pinned WangWilly/OctopusBeak ecma allowlist for Smith GO admit
[#287](https://github.com/lucas-albers-lz4/regexproof/issues/287)
under umbrella [#284](https://github.com/lucas-albers-lz4/regexproof/issues/284).

Banking-data app. Top-60 first-party ecma files measured **847/1,144 =
0.7404 encodable** (complete, deterministic) with 102 findings.

## Materialize

```bash
PIN=fbde2b23cefb5d6a423576c63256e07e18c49218
git clone --filter=blob:none https://github.com/WangWilly/OctopusBeak.git /tmp/OctopusBeak
git -C /tmp/OctopusBeak fetch --depth 1 origin "$PIN"
git -C /tmp/OctopusBeak checkout "$PIN"
ln -sfn /tmp/OctopusBeak batch/corpora/OctopusBeak/rules
test "$(git -C /tmp/OctopusBeak rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/OctopusBeak_gate_decision.json` (`go`).
Smith: `properties/generated/OctopusBeak_smith_decision.json` (`go`).
Banking-data boundary → `private_first` via `SECURITY_TOOL_CORPORA`.
