"""Adapter stub for connecting to a cjdns overlay network."""

from __future__ import annotations


class CJDNSAdapter:
    """Minimal adapter simulating a cjdns connection."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.running = False

    async def start(self) -> None:
        """Pretend to start the cjdns interface."""
        self.running = True

    async def stop(self) -> None:
        """Pretend to stop the interface."""
        self.running = False
