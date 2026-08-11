"""
Unit tests for Question 36: Double-base Palindromes.
"""

from solutions.q036_double_base_palindromes import is_palindrome, solve


def test_q036_sample():
    # 585 = 1001001001_2 is palindromic in base 10 and base 2
    assert is_palindrome(str(585)) is True
    assert is_palindrome(bin(585)[2:]) is True


def test_q036_full():
    # Sum of all double-base palindromes less than 1,000,000 is 872187
    assert solve() == 872187
