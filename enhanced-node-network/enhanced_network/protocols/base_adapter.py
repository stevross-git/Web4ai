"""Base protocol adapter."""

class BaseAdapter:
    def __init__(self, config):
        self.config = config

    async def start(self):
        raise NotImplementedError
