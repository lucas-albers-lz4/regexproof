# typescript-go corpus

Pinned microsoft/typescript-go testdata ecma corpus for Smith GO admit
[#300](https://github.com/lucas-albers-lz4/regexproof/issues/300)
under umbrella [#299](https://github.com/lucas-albers-lz4/regexproof/issues/299).

TypeScript-in-Go. **98% of the probe surface is testdata** (the ported TS
test suite baselines — the v8/test262 class). Manifest scopes to the top-80
testdata files. Measured **1,483/2,558 = 0.5797 encodable** (complete,
deterministic) with 12 findings.

## Materialize

```bash
PIN=34ffe2a2531a226da0046d213899ae0b721229b0
git clone --filter=blob:none https://github.com/microsoft/typescript-go.git /tmp/typescript-go
git -C /tmp/typescript-go fetch --depth 1 origin "$PIN"
git -C /tmp/typescript-go checkout "$PIN"
ln -sfn /tmp/typescript-go batch/corpora/typescript-go/rules
test "$(git -C /tmp/typescript-go rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/typescript-go_gate_decision.json` (`go`).
Smith: `properties/generated/typescript-go_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus typescript-go --assert-determinism
python -m regexproof.batch --corpus typescript-go
```

## Notes

- 640 additional testdata files (~3,272 sites) exist beyond the top-80
  allowlist — a follow-on PR can widen scope.
- First-party Go code (33 files, 122 sites) is out of scope — the Go surface
  is the re2-dialect engine, not the ecma corpus value.
