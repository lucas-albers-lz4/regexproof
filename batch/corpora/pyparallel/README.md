# pyparallel corpus

Pinned pyparallel/pyparallel py_re allowlist for Smith GO admit
[#330](https://github.com/lucas-albers-lz4/regexproof/issues/330)
under umbrella [#328](https://github.com/lucas-albers-lz4/regexproof/issues/328).

Python fork. Top-60 .py files measured **580/1,027 = 0.5648 encodable**
(complete, deterministic) with **173 findings**.

## Materialize

```bash
PIN=5e0b13026072ba0de7dcc86d254e8b357ca3e9db
git clone --filter=blob:none https://github.com/pyparallel/pyparallel.git /tmp/pyparallel
git -C /tmp/pyparallel fetch --depth 1 origin "$PIN"
git -C /tmp/pyparallel checkout "$PIN"
ln -sfn /tmp/pyparallel batch/corpora/pyparallel/rules
test "$(git -C /tmp/pyparallel rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/pyparallel_gate_decision.json` (`go`).
Smith: `properties/generated/pyparallel_smith_decision.json` (`go`).
Non-security interpreter → public-first.
