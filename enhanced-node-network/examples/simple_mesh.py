"""Example starting a simple mesh node."""

import asyncio

from enhanced_network.core.mesh_node import MeshNode
from enhanced_network.coordination.resource_manager import ResourceManager
from enhanced_network.discovery.topology_manager import TopologyManager
from enhanced_network.utils import EventDispatcher

async def main():
    node = MeshNode({})
    resources = ResourceManager()
    topology = TopologyManager()
    dispatcher = EventDispatcher()

    dispatcher.register("node_started", lambda n: print(f"Node {n.node_id} started"))

    await node.start()
    await dispatcher.dispatch("node_started", node)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await node.stop()

if __name__ == "__main__":
    asyncio.run(main())
