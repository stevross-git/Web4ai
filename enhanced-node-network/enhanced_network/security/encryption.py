"""Simple symmetric encryption helpers using Fernet."""

from __future__ import annotations

from cryptography.fernet import Fernet


def generate_key() -> bytes:
    """Generate a new Fernet key."""
    return Fernet.generate_key()


def encrypt(key: bytes, data: bytes) -> bytes:
    """Encrypt ``data`` with ``key``."""
    return Fernet(key).encrypt(data)


def decrypt(key: bytes, token: bytes) -> bytes:
    """Decrypt ``token`` with ``key``."""
    return Fernet(key).decrypt(token)
