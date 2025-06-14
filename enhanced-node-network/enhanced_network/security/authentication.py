"""Simple hook for plugging in authentication logic."""

from __future__ import annotations

from typing import Dict, Any


class Authenticator:
    """Very small token based authenticator."""

    def __init__(self, tokens: Dict[str, str] | None = None):
        self.tokens = tokens or {}

    def authenticate(self, node_id: str, token: str) -> bool:
        return self.tokens.get(node_id) == token
