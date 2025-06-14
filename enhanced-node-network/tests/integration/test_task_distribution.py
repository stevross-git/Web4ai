import asyncio

import pytest

from enhanced_network.coordination.resource_manager import ResourceManager


@pytest.mark.asyncio
async def test_resource_allocation_flow():
    rm = ResourceManager()
    rm.allocate("gpu", 4)
    await asyncio.sleep(0)
    rm.release("gpu", 2)
    assert rm.usage("gpu") == 2
