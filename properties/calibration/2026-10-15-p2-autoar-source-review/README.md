# AutoAR exact-pin source review

This second-pass review covers all 34 literal Go regexp sites in frozen
20-r2 AutoAR at `01cd447ad3b1acfed7e0680596c2c74458a4cf06`. Source windows are
bound to the corrected v2 inventory and exact checkout in
[`evidence.json`](evidence.json).

| Decision | Count | Disposition |
|---|---:|---|
| Skip | 28 | Scanner-output parsers/classifiers and test fixtures with no separately specified security-boundary property |
| Unresolved | 3 | Nuclei host grammar, SQLMap target filtering, and misconfiguration-scan URL composition need independent target-scope contracts |
| Adopted | 3 | Two existing JavaScript endpoint contracts plus the new phase-log filename-component contract |
| Product questions asked | 3 | Each adopted identity is source-bound; the new phase-key question was frozen before its formal solver run |

The phase-key contract is limited to the caller-controlled `module` query's
filename component. It establishes that the pinned `sanitizeRe` replaces dot
and separator characters before `filepath.Join`; it does not establish safety
for the separately supplied `scanID`, the results root, symlinks, or aliasing
between module names. Its source review and exact-pin gate artifacts are in
[`2026-10-15-autonomous-autoar-phasekey-20r2/`](../2026-10-15-autonomous-autoar-phasekey-20r2/README.md).

The unresolved rows remain out of product-question denominators because the
repository does not define the authorized target language needed to assess
their network behavior. Scanner extraction and response-classification
patterns are recorded as skips rather than counted as boundary proofs.
