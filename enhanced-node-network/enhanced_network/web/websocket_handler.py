"""Simple WebSocket echo handler for examples."""

import asyncio


async def handle_websocket(websocket, path):
    """Echo all received messages back to the client."""
    await websocket.send("welcome")
    try:
        async for message in websocket:
            await websocket.send(message)
    except asyncio.CancelledError:
        pass

async def handle_websocket(websocket, path):
    await websocket.send("welcome")
