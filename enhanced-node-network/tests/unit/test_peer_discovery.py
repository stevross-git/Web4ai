import pytest
from enhanced_network.core.peer_discovery import PeerDiscovery


@pytest.mark.asyncio
async def test_discover_bootstrap():
    pd = PeerDiscovery({"bootstrap_nodes": ["127.0.0.1:9000"]})
    peers = await pd.discover()
    assert "127.0.0.1:9000" in peers
