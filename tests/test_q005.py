"""
Unit tests for Question 5: Smallest Multiple.
"""

from solutions.q005_smallest_multiple import solve


def test_q005_sample():
    assert solve(10) == 2520


def test_q005_full():
    assert solve(20) == 232792560
