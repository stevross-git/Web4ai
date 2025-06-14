"""Bridge between mesh network and an Enhanced Node server."""
import requests
from typing import Dict, Any
from ..core.mesh_node import MeshNode, NetworkMessage

class EnhancedNodeBridge:
    def __init__(self, mesh_node: MeshNode, config: Dict[str, Any]):
        self.mesh_node = mesh_node
        self.enhanced_node_url = config.get('url', 'http://localhost:5000')
        self.mesh_node.register_message_handler('task_response', self._handle_task_response)

    async def distribute_task(self, task: Dict[str, Any]):
        await self.mesh_node.broadcast_message('task_request', task)

    async def _handle_task_response(self, message: NetworkMessage):
        requests.post(f"{self.enhanced_node_url}/task/result", json=message.payload)
