"""Thin wrapper around :class:`MeshNode` used by the example scripts."""
from typing import Dict, Any
from .mesh_node import MeshNode

class NetworkManager:
    def __init__(self, config: Dict[str, Any]):
        self.mesh_node = MeshNode(config)

    async def start(self):
        await self.mesh_node.start()

    async def stop(self):
        await self.mesh_node.stop()
