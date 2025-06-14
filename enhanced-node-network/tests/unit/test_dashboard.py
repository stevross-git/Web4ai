import asyncio
import socket
import urllib.request

import pytest

pytest.importorskip("websockets")

from enhanced_network.core.mesh_node import MeshNode
from enhanced_network.web.dashboard import start_dashboard, stop_dashboard


@pytest.mark.asyncio
async def test_dashboard_reports_device():
    node = MeshNode({"listen_port": 9310})
    await node.start()
    server, _ = start_dashboard(node, port=0)
    host = socket.gethostname()
    url = f"http://localhost:{server.server_port}/"
    with urllib.request.urlopen(url) as resp:
        body = resp.read().decode()
    assert host in body
    stop_dashboard(server)
    await node.stop()
