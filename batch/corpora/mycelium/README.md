# mycelium corpus

Pinned mycelium0/mycelium shell corpus for Smith GO admit
[#288](https://github.com/lucas-albers-lz4/regexproof/issues/288)
under umbrella [#284](https://github.com/lucas-albers-lz4/regexproof/issues/284).

**Shell milestone**: 142 shell files / 32,023 lines / **1,029 regex sites**
(3.5× the OpenWrt feed's 713, 3.5× the dogfooding surface's 292). Measured
**834/1,029 = 0.8105 encodable** (complete, deterministic) — the strongest
shell fraction in the matrix (anax 0.7990 second).

## Materialize

```bash
PIN=4b53dc7629ca3bc88bf5467db481ad2af7130711
git clone --filter=blob:none https://github.com/mycelium0/mycelium.git /tmp/mycelium
git -C /tmp/mycelium fetch --depth 1 origin "$PIN"
git -C /tmp/mycelium checkout "$PIN"
ln -sfn /tmp/mycelium batch/corpora/mycelium/rules
test "$(git -C /tmp/mycelium rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/mycelium_gate_decision.json` (`go`).
Smith: `properties/generated/mycelium_smith_decision.json` (`go`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus mycelium --assert-determinism
python -m regexproof.batch --corpus mycelium
```

## Bucket profile (2026-08-12 measure)

195 unencodable of 1,029 (19%) — bucket analysis pending in #288; the shell
corpus family now has four datapoints: dogfooding 292, OpenWrt feed 713,
anax 194 (0.7990), mycelium 1,029 (0.8105).
