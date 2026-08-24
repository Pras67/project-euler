"""
Question 36: Double-base Palindromes
URL: https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Measured Runtime: ~0.073717s
"""

import time


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def solve(limit: int = 1000000) -> int:
    """Calculates the sum of all numbers below limit that are palindromic in base 10 and base 2."""
    total_sum = 0

    # Double-base palindromes must be odd because binary palindromes must end with '1'
    for n in range(1, limit, 2):
        s_decimal = str(n)
        if is_palindrome(s_decimal):
            s_binary = bin(n)[2:]
            if is_palindrome(s_binary):
                total_sum += n

    return total_sum


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
