"""Distributes work items across available nodes."""

from __future__ import annotations

from typing import Dict, Any

from .load_balancer import RoundRobinBalancer


class TaskDistributor:
    """Very small wrapper that assigns tasks using a balancer."""

    def __init__(self, balancer: RoundRobinBalancer | None = None):
        self.balancer = balancer or RoundRobinBalancer()

    def register_node(self, node_id: str) -> None:
        self.balancer.add_node(node_id)

    def unregister_node(self, node_id: str) -> None:
        self.balancer.remove_node(node_id)

    def next_node(self) -> str | None:
        return self.balancer.choose()

    async def distribute(self, task: Dict[str, Any], send_func) -> None:
        """Distribute ``task`` using ``send_func`` which sends to a node id."""

        node_id = self.next_node()
        if node_id:
            await send_func(node_id, task)
