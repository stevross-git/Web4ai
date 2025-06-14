import asyncio

import pytest

from enhanced_network.coordination.resource_manager import ResourceManager
from enhanced_network.discovery.topology_manager import TopologyManager
from enhanced_network.utils import EventDispatcher


def test_resource_manager_allocate_release():
    rm = ResourceManager()
    rm.allocate("cpu", 2)
    assert rm.usage("cpu") == 2
    rm.release("cpu", 1)
    assert rm.usage("cpu") == 1


def test_topology_manager_connections():
    tm = TopologyManager()
    tm.add_node("a")
    tm.add_node("b")
    tm.connect("a", "b")
    assert "b" in tm.neighbors("a")
    assert "a" in tm.neighbors("b")


@pytest.mark.asyncio
async def test_event_dispatcher():
    dispatcher = EventDispatcher()
    results = []

    async def handler(x):
        results.append(x)

    dispatcher.register("test", handler)
    await dispatcher.dispatch("test", 5)
    assert results == [5]
