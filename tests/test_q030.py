"""
Unit tests for Question 30: Digit Fifth Powers.
"""

from solutions.q030_digit_fifth_powers import solve


def test_q030_sample():
    # Sum of fourth powers of digits = 19316 (1634 + 8208 + 9474)
    assert solve(4) == 19316


def test_q030_full():
    # Sum of fifth powers of digits = 443839
    assert solve() == 443839
