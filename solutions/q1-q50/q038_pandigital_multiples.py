"""
Question 38: Pandigital Multiples
URL: https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:
192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

Concatenating these products yields the 9-digit number 192384576, which is 1 to 9 pandigital.

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?

Measured Runtime: ~0.002000s
"""

import time


def is_pandigital_1_to_9(s: str) -> bool:
    """Checks if a string consists of digits 1 to 9 exactly once."""
    return len(s) == 9 and set(s) == set("123456789")


def get_concatenated_product(x: int) -> str:
    """Generates the concatenated product of x with (1, 2, ..., n) until length is at least 9."""
    result = ""
    n = 1
    while len(result) < 9:
        result += str(x * n)
        n += 1
    return result


def solve() -> int:
    """Finds the largest 1 to 9 pandigital 9-digit number formed as a concatenated product."""
    max_pandigital = 0

    # Since n > 1, x must be at most 4 digits (x < 10000)
    for x in range(1, 10000):
        concatenated = get_concatenated_product(x)
        if is_pandigital_1_to_9(concatenated):
            value = int(concatenated)
            if value > max_pandigital:
                max_pandigital = value

    return max_pandigital


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
