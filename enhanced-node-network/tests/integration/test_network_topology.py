import asyncio

import pytest

from enhanced_network.discovery.topology_manager import TopologyManager


@pytest.mark.asyncio
async def test_build_topology():
    tm = TopologyManager()
    tm.add_node("n1")
    tm.add_node("n2")
    tm.connect("n1", "n2")
    assert "n2" in tm.neighbors("n1")
