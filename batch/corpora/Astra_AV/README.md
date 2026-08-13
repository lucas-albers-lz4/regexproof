# Astra_AV corpus

Pinned Ph4wkm00n/Astra_AV yara pack for Smith GO admit
[#326](https://github.com/lucas-albers-lz4/regexproof/issues/326)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

AV yara pack (3 files: emotet/ransomware_generic/wannacry). Measured
**97/97 = 1.0000 encodable** (complete, deterministic) — perfect despite
tiny size.

## Materialize

```bash
PIN=87fe9529fdf9c64126bd81fc45658bb86bd64755
git clone --filter=blob:none https://github.com/Ph4wkm00n/Astra_AV.git /tmp/Astra_AV
git -C /tmp/Astra_AV fetch --depth 1 origin "$PIN"
git -C /tmp/Astra_AV checkout "$PIN"
ln -sfn /tmp/Astra_AV batch/corpora/Astra_AV/rules
test "$(git -C /tmp/Astra_AV rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/Astra_AV_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/Astra_AV_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Notes

- Reverses the tiny-size no-go assumption (pkt/YaraCapper/MobProtID):
  hand-curated packs are fully encodable even at <100 sites. The
  distinction: curated rule packs (structured, bounded) vs throwaway
  scripts (tiny, no structure).
