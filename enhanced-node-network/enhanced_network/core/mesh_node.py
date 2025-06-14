"""Core mesh networking node with WebSocket support."""
import asyncio
import json
import uuid
import socket
import logging
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional, Callable
import websockets

@dataclass
class NodeInfo:
    node_id: str
    node_type: str
    public_key: str
    endpoints: List[str]
    capabilities: List[str]
    metadata: Dict[str, Any]
    last_seen: datetime
    status: str = "online"

@dataclass
class NetworkMessage:
    message_id: str
    sender_id: str
    recipient_id: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: datetime
    ttl: int = 300

class MeshNode:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.node_id = config.get('node_id', f"node-{uuid.uuid4().hex[:12]}")
        self.node_type = config.get('node_type', 'enhanced_node')
        self.listen_port = config.get('listen_port', 9000)
        self.bootstrap_nodes: List[str] = config.get('bootstrap_nodes', [])
        self.peers: Dict[str, NodeInfo] = {}
        self.connections: Dict[str, websockets.WebSocketServerProtocol] = {}
        self.message_handlers: Dict[str, Callable] = {}
        self.running = False
        self.server: Optional[websockets.server.Serve] = None
        self.logger = logging.getLogger(f"MeshNode-{self.node_id}")
        self.logger.setLevel(logging.INFO)
        self._register_default_handlers()

    def _register_default_handlers(self):
        self.message_handlers['peer_discovery'] = self._handle_peer_discovery

    async def start(self):
        self.running = True
        await self._start_websocket_server()
        await self._connect_to_bootstrap_nodes()
        self.logger.info("Mesh node started")

    async def stop(self):
        self.running = False
        for ws in list(self.connections.values()):
            await ws.close()
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        self.logger.info("Mesh node stopped")

    async def _start_websocket_server(self):
        async def handler(websocket, path):
            peer_id = f"peer-{uuid.uuid4().hex[:8]}"
            self.connections[peer_id] = websocket
            try:
                async for msg in websocket:
                    await self._handle_message(json.loads(msg), peer_id)
            finally:
                self.connections.pop(peer_id, None)
        self.server = await websockets.serve(handler, "0.0.0.0", self.listen_port)

    async def connect_to_peer(self, address: str):
        ws = await websockets.connect(f"ws://{address}")
        peer_id = f"peer-{uuid.uuid4().hex[:8]}"
        self.connections[peer_id] = ws
        asyncio.create_task(self._handle_peer_messages(ws, peer_id))
        return peer_id

    async def _handle_peer_messages(self, websocket, peer_id):
        try:
            async for msg in websocket:
                await self._handle_message(json.loads(msg), peer_id)
        finally:
            self.connections.pop(peer_id, None)

    async def send_message(self, recipient_id: str, message_type: str, payload: Dict[str, Any]):
        if recipient_id in self.connections:
            msg = NetworkMessage(
                message_id=str(uuid.uuid4()),
                sender_id=self.node_id,
                recipient_id=recipient_id,
                message_type=message_type,
                payload=payload,
                timestamp=datetime.now(),
            )
            await self.connections[recipient_id].send(json.dumps({'type': 'network_message', 'message': asdict(msg)}))

    async def broadcast_message(self, message_type: str, payload: Dict[str, Any]):
        for peer in list(self.connections.keys()):
            await self.send_message(peer, message_type, payload)

    async def _handle_message(self, data: Dict[str, Any], sender_id: str):
        m_type = data.get('type')
        if m_type == 'network_message':
            nm = NetworkMessage(**data['message'])
            handler = self.message_handlers.get(nm.message_type)
            if handler:
                await handler(nm)
        elif m_type in self.message_handlers:
            await self.message_handlers[m_type](data, sender_id)

    async def _handle_peer_discovery(self, message: NetworkMessage):
        await self.send_message(message.sender_id, 'peer_discovery_response', {
            'node_id': self.node_id,
            'endpoints': [f"{socket.gethostname()}:{self.listen_port}"]
        })

    async def _connect_to_bootstrap_nodes(self):
        for address in self.bootstrap_nodes:
            try:
                await self.connect_to_peer(address)
            except Exception as exc:
                self.logger.warning(f"Failed to connect to bootstrap node {address}: {exc}")

    def register_message_handler(self, message_type: str, handler: Callable):
        self.message_handlers[message_type] = handler
