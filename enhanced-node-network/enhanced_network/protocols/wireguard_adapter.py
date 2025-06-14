"""Adapter stub for WireGuard tunnels."""

from __future__ import annotations


class WireGuardAdapter:
    """Minimal adapter representing a WireGuard tunnel."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.tunnel_up = False

    async def up(self) -> None:
        """Simulate bringing up the tunnel."""
        self.tunnel_up = True

    async def down(self) -> None:
        """Simulate tearing down the tunnel."""
        self.tunnel_up = False
