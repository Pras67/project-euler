"""
Unit tests for Question 13: Large Sum.
"""

from solutions.q013_large_sum import solve


def test_q013_full():
    # First ten digits of the sum of the one hundred 50-digit numbers
    assert solve() == 5537376230
