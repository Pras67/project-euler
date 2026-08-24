"""
Question 14: Longest Collatz Sequence
URL: https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Which starting number, under one million, produces the longest chain?

Measured Runtime: ~0.549759s
"""

import time

# q14
# collatz conjecture longest < 1 milly


def collatz_conjecture(n: int) -> int:
    steps = []

    if n == 1:
        return len(steps)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            steps.append(n)
        else:
            n = 3 * n + 1
            steps.append(n)

    return len(steps)


def find_longest_path(limit: int = 1000000) -> tuple[int, int]:
    # Fixed-size cache array for numbers below limit
    # cache[n] stores the remaining steps from n to reach 1
    cache = [0] * limit
    cache[1] = 1  # Base case: 1 takes 1 step

    max_length = 0
    best_starting_number = 0

    for i in range(1, limit):
        n = i
        steps = 0

        while n >= limit or cache[n] == 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            steps += 1

        total_steps = steps + cache[n]
        cache[i] = total_steps

        if total_steps > max_length:
            max_length = total_steps
            best_starting_number = i

    return max_length, best_starting_number


def solve(limit: int = 1000000) -> int:
    _, starting_number = find_longest_path(limit)
    return starting_number


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
