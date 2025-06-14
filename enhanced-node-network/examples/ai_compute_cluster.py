"""Example AI compute cluster starter."""

import asyncio
from enhanced_network.core.mesh_node import MeshNode


async def main() -> None:
    node = MeshNode({})
    await node.start()
    print(f"Compute node {node.node_id} running on port {node.listen_port}")
    await node.stop()


if __name__ == "__main__":
    asyncio.run(main())
