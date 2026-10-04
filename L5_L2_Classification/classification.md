# L5 Narrow / L2 General Classification — K_SWARMS
**Platform:** Anticloud | **Tier:** TIER_4_INFERENCE_AGENTS | **PAX:** 27B
**IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg | **License:** Apache-2.0

## L5 Narrow
K_SWARMS integrates the Swarms framework with Anticloud's PAX harness for large-scale agent coordination. Narrow scope: Anticloud domain swarm tasks — parallel document analysis, distributed AIOSS chain verification, batch compliance auditing. Not a general-purpose swarm platform.

## L2 General
L2 General: K_SWARMS scales any TIER_4 agent task across available compute. Parallel TIER_7 biosignal batch analysis and parallel TIER_6 security eval both use K_SWARMS for horizontal scaling.

## PAX 27B Integration
PAX 27B runs as the shared inference backend for all swarm agents. K_SWARMS manages request queuing to PAX, ensuring GPU memory is not exceeded while maximizing throughput across concurrent agent tasks.

## AIOSS Audit Chain
Every swarm execution (task graph hash + agent assignments + completion hashes + aggregate result hash) is chained: H_n = SHA3-256(H_{n-1} || entry_hash_n || timestamp_n).
Offline-verifiable, tamper-evident, zero cloud dependency.

## Regulatory / Compliance
NIST AI RMF 1.0 (multi-agent accountability). ISO/IEC 42001 (AI system governance).
