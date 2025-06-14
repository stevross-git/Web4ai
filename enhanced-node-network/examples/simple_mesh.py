"""Example starting a simple mesh node."""

from enhanced_network.core.mesh_node import MeshNode
import asyncio

async def main():
    node = MeshNode({})
    await node.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await node.stop()

if __name__ == "__main__":
    asyncio.run(main())
