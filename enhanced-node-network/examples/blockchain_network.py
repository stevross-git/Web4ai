"""Spin up a mesh node that represents a blockchain participant."""

import asyncio
from enhanced_network.core.network_manager import NetworkManager


async def main():
    manager = NetworkManager({"node_type": "blockchain", "listen_port": 9200})
    await manager.start()
    print("Blockchain network node running. Press Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        await manager.stop()


if __name__ == "__main__":
    asyncio.run(main())
