# nogil-3.12 corpus

Pinned colesbury/nogil-3.12 first-party py_re allowlist for Smith GO admit
[#337](https://github.com/lucas-albers-lz4/regexproof/issues/337)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Multithreaded Python without the GIL. Top-60 .py files measured
**539/1,084 = 0.4972 encodable** (complete, deterministic) with 140
findings.

## Materialize

```bash
PIN=cedde4f5ec3759ad723c89d44738776f362df564
git clone --filter=blob:none https://github.com/colesbury/nogil-3.12.git /tmp/nogil-3.12
git -C /tmp/nogil-3.12 fetch --depth 1 origin "$PIN"
git -C /tmp/nogil-3.12 checkout "$PIN"
ln -sfn /tmp/nogil-3.12 batch/corpora/nogil-3.12/rules
test "$(git -C /tmp/nogil-3.12 rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/nogil-3.12_gate_decision.json` (`go`).
Smith: `properties/generated/nogil-3.12_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus nogil-3.12 --assert-determinism
python -m regexproof.batch --corpus nogil-3.12
```
