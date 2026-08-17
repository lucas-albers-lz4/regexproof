# AutoAR corpus — Smith no-go

Pinned `h0tak88r/AutoAR` at `01cd447ad3b1acfed7e0680596c2c74458a4cf06`.
Gate renamed to `AutoAR_gate_decision.json` (stem matches `corpus=`).

## Decision: no-go (low encodable fraction)

First-party UI JS allowlist (29 files, vendor `lib/*.min.js` + `tests/`
excluded): **230/891 = 0.2581** encodable (`complete_run`). Below the
WAVE encode floor used for GO packs.

Not added to `WAVE_CORPORA` / `SECURITY_TOOL_CORPORA` / `CORPUS_MANIFESTS`.

## Materialize (for re-measure)

```bash
cat > /tmp/autoar-allowlist.txt <<'LIST'
internal/api/ui/adbauditor/js/adb-core.js
internal/api/ui/adbauditor/js/app.js
internal/api/ui/adbauditor/js/security-auditor.js
internal/api/ui/apkauditor/src/core/engine.js
internal/api/ui/apkauditor/src/core/entropy.js
internal/api/ui/apkauditor/src/core/export.js
internal/api/ui/apkauditor/src/core/pdf.js
internal/api/ui/apkauditor/src/main.js
internal/api/ui/ipaauditor/ipa-analyzer.js
internal/api/ui/pages/html-escape.js
internal/api/ui/pages/keyhacks.js
internal/api/ui/pages/launcher.js
internal/api/ui/pages/module-registry.js
internal/api/ui/pages/ops-tools.js
internal/api/ui/pages/program-lookup.js
internal/api/ui/pages/programs.js
internal/api/ui/pages/r2-prefixes.js
internal/api/ui/pages/r2.js
internal/api/ui/pages/report-templates.js
internal/api/ui/pages/result-tables.js
internal/api/ui/pages/router-core.js
internal/api/ui/pages/router-navigation.js
internal/api/ui/pages/scan-common.js
internal/api/ui/pages/scan-detail-manifest.js
internal/api/ui/pages/scan-detail.js
internal/api/ui/pages/scan-results-core.js
internal/api/ui/pages/scans-page.js
internal/api/ui/pages/targets.js
internal/api/ui/securitylab/takeover-reference.js
LIST
python scripts/materialize-corpus.py --gate properties/generated/AutoAR_gate_decision.json \
  --allowlist-file /tmp/autoar-allowlist.txt
ln -sfn /tmp/h0tak88r-AutoAR-AutoAR batch/corpora/AutoAR/rules
```
