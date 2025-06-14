"""Adapter skeleton for Yggdrasil integration."""

from .base_adapter import BaseAdapter


class YggdrasilAdapter(BaseAdapter):
    async def send(self, data: bytes, address: str) -> None:
        raise NotImplementedError("Yggdrasil send not implemented")

    async def recv(self) -> bytes:
        raise NotImplementedError("Yggdrasil recv not implemented")
