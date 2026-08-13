# cpython-13 corpus

Pinned aikwp/cpython-13 first-party py_re allowlist for Smith GO admit
[#348](https://github.com/lucas-albers-lz4/regexproof/issues/348)
under umbrella [#343](https://github.com/lucas-albers-lz4/regexproof/issues/343).

Python 3.13 fork. Top-60 .py files measured **602/1,277 = 0.4714
encodable** (complete, deterministic) with 131 findings.

## Materialize

```bash
PIN=5975602bc460d4e684807260e8ce2f6363910a55
git clone --filter=blob:none https://github.com/aikwp/cpython-13.git /tmp/cpython-13
git -C /tmp/cpython-13 fetch --depth 1 origin "$PIN"
git -C /tmp/cpython-13 checkout "$PIN"
ln -sfn /tmp/cpython-13 batch/corpora/cpython-13/rules
test "$(git -C /tmp/cpython-13 rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/cpython-13_gate_decision.json` (`go`).
Smith: `properties/generated/cpython-13_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus cpython-13 --assert-determinism
python -m regexproof.batch --corpus cpython-13
```
