"""Example blockchain network starter."""

import asyncio
from enhanced_network.core.mesh_node import MeshNode


async def main() -> None:
    node = MeshNode({"node_type": "blockchain"})
    await node.start()
    print(f"Blockchain node {node.node_id} listening on {node.listen_port}")
    await node.stop()


if __name__ == "__main__":
    asyncio.run(main())
