"""
Question 6: Sum Square Difference
URL: https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Measured Runtime: ~0.000018s (Normal Solution)
Measured Runtime: ~0.000008s (Optimised Solution)
"""

import time


def sum_of_squares(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    return total_sum


def square_of_sum(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum ** 2


def solve(n: int = 100) -> int:
    return square_of_sum(n) - sum_of_squares(n)


"""
Optimised O(1) time complexity solution (below)
Uses algebraic formulas to solve in constant time
"""


def solve_o1(n: int = 100) -> int:
    sq_of_sum = (n * (n + 1) // 2) ** 2
    sum_of_sq = (n * (n + 1) * (2 * n + 1)) // 6
    return sq_of_sum - sum_of_sq


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve_o1()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
