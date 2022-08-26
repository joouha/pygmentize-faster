#!/usr/bin/env python

from pygments import cmdline
from pygments_cache import (
    get_filter_by_name,
    get_formatter_by_name,
    get_formatter_for_filename,
    get_lexer_for_filename,
    get_style_by_name,
    guess_lexer_for_filename,
)

__version__ = "1.0.1"


def main() -> None:
    """Monkey-patch pygmentize to use functions from pygmentize-cache."""
    cmdline.get_lexer_for_filename = get_lexer_for_filename
    cmdline.get_formatter_for_filename = get_formatter_for_filename
    cmdline.get_formatter_by_name = get_formatter_by_name
    cmdline.get_style_by_name = get_style_by_name

    cmdline.main()


if __name__ == "__main__":
    main()
