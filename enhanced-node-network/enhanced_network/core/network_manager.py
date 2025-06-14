"""High level manager to control a :class:`MeshNode`."""
from typing import Dict, Any
from .mesh_node import MeshNode

class NetworkManager:
    def __init__(self, config: Dict[str, Any]):
        self.mesh_node = MeshNode(config)

    async def connect_to_bootstrap(self, peers: list[str]):
        for peer in peers:
            await self.mesh_node.connect_to_peer(peer)

    async def start(self):
        await self.mesh_node.start()

    async def stop(self):
        await self.mesh_node.stop()

    async def broadcast(self, message_type: str, payload: Dict[str, Any]):
        await self.mesh_node.broadcast_message(message_type, payload)
