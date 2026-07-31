"""
Unit tests for Question 2: Even Fibonacci Numbers.
"""

from solutions.q002_even_fibonacci_numbers import solve


def test_q002_sample():
    # Terms <= 10: 1, 2, 3, 5, 8 -> even terms: 2, 8 -> sum = 10
    assert solve(10) == 10


def test_q002_full():
    assert solve(4_000_000) == 4613732
