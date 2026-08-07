"""
Unit tests for Question 16: Power Digit Sum.
"""

from solutions.q016_power_digit_sum import solve


def test_q016_sample():
    # 2^15 = 32768, sum of digits = 26
    assert solve(15) == 26


def test_q016_full():
    # Sum of digits of 2^1000 = 1366
    assert solve(1000) == 1366
