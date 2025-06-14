"""Example integration with an enhanced node server."""

from enhanced_network.core.mesh_node import MeshNode
from enhanced_network.integration.enhanced_node_bridge import EnhancedNodeBridge

node = MeshNode({})
bridge = EnhancedNodeBridge(node, {"url": "http://localhost:5000"})

import asyncio


async def main() -> None:
    await bridge.distribute_task({"task": "demo"})
    print("Sent demo task to the mesh")


if __name__ == "__main__":
    asyncio.run(main())
