# anax corpus

Pinned open-horizon/anax edge-agent shell corpus for Smith triage-trial
[#280](https://github.com/lucas-albers-lz4/regexproof/issues/280)
under umbrella [#277](https://github.com/lucas-albers-lz4/regexproof/issues/277).

First **non-dogfooding posix-shell** corpus: 194 shell sites measured
**155/194 = 0.7990 encodable** (complete, deterministic) — strong validation
of the BRE→ERE normalize → pcre backend on real edge-agent shell.

## Materialize

```bash
PIN=2f3fa5a506d6565fa68858b7963450567ddda114
git clone --filter=blob:none https://github.com/open-horizon/anax.git /tmp/anax
git -C /tmp/anax fetch --depth 1 origin "$PIN"
git -C /tmp/anax checkout "$PIN"
ln -sfn /tmp/anax batch/corpora/anax/rules
test "$(git -C /tmp/anax rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/anax_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/anax_smith_decision.json` (`triage-continues`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus anax --assert-determinism
python -m regexproof.batch --corpus anax
```

## Bucket profile (2026-08-12 measure)

39 unencodable of 194 — bucket analysis pending in #280 (expected: BRE/ERE
semantics edge cases, sed-address false positives). Shell corpus family
now has three datapoints: dogfooding (292 sites), OpenWrt feed (713),
anax (194).
