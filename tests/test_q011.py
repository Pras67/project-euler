"""
Unit tests for Question 11: Largest Product in a Grid.
"""

from solutions.q011_largest_product_in_a_grid import solve


def test_q011_full():
    # Greatest product of 4 adjacent numbers in the 20x20 grid (89 * 94 * 97 * 87)
    assert solve() == 70600674
