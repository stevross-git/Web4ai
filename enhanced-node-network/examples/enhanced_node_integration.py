"""Demonstration of integrating a mesh node with an external server."""

import asyncio
from enhanced_network.core.mesh_node import MeshNode
from enhanced_network.integration.enhanced_node_bridge import EnhancedNodeBridge


async def main():
    node = MeshNode({"listen_port": 9300})
    bridge = EnhancedNodeBridge(node, {"url": "http://localhost:5000"})
    await node.start()
    await bridge.start()
    print("Mesh node integrated with enhanced server. Press Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        await bridge.stop()
        await node.stop()


if __name__ == "__main__":
    asyncio.run(main())
