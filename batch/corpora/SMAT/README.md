# SMAT corpus

Pinned mr-satan1/SMAT yara pack for Smith GO admit
[#344](https://github.com/lucas-albers-lz4/regexproof/issues/344)
under umbrella [#343](https://github.com/lucas-albers-lz4/regexproof/issues/343).

Simple Malware Analysis Tool. 628 yara files measured **5,652/9,016 =
0.6269 encodable** (complete, deterministic) with 52 findings.

## Materialize

```bash
PIN=def00ebdfb7f3e004677c0edf15164819a8e6c6d
git clone --filter=blob:none https://github.com/mr-satan1/SMAT.git /tmp/SMAT
git -C /tmp/SMAT fetch --depth 1 origin "$PIN"
git -C /tmp/SMAT checkout "$PIN"
ln -sfn /tmp/SMAT/rules batch/corpora/SMAT/rules
test "$(git -C /tmp/SMAT rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/SMAT_gate_decision.json` (`go`).
Smith: `properties/generated/SMAT_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus SMAT --assert-determinism
python -m regexproof.batch --corpus SMAT
```
