"""Simple HTTP dashboard for displaying node and device information."""

from __future__ import annotations

import http.server
import threading
import socket
from typing import Tuple

from ..core.mesh_node import MeshNode


def start_dashboard(node: MeshNode, port: int = 8080) -> Tuple[http.server.HTTPServer, threading.Thread]:
    """Start a minimal dashboard for ``node`` on ``port``.

    The dashboard runs in a background thread and returns the ``HTTPServer``
    object along with the thread instance.
    """

    class DashboardHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # type: ignore[override]
            if self.path != "/":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            device = socket.gethostname()
            peers = ", ".join(node.connections.keys()) or "none"
            html = (
                "<html><body>"
                "<h1>Mesh Node Dashboard</h1>"
                f"<p>Device: {device}</p>"
                f"<p>Node ID: {node.node_id}</p>"
                f"<p>Connected peers: {peers}</p>"
                "</body></html>"
            )
            self.wfile.write(html.encode())

        def log_message(self, format: str, *args: object) -> None:  # noqa: D401
            return  # silence default logging

    server = http.server.HTTPServer(("0.0.0.0", port), DashboardHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def stop_dashboard(server: http.server.HTTPServer) -> None:
    """Stop a previously started dashboard server."""
    server.shutdown()
