"""Minimal DHT interface for peer lookup."""

from __future__ import annotations

from typing import Dict, Any


class SimpleDHT:
    """Tiny in-memory DHT mapping keys to values."""

    def __init__(self):
        self._store: Dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str) -> Any | None:
        return self._store.get(key)
