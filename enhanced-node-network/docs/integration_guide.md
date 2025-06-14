# Integration Guide

To integrate an existing project with the mesh, import the :class:`MeshNode`
class and register your own message handlers.  The example below distributes a
simple task to all connected peers:

```python
from enhanced_network.core.mesh_node import MeshNode

node = MeshNode({})

@node.handler('task_request')
async def handle_task(message):
    print('Received task', message.payload)
```

Extending the framework with custom protocols or authentication mechanisms is
encouraged; the provided modules merely demonstrate the concept.
