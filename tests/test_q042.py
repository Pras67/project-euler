"""
Unit tests for Question 42: Coded Triangle Numbers.
"""

from solutions.q042_coded_triangle_numbers import is_triangle_number, solve, word_value


def test_q042_sample():
    # "SKY" has value 19 + 11 + 25 = 55, which is t_10 (the 10th triangle number)
    assert word_value("SKY") == 55
    assert is_triangle_number(55) is True

    # 20 is not a triangle number
    assert is_triangle_number(20) is False


def test_q042_full():
    # There are 162 triangle words in p042_words.txt
    assert solve() == 162
