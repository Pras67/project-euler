"""
Question 21: Amicable Numbers
URL: https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Measured Runtime: ~0.034876s
"""

import time


def sum_proper_divisors(n: int) -> int:
    if n <= 1:
        return 0
    sum_divs = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divs += i
            if i * i != n:
                sum_divs += n // i
    return sum_divs


def solve(limit: int = 10000) -> int:
    amicable_numbers_sum = 0
    found_amicable_numbers = set()

    for a in range(1, limit):
        if a in found_amicable_numbers:
            continue  # Skip if already processed as part of a pair

        b = sum_proper_divisors(a)

        # Check for amicable pair conditions
        if b > a and sum_proper_divisors(b) == a:
            amicable_numbers_sum += a + b
            found_amicable_numbers.add(a)
            found_amicable_numbers.add(b)

    return amicable_numbers_sum


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
