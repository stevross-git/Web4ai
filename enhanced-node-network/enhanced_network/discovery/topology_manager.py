"""Manage known nodes within the mesh network."""

from typing import Dict, Any, Optional


class TopologyManager:
    """Hold basic information about connected nodes."""

    def __init__(self) -> None:
        self.nodes: Dict[str, Dict[str, Any]] = {}

    def add_node(self, node_id: str, info: Dict[str, Any]) -> None:
        """Add or update information about ``node_id``."""
        self.nodes[node_id] = info

    def remove_node(self, node_id: str) -> None:
        """Remove ``node_id`` if present."""
        self.nodes.pop(node_id, None)

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Return info for ``node_id`` or ``None``."""
        return self.nodes.get(node_id)

    def all_nodes(self) -> Dict[str, Dict[str, Any]]:
        """Return snapshot of all known nodes."""
        return dict(self.nodes)

    def count(self) -> int:
        """Return number of known nodes."""
        return len(self.nodes)
