"""
Question 51: Prime Digit Replacements
URL: https://projecteuler.net/problem=51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number
is the first example of having seven primes among the ten generated numbers, yielding
the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

Measured Runtime: ~0.105000s
"""

import time


def sieve_of_eratosthenes(limit: int = 1000000) -> list[bool]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime




def solve(target_family_size: int = 8) -> int:
    """
    Find the smallest prime which, by replacing part of the number with the same digit,
    is part of an `target_family_size` prime value family.
    """
    is_prime = sieve_of_eratosthenes()
    primes = [i for i, prime in enumerate(is_prime) if prime]

    for p in primes:
        s = str(p)
        for d in ['0', '1', '2']:
            if s[:-1].count(d) == 3:
                pattern = s[:-1].replace(d, '*') + s[-1]
                family = []

                for digit in '0123456789':
                    if digit == '0' and pattern[0] == '*':
                        continue

                    num = int(pattern.replace('*', digit))

                    if is_prime[num]:
                        family.append(num)

                if len(family) == target_family_size:
                    return min(family)

    return -1


if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    elapsed = time.time() - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
