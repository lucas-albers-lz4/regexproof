# cpython corpus

Pinned ColdGrub1384/cpython py_re allowlist for Smith GO admit
[#359](https://github.com/lucas-albers-lz4/regexproof/issues/359)
under umbrella [#356](https://github.com/lucas-albers-lz4/regexproof/issues/356).

CPython fork. Top-60 .py files measured **500/965 = 0.5181 encodable**
(complete, deterministic) with 138 findings.

## Materialize

```bash
PIN=a487e12da470edf59e6bc96166d2178dad54dd85
git clone --filter=blob:none https://github.com/ColdGrub1384/cpython.git /tmp/cpython
git -C /tmp/cpython fetch --depth 1 origin "$PIN"
git -C /tmp/cpython checkout "$PIN"
ln -sfn /tmp/cpython batch/corpora/cpython/rules
test "$(git -C /tmp/cpython rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/cpython_gate_decision.json` (`go`).
Smith: `properties/generated/cpython_smith_decision.json` (`go`).
Non-security interpreter fork → public-first.
