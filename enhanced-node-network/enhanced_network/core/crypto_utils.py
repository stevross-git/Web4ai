"""Basic cryptographic helpers for signing and verifying messages."""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


def generate_keypair() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()


def sign(private_key: rsa.RSAPrivateKey, data: bytes) -> bytes:
    return private_key.sign(data, padding.PKCS1v15(), hashes.SHA256())


def verify(public_key: rsa.RSAPublicKey, signature: bytes, data: bytes) -> bool:
    try:
        public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
        return True
    except Exception:
        return False


def export_private_key(private_key: rsa.RSAPrivateKey) -> bytes:
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )


def export_public_key(public_key: rsa.RSAPublicKey) -> bytes:
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
