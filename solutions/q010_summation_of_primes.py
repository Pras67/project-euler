"""
Question 10: Summation of Primes
URL: https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Measured Runtime: ~0.266639s
"""

import time


# Sieve of Eratosthenes solution (Optimized O(N log log N))
def solve(limit: int = 2000000) -> int:
    if limit <= 2:
        return 0

    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    return sum(i for i, is_p in enumerate(sieve) if is_p)


"""
ORIGINAL SOLUTION I DID (Trial Division)
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_of_primes(n: int) -> int:
    primes = []
    i = 2
    while i < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return sum(primes)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
