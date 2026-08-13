# json-editor corpus

Pinned json-editor/json-editor ecma allowlist for Smith GO admit
[#282](https://github.com/lucas-albers-lz4/regexproof/issues/282)
under umbrella [#277](https://github.com/lucas-albers-lz4/regexproof/issues/277).

JSON-schema form editor (validator class). Measured **6/13 = 0.4615
encodable** (complete, deterministic).

## Materialize

```bash
PIN=b31ddabecf4ed3209d37a2f5b29956120cd8f9ce
git clone --filter=blob:none https://github.com/json-editor/json-editor.git /tmp/json-editor
git -C /tmp/json-editor fetch --depth 1 origin "$PIN"
git -C /tmp/json-editor checkout "$PIN"
ln -sfn /tmp/json-editor/src batch/corpora/json-editor/rules
test "$(git -C /tmp/json-editor rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/json-editor_gate_decision.json` (triage-trial).
Smith: `properties/generated/json-editor_smith_decision.json` (go).
Non-security validator → public-first.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus json-editor --assert-determinism
python -m regexproof.batch --corpus json-editor
```
