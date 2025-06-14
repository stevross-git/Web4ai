"""Start a small mesh for AI compute nodes."""

import asyncio
from enhanced_network.core.network_manager import NetworkManager


async def main():
    manager = NetworkManager({"node_type": "ai_compute", "listen_port": 9100})
    await manager.start()
    print("AI compute cluster running. Press Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        await manager.stop()


if __name__ == "__main__":
    asyncio.run(main())
