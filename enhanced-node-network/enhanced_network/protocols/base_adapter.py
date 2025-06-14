"""Base protocol adapter providing common lifecycle hooks."""

class BaseAdapter:
    """Base class for network protocol adapters."""

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}
        self.running = False
        self.on_message = None

    async def start(self) -> None:
        """Start the adapter."""
        self.running = True

    async def stop(self) -> None:
        """Stop the adapter."""
        self.running = False

    async def send(self, message: str) -> None:
        """Send a message to connected peers."""
        raise NotImplementedError
