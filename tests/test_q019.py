"""
Unit tests for Question 19: Counting Sundays.
"""

from solutions.q019_counting_sundays import is_leap, solve


def test_q019_is_leap():
    assert is_leap(2000) is True
    assert is_leap(1900) is False
    assert is_leap(1904) is True
    assert is_leap(1901) is False


def test_q019_full():
    # 171 Sundays fell on 1st of month during 1901-2000
    assert solve() == 171
