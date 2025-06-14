"""Example starting a simple mesh node."""

import asyncio
from enhanced_network.core.mesh_node import MeshNode

async def main():
    node = MeshNode({"listen_port": 9001})
    await node.start()
    print(f"Mesh node started with id {node.node_id} on port {node.listen_port}")
    try:
        while True:
            await asyncio.sleep(5)
            status = node.get_network_status()
            print(f"Known peers: {status['known_peers']} connected: {status['connected_peers']}")
    except KeyboardInterrupt:
        await node.stop()

if __name__ == "__main__":
    asyncio.run(main())
