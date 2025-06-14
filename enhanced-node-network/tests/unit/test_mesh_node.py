import asyncio

import pytest

pytest.importorskip("websockets")

from enhanced_network.core.mesh_node import MeshNode


@pytest.mark.asyncio
async def test_start_and_stop_mesh_node():
    node = MeshNode({"listen_port": 9100})
    await node.start()
    assert node.running
    await node.stop()
    assert not node.running
