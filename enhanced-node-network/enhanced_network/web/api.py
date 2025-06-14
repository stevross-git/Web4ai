"""Flask-style HTTP API endpoints for controlling the mesh."""

from __future__ import annotations

import http.server
import json
import threading
from typing import Tuple

from ..core.mesh_node import MeshNode


def start_api(node: MeshNode, port: int = 8082) -> Tuple[http.server.HTTPServer, threading.Thread]:
    """Start a minimal API server exposing the mesh node."""

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # type: ignore[override]
            if self.path != "/state":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"node": node.node_id, "connections": list(node.connections.keys())}
            self.wfile.write(json.dumps(data).encode())

        def log_message(self, format: str, *args: object) -> None:  # noqa: D401
            return

    server = http.server.HTTPServer(("0.0.0.0", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def stop_api(server: http.server.HTTPServer) -> None:
    server.shutdown()
