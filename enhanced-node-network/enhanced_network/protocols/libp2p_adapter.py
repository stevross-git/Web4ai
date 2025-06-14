"""Adapter skeleton for libp2p integration."""

from .base_adapter import BaseAdapter


class Libp2pAdapter(BaseAdapter):
    async def send(self, data: bytes, address: str) -> None:
        raise NotImplementedError("libp2p send not implemented")

    async def recv(self) -> bytes:
        raise NotImplementedError("libp2p recv not implemented")
