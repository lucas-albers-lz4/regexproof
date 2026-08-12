# xibo-cms corpus

Pinned xibosignage/xibo-cms first-party frontend/ui/module-src ecma surface
for Smith go [#241](https://github.com/lucas-albers-lz4/regexproof/issues/241)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Allowlist focuses on first-party validators/parsers/helpers (regex.ts,
date/schema validators, XSRF cookie parse, template substitution, upload
validation) — excludes `__tests__`, `__mocks__`, `setupTests`, bundled
`modules/bundle.js` / `player_bundle.js`, vendored `flipclock`, and build
config (`webpack.config.js`, `vite.config.ts`).

## Materialize

```bash
PIN=978def55c8e68cab3a50a7ee4725039da753f0a1
git clone --filter=blob:none https://github.com/xibosignage/xibo-cms.git /tmp/xibo-cms
git -C /tmp/xibo-cms fetch --depth 1 origin "$PIN"
git -C /tmp/xibo-cms checkout "$PIN"
ln -sfn /tmp/xibo-cms batch/corpora/xibo-cms/rules
test "$(git -C /tmp/xibo-cms rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/xibo-cms_gate_decision.json` (`go`, scale-only;
`security_boundary=unknown` — not a security tool, so not in
`SECURITY_TOOL_CORPORA`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus xibo-cms --assert-determinism
python -m regexproof.batch --corpus xibo-cms
```
