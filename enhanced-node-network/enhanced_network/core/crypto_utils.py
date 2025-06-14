"""Helpers for symmetric encryption using AES-GCM."""

from __future__ import annotations

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key() -> bytes:
    """Return a new 128-bit key."""
    return AESGCM.generate_key(bit_length=128)


def encrypt(key: bytes, data: bytes, associated_data: bytes | None = None) -> bytes:
    """Encrypt ``data`` and return nonce + ciphertext."""
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ct = aes.encrypt(nonce, data, associated_data)
    return nonce + ct


def decrypt(key: bytes, token: bytes, associated_data: bytes | None = None) -> bytes:
    """Decrypt ``token`` produced by :func:`encrypt`."""
    aes = AESGCM(key)
    nonce, ct = token[:12], token[12:]
    return aes.decrypt(nonce, ct, associated_data)
