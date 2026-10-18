# Everclaw pinned submodule metadata audit

**Root repository:** `profbernardoj/everclaw-community-branches`
**Pinned commit:** `7ea3b445ee7d2ef8004d5ee77dab7544e1b8ef88`
**Parent inventory:** [P2 source inventory v5](../2026-10-16-p2-source-inventory-v5/README.md)

## Finding

The exact root pin has no `.gitmodules` file. Git reports
`fatal: path '.gitmodules' does not exist in 'HEAD'`; there is no file to parse
or repair. The root checkout's origin does not by itself name the child
repositories.

A follow-up by exact gitlink object ID recovered public source locations for
four of the six child commits. The GitHub commit endpoint returned each exact
gitlink SHA and its tree ID. This identifies a repository that serves the
pinned commit object; it does not recover an original configured remote (the
root commit has no `.gitmodules`). The remaining two commit IDs have no public
exact-commit search result and remain unresolved.

| Gitlink path | Commit | Verified source repository | Status |
| --- | --- | --- | --- |
| `archive/misc/everclaw` | `1e2ba9c2baa8dd41a8459f8257ab2578470b0f77` | [profbernardoj/morpheus-agent](https://github.com/profbernardoj/morpheus-agent/commit/1e2ba9c2baa8dd41a8459f8257ab2578470b0f77) | exact commit and tree verified |
| `archive/misc/everclaw-fork` | `603157608c740e365f705488a33bec7080843525` | — | unresolved |
| `archive/misc/everclaw-template` | `f161a75ab9ce3460e85ccbbf3042b0330972979a` | — | unresolved |
| `archive/misc/installopenclaw.xyz` | `798f7285dbd2b77be772326f53f9853b6730acb0` | [profbernardoj/installopenclaw.xyz](https://github.com/profbernardoj/installopenclaw.xyz/commit/798f7285dbd2b77be772326f53f9853b6730acb0) | exact commit and tree verified |
| `skills/clawdstrike` | `e87e752589ad460c17d434ff56bcac4762a117c3` | [cantinaxyz/clawdstrike-skill](https://github.com/cantinaxyz/clawdstrike-skill/commit/e87e752589ad460c17d434ff56bcac4762a117c3) | exact commit and tree verified |
| `skills/everclaw` | `a6f294ee0ba5aab91d8b0f5b798dda160a8a0279` | [profbernardoj/morpheus-agent](https://github.com/profbernardoj/morpheus-agent/commit/a6f294ee0ba5aab91d8b0f5b798dda160a8a0279) | exact commit and tree verified |

The structured evidence, including tree object IDs, is in
[`gitlinks.json`](gitlinks.json). The root `git ls-tree -r` output was checked
against all six path/SHA pairs. Exact commit matches were verified through the
public GitHub commit API. Four exact child trees were fetched and scanned in an
additive record; see the
[submodule inventory addendum](../2026-10-16-p2-everclaw-submodule-inventory-v1/README.md).

## Inventory effect and next action

The frozen v5 inventory is unchanged: its 423 Everclaw root sites remain, and
the repository is still `incomplete_submodules`. The additive scan records
8,361 raw sites from two child snapshots, but both snapshots omit 15 nested
gitlinks; two other verified children contain no registered ECMA sites, and
two root Gitlinks remain unresolved. None of the 8,361 rows has been reviewed
or added to the v5 cohort total. Keep every nested and unresolved source
visible as an exclusion; do not treat these rows as unique product yield.
