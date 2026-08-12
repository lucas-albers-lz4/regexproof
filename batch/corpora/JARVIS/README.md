# JARVIS corpus

Pinned drussell23/JARVIS first-party py_re allowlist for Smith GO admit
[#286](https://github.com/lucas-albers-lz4/regexproof/issues/286)
under umbrella [#284](https://github.com/lucas-albers-lz4/regexproof/issues/284).

JARVIS Trinity AGI OS. First-party py_re surface scoped to the top-60 py
files by probe sites. Measured **359/848 = 0.4233 encodable** (complete,
deterministic) with **95 findings**.

## Materialize

```bash
PIN=d9164ff679c6f2cd3e1fa19c311db7a9eed32c7e
git clone --filter=blob:none https://github.com/drussell23/JARVIS.git /tmp/JARVIS
git -C /tmp/JARVIS fetch --depth 1 origin "$PIN"
git -C /tmp/JARVIS checkout "$PIN"
ln -sfn /tmp/JARVIS batch/corpora/JARVIS/rules
test "$(git -C /tmp/JARVIS rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/JARVIS_gate_decision.json` (`go`).
Smith: `properties/generated/JARVIS_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus JARVIS --assert-determinism
python -m regexproof.batch --corpus JARVIS
```

## Notes

- Extractor is `python_dir` (registry name), NOT `python_ast` — the measure
  fails with a ValueError otherwise.
- 420 additional first-party py files (~950 sites) + ecma/shell surface
  (~380 sites) exist beyond the allowlist — a follow-on PR can widen scope.
- The 0.4233 fraction is the lowest py corpus yet (cpython_re 0.556) — the
  complex AGI-OS patterns are the residual; bucket analysis pending in #286.
