"""
Question 23: Non-Abundant Sums
URL: https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number (1 + 2 + 3 + 4 + 6 = 16), the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Measured Runtime: ~0.632375s
"""

import time

LIMIT = 28123


def sum_proper_divisors(n: int) -> int:
    """
    Calculates the sum of proper divisors of n (all divisors of n less than n).
    """
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
    return total


def solve(limit: int = LIMIT) -> int:
    """
    Finds the sum of all positive integers less than or equal to limit
    that cannot be written as the sum of two abundant numbers.
    """
    # Precomputes sum of proper divisors using a sieve for maximum speed
    divisor_sum = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sum[j] += i

    # Identifies all abundant numbers <= limit (where sum of proper divisors > n)
    abundant = [i for i in range(12, limit + 1) if divisor_sum[i] > i]

    # Marks all numbers that CAN be expressed as the sum of two abundant numbers
    can_be_abundant_sum = [False] * (limit + 1)
    for i, a1 in enumerate(abundant):
        for a2 in abundant[i:]:
            s = a1 + a2
            if s > limit:
                break
            can_be_abundant_sum[s] = True

    # Sums all positive integers <= limit that CANNOT be written as sum of two abundant numbers
    return sum(i for i in range(1, limit + 1) if not can_be_abundant_sum[i])


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
