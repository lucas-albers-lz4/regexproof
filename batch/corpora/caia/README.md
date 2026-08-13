# caia corpus

Pinned prakashgbid/caia ecma allowlist for Smith GO admit
[#307](https://github.com/lucas-albers-lz4/regexproof/issues/307)
under umbrella [#305](https://github.com/lucas-albers-lz4/regexproof/issues/305).

AI-agent monorepo. Top-60 first-party ecma files measured **439/702 =
0.6254 encodable** (complete, deterministic).

## Materialize

```bash
PIN=95e3ba012416cfd7c92c6689ba9fc399e06cbc20
git clone --filter=blob:none https://github.com/prakashgbid/caia.git /tmp/caia
git -C /tmp/caia fetch --depth 1 origin "$PIN"
git -C /tmp/caia checkout "$PIN"
ln -sfn /tmp/caia batch/corpora/caia/rules
test "$(git -C /tmp/caia rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/caia_gate_decision.json` (`go`).
Smith: `properties/generated/caia_smith_decision.json` (`go`).
Boundary label was a classifier false positive (AI app) → public-first.
