"""Utility class for loading SSL/TLS certificates."""

class CertificateManager:
    def __init__(self, cert_path: str):
        self.cert_path = cert_path

    def load(self) -> bytes | None:
        """Return the certificate bytes or ``None`` if reading fails."""

        try:
            with open(self.cert_path, "rb") as fh:
                return fh.read()
        except OSError:
            return None
