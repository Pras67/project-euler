"""
Question 10: Summation of Primes
URL: https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Measured Runtime: ~0.223152s
"""

import time

# Sieve of Eratosthenes solution
def sieve_of_eratosthenes(limit: int = 2000000) -> int:
    if limit <= 2:
        return 0

    n = limit - 1
    primes_list = [True] * (n + 1)
    primes_list[0] = primes_list[1] = False


    p = 2
    while p * p <= n:
        if primes_list[p]:
            for i in range(p * p, n + 1, p):
                primes_list[i] = False
        p += 1

    # print(primes_list)

    sum_of_primes = sum(i for i in range(len(primes_list)) if primes_list[i])

    return sum_of_primes


def solve(limit: int = 2000000) -> int:
    return sieve_of_eratosthenes(limit)


"""
ORIGINAL SOLUTION I DID
NOT used for timing as it is too slow for large inputs
"""

n = 2000000

def is_prime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  for i in range (3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def sum_of_primes(n):
  primes = []

  i = 2
  while i < n:
    if is_prime(i):
      primes.append(i)

    i += 1

  sum_of_the_primes = sum(primes)

  return sum_of_the_primes

sum_of_primes(n)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
