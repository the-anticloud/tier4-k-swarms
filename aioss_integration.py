"""
K-SWARMS Anticloud Integration — Multi-Agent Swarm with AIOSS Per-Agent Ledger

Every agent in the swarm gets its own AIOSS ledger. The swarm coordinator
writes to a shared meta-ledger. This creates a complete audit trail of:
- Which agent received which task
- What each agent produced
- Inter-agent communication hashes
- Total swarm cost (always 0 for local inference)

Usage:
    from aioss_integration import AnticloudSwarm, SwarmAgent

    swarm = AnticloudSwarm(
        agents=[
            SwarmAgent("planner", "You plan tasks"),
            SwarmAgent("coder", "You write code"),
            SwarmAgent("reviewer", "You review code"),
        ],
        model_endpoint="http://localhost:11434/v1",
        model_name="pax-one-27b",
        shared_ledger_path="./swarm_ledger.aioss",
    )
    result = swarm.run("Build a REST API for user management")

No frontier API keys.
"""

from __future__ import annotations
import hashlib
import json
import subprocess
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


def _sha3(text: str) -> str:
    return hashlib.sha3_256(text.encode()).hexdigest()


@dataclass
class AgentMessage:
    sender: str
    recipient: str
    content: str
    message_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    timestamp: float = field(default_factory=time.time)

    @property
    def content_hash(self) -> str:
        return _sha3(self.content)


class AIossLedger:
    def __init__(self, ledger_path: str, aioss_bin: str = "aioss"):
        self.path = Path(ledger_path)
        self.bin = aioss_bin

        if not self.path.exists():
            subprocess.run(
                [aioss_bin, "init", str(self.path.parent), "--user", "swarm"],
                capture_output=True,
            )

    def append(self, entry_type: str, actor: str, content: dict):
        subprocess.run(
            [
                self.bin, "append", str(self.path),
                "--type", entry_type[:19],
                "--actor", actor[:15],
                "--content", json.dumps(content),
            ],
            capture_output=True,
        )

    def verify(self) -> bool:
        r = subprocess.run([self.bin, "verify", str(self.path)], capture_output=True)
        return r.returncode == 0


@dataclass
class SwarmAgent:
    name: str
    system_prompt: str
    ledger: Optional[AIossLedger] = None

    def bind_ledger(self, ledger_path: str):
        self.ledger = AIossLedger(ledger_path)

    def run(self, task: str, llm, context: str = "") -> str:
        """Execute a task and log to this agent's AIOSS ledger."""
        start = time.perf_counter()

        prompt = f"{self.system_prompt}\n\nContext: {context}\n\nTask: {task}\n\nResponse:"
        response = llm.complete(prompt)
        elapsed = (time.perf_counter() - start) * 1000

        if self.ledger:
            self.ledger.append(
                entry_type="agent_task",
                actor=self.name,
                content={
                    "task_hash": _sha3(task),
                    "response_hash": _sha3(response),
                    "tokens_in": len(prompt.split()),
                    "tokens_out": len(response.split()),
                    "wall_time_ms": round(elapsed, 1),
                    "cost_if_cloud_microcents": 0,
                },
            )

        return response


class LocalLLM:
    """Minimal OpenAI-compat client for local models."""

    def __init__(self, endpoint: str = "http://localhost:11434/v1", model: str = "llama3.2"):
        self.endpoint = endpoint
        self.model = model

    def complete(self, prompt: str) -> str:
        import urllib.request, urllib.error

        payload = json.dumps({
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1024,
            "temperature": 0.0,
        }).encode()

        try:
            req = urllib.request.Request(
                self.endpoint + "/chat/completions",
                data=payload,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[LLM unavailable: {e}]"


class AnticloudSwarm:
    """
    Multi-agent swarm with AIOSS audit trail.

    Each agent writes to its own ledger. The coordinator writes to a shared
    meta-ledger linking all agent interactions into one verifiable chain.
    """

    def __init__(
        self,
        agents: list[SwarmAgent],
        model_endpoint: str = "http://localhost:11434/v1",
        model_name: str = "llama3.2",
        shared_ledger_path: str = "./swarm_ledger.aioss",
        agent_ledger_dir: str = "./swarm_agent_ledgers",
    ):
        self.agents = {a.name: a for a in agents}
        self.llm = LocalLLM(endpoint=model_endpoint, model=model_name)
        self.shared_ledger = AIossLedger(shared_ledger_path)

        # Give each agent its own ledger
        ledger_dir = Path(agent_ledger_dir)
        ledger_dir.mkdir(parents=True, exist_ok=True)
        for agent in agents:
            agent.bind_ledger(str(ledger_dir / f"{agent.name}_ledger.aioss"))

        self.message_history: list[AgentMessage] = []

    def send(self, sender: str, recipient: str, content: str) -> AgentMessage:
        msg = AgentMessage(sender=sender, recipient=recipient, content=content)
        self.message_history.append(msg)

        self.shared_ledger.append(
            entry_type="agent_message",
            actor=sender[:15],
            content={
                "message_id": msg.message_id,
                "from": sender,
                "to": recipient,
                "content_hash": msg.content_hash,
                "timestamp": msg.timestamp,
            },
        )

        return msg

    def run(self, task: str) -> dict:
        """
        Run the swarm on a task. Agents execute sequentially by default.
        Returns final output + full audit trail.
        """
        swarm_id = str(uuid.uuid4())[:8]
        start = time.time()

        self.shared_ledger.append(
            entry_type="swarm_start",
            actor="coordinator",
            content={
                "swarm_id": swarm_id,
                "task_hash": _sha3(task),
                "agent_count": len(self.agents),
                "agents": list(self.agents.keys()),
            },
        )

        outputs = {}
        context = ""

        for agent_name, agent in self.agents.items():
            msg = self.send("coordinator", agent_name, task)

            response = agent.run(
                task=task,
                llm=self.llm,
                context=context,
            )

            self.send(agent_name, "coordinator", response)
            outputs[agent_name] = response
            context = f"Previous {agent_name} output: {response[:500]}"

        elapsed = time.time() - start
        final_output = list(outputs.values())[-1] if outputs else ""

        self.shared_ledger.append(
            entry_type="swarm_complete",
            actor="coordinator",
            content={
                "swarm_id": swarm_id,
                "total_agents": len(self.agents),
                "total_messages": len(self.message_history),
                "output_hash": _sha3(final_output),
                "wall_time_ms": round(elapsed * 1000, 1),
                "cost_if_cloud_microcents": 0,
            },
        )

        return {
            "swarm_id": swarm_id,
            "task": task,
            "agent_outputs": outputs,
            "final_output": final_output,
            "messages": len(self.message_history),
            "shared_chain_valid": self.shared_ledger.verify(),
        }


# Example
if __name__ == "__main__":
    swarm = AnticloudSwarm(
        agents=[
            SwarmAgent("planner", "You break down tasks into subtasks. Be concise."),
            SwarmAgent("coder", "You write Python code. Use local models, no API keys."),
            SwarmAgent("reviewer", "You review code for security issues. Be specific."),
        ],
        model_endpoint="http://localhost:11434/v1",
        model_name="llama3.2",
        shared_ledger_path="./swarm_test.aioss",
    )

    result = swarm.run("Create a function that validates email addresses")
    print(f"Final output: {result['final_output'][:200]}")
    print(f"Messages exchanged: {result['messages']}")
    print(f"Chain valid: {result['shared_chain_valid']}")
