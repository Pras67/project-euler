"""
Unit tests for Question 3: Largest Prime Factor.
"""

from solutions.q003_largest_prime_factor import solve


def test_q003_sample():
    # Sample from problem statement: prime factors of 13195 are 5, 7, 13, 29
    assert solve(13195) == 29


def test_q003_full():
    assert solve(600851475143) == 6857
