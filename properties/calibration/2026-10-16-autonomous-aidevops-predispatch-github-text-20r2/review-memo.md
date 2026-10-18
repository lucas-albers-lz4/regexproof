# Representative review: Aidevops pre-dispatch detector marker

- Cohort: `2026-09-12-calibration-20-r2`
- Repository pin: `marcusquinn/aidevops@8666b6c6c52472b5535aa295f2df593918152cb1`
- Site: `.agents/scripts/pre-dispatch-validator-helper.sh:1881:column-47`
- Regex: `detector=[a-z0-9_-]+` (`grep -oE`, ERE, search)
- Trust source: GitHub issue body returned by `gh api`; it is not treated as trusted policy.
- Destination: local `runtime-audit-rules/<detector>.sh`, sourced by `bash -c` with the generated filename inside single quotes.

The marker producer documents `<!-- aidevops:generator=runtime-audit detector=<id> -->`; it enumerates local `*.sh` rule files and emits the rule's ID. The pre-dispatch helper fetches the issue body, extracts the marker, extracts each `detector=` match, strips the fixed key, builds `rules_dir/DETECTOR_ID.sh`, and uses that path inside single quotes in a shell program. The local detector file is only reached when the marker resolves to the registered `runtime-audit` validator and the file exists.

## Contract boundary

The adopted property concerns each individual ERE match: the captured filename component contains no slash, dot, or single quote. The complete product replay must account for command substitution joining multiple matches with LF; LF remains inside the existing shell quotes. This supports a narrow path-component / shell-quote guarantee.

## Explicitly refuted or unproven claims

- The code does not enforce a detector allowlist: any matching local `*.sh` name that exists in the configured rules directory can be selected.
- This regex does not validate `RUNTIME_AUDIT_RULES_DIR`; that value is treated as trusted local configuration and lies outside the issue-controlled component contract.
- A single attribute match is not enforced; repeated matches can be joined with LF. The gate must exercise this case.
- The helper does not set `LC_COLLATE`. The formal mirror uses the recorded ERE/ASCII domain and the product gate must record its locale; this contract makes no universal claim for unusual locale range semantics.
- The pinned producer and test cover marker emission and detector behavior, but do not establish a demonstrated attacker exploit, confirmed impact, maintainer report, or fix.
- This is a component contract, not proof that the selected detector's verdict is correct or that every issue body with a marker reaches a validator.

The source-bound review evidence is generated from the exact clean checkout and includes the local source window and file digest.
