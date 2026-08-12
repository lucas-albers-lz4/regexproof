# PEpper corpus

Pinned 0x0be/PEpper yara pack for Smith GO admit
[#318](https://github.com/lucas-albers-lz4/regexproof/issues/318)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

PE malware static-analysis script. 520 yara files measured **9,733/15,626 =
0.6229 encodable** (complete, deterministic) with 64 findings.

## Materialize

```bash
PIN=9dfcade04b41422b5c8457956f984cd25fe3e6d2
git clone --filter=blob:none https://github.com/0x0be/PEpper.git /tmp/PEpper
git -C /tmp/PEpper fetch --depth 1 origin "$PIN"
git -C /tmp/PEpper checkout "$PIN"
ln -sfn /tmp/PEpper/rules batch/corpora/PEpper/rules
test "$(git -C /tmp/PEpper rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/PEpper_gate_decision.json` (`go`).
Smith: `properties/generated/PEpper_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus PEpper --assert-determinism
python -m regexproof.batch --corpus PEpper
```

## Notes

- rules/ structure is identical to sec_check (utils/virustotal, url,
  suspicious_strings, magic) — likely a shared/derived ruleset. Overlap
  analysis vs sec_check is a follow-on.
