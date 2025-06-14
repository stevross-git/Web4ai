"""Symmetric encryption utilities using Fernet."""

from cryptography.fernet import Fernet


class Encryptor:
    def __init__(self, key: bytes | None = None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.cipher.decrypt(token)

    def get_key(self) -> bytes:
        return self.key
