"""Adapter stub for Yggdrasil mesh networking."""

from __future__ import annotations


class YggdrasilAdapter:
    """Minimal adapter simulating Yggdrasil connectivity."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.connected = False

    async def connect(self) -> None:
        """Simulate establishing a connection."""
        self.connected = True

    async def disconnect(self) -> None:
        """Simulate closing the connection."""
        self.connected = False
