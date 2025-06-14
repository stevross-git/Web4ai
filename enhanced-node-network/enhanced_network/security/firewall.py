"""Very simple IP allow/deny firewall."""

from typing import Set


class Firewall:
    def __init__(self, allowed: Set[str] | None = None):
        self.allowed = allowed or set()

    def allow(self, ip: str) -> None:
        self.allowed.add(ip)

    def deny(self, ip: str) -> None:
        if ip in self.allowed:
            self.allowed.remove(ip)

    def is_allowed(self, ip: str) -> bool:
        return ip in self.allowed
