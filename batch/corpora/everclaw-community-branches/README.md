# everclaw-community-branches corpus

Pinned first-party ecma regex surfaces for Smith triage-trial
[#156](https://github.com/lucas-albers-lz4/regexproof/issues/156).

Admission probe reported **533** sites (ecma 468 + py_re 65). Bundled
`docs/docs/assets/*.js` and tests are excluded. Primary Smith surface is
**skillguard** plus first-party scripts / auth-proxy.

## Materialize

```bash
PIN=7ea3b445ee7d2ef8004d5ee77dab7544e1b8ef88
git clone https://github.com/profbernardoj/everclaw-community-branches.git /tmp/everclaw
git -C /tmp/everclaw fetch --depth 1 origin "$PIN"
git -C /tmp/everclaw checkout "$PIN"
ln -sfn /tmp/everclaw batch/corpora/everclaw-community-branches/rules
test "$(git -C /tmp/everclaw rev-parse HEAD)" = "$PIN"
```

## Extractor

- Dialect: `ecma`
- Extractor: `js_precise_dir` (`extract_js_precise`)

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus everclaw-community-branches --assert-determinism
python -m regexproof.batch --corpus everclaw-community-branches
```

At pin: **145/343 = 0.4227** fraction go.

Python `prompt-guard` / bagman examples (py_re) are noted in the gate probe
but not in this ecma allowlist; revisit if a follow-on py slice is needed.

## Admission

Gate already on `main`: `properties/generated/everclaw-community-branches_gate_decision.json`
(`triage-trial`). Required by `check_admission_gates` before batch.
