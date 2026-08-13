# pm_shredder corpus

Pinned x41x41x90/pm_shredder yara pack for Smith GO admit
[#350](https://github.com/lucas-albers-lz4/regexproof/issues/350)
under umbrella [#343](https://github.com/lucas-albers-lz4/regexproof/issues/343).

6-file yara pack (zeus/spyeye/magic/email_contents). Measured **834/834 =
1.0000 encodable** — **first perfect fraction in the matrix**.

## Materialize

```bash
PIN=7fa83b2250a434bfe153a67eb52e015558e9409a
git clone --filter=blob:none https://github.com/x41x41x90/pm_shredder.git /tmp/pm_shredder
git -C /tmp/pm_shredder fetch --depth 1 origin "$PIN"
git -C /tmp/pm_shredder checkout "$PIN"
ln -sfn /tmp/pm_shredder batch/corpora/pm_shredder/rules
test "$(git -C /tmp/pm_shredder rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/pm_shredder_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/pm_shredder_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus pm_shredder --assert-determinism
python -m regexproof.batch --corpus pm_shredder
```
