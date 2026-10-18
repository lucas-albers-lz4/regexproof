# Everclaw verified Gitlink inventory addendum v1

**Root pin:** `profbernardoj/everclaw-community-branches@7ea3b445ee7d2ef8004d5ee77dab7544e1b8ef88`
**Parent inventory:** [v5](../2026-10-16-p2-source-inventory-v5/README.md)
**Gitlink mapping evidence:** [audit](../2026-10-16-p2-everclaw-submodule-audit/README.md)

## Result

Four Gitlink commit objects were fetched by their exact SHA from the source
repositories recorded in the audit. Local `HEAD`, tree ID, origin, and clean
checkout state were checked before extraction. The same registered ECMA
extractor, hidden-path behavior, extensions, size cap, and symlink containment
check used by inventory v5 were applied.

| Gitlink path | Site rows | Result |
| --- | ---: | --- |
| `archive/misc/everclaw` | 4,184 | incomplete: 15 nested Gitlinks excluded |
| `archive/misc/installopenclaw.xyz` | 0 | complete under registered ECMA extractor |
| `skills/clawdstrike` | 0 | complete under registered ECMA extractor |
| `skills/everclaw` | 4,177 | incomplete: 15 nested Gitlinks excluded |

The addendum contains **8,361 raw site rows**. The two populated Gitlinks point
to different exact commits in `profbernardoj/morpheus-agent`; their source
sets may overlap and must not be treated as 8,361 unique regexes or as new
product yield. The 30 nested Gitlink references across those two snapshots
were not materialized. Two root Gitlinks also remain unresolved. The v5
aggregate is unchanged at 21,956 rows and still marks Everclaw incomplete.

All rows remain unreviewed source sightings. The addendum records zero
contracts, questions, solver outcomes, or security boundaries. See
[`inventory.json`](inventory.json) for commit/tree IDs, per-tree completeness,
extractor source fingerprints, and the sites digest; raw rows are in
[`sites.ndjson`](sites.ndjson).

## Reproduce

Fetch the four exact child commits listed in
[`gitlinks.json`](../2026-10-16-p2-everclaw-submodule-audit/gitlinks.json),
check out each commit detached, and pass the clean checkout paths to:

```sh
.venv/bin/python scripts/freeze-p2-gitlink-inventory.py \
  --parent-inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --gitlink-audit properties/calibration/2026-10-16-p2-everclaw-submodule-audit/gitlinks.json \
  --checkout archive/misc/everclaw=CHECKOUT_PATH \
  --checkout archive/misc/installopenclaw.xyz=CHECKOUT_PATH \
  --checkout skills/clawdstrike=CHECKOUT_PATH \
  --checkout skills/everclaw=CHECKOUT_PATH \
  --out-dir properties/calibration/2026-10-16-p2-everclaw-submodule-inventory-v1
```

The command exits nonzero while any root Gitlink is unresolved. It writes the
available rows and keeps their nested and unresolved exclusions explicit.
