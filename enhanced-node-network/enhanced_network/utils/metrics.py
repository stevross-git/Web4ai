"""Very small in-memory metrics helper."""

import time
from contextlib import contextmanager
from typing import Dict


class Metrics:
    def __init__(self) -> None:
        self.counters: Dict[str, int] = {}
        self.timers: Dict[str, float] = {}

    def inc(self, name: str) -> None:
        """Increment counter ``name`` by one."""
        self.counters[name] = self.counters.get(name, 0) + 1

    def get(self, name: str) -> int:
        return self.counters.get(name, 0)

    @contextmanager
    def time(self, name: str):
        """Context manager for timing operations."""
        start = time.monotonic()
        try:
            yield
        finally:
            duration = time.monotonic() - start
            self.timers[name] = duration

    def timer(self, name: str) -> float:
        return self.timers.get(name, 0.0)
