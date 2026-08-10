"""
Unit tests for Question 31: Coin Sums.
"""

from solutions.q031_coin_sums import solve


def test_q031_sample():
    # 5p can be made in 4 ways: [5], [2+2+1], [2+1+1+1], [1+1+1+1+1]
    assert solve(5, [1, 2, 5]) == 4


def test_q031_full():
    # Number of ways to make 200p (£2) is 73682
    assert solve() == 73682
