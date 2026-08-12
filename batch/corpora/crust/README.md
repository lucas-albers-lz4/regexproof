# crust corpus

Pinned BakeLens/crust first-party Go DLP/rules surface for Smith triage-trial
[#246](https://github.com/lucas-albers-lz4/regexproof/issues/246)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Allowlist focuses on `internal/rules` + `internal/configscan` regexp sites
(nearest admitted=`gitleaks`). Excludes tests and the small py_re CVE-tracker
script (single-dialect `go_regexp` / `re2`).

## Materialize

```bash
PIN=f4a47e2cf2822196275075ab9a2e258b6fa9be8b
git clone --filter=blob:none https://github.com/BakeLens/crust.git /tmp/crust
git -C /tmp/crust fetch --depth 1 origin "$PIN"
git -C /tmp/crust checkout "$PIN"
ln -sfn /tmp/crust batch/corpora/crust/rules
test "$(git -C /tmp/crust rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/crust_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus crust --assert-determinism
python -m regexproof.batch --corpus crust
```
