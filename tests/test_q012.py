"""
Unit tests for Question 12: Highly Divisible Triangular Number.
"""

from solutions.q012_highly_divisible_triangular_number import solve


def test_q012_sample():
    # Sample from problem statement: first triangle number with > 5 divisors is 28
    assert solve(5) == 28


def test_q012_full():
    assert solve(500) == 76576500
