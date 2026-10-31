# AlienVaultLabs corpus — Smith no-go

Pinned `AlienVault-Labs/AlienVaultLabs` at `347a57b31829b6f8e3280e0fd6a0ed49e5453c67`.
Gate renamed to `AlienVaultLabs_gate_decision.json` (stem matches `corpus=`).

## Decision: no-go (novelty collapse)

After admitting `yarasigs` (#422), file-map SHA256 comparison shows **1255/1463
(~85.8%) of probe YARA sites** are byte-identical to
`0day1day/yarasigs/signatures/AlienVault/*` (CommentCrew apt1, avdetect,
vmdetect, dbgdetect, sandboxdetect, APT_NGO_wuaclt, GeorBot).

Remaining novel YARA mass (~208 sites: Hangover/KINS/mask/leverage/urausy) is
not worth a separate WAVE pack on top of that overlap. The pinned compiler
measurement is **1447/1463 = 0.9891 encodable** (`decision: go`); this measures
compiler coverage and does not override Smith's novelty-based `no-go`. The
admission gate stayed `go`; Smith supersedes it — see
`properties/generated/AlienVaultLabs_smith_decision.json`.

Registered in `CORPUS_MANIFESTS` only to reproduce the measurement, and in
`SECURITY_TOOL_CORPORA` for private-first handling; intentionally excluded from
`WAVE_CORPORA`.

## Materialize

```bash
PIN=347a57b31829b6f8e3280e0fd6a0ed49e5453c67
SCRATCH="${TMPDIR:-/tmp}/AlienVaultLabs-$PIN"
if [ ! -d "$SCRATCH/.git" ]; then
  git clone --filter=blob:none https://github.com/AlienVault-Labs/AlienVaultLabs.git "$SCRATCH"
fi
git -C "$SCRATCH" fetch --depth 1 origin "$PIN"
git -C "$SCRATCH" checkout "$PIN"
ln -sfn "$SCRATCH" batch/corpora/AlienVaultLabs/rules
test "$(git -C "$SCRATCH" rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/AlienVaultLabs_gate_decision.json` (`go`);
Smith: `properties/generated/AlienVaultLabs_smith_decision.json` (`no-go`,
novelty collapse).

## Measure

```bash
python scripts/measure-corpus-fraction.py --corpus AlienVaultLabs --assert-determinism
```

This writes `properties/generated/AlienVaultLabs_encodable_fraction.json` and
`properties/generated/AlienVaultLabs-inventory.ndjson`. Do not run
`python -m regexproof.batch --corpus AlienVaultLabs`: the later Smith no-go
supersedes the admission gate.
