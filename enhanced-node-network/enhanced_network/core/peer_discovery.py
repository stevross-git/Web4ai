"""Simple bootstrap-based peer discovery."""
from typing import Dict, Any

class PeerDiscovery:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    async def discover(self) -> list[str]:
        """Return peers from the ``bootstrap_nodes`` config key."""
        nodes = self.config.get("bootstrap_nodes", [])
        return list(nodes)
