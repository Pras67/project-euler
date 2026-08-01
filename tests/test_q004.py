"""
Unit tests for Question 4: Largest Palindrome Product.
"""

from solutions.q004_largest_palindrome_product import is_palindrome, solve


def test_is_palindrome():
    assert is_palindrome(12321)
    assert is_palindrome(9009)
    assert not is_palindrome(12345)


def test_q004_full():
    assert solve() == 906609
