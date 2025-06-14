"""Simple resource manager for tracking shared resources."""

class ResourceManager:
    """Track and allocate named numeric resources."""

    def __init__(self):
        self.resources = {}

    def allocate(self, name: str, amount: int) -> int:
        """Allocate ``amount`` of a resource and return the new total."""
        self.resources[name] = self.resources.get(name, 0) + amount
        return self.resources[name]

    def release(self, name: str, amount: int) -> int:
        """Release ``amount`` of a resource and return the remaining total."""
        if name in self.resources:
            self.resources[name] = max(0, self.resources[name] - amount)
        return self.resources.get(name, 0)

    def usage(self, name: str) -> int:
        """Return the currently allocated amount for ``name``."""
        return self.resources.get(name, 0)
