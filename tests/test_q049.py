"""
Unit tests for Question 49: Prime Permutations.
"""

from solutions.q049_prime_permutations import is_permutation, is_prime, solve


def test_q049_helpers():
    assert is_prime(1487)
    assert is_prime(4817)
    assert is_prime(8147)
    assert is_permutation(1487, 4817, 8147)


def test_q049_full():
    assert solve() == "296962999629"
