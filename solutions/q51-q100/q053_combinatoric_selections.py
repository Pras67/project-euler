"""
Question 53: Combinatoric Selections
URL: https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n! / (r!(n-r)!), where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?

Measured Runtime: ~0.000400s
"""

import time
from math import comb 


def solve() -> int:

    count = 0 
    
    # calculating up to 100 
    for i in range (0, 100 + 1):
        for j in range (0, i // 2 + 1):
            if comb(i, j) > 1_000_000:
                if j == i- j:
                    count += 1
                else:
                    count += 2 

    return count

if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    elapsed = time.time() - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
