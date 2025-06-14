"""Simple network manager that loads configuration and manages a mesh node."""
from typing import Dict, Any, Optional
from pathlib import Path
import yaml

from .mesh_node import MeshNode

class NetworkManager:
    def __init__(self, config_path: Optional[str] = None):
        base_path = Path(__file__).resolve().parents[2] / "config"
        config_file = Path(config_path) if config_path else base_path / "network_config.yaml"
        with open(config_file, 'r') as f:
            config: Dict[str, Any] = yaml.safe_load(f) or {}
        bootstrap_file = base_path / "bootstrap_nodes.yaml"
        if bootstrap_file.exists():
            with open(bootstrap_file, 'r') as f:
                nodes = yaml.safe_load(f) or {}
                config['bootstrap_nodes'] = nodes.get('bootstrap_nodes', [])
        self.mesh_node = MeshNode(config)

    async def start(self):
        await self.mesh_node.start()

    async def stop(self):
        await self.mesh_node.stop()
