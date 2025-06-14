"""Trivial majority vote consensus mechanism."""

from typing import Any, Dict


def majority_vote(votes: Dict[str, Any]) -> Any:
    """Return the value that appears most often in ``votes``."""
    counts: Dict[Any, int] = {}
    for value in votes.values():
        counts[value] = counts.get(value, 0) + 1
    return max(counts, key=counts.get, default=None)
