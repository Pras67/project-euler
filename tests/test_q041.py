"""
Unit tests for Question 41: Pandigital Prime.
"""

from solutions.q041_pandigital_prime import is_prime, solve


def test_q041_sample():
    # 2143 is a 4-digit pandigital prime
    assert is_prime(2143) is True


def test_q041_full():
    # The largest n-digit pandigital prime is 7652413
    assert solve() == 7652413
