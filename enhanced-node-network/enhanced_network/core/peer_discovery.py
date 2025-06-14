"""Utility for locating other nodes on the network."""
from typing import Dict, Any

class PeerDiscovery:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    async def discover(self) -> list[str]:
        """Return peers from the configured ``bootstrap_nodes`` list."""
        return list(self.config.get("bootstrap_nodes", []))
