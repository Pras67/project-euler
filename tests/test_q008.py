"""
Unit tests for Question 8: Largest Product in a Series.
"""

from solutions.q008_largest_product_in_a_series import solve


def test_q008_sample():
    # Greatest product for 4 adjacent digits
    assert solve(4) == 6561


def test_q008_full():
    # Greatest product for 13 adjacent digits
    assert solve(13) == 89996344704
