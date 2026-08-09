"""
Unit tests for Question 29: Distinct Powers.
"""

from solutions.q029_distinct_powers import solve


def test_q029_sample():
    # 2 <= a <= 5 and 2 <= b <= 5 generates 15 distinct terms
    assert solve(5, 5) == 15


def test_q029_full():
    # 2 <= a <= 100 and 2 <= b <= 100 generates 9183 distinct terms
    assert solve() == 9183
