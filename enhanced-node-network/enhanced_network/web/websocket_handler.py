"""Tiny example WebSocket handler used by the tests."""

async def handle_websocket(websocket, path):
    await websocket.send("welcome")
