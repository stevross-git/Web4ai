"""WebSocket protocol adapter using the :mod:`websockets` package."""

import asyncio
import websockets

from .base_adapter import BaseAdapter

class WebSocketAdapter(BaseAdapter):
    """Lightweight WebSocket server that echoes received messages."""

    def __init__(self, config: dict | None = None) -> None:
        super().__init__(config)
        self.server = None
        self.connections: set[websockets.WebSocketServerProtocol] = set()

    async def start(self) -> None:
        await super().start()
        host = self.config.get("host", "0.0.0.0")
        port = self.config.get("port", 9000)
        self.server = await websockets.serve(self._handler, host, port)

    async def stop(self) -> None:
        await super().stop()
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        for ws in list(self.connections):
            await ws.close()

    async def _handler(self, websocket: websockets.WebSocketServerProtocol, path: str) -> None:
        self.connections.add(websocket)
        try:
            async for message in websocket:
                if self.on_message:
                    await self.on_message(message)
        finally:
            self.connections.discard(websocket)

    async def send(self, message: str) -> None:
        for ws in list(self.connections):
            await ws.send(message)
