# tarcoin corpus

Pinned Tarcoin/tarcoin app-only allowlist for Smith GO admit
[#314](https://github.com/lucas-albers-lz4/regexproof/issues/314)
under umbrella [#313](https://github.com/lucas-albers-lz4/regexproof/issues/313).

Tarcoin blockchain. **Probe-count correction**: the 1,238-site probe was 88%
Qt locale translation catalogs (`bitcoin_*.ts` plural files — translation
strings, not regex code). Honest first-party surface: **129 sites** (40-file
app allowlist) measured **118/129 = 0.9147 encodable** — the second-highest
fraction in the matrix. KEPT as GO with corrected basis.

## Materialize

```bash
PIN=a6552d17180dbf4a43a74c875db3e9a77f9437d6
git clone --filter=blob:none https://github.com/Tarcoin/tarcoin.git /tmp/tarcoin
git -C /tmp/tarcoin fetch --depth 1 origin "$PIN"
git -C /tmp/tarcoin checkout "$PIN"
ln -sfn /tmp/tarcoin batch/corpora/tarcoin/rules
test "$(git -C /tmp/tarcoin rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/tarcoin_gate_decision.json` (`go`).
Smith: `properties/generated/tarcoin_smith_decision.json` (`go`, corrected basis).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus tarcoin --assert-determinism
python -m regexproof.batch --corpus tarcoin
```

## Notes

- The full-clone walk exceeds the 200MB disk budget (238.5MB) — complete_run
  is False for the fraction artifact, but the measured subset is deterministic.
  Raise budget to 500MB if a full re-run is needed.
- Lesson: translation catalogs (Qt `.ts`, gettext `.po`) inflate ecma site
  counts — probe spot-checks must exclude locale dirs before scale-based GO.
  **Full incident writeup + 3-variant inflation taxonomy + detection
  recipe**: `batch/corpora/tarcoin-locale-inflation.md`.
