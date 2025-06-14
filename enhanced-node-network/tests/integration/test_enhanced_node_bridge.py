from enhanced_network.integration.event_handlers import EventHandler
import pytest


@pytest.mark.asyncio
async def test_event_handler_dispatch():
    ev = EventHandler()
    result = {}

    @ev.on("ping")
    async def handle(data):
        result["msg"] = data

    await ev.dispatch("ping", "pong")
    assert result["msg"] == "pong"
