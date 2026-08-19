"""
Unit tests for Question 50: Consecutive Prime Sum.
"""

from solutions.q050_consecutive_prime_sum import solve


def test_q050_small_cases():
    assert solve(100) == 41
    assert solve(1000) == 953


def test_q050_full():
    assert solve() == 997651

