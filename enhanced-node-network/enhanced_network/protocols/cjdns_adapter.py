"""Adapter skeleton for CJDNS integration."""

from .base_adapter import BaseAdapter


class CjdnsAdapter(BaseAdapter):
    async def send(self, data: bytes, address: str) -> None:
        raise NotImplementedError("CJDNS send not implemented")

    async def recv(self) -> bytes:
        raise NotImplementedError("CJDNS recv not implemented")
