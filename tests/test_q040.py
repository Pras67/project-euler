"""
Unit tests for Question 40: Champernowne's Constant.
"""

from solutions.q040_champernowne_constant import solve


def test_q040_sample():
    # The 12th digit of the fractional part is 1 (since 0.1234567891011...)
    assert solve([12]) == 1


def test_q040_full():
    # Product of d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000 is 210
    assert solve() == 210
