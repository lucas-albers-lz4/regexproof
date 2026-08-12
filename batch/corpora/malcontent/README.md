# malcontent corpus

Pinned chainguard-dev/malcontent own-rules pack for Smith GO admit
[#261](https://github.com/lucas-albers-lz4/regexproof/issues/261)
under umbrella [#260](https://github.com/lucas-albers-lz4/regexproof/issues/260).

Malware-content scanner — security tool. `private_first` via
`SECURITY_TOOL_CORPORA`.

## Materialize

```bash
PIN=ea3e83e24676a1678a9522141da29b636c9451ab
git clone --filter=blob:none https://github.com/chainguard-dev/malcontent.git /tmp/malcontent
git -C /tmp/malcontent fetch --depth 1 origin "$PIN"
git -C /tmp/malcontent checkout "$PIN"
ln -sfn /tmp/malcontent/rules batch/corpora/malcontent/rules
test "$(git -C /tmp/malcontent rev-parse HEAD)" = "$PIN"
```

Path pinned to `rules/` — excludes the 1,386 vendored `third_party/` yara
files (huntress/guarddog/etc. packs); this corpus is the 1,156-file
first-party pack (32,908 lines). Probe counted 19,578 sites including
third_party; the manifest scope is the own-rules subset.

Gate: `properties/generated/malcontent_gate_decision.json` (`go`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus malcontent --assert-determinism
python -m regexproof.batch --corpus malcontent
```

Largest yara corpus in the matrix — budget max_patterns 30000 / max_wall_s 900
may need a raise if the Z3 compile exceeds it (spamassassin precedent: perl
dialect 73.6s per 1k sites; yara fullword-boundary heavy at 5,902 rejects in
yara_rules).
