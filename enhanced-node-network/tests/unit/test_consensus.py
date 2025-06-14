import asyncio

import pytest

pytest.importorskip("cryptography")

from enhanced_network.core import crypto_utils


@pytest.mark.asyncio
async def test_crypto_roundtrip():
    key = crypto_utils.generate_key()
    data = b"hello"
    enc = crypto_utils.encrypt(key, data)
    dec = crypto_utils.decrypt(key, enc)
    assert dec == data
