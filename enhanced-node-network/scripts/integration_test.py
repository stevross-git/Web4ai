"""Entry point for running a minimal integration test suite."""

import subprocess


def main() -> None:
    subprocess.run(["pytest", "tests/integration"], check=False)


if __name__ == "__main__":
    main()
