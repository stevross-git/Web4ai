# Web4ai

Web4ai is an experimental collection of networking and tooling 
for distributed AI systems. It provides a small Python package,
**Enhanced Node Network**, which demonstrates a simple mesh
architecture that can be extended with additional protocols.

The repository is organised as follows:

- `enhanced-node-network/` – Python sources, example scripts and
  placeholder docs for the mesh networking layer.

## Getting started

To run the example mesh node:

```bash
cd enhanced-node-network
python -m examples.simple_mesh
```

The example starts a minimal node that listens for WebSocket
connections on port `9000` by default.

