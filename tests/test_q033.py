"""
Unit tests for Question 33: Digit Cancelling Fractions.
"""

from solutions.q033_digit_cancelling_fractions import solve


def test_q033_sample():
    # 49/98 cancelling 9s yields 4/8, both equal 0.5
    assert 49 * 8 == 98 * 4


def test_q033_full():
    # Product of 4 non-trivial digit-cancelling fractions in lowest terms has denominator 100
    assert solve() == 100
