# AlienVaultLabs corpus — Smith no-go

Pinned `AlienVault-Labs/AlienVaultLabs` at `347a57b31829b6f8e3280e0fd6a0ed49e5453c67`.
Gate renamed to `AlienVaultLabs_gate_decision.json` (stem matches `corpus=`).

## Decision: no-go (novelty collapse)

After admitting `yarasigs` (#422), file-map SHA256 comparison shows **1255/1463
(~85.8%) of probe YARA sites** are byte-identical to
`0day1day/yarasigs/signatures/AlienVault/*` (CommentCrew apt1, avdetect,
vmdetect, dbgdetect, sandboxdetect, APT_NGO_wuaclt, GeorBot).

Remaining novel YARA mass (~208 sites: Hangover/KINS/mask/leverage/urausy) is
not worth a separate WAVE pack on top of that overlap. Admission gate stayed
`go`; Smith supersedes with `no-go` — see
`properties/generated/AlienVaultLabs_smith_decision.json`.

Not added to `WAVE_CORPORA` / `SECURITY_TOOL_CORPORA` / `CORPUS_MANIFESTS`.
