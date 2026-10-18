# Everclaw unresolved Gitlink follow-up

**Root pin:** `profbernardoj/everclaw-community-branches@7ea3b445ee7d2ef8004d5ee77dab7544e1b8ef88`
**Status:** both remaining Gitlinks stay unresolved

The public [`profbernardoj/everclaw-fork` repository](https://github.com/profbernardoj/everclaw-fork) exists, but GitHub's exact-commit endpoint returns HTTP 422 for the root Gitlink commit `603157608c740e365f705488a33bec7080843525`; exact-object `git fetch` returns `not our ref`, and public commit search returns zero results. This is a checked candidate, not an established source mapping.

For `archive/misc/everclaw-template` at `f161a75ab9ce3460e85ccbbf3042b0330972979a`, public exact-commit search returns zero results, no public `profbernardoj/everclaw-template` repository appears in the owner's repository inventory, and exact-object fetches from the checked related public repositories did not find the commit. The original URL remains unknown.

The exact root pin has no `.gitmodules` file. The checked search methods can miss deleted, private, or unindexed repositories, so neither path is remapped by guess. This follow-up adds no verified child checkout, regex rows, source review, contracts, product questions, or P2 yield. See [`followup.json`](followup.json) for the machine-readable evidence and limitations.
