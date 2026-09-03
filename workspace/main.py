#!/usr/bin/env python3
"""
Sum Calculator for Integer Ranges

This module provides an efficient O(1) function to compute the sum of all integers
in a closed interval [start, end], using the arithmetic series formula.
It is designed for correctness, readability, and future extensibility (e.g., CLI, tests, config).
"""

from typing import Union


def sum_range(start: int, end: int) -> int:
    """
    Compute the sum of all integers from `start` to `end` inclusive.

    Uses the arithmetic series formula:
        sum = (sum 1..end) - (sum 1..(start-1))
            = end*(end+1)//2 - (start-1)*start//2

    Args:
        start: The inclusive lower bound (must be <= end)
        end:   The inclusive upper bound (must be >= start)

    Returns:
        The integer sum of all values in [start, end]

    Raises:
        ValueError: If start > end or either argument is not an integer.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError(f"Invalid range: start ({start}) > end ({end})")

    # Sum from 1 to end
    sum_to_end = end * (end + 1) // 2
    # Sum from 1 to (start - 1)
    sum_to_start_minus_1 = (start - 1) * start // 2
    return sum_to_end - sum_to_start_minus_1


def main() -> None:
    """Entry point: computes and prints sum from 1 to 100."""
    result = sum_range(1, 100)
    print(f"Sum from 1 to 100 is: {result}")


# --- Unit Tests (lightweight, inline for simplicity & zero dependencies) ---
if __name__ == "__main__":
    # Run basic correctness assertions before main
    assert sum_range(1, 100) == 5050, "Failed: sum(1..100) != 5050"
    assert sum_range(1, 1) == 1, "Failed: sum(1..1) != 1"
    assert sum_range(5, 5) == 5, "Failed: sum(5..5) != 5"
    assert sum_range(1, 10) == 55, "Failed: sum(1..10) != 55"
    assert sum_range(10, 10) == 10, "Failed: sum(10..10) != 10"
    
    # Run main program
    main()