"""
Unit tests for Question 35: Circular Primes.
"""

from solutions.q035_circular_primes import solve


def test_q035_sample():
    # There are 13 circular primes below 100
    assert solve(100) == 13


def test_q035_full():
    # There are 55 circular primes below 1,000,000
    assert solve() == 55
