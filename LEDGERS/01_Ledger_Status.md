# Ledger Status

**Project:** `K_SWARMS`  
**Tier:** TIER_4_INFERENCE_AGENTS  
**Identity:** Upstream `kyegomez/swarms` @ `5185db33949e` (Apache-2.0)

## Chain state

| Fact | Value |
| --- | --- |
| Upstream | `kyegomez/swarms` |
| Commit | `5185db33949e17ffe3dbcf80f129b1866834ab92` |
| Upstream licence | Apache-2.0 |
| Licence class | permissive |
| Clone size | 55.26 MB |
| Ledger | 0 blocks, chain verified |
| Current TRL | NOT YET MEASURED |
| Post-optimisation TRL | NOT YET MEASURED |
| II budget cap | 1000.0 IIU |
| Verified upstream edits | 1 |

- Blocks: **0**
- Head digest: `None`
- Chain verification: **verified**

## Independent verification

The chain is verifiable without trusting this project's tooling:

```
anticloud ledger verify
anticloud ledger export > ledger.jsonl
```

Each block carries the previous block's digest, so removing or reordering an
entry invalidates every block after it. That property is the reason the
ledger can stand in for a claim of what happened.
