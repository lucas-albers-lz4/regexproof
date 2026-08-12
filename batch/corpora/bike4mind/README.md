# bike4mind corpus

Pinned Bike4Mind/bike4mind first-party ecma allowlist for Smith GO admit
[#278](https://github.com/lucas-albers-lz4/regexproof/issues/278)
under umbrella [#277](https://github.com/lucas-albers-lz4/regexproof/issues/277).

AI workbench (notebooks/agents/RAG). First-party surface scoped to the top-60
files by probe sites (excludes ~2,014 vendored/test sites in
`public/static/lib` — xlsx/recharts/mathjs/lodash/d3 bundles — plus tests and
playwright config). Measured **815/1,386 = 0.5880 encodable** (complete,
deterministic) with **194 findings** (175 usage_mismatch, 15 intent_mismatch,
4 property).

## Materialize

```bash
PIN=391c37a5d7de13c9296667ceb65b3148bc276f82
git clone --filter=blob:none https://github.com/Bike4Mind/bike4mind.git /tmp/bike4mind
git -C /tmp/bike4mind fetch --depth 1 origin "$PIN"
git -C /tmp/bike4mind checkout "$PIN"
ln -sfn /tmp/bike4mind batch/corpora/bike4mind/rules
test "$(git -C /tmp/bike4mind rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/bike4mind_gate_decision.json` (`go`).
Smith: `properties/generated/bike4mind_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus bike4mind --assert-determinism
python -m regexproof.batch --corpus bike4mind
```

## Notes

- 687 additional first-party files (~1,552 sites) exist beyond the top-60
  allowlist — a follow-on PR can widen the allowlist if the initial fraction
  holds.
- The 194 findings are usage/intent mismatches (anchored patterns consumed via
  search/test, etc.) — the same finding classes malcontent surfaced.
