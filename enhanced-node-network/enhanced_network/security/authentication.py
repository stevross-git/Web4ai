"""Simple token based authentication helpers."""

from typing import Dict


class Authenticator:
    """Validate API tokens for nodes."""

    def __init__(self, tokens: Dict[str, str]):
        self.tokens = tokens

    def validate(self, node_id: str, token: str) -> bool:
        """Return ``True`` if ``token`` matches the stored token for ``node_id``."""
        return self.tokens.get(node_id) == token
