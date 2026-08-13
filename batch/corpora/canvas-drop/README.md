# canvas-drop corpus

Pinned markpasternak/canvas-drop ecma allowlist for Smith GO admit
[#290](https://github.com/lucas-albers-lz4/regexproof/issues/290)
under umbrella [#284](https://github.com/lucas-albers-lz4/regexproof/issues/284).

Auth/identity app. Top-60 ecma files measured **42/76 = 0.5526 encodable**
(complete, deterministic).

## Materialize

```bash
PIN=ef9baeb3743426c58853e58fbad820e69e459144
git clone --filter=blob:none https://github.com/markpasternak/canvas-drop.git /tmp/canvas-drop
git -C /tmp/canvas-drop fetch --depth 1 origin "$PIN"
git -C /tmp/canvas-drop checkout "$PIN"
ln -sfn /tmp/canvas-drop batch/corpora/canvas-drop/rules
test "$(git -C /tmp/canvas-drop rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/canvas-drop_gate_decision.json` (triage-trial).
Smith: `properties/generated/canvas-drop_smith_decision.json` (go).
Identity-handling boundary → `private_first` via `SECURITY_TOOL_CORPORA`.
