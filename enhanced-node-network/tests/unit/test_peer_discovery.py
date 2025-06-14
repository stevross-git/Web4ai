import asyncio

import pytest

from enhanced_network.core.peer_discovery import PeerDiscovery


@pytest.mark.asyncio
async def test_discover_returns_list():
    pd = PeerDiscovery({})
    peers = await pd.discover()
    assert isinstance(peers, list)
