"""Metrics collection stubs."""

class Metrics:
    def __init__(self):
        self.counters = {}

    def inc(self, name: str):
        self.counters[name] = self.counters.get(name, 0) + 1
