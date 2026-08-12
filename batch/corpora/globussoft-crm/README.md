# globussoft-crm corpus

Pinned Globussoft-Technologies/globussoft-crm first-party ecma allowlist for
Smith GO admit
[#285](https://github.com/lucas-albers-lz4/regexproof/issues/285)
under umbrella [#284](https://github.com/lucas-albers-lz4/regexproof/issues/284).

Open-source CRM. **88% of the probe surface (14,437 of 16,565 sites) is
vendored/test** (node_modules/dist/public/test bundles) — the manifest scopes
to the top-60 first-party files. Measured **665/975 = 0.6821 encodable**
(complete, deterministic) with **252 findings**.

## Materialize

```bash
PIN=8a53d8b624cacad6049d9a49255f4f8493169085
git clone --filter=blob:none https://github.com/Globussoft-Technologies/globussoft-crm.git /tmp/globussoft-crm
git -C /tmp/globussoft-crm fetch --depth 1 origin "$PIN"
git -C /tmp/globussoft-crm checkout "$PIN"
ln -sfn /tmp/globussoft-crm batch/corpora/globussoft-crm/rules
test "$(git -C /tmp/globussoft-crm rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/globussoft-crm_gate_decision.json` (`go`).
Smith: `properties/generated/globussoft-crm_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus globussoft-crm --assert-determinism
python -m regexproof.batch --corpus globussoft-crm
```

## Notes

- 421 additional first-party files (~1,153 sites) exist beyond the top-60
  allowlist — a follow-on PR can widen the allowlist.
- 252 findings from the CRM surface (validators.js, sanitizeJson.js,
  inboundLeadVerification.js, auth.js in the allowlist).
