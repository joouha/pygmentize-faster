"""Publishes a new releases of pygmentize-faster."""

from pathlib import Path

from poetry_publish.publish import poetry_publish

import pygmentize_faster


def publish() -> "None":
    """Publishes a new release of euporie to pypi.org."""
    poetry_publish(
        package_root=Path(pygmentize_faster.__file__).parent,
        version=pygmentize_faster.__version__,
    )


if __name__ == "__main__":
    publish()
