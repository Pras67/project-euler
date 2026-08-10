"""
Unit tests for Question 34: Digit Factorials.
"""

import math
from solutions.q034_digit_factorials import solve


def test_q034_sample():
    # 145 = 1! + 4! + 5!
    assert sum(math.factorial(int(d)) for d in "145") == 145


def test_q034_full():
    # Sum of all numbers equal to the sum of digit factorials is 40730 (145 + 40585)
    assert solve() == 40730
