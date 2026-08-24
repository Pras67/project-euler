"""
Question 4: Largest Palindrome Product
URL: https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Measured Runtime: ~0.001485s
"""

import time


def is_palindrome(n: int) -> bool:
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]


def solve() -> int:
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j

            # halves calculations done by using commutative property
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
