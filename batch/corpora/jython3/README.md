# jython3 corpus

Pinned jython/jython3 first-party py_re allowlist for Smith GO admit
[#349](https://github.com/lucas-albers-lz4/regexproof/issues/349)
under umbrella [#343](https://github.com/lucas-albers-lz4/regexproof/issues/343).

Jython 3. Top-60 .py files measured **653/1,172 = 0.5572 encodable**
(complete, deterministic) with **182 findings — highest py yield**.

## Materialize

```bash
PIN=e0d80bbddff0d5465f2da3f9de52bff89ab00e53
git clone --filter=blob:none https://github.com/jython/jython3.git /tmp/jython3
git -C /tmp/jython3 fetch --depth 1 origin "$PIN"
git -C /tmp/jython3 checkout "$PIN"
ln -sfn /tmp/jython3 batch/corpora/jython3/rules
test "$(git -C /tmp/jython3 rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/jython3_gate_decision.json` (`go`).
Smith: `properties/generated/jython3_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus jython3 --assert-determinism
python -m regexproof.batch --corpus jython3
```

## Notes

- The admission-time 113 extractor_errors were in files outside the top-60
  allowlist — the measured surface is clean.
