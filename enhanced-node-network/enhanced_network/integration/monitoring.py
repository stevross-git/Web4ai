"""Hooks for integrating basic health monitoring."""

from __future__ import annotations

import logging
from typing import Dict, Any


logger = logging.getLogger("enhanced_network.monitoring")


def emit(metric: str, value: Any) -> None:
    """Log a metric for external collectors to scrape."""

    logger.info("metric %s=%s", metric, value)


class HealthMonitor:
    """Container for node health information."""

    def __init__(self):
        self.stats: Dict[str, Any] = {}

    def update(self, name: str, value: Any) -> None:
        self.stats[name] = value
        emit(name, value)
