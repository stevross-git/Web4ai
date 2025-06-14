"""Simple asynchronous event dispatcher."""

from __future__ import annotations

import asyncio
from collections import defaultdict
from typing import Any, Awaitable, Callable, Dict, List


class EventDispatcher:
    """Register callbacks and dispatch events to them."""

    def __init__(self) -> None:
        self._listeners: Dict[str, List[Callable[..., Awaitable | Any]]] = defaultdict(list)

    def register(self, event: str, handler: Callable[..., Awaitable | Any]) -> None:
        """Register ``handler`` to be called when ``event`` is dispatched."""
        self._listeners[event].append(handler)

    async def dispatch(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Dispatch ``event`` to all registered handlers."""
        for handler in list(self._listeners.get(event, [])):
            if asyncio.iscoroutinefunction(handler):
                await handler(*args, **kwargs)
            else:
                handler(*args, **kwargs)

    def dispatch_sync(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Synchronously dispatch ``event`` creating tasks for async handlers."""
        loop = asyncio.get_event_loop()
        for handler in list(self._listeners.get(event, [])):
            if asyncio.iscoroutinefunction(handler):
                loop.create_task(handler(*args, **kwargs))
            else:
                handler(*args, **kwargs)

