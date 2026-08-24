"""
Question 49: Prime Permutations
URL: https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms is prime, and
(ii) each of the 4-digit numbers are permutations of one another.

There are no 4-digit terms that increase by 3330 that share this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Measured Runtime: ~0.001100s
"""


import time
import math

def is_prime(n : int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_permutation(n1: int, n2: int, n3: int) -> bool:
    return sorted(str(n1)) == sorted(str(n2)) == sorted(str(n3))

def find_sequence() -> list[int]:
    primes = [i for i in range(1000, 3340) if is_prime(i)]

    sequence = []
    
    for i in primes:
        if i == 1487:
            continue

        if not is_prime(i + 3330) or not is_prime(i + 6660):
            continue

        if is_permutation(i, i + 3330, i + 6660):
            sequence.append(i)
            sequence.append(i + 3330)
            sequence.append(i + 6660)
    
    return sequence


def solve() -> str:
    """Finds the 12-digit number 
    formed by concatenating the 3-term prime permutation arithmetic sequence."""
    seq = find_sequence()
    return "".join(map(str, seq))



if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
