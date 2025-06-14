"""Basic firewall hooks for controlling inbound connections."""

from __future__ import annotations

from typing import Set


class Firewall:
    """Track allowed peer identifiers."""

    def __init__(self):
        self.allowed: Set[str] = set()

    def allow(self, peer_id: str) -> None:
        self.allowed.add(peer_id)

    def deny(self, peer_id: str) -> None:
        self.allowed.discard(peer_id)

    def is_allowed(self, peer_id: str) -> bool:
        return peer_id in self.allowed
