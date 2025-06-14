"""Event handling system."""

class EventHandler:
    """Very small async event dispatcher used by integration examples."""

    def __init__(self):
        self._handlers = {}

    def register(self, event: str, func):
        self._handlers.setdefault(event, []).append(func)

    async def dispatch(self, event: str, *args, **kwargs):
        for func in self._handlers.get(event, []):
            await func(*args, **kwargs)
