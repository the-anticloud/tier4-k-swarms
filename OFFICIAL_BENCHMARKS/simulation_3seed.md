# 3-Seed Simulation — K_SWARMS

**Seeds:** `81121` · `12458` · `46657`

**Seed method:** `sha256("K_SWARMS")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `K_SWARMS`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 6.8903 | 0.1587 | ±0.3111 |
| throughput_tokens_per_sec | 237.1 | 31.7409 | ±62.2122 |
| p50_latency_ms | 45.9867 | 4.5509 | ±8.9198 |
| p99_latency_ms | 107.7133 | 11.1548 | ±21.8634 |
| ttft_ms | 30.25 | 1.7439 | ±3.418 |
| mmlu_proxy | 0.7566 | 0.0261 | ±0.0512 |
| hellaswag_proxy | 0.7779 | 0.0328 | ±0.0643 |
| truthfulqa_proxy | 0.591 | 0.0375 | ±0.0735 |
| arc_proxy | 0.6903 | 0.0318 | ±0.0623 |
| complexity_cyclomatic | 4.67 | 0.6163 | ±1.2079 |
| maintainability_index | 69.7533 | 4.337 | ±8.5005 |
| security_issues_high | 1.3333 | 0.9428 | ±1.8479 |
| dependency_freshness_pct | 76.0 | 2.9631 | ±5.8077 |
| test_coverage_pct | 50.8333 | 10.585 | ±20.7466 |
| doc_coverage_pct | 65.5333 | 8.5986 | ±16.8533 |
| memory_mb | 50.0 | 0.0 | ±0.0 |
| gpu_util_pct | 70.1333 | 6.2941 | ±12.3364 |
| openssf_score | 6.0933 | 0.2963 | ±0.5807 |
| eu_ai_act_compliance_pct | 80.9333 | 1.1898 | ±2.332 |
| slsa_level | 1.3333 | 0.4714 | ±0.9239 |

## Per-Seed Raw Results

| Metric | Seed 81121 | Seed 12458 | Seed 46657 |
|--------|------------|------------|------------|
| trl_score | 7.114 | 6.794 | 6.763 |
| throughput_tokens_per_sec | 205.2 | 225.7 | 280.4 |
| p50_latency_ms | 40.3 | 51.44 | 46.22 |
| p99_latency_ms | 123.38 | 101.48 | 98.28 |
| ttft_ms | 28.5 | 32.63 | 29.62 |
| mmlu_proxy | 0.7196 | 0.775 | 0.7751 |
| hellaswag_proxy | 0.8058 | 0.7961 | 0.7319 |
| truthfulqa_proxy | 0.541 | 0.6005 | 0.6314 |
| arc_proxy | 0.6497 | 0.6937 | 0.7274 |
| complexity_cyclomatic | 3.8 | 5.06 | 5.15 |
| maintainability_index | 72.79 | 63.62 | 72.85 |
| security_issues_high | 2 | 2 | 0 |
| dependency_freshness_pct | 73.2 | 80.1 | 74.7 |
| test_coverage_pct | 65.8 | 43.1 | 43.6 |
| doc_coverage_pct | 61.9 | 57.3 | 77.4 |
| memory_mb | 50 | 50 | 50 |
| gpu_util_pct | 73.6 | 75.5 | 61.3 |
| openssf_score | 6.04 | 5.76 | 6.48 |
| eu_ai_act_compliance_pct | 79.4 | 82.3 | 81.1 |
| slsa_level | 2 | 1 | 1 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._