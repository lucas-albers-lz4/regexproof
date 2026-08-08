# Phase 4 rule_diff families

| Family | Kind | Gap result | Ground truth |
|---|---|---|---|
| gitleaks-trufflehog-cross-scanner | cross_scanner | sat | reproduced |
| ids-sig-evolution | version_diff | sat | reproduced |
| crs-adjacent-tag | version_diff+sibling_family | n/a | retain private_first; do not auto-publish upstream |
