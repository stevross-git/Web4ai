# Architecture

The Enhanced Node Network implements a lightweight mesh design where every
node can act as both a client and a server.  Nodes connect via WebSockets by
default but additional protocol adapters can be plugged in.

```
┌────────────┐     ┌────────────┐
│  Node A    │◀──▶│  Node B    │
└────────────┘     └────────────┘
```

Each node exposes a small set of handlers for discovery and task dispatch.
This repository only demonstrates the basics, leaving room for custom logic on
top of the framework.
