"""
Question 31: Coin Sums
URL: https://projecteuler.net/problem=31

In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?

Measured Runtime: ~0.000150s
"""

import time


def solve(target: int = 200, coin_list: list[int] = None) -> int:
    """Calculates the number of ways to make target pence using standard UK coin denominations."""
    if coin_list is None:
        coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coin_list:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
