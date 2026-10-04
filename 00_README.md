# Anticloud × SWARMS
> Multi-agent coordination under cryptographic audit — no cloud required.

**Part of:** Inference Agents · Anticloud FZ LLE · 0-1.gg
**Upstream:** kyegomez/swarms (MIT)
**License:** Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0
**IP:** USPTO pending · Lois-Kleinner Alpasan · 2026

Coordinate 100s of agents on complex tasks. We add cryptographic proof of task execution for enterprise compliance.

```python
from swarms_anticloud import SwarmOrchestrator

swarm = SwarmOrchestrator(
    agents=[math_agent, code_agent, search_agent],
    ledger_path="./pax_ledger.aioss",
)

result = swarm.execute_task("Solve this problem and verify the answer")
# Every agent action: hashed, signed, appended to ledger
```

**Plays well with:** K-PAXSCHED, L-TASKWEAVER, K-RAVEN (harness of harnesses)
