# sec_check corpus

Pinned netxfly/sec_check yara pack for Smith GO admit
[#319](https://github.com/lucas-albers-lz4/regexproof/issues/319)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

Cross-platform security detection tool. 509 yara files measured
**9,567/15,459 = 0.6189 encodable** (complete, deterministic) with 64
findings.

## Materialize

```bash
PIN=b7b9841432f0f4c69f360d910c5fcce4d0e4a01f
git clone --filter=blob:none https://github.com/netxfly/sec_check.git /tmp/sec_check
git -C /tmp/sec_check fetch --depth 1 origin "$PIN"
git -C /tmp/sec_check checkout "$PIN"
ln -sfn /tmp/sec_check/rules batch/corpora/sec_check/rules
test "$(git -C /tmp/sec_check rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/sec_check_gate_decision.json` (`go`).
Smith: `properties/generated/sec_check_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus sec_check --assert-determinism
python -m regexproof.batch --corpus sec_check
```

## Notes

- rules/ structure is identical to PEpper — **shared/derived ruleset
  CONFIRMED** by overlap analysis (2026-08-13): 520/538 shared files
  byte-identical, 19,858/19,866 pattern strings identical (99.86%),
  45/64 findings pattern-identical. sec_check (2018-09) is the original;
  PEpper (2019-07) vendored it and added ~128 patterns in new dirs.
  This row is the canonical one. Full analysis:
  `batch/corpora/pepper-sec_check-overlap.md`.
