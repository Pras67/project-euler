"""
Question 42: Coded Triangle Numbers
URL: https://projecteuler.net/problem=42

The n-th term of the sequence of triangle numbers is given by, t_n = 1/2 * n * (n+1);
so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we obtain a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we call the word a triangle word.

Using p042_words.txt, a text file containing nearly two-thousand common English words,
how many are triangle words?

Measured Runtime: ~0.005755s
"""

import math
from pathlib import Path
import time


def word_value(word: str) -> int:
    """Calculates alphabetical sum for a word (A=1, B=2, ..., Z=26)."""
    return sum(ord(char) - ord("A") + 1 for char in word.upper())


def is_triangle_number(n: int) -> bool:
    """Checks if n is a triangle number by checking if 8*n + 1 is a perfect square."""
    s = math.isqrt(8 * n + 1)
    return s * s == (8 * n + 1)


def solve(filepath: str = "data/p042_words.txt") -> int:
    """Counts how many words in the specified file are triangle words."""
    path = Path(filepath)
    if not path.is_absolute():
        path = Path(__file__).parent.parent / filepath

    words = [w.strip('"') for w in path.read_text().split(",")]
    return sum(1 for word in words if is_triangle_number(word_value(word)))


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
