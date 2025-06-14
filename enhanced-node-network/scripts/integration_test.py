"""Entry point to execute the integration test suite."""

import subprocess
import sys


def main() -> int:
    result = subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], cwd="..")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
