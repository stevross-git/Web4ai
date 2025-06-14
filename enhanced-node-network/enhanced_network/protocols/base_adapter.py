"""Abstract protocol adapter."""

import asyncio
from typing import Any, Dict


class BaseAdapter:
    """Base class for implementing network transport adapters."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.running = False
        self._lock = asyncio.Lock()

    async def start(self) -> None:
        """Start the adapter."""
        self.running = True

    async def stop(self) -> None:
        """Stop the adapter."""
        self.running = False

    async def send(self, data: bytes, address: str) -> None:
        """Send ``data`` to ``address`` using the adapter."""
        raise NotImplementedError

    async def recv(self) -> bytes:
        """Receive raw data from the adapter."""
        raise NotImplementedError
