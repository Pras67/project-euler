"""
Unit tests for Question 18: Maximum Path Sum I.
"""

from solutions.q018_maximum_path_sum_i import solve


def test_q018_sample():
    # Sample 4-row triangle from problem statement = 23
    sample_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    assert solve(sample_triangle) == 23


def test_q018_full():
    # 15-row triangle maximum path sum = 1074
    assert solve() == 1074
