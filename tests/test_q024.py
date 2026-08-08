"""
Unit tests for Question 24: Lexicographic Permutations.
"""

from solutions.q024_lexicographic_permutations import solve


def test_q024_sample():
    # Sample from problem statement: permutations of digits 0, 1, 2
    digits = [0, 1, 2]
    assert solve(1, digits) == "012"
    assert solve(3, digits) == "102"
    assert solve(6, digits) == "210"


def test_q024_full():
    # Millionth lexicographic permutation of 0..9 = 2783915460
    assert solve() == "2783915460"
