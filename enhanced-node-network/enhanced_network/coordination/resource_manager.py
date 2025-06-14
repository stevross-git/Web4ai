"""Simple asynchronous resource manager."""

from typing import Dict
import asyncio


class ResourceManager:
    """Track and allocate shared resources across the network."""

    def __init__(self) -> None:
        self.resources: Dict[str, int] = {}
        self._lock = asyncio.Lock()

    async def allocate(self, name: str, amount: int) -> int:
        """Allocate ``amount`` of resource ``name``.

        Returns the total allocated amount for that resource after the
        allocation completes.
        """
        async with self._lock:
            self.resources[name] = self.resources.get(name, 0) + amount
            return self.resources[name]

    async def release(self, name: str, amount: int) -> int:
        """Release ``amount`` of resource ``name`` and return remaining."""
        async with self._lock:
            current = self.resources.get(name, 0)
            current = max(current - amount, 0)
            self.resources[name] = current
            return current

    async def usage(self, name: str) -> int:
        """Return the current allocation for ``name``."""
        return self.resources.get(name, 0)

    async def all_resources(self) -> Dict[str, int]:
        """Return a snapshot of all resources."""
        return dict(self.resources)
