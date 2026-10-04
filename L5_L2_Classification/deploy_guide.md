# Deploy Guide — K_SWARMS
**Tier:** TIER_4_INFERENCE_AGENTS | **Stack:** Python 3.11, asyncio, swarms 5.x, PAX 27B, ZeroMQ, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, swarms 5.x, asyncio (stdlib), pyzmq 25.0+, PAX 27B weights.

## Environment
16GB RAM minimum. GPU shared across all swarm agents via K_NANOVLLM continuous batching. ZeroMQ for inter-agent messaging.

## AIOSS Integration
```bash
aioss init --module K_SWARMS --output ./k_swarms.aioss
aioss append --chain ./k_swarms.aioss --payload ./output.bin --module K_SWARMS
aioss verify --chain ./k_swarms.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="K_SWARMS",
    aioss_chain="./K_SWARMS.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./K_SWARMS.aioss --verbose
python -m K_SWARMS.tests.smoke
```
