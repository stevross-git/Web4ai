"""Configuration management utilities."""
import yaml
from pathlib import Path
from typing import Any, Dict

def load_config(path: str) -> Dict[str, Any]:
    if not Path(path).is_file():
        return {}
    with open(path, 'r') as fh:
        return yaml.safe_load(fh) or {}
