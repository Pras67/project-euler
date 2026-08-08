"""
Unit tests for Question 22: Names Scores.
"""

from solutions.q022_names_scores import name_value, solve


def test_q022_colin_value():
    # COLIN: C=3, O=15, L=12, I=9, N=14 -> sum = 53
    assert name_value("COLIN") == 53


def test_q022_full():
    # Total of all name scores in names.txt = 870818385
    assert solve() == 870818385
