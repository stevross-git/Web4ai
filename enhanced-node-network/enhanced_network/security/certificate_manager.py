"""Helpers for loading SSL/TLS certificates."""

import ssl
from pathlib import Path


class CertificateManager:
    """Load certificate/key pairs and create SSL contexts."""

    def __init__(self, cert_path: str) -> None:
        self.cert_path = Path(cert_path)

    def create_ssl_context(self) -> ssl.SSLContext:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        cert_file = self.cert_path / "cert.pem"
        key_file = self.cert_path / "key.pem"
        if cert_file.exists() and key_file.exists():
            context.load_cert_chain(str(cert_file), str(key_file))
        return context
