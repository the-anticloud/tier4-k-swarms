# Developer Cookbook — K_SWARMS
**Stack:** Python 3.11, asyncio, swarms 5.x, PAX 27B, ZeroMQ, AIOSS_FORMAT
**Domain:** Swarm intelligence: large-scale multi-agent coordination for Anticloud inference pipelines

## Create and run a swarm
```python
from k_swarms import AnticloudSwarm, PAXAgent

# Define agent template
def create_biosignal_agent(agent_id):
    return PAXAgent(
        name=f"biosignal_analyst_{agent_id}",
        pax_model="./pax-27b-q4.gguf",
        system_prompt="You are a biosignal analysis expert. Analyze EEG data and return structured JSON.",
        aioss_chain=f"./swarm_agent_{agent_id}.aioss"
    )

swarm = AnticloudSwarm(
    agents=[create_biosignal_agent(i) for i in range(8)],
    coordinator_aioss="./swarm_coordinator.aioss"
)

# Parallel batch analysis
eeg_files = ["./eeg_001.edf", "./eeg_002.edf", ..., "./eeg_100.edf"]
results = swarm.run_parallel(task="analyze_eeg", inputs=eeg_files)
print(f"Processed {len(results)} EEG files")
print(f"Coordinator chain: {swarm.chain_hash}")
```

## Sequential swarm pipeline
```python
pipeline_result = swarm.run_sequential([
    ("retrieve", {"query": "HIPAA biosignal protocols"}),
    ("analyze", {"domain": "clinical"}),
    ("report", {"format": "compliance_summary"})
])
```

## Monitor swarm health
```python
status = swarm.status()
for agent in status.agents:
    print(f"{agent.name}: tasks={agent.completed_tasks}, queue={agent.queue_depth}")
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
