# pythowon corpus

Pinned vcokltfre/pythowon first-party py_re allowlist for Smith GO admit
[#357](https://github.com/lucas-albers-lz4/regexproof/issues/357)
under umbrella [#356](https://github.com/lucas-albers-lz4/regexproof/issues/356).

Python fork. Top-60 .py files measured **545/1,113 = 0.4897 encodable**
(complete, deterministic) with 144 findings.

## Materialize

```bash
PIN=2b78a358c0da53219e48cf10dddb7ad3f93d474a
git clone --filter=blob:none https://github.com/vcokltfre/pythowon.git /tmp/pythowon
git -C /tmp/pythowon fetch --depth 1 origin "$PIN"
git -C /tmp/pythowon checkout "$PIN"
ln -sfn /tmp/pythowon batch/corpora/pythowon/rules
test "$(git -C /tmp/pythowon rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/pythowon_gate_decision.json` (`go`).
Smith: `properties/generated/pythowon_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus pythowon --assert-determinism
python -m regexproof.batch --corpus pythowon
```
