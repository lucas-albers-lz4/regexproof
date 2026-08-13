# three-ui corpus

Pinned nirholas/three-ui ecma allowlist for Smith GO admit
[#332](https://github.com/lucas-albers-lz4/regexproof/issues/332)
under umbrella [#328](https://github.com/lucas-albers-lz4/regexproof/issues/328).

three.ws chat UI sibling. Top-60 first-party ecma files measured **463/800
= 0.5787 encodable** (complete, deterministic) with 260 findings.

## Materialize

```bash
PIN=c21b982a9f1583a44a5d9d15df403964d8c8aa0b
git clone --filter=blob:none https://github.com/nirholas/three-ui.git /tmp/three-ui
git -C /tmp/three-ui fetch --depth 1 origin "$PIN"
git -C /tmp/three-ui checkout "$PIN"
ln -sfn /tmp/three-ui batch/corpora/three-ui/rules
test "$(git -C /tmp/three-ui rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/three-ui_gate_decision.json` (`go`).
Smith: `properties/generated/three-ui_smith_decision.json` (`go`).
Non-security app → public-first.

## Notes

- Budget gotcha: initial `max_disk_mb: 500` breached at 512MB (the
  symlinked tree is larger than the allowlist) → `complete_run=False`.
  Raised to 1000 → complete. Large allowlist corpora should start at 1000.
