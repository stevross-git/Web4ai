version = "1.0.0"
author = "Enhanced Node Network Team"
description = "Distributed Mesh Network for Enhanced Node Servers"
__all__ = [
    'MeshNode',
    'NetworkManager',
    'PeerDiscovery',
    'EnhancedNodeBridge'
]

try:
    from .core.mesh_node import MeshNode
    from .core.network_manager import NetworkManager
    from .core.peer_discovery import PeerDiscovery
    from .integration.enhanced_node_bridge import EnhancedNodeBridge
except Exception:  # pragma: no cover - optional deps may be missing
    pass
