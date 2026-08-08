---
schema_version: "1"
pilot: gitleaks
admitted_pairs: 22
timeout_rate: 0.0
shape: 5
---

# gitleaks shape-5 rule_diff (encodable subset)

## bedrock-short-lived__aws-amazon-bedrock-api-key-short-lived

- regex_id: `8e85516ffe8da0722025a25b39228d52`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [32,52]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 3.715

### Pattern

- R1: `bedrock-api-key-[A-Za-z0-9]+`
- R2: `bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29t`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:232:0`
- rule_id: `aws-amazon-bedrock-api-key-short-lived`

### Witness

```json
null
```

### Ground-truth

N/A

## github-oauth-token__github-oauth

- regex_id: `dbcaaf86d1043b173b9e5b326b2db352`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [28,48]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.538

### Pattern

- R1: `gho_[A-Za-z0-9]{36}`
- R2: `gho_[0-9a-zA-Z]{36}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2154:0`
- rule_id: `github-oauth`

### Witness

```json
null
```

### Ground-truth

N/A

## github-pat-classic__github-pat

- regex_id: `744a90c843ea77c77259cc357d9ebec3`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [28,48]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 3.282

### Pattern

- R1: `ghp_[A-Za-z0-9]{36}`
- R2: `ghp_[0-9a-zA-Z]{36}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2161:0`
- rule_id: `github-pat`

### Witness

```json
null
```

### Ground-truth

N/A

## github-refresh-token__github-refresh-token

- regex_id: `2b51dbd04e455535b3e3a7885698af37`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [28,48]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.728

### Pattern

- R1: `ghr_[A-Za-z0-9]{36}`
- R2: `ghr_[0-9a-zA-Z]{36}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2172:0`
- rule_id: `github-refresh-token`

### Witness

```json
null
```

### Ground-truth

N/A

## github-user-to-server__github-app-token

- regex_id: `89f0b3e0fab988bce925ea5a4b3a4fd4`
- result: `sat`
- ground_truth_status: `PASS`
- domain: len(s) in [31,51]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 842.035

### Pattern

- R1: `ghu_[A-Za-z0-9]{36}`
- R2: `(?:ghu|ghs)_[0-9a-zA-Z]{36}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2133:0`
- rule_id: `github-app-token`

### Witness

```json
{"s": "<redacted len=40>"}
```

### Ground-truth

PASS

## gitlab-cicd-job__gitlab-cicd-job-token

- regex_id: `13d7917dbc832d53b469e54a1f3c266e`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [16,36]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.792

### Pattern

- R1: `glcbt-[A-Za-z0-9]{1,5}_[A-Za-z0-9_\-]{20}`
- R2: `glcbt-[0-9a-zA-Z]{1,5}_[0-9a-zA-Z_-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2179:0`
- rule_id: `gitlab-cicd-job-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-deploy-token__gitlab-deploy-token

- regex_id: `6f08a9109dc65ce1e408ae5c12ffb103`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [13,33]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.767

### Pattern

- R1: `gldt-[A-Za-z0-9_\-]{20}`
- R2: `gldt-[0-9a-zA-Z_\-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2186:0`
- rule_id: `gitlab-deploy-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-feature-flag__gitlab-feature-flag-client-token

- regex_id: `718d002ce737ed78d6351f7890e407a7`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [15,35]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.858

### Pattern

- R1: `glffct-[A-Za-z0-9_\-]{20}`
- R2: `glffct-[0-9a-zA-Z_\-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2193:0`
- rule_id: `gitlab-feature-flag-client-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-feed-token__gitlab-feed-token

- regex_id: `8c6cfc3514ae624e1f0cd92d6374dc71`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [13,33]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.757

### Pattern

- R1: `glft-[A-Za-z0-9_\-]{20}`
- R2: `glft-[0-9a-zA-Z_\-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2200:0`
- rule_id: `gitlab-feed-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-incoming-mail__gitlab-incoming-mail-token

- regex_id: `85af104ed1dbf180cf79d708d37eaa35`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [19,39]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.808

### Pattern

- R1: `glimt-[A-Za-z0-9_\-]{25}`
- R2: `glimt-[0-9a-zA-Z_\-]{25}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2207:0`
- rule_id: `gitlab-incoming-mail-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-pat-ascii__gitlab-pat

- regex_id: `a2d374ce5ef8ef50a688e12a31540aa5`
- result: `sat`
- ground_truth_status: `PASS`
- domain: len(s) in [14,34]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 223.82

### Pattern

- R1: `glpat-[A-Za-z0-9]{20}`
- R2: `glpat-[\w-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2228:0`
- rule_id: `gitlab-pat`

### Witness

```json
{"s": "<redacted len=26>"}
```

### Ground-truth

PASS

## gitlab-rrt__gitlab-rrt

- regex_id: `694d083f4f32aea337f83a26b08ef19e`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [17,37]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 1657.248

### Pattern

- R1: `GR1348941[A-Za-z0-9_\-]{20}`
- R2: `GR1348941[\w-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2249:0`
- rule_id: `gitlab-rrt`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-runner-token__gitlab-runner-authentication-token

- regex_id: `486592a2dfbca98126a7c5efb932dc5f`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [13,33]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.782

### Pattern

- R1: `glrt-[A-Za-z0-9_\-]{20}`
- R2: `glrt-[0-9a-zA-Z_\-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2256:0`
- rule_id: `gitlab-runner-authentication-token`

### Witness

```json
null
```

### Ground-truth

N/A

## gitlab-scim__gitlab-scim-token

- regex_id: `2d0e5c83421e5bd5f7a22dc21f695879`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [15,35]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.702

### Pattern

- R1: `glsoat-[A-Za-z0-9_\-]{20}`
- R2: `glsoat-[0-9a-zA-Z_\-]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2270:0`
- rule_id: `gitlab-scim-token`

### Witness

```json
null
```

### Ground-truth

N/A

## harness-pat__harness-api-key

- regex_id: `6b67e673a9f69748b251f191ef308699`
- result: `sat`
- ground_truth_status: `PASS`
- domain: len(s) in [63,83]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2367.433

### Pattern

- R1: `pat\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9]{24}\.[A-Za-z0-9]{20}`
- R2: `(?:pat|sat)\.[a-zA-Z0-9_-]{22}\.[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{20}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2320:0`
- rule_id: `harness-api-key`

### Witness

```json
{"s": "<redacted len=72>"}
```

### Ground-truth

PASS

## shopify-access-token__shopify-access-token

- regex_id: `bf7fb5c4e9415b03f859ac170411e807`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [26,46]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 0.952

### Pattern

- R1: `shpat_[A-Fa-f0-9]{32}`
- R2: `shpat_[a-fA-F0-9]{32}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2920:0`
- rule_id: `shopify-access-token`

### Witness

```json
null
```

### Ground-truth

N/A

## shopify-custom-token__shopify-custom-access-token

- regex_id: `948761e183cbc98566e248d6e2177e90`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [26,46]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 0.925

### Pattern

- R1: `shpca_[A-Fa-f0-9]{32}`
- R2: `shpca_[a-fA-F0-9]{32}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2927:0`
- rule_id: `shopify-custom-access-token`

### Witness

```json
null
```

### Ground-truth

N/A

## shopify-private-token__shopify-private-app-access-token

- regex_id: `65aa7c6dcf1442e6476a7f91b5097b16`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [26,46]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 0.946

### Pattern

- R1: `shppa_[A-Fa-f0-9]{32}`
- R2: `shppa_[a-fA-F0-9]{32}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2934:0`
- rule_id: `shopify-private-app-access-token`

### Witness

```json
null
```

### Ground-truth

N/A

## shopify-shared-secret__shopify-shared-secret

- regex_id: `c8f46ba46d0cb2415aee4bdbb8710283`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [26,46]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 0.922

### Pattern

- R1: `shpss_[A-Fa-f0-9]{32}`
- R2: `shpss_[a-fA-F0-9]{32}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2941:0`
- rule_id: `shopify-shared-secret`

### Witness

```json
null
```

### Ground-truth

N/A

## slack-bot-token-fixed__slack-bot-token

- regex_id: `926db647f68c3fc0a0a80945ce0366cd`
- result: `sat`
- ground_truth_status: `PASS`
- domain: len(s) in [14,34]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 157.652

### Pattern

- R1: `xoxb-[0-9]{10,13}-[0-9]{10,13}-[A-Za-z0-9]{24}`
- R2: `xoxb-[0-9]{10,13}-[0-9]{10,13}[a-zA-Z0-9-]*`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2973:0`
- rule_id: `slack-bot-token`

### Witness

```json
{"s": "<redacted len=26>"}
```

### Ground-truth

PASS

## slack-legacy-bot__slack-legacy-bot-token

- regex_id: `6c7d71cbe123726b4661e6df7fdcb455`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [20,40]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 2.714

### Pattern

- R1: `xoxb-[0-9]{8,14}-[A-Za-z0-9]{18,26}`
- R2: `xoxb-[0-9]{8,14}-[a-zA-Z0-9]{18,26}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:2997:0`
- rule_id: `slack-legacy-bot-token`

### Witness

```json
null
```

### Ground-truth

N/A

## twilio-api-key__twilio-api-key

- regex_id: `4bdb1d0ea564c5967d6e27fcf63c3733`
- result: `unsat`
- ground_truth_status: `N/A`
- domain: len(s) in [22,42]; dialect=re2; solver_call_kind=fullmatch; site_call_kind=search
- wall_ms: 0.907

### Pattern

- R1: `SK[A-Fa-f0-9]{32}`
- R2: `SK[0-9a-fA-F]{32}`

### Context

- site: `pilots/gitleaks/config/gitleaks.toml:3119:0`
- rule_id: `twilio-api-key`

### Witness

```json
null
```

### Ground-truth

N/A
