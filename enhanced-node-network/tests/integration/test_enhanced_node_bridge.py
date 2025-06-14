import asyncio

import pytest

pytest.importorskip("websockets")

from enhanced_network.core.mesh_node import MeshNode


@pytest.mark.asyncio
async def test_two_nodes_can_connect():
    node1 = MeshNode({"listen_port": 9202})
    node2 = MeshNode({"listen_port": 9203})
    await asyncio.gather(node1.start(), node2.start())
    peer_id = await node1.connect_to_peer(f"localhost:{node2.listen_port}")
    assert peer_id in node1.connections
    await asyncio.gather(node1.stop(), node2.stop())
