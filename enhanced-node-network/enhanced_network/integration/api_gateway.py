"""HTTP gateway for exposing mesh functionality to external clients."""

from __future__ import annotations

import http.server
import json
import threading
from typing import Tuple

from ..core.mesh_node import MeshNode


def start_api_gateway(node: MeshNode, port: int = 8081) -> Tuple[http.server.HTTPServer, threading.Thread]:
    """Expose a very small HTTP API for inspecting ``node``."""

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # type: ignore[override]
            if self.path != "/info":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = {"node_id": node.node_id, "peers": list(node.connections.keys())}
            self.wfile.write(json.dumps(payload).encode())

        def log_message(self, format: str, *args: object) -> None:  # noqa: D401
            return

    server = http.server.HTTPServer(("0.0.0.0", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def stop_api_gateway(server: http.server.HTTPServer) -> None:
    server.shutdown()
