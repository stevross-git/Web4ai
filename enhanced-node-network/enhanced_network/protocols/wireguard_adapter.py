"""Adapter skeleton for WireGuard integration."""

from .base_adapter import BaseAdapter


class WireguardAdapter(BaseAdapter):
    async def send(self, data: bytes, address: str) -> None:
        raise NotImplementedError("WireGuard send not implemented")

    async def recv(self) -> bytes:
        raise NotImplementedError("WireGuard recv not implemented")
