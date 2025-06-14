"""Manage nodes and connections in the network topology."""

class TopologyManager:
    def __init__(self):
        self.nodes = {}
        self.links = {}

    def add_node(self, node_id: str, info: dict | None = None) -> None:
        """Add a node to the topology."""
        self.nodes[node_id] = info or {}

    def remove_node(self, node_id: str) -> None:
        """Remove a node and any associated links."""
        self.nodes.pop(node_id, None)
        self.links.pop(node_id, None)
        for peers in self.links.values():
            peers.discard(node_id)

    def connect(self, node_a: str, node_b: str) -> None:
        """Create a bidirectional link between ``node_a`` and ``node_b``."""
        self.links.setdefault(node_a, set()).add(node_b)
        self.links.setdefault(node_b, set()).add(node_a)

    def neighbors(self, node_id: str) -> list[str]:
        """Return a list of neighbouring node identifiers."""
        return list(self.links.get(node_id, set()))
