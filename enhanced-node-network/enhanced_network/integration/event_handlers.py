"""Asynchronous event dispatching helpers."""

from collections import defaultdict
from typing import Callable, Awaitable, Dict, List


Callback = Callable[..., Awaitable[None]]


class EventHandler:
    """Register and dispatch events to async callbacks."""

    def __init__(self) -> None:
        self._handlers: Dict[str, List[Callback]] = defaultdict(list)

    def register(self, event: str, func: Callback) -> None:
        """Register ``func`` to be called whenever ``event`` is dispatched."""
        self._handlers[event].append(func)

    def unregister(self, event: str, func: Callback) -> None:
        """Remove ``func`` from the handler list for ``event`` if present."""
        if event in self._handlers and func in self._handlers[event]:
            self._handlers[event].remove(func)

    def on(self, event: str) -> Callable[[Callback], Callback]:
        """Decorator to register a function for ``event``."""

        def decorator(func: Callback) -> Callback:
            self.register(event, func)
            return func

        return decorator

    async def dispatch(self, event: str, *args, **kwargs) -> None:
        """Invoke all callbacks registered for ``event``."""
        for func in list(self._handlers.get(event, [])):
            await func(*args, **kwargs)
