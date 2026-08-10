"""
Unit tests for Question 32: Pandigital Products.
"""

from solutions.q032_pandigital_products import is_pandigital_identity, solve


def test_q032_sample():
    # 39 * 186 = 7254 is a 1 through 9 pandigital identity
    assert is_pandigital_identity(39, 186, 7254) is True


def test_q032_full():
    # Sum of all unique products whose identity is 1 through 9 pandigital is 45228
    assert solve() == 45228
