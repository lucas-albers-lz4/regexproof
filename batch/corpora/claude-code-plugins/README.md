# claude-code-plugins corpus

Pinned melodic-software/claude-code-plugins shell corpus for Smith GO admit
[#292](https://github.com/lucas-albers-lz4/regexproof/issues/292)
under umbrella [#291](https://github.com/lucas-albers-lz4/regexproof/issues/291).

Claude Code plugin marketplace (skills/hooks/MCP servers). **NEW SHELL
RECORD**: 490 shell files / **1,344 regex sites** (largest shell corpus;
mycelium 1,029, OpenWrt 713). Measured **1,093/1,344 = 0.8132 encodable**
(complete, deterministic) — the strongest shell fraction — with **429
findings** (highest yield of any corpus).

## Materialize

```bash
PIN=f44d0df5e7bf023b88cccc37301402ba7f9dcdb1
git clone --filter=blob:none https://github.com/melodic-software/claude-code-plugins.git /tmp/claude-code-plugins
git -C /tmp/claude-code-plugins fetch --depth 1 origin "$PIN"
git -C /tmp/claude-code-plugins checkout "$PIN"
ln -sfn /tmp/claude-code-plugins batch/corpora/claude-code-plugins/rules
test "$(git -C /tmp/claude-code-plugins rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/claude-code-plugins_gate_decision.json` (`go`).
Smith: `properties/generated/claude-code-plugins_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus claude-code-plugins --assert-determinism
python -m regexproof.batch --corpus claude-code-plugins
```

## Notes

- 429 findings: shell usage/intent mismatches in plugin hooks — the highest
  yield of any corpus, confirming the shell value stream (compiler-fix
  discovery + findings).
- Shell family now: dogfooding 292, OpenWrt 713, anax 194 (0.7990), mycelium
  1,029 (0.8105), claude-code-plugins 1,344 (0.8132).
