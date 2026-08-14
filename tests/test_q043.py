"""
Unit tests for Question 43: Sub-string Divisibility.
"""

from solutions.q043_substring_divisibility import is_valid_pandigital, solve


def test_q043_sample():
    # 1406357289 as list of digits satisfies the divisibility property
    d1 = [1, 4, 0, 6, 3, 5, 7, 2, 8, 9]
    assert is_valid_pandigital(d1) is True

    # 1234567890 does not satisfy the property
    d2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert is_valid_pandigital(d2) is False


def test_q043_full():
    # The sum of all 0 to 9 pandigital numbers with the divisibility property is 16695334890
    assert solve() == 16695334890
