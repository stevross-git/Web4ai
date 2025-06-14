"""Simplified consensus helpers used in tests."""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Any


def reach_consensus(values: Iterable[Any]) -> Any | None:
    """Return the most common value from ``values``.

    If ``values`` is empty the function returns ``None``.  The implementation is
    deliberately trivial but sufficient for unit tests and example usage.
    """

    counter = Counter(values)
    if not counter:
        return None
    return counter.most_common(1)[0][0]
