import asyncio

import pytest

from enhanced_network.coordination.resource_manager import ResourceManager


@pytest.mark.asyncio
async def test_basic_load_balancing():
    rm = ResourceManager()
    rm.allocate("task", 10)
    await asyncio.sleep(0)
    rm.release("task", 5)
    assert rm.usage("task") == 5
