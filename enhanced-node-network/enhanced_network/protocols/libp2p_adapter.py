"""Adapter stub for libp2p based communication."""

from __future__ import annotations


class LibP2PAdapter:
    """Minimal adapter that records connection state."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.connected = False

    async def connect(self) -> None:
        """Simulate establishing a connection."""
        self.connected = True

    async def disconnect(self) -> None:
        """Simulate closing the connection."""
        self.connected = False
