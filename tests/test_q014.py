"""
Unit tests for Question 14: Longest Collatz Sequence.
"""

from solutions.q014_longest_collatz_sequence import collatz_conjecture, solve


def test_q014_sample():
    # Sequence starting at 13 contains 10 terms (9 steps + starting term)
    assert collatz_conjecture(13) == 9


def test_q014_full():
    # Longest Collatz chain under 1,000,000 starts at 837799
    assert solve(1000000) == 837799
