"""Utility helpers for synchronising blockchain state between nodes."""

from __future__ import annotations

import asyncio
from typing import Dict, Any, List


class BlockchainSync:
    """Very small blockchain synchroniser used in examples."""

    def __init__(self, node):
        self.node = node

    async def request_latest_block(self, peer_id: str) -> Dict[str, Any] | None:
        """Ask ``peer_id`` for its latest block.

        The function sends a ``block_request`` message and waits for a
        ``block_response`` reply.  It returns the block dictionary or ``None`` if
        no response arrives within a short timeout.
        """

        fut: asyncio.Future | None = None

        async def handler(message):
            nonlocal fut
            if fut is not None and not fut.done():
                fut.set_result(message.payload)

        self.node.register_message_handler("block_response", handler)
        await self.node.send_message(peer_id, "block_request", {})
        fut = asyncio.get_event_loop().create_future()
        try:
            return await asyncio.wait_for(fut, timeout=5)
        except asyncio.TimeoutError:
            return None

    async def broadcast_block(self, block: Dict[str, Any]) -> None:
        """Broadcast ``block`` to all connected peers."""

        await self.node.broadcast_message("block_announce", block)
