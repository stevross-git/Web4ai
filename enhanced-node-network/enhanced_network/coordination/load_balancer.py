"""Simple round-robin load balancer for tasks."""

from collections import deque
from typing import Any, Deque, Optional


class LoadBalancer:
    def __init__(self):
        self._queue: Deque[Any] = deque()

    def register(self, worker: Any) -> None:
        self._queue.append(worker)

    def next_worker(self) -> Optional[Any]:
        if not self._queue:
            return None
        worker = self._queue.popleft()
        self._queue.append(worker)
        return worker
