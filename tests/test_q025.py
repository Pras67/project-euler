"""
Unit tests for Question 25: 1000-digit Fibonacci Number.
"""

from solutions.q025_1000_digit_fibonacci_number import solve


def test_q025_sample():
    # F12 is the first term with 3 digits (144)
    assert solve(3) == 12


def test_q025_full():
    # Index of first term to contain 1000 digits = 4782
    assert solve() == 4782
