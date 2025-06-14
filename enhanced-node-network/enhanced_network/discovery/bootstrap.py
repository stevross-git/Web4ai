"""Initial peer bootstrapping helpers."""

from __future__ import annotations

from typing import Iterable, List


def load_bootstrap_peers(sources: Iterable[str]) -> List[str]:
    """Return a list of peer addresses from ``sources``.

    ``sources`` may contain file paths or raw ``host:port`` strings.  The
    implementation merely returns the items that look like addresses and ignores
    missing files.  It is intentionally minimal.
    """

    peers: List[str] = []
    for item in sources:
        if ":" in item and "\n" not in item:
            peers.append(item)
        else:
            try:
                with open(item, "r", encoding="utf-8") as f:
                    peers.extend(line.strip() for line in f if ":" in line)
            except OSError:
                continue
    return peers
