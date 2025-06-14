"""Very small round-robin load balancer implementation."""

from __future__ import annotations

from typing import List


class RoundRobinBalancer:
    """Cycle through a list of node identifiers."""

    def __init__(self, nodes: List[str] | None = None):
        self.nodes = nodes or []
        self._index = 0

    def add_node(self, node_id: str) -> None:
        self.nodes.append(node_id)

    def remove_node(self, node_id: str) -> None:
        if node_id in self.nodes:
            self.nodes.remove(node_id)
            self._index %= max(len(self.nodes), 1)

    def choose(self) -> str | None:
        """Return the next node identifier to use."""

        if not self.nodes:
            return None
        node = self.nodes[self._index]
        self._index = (self._index + 1) % len(self.nodes)
        return node
