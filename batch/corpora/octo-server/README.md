# octo-server corpus

Pinned Mininglamp-OSS/octo-server Go/`re2` surfaces for Smith triage-trial
[#158](https://github.com/lucas-albers-lz4/regexproof/issues/158).

Probe reported 228 sites; **jquery min (~80)** and `*_test.go` are excluded.
Allowlist is non-test `.go` product/tools code only.

## Materialize

```bash
PIN=d3daa912a04d17f78df2d0c059a111cafff75534
git clone https://github.com/Mininglamp-OSS/octo-server.git /tmp/octo-server
git -C /tmp/octo-server fetch --depth 1 origin "$PIN"
git -C /tmp/octo-server checkout "$PIN"
ln -sfn /tmp/octo-server batch/corpora/octo-server/rules
test "$(git -C /tmp/octo-server rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/octo-server_gate_decision.json` (`triage-trial`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus octo-server --assert-determinism
python -m regexproof.batch --corpus octo-server
```
