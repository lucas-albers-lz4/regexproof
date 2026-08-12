# gilectomy corpus

Pinned larryhastings/gilectomy first-party py_re allowlist for Smith GO admit
[#338](https://github.com/lucas-albers-lz4/regexproof/issues/338)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Gilectomy CPython branch. Top-60 .py files measured **480/904 = 0.5310
encodable** (complete, deterministic).

## Materialize

```bash
PIN=4315ec3f1d6d4f813cc82ce27a24e7f784dbfc1a
git clone --filter=blob:none https://github.com/larryhastings/gilectomy.git /tmp/gilectomy
git -C /tmp/gilectomy fetch --depth 1 origin "$PIN"
git -C /tmp/gilectomy checkout "$PIN"
ln -sfn /tmp/gilectomy batch/corpora/gilectomy/rules
test "$(git -C /tmp/gilectomy rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/gilectomy_gate_decision.json` (`go`).
Smith: `properties/generated/gilectomy_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus gilectomy --assert-determinism
python -m regexproof.batch --corpus gilectomy
```

## Notes

- **Allowlist gotcha**: the probe's `regex_sites_per_file` includes non-.py
  files (Modules/zlib/configure, Modules/_ctypes/libffi/msvcc.sh) — they
  break `ast.parse` with SyntaxError. py_re allowlists must filter to `.py`
  files only. Same fix applied before measure.
