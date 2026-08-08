"""
Question 22: Names Scores
URL: https://projecteuler.net/problem=22

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Measured Runtime: ~0.005692s
"""

import os
import time

# Locate the data/names.txt file relative to this solution script
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "names.txt")


def name_value(name: str) -> int:
    """
    Calculates the alphabetical value of a name.
    Each letter is converted to its 1-based alphabet position:
    'A' -> 1, 'B' -> 2, ..., 'Z' -> 26 using ASCII character codes (ord).
    """
    return sum(ord(char) - ord("A") + 1 for char in name)


def solve(filepath: str = DATA_FILE) -> int:
    """
    Reads names from file, sorts them alphabetically, and computes the sum
    of (1-based position * alphabetical name value) for every name.
    """
    # Reads raw file contents containing "NAME1","NAME2",...
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Splits comma-separated names and strip surrounding double quotes
    names = [name.strip('"') for name in content.split(",")]

    # Sorts all names into alphabetical order
    names.sort()

    # Multiplies each name's 1-based position by its alphabetical score & sums them up
    total_score = 0
    for position, name in enumerate(names, start=1):
        total_score += position * name_value(name)

    return total_score


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
