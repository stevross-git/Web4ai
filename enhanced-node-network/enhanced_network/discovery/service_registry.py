"""Registers and locates services offered by nodes."""

from __future__ import annotations

from typing import Dict, List


class ServiceRegistry:
    """Keep track of services provided by mesh nodes."""

    def __init__(self):
        self._services: Dict[str, List[str]] = {}

    def register(self, service: str, node_id: str) -> None:
        self._services.setdefault(service, []).append(node_id)

    def lookup(self, service: str) -> List[str]:
        return list(self._services.get(service, []))
