#!/usr/bin/env python3
"""Generate unbiased, cryptographically secure random integers from the command line."""

from __future__ import annotations

import argparse
import secrets
import sys
from typing import Sequence


def random_integer(minimum: int, maximum: int) -> int:
    """Return a secure random integer in the inclusive [minimum, maximum] range.

    Raises:
        ValueError: If minimum is greater than maximum.
    """
    if minimum > maximum:
        raise ValueError("minimum must be less than or equal to maximum")
    return minimum + secrets.randbelow(maximum - minimum + 1)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure random integers."
    )
    parser.add_argument("minimum", type=int, help="smallest possible value (inclusive)")
    parser.add_argument("maximum", type=int, help="largest possible value (inclusive)")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=1,
        help="number of values to generate (default: 1)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line application."""
    args = build_parser().parse_args(argv)

    if args.count < 1:
        print("error: count must be at least 1", file=sys.stderr)
        return 2

    try:
        for _ in range(args.count):
            print(random_integer(args.minimum, args.maximum))
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
