"""Data serialization helpers."""
import json
from typing import Any

def serialize(data: Any) -> str:
    return json.dumps(data)

def deserialize(data: str) -> Any:
    return json.loads(data)
