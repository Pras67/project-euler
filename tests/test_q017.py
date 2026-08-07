"""
Unit tests for Question 17: Number Letter Counts.
"""

from solutions.q017_number_letter_counts import get_letter_count, solve


def test_q017_sample():
    # 1 to 5 = 19
    assert solve(5) == 19
    # 342 = 23 (three hundred and forty-two)
    assert get_letter_count(342) == 23
    # 115 = 20 (one hundred and fifteen)
    assert get_letter_count(115) == 20


def test_q017_full():
    # 1 to 1000 = 21124
    assert solve(1000) == 21124
