import asyncio
import time

import pytest

pytest.importorskip("websockets")
import websockets


@pytest.mark.asyncio
async def test_local_websocket_latency():
    async def echo(ws, path):
        async for msg in ws:
            await ws.send(msg)

    server = await websockets.serve(echo, "localhost", 9301)
    async with websockets.connect("ws://localhost:9301") as ws:
        start = time.monotonic()
        await ws.send("ping")
        await ws.recv()
        latency = time.monotonic() - start
    server.close()
    await server.wait_closed()
    assert latency < 1
