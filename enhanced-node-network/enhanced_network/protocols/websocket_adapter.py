"""WebSocket-based transport adapter."""

import asyncio
import uuid
from typing import Dict, Optional

import websockets

from .base_adapter import BaseAdapter


class WebSocketAdapter(BaseAdapter):
    """Provide WebSocket communication for the mesh network."""

    def __init__(self, config):
        super().__init__(config)
        self.server: Optional[websockets.server.Serve] = None
        self.connections: Dict[str, websockets.WebSocketClientProtocol] = {}
        self.listen_port = self.config.get("port", 9000)

    async def start(self) -> None:
        await super().start()

        async def handler(ws, path):
            peer_id = f"peer-{uuid.uuid4().hex[:8]}"
            self.connections[peer_id] = ws
            try:
                async for msg in ws:
                    await self.on_message(peer_id, msg)
            finally:
                self.connections.pop(peer_id, None)

        self.server = await websockets.serve(handler, "0.0.0.0", self.listen_port)

    async def stop(self) -> None:
        await super().stop()
        for ws in list(self.connections.values()):
            await ws.close()
        if self.server:
            self.server.close()
            await self.server.wait_closed()

    async def connect(self, address: str) -> str:
        ws = await websockets.connect(f"ws://{address}")
        peer_id = f"peer-{uuid.uuid4().hex[:8]}"
        self.connections[peer_id] = ws
        asyncio.create_task(self._recv(ws, peer_id))
        return peer_id

    async def _recv(self, ws: websockets.WebSocketClientProtocol, peer_id: str) -> None:
        try:
            async for msg in ws:
                await self.on_message(peer_id, msg)
        finally:
            self.connections.pop(peer_id, None)

    async def send(self, data: str, peer_id: str) -> None:
        if peer_id in self.connections:
            await self.connections[peer_id].send(data)

    async def on_message(self, peer_id: str, message: str) -> None:
        """Hook for subclasses to process incoming messages."""
        pass
