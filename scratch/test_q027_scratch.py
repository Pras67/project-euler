import time

def solve(max_abs_a: int = 999, max_abs_b: int = 1000) -> int:
    sieve_limit = 200000
    is_prime_arr = [True] * (sieve_limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    for p in range(2, int(sieve_limit**0.5) + 1):
        if is_prime_arr[p]:
            for m in range(p * p, sieve_limit + 1, p):
                is_prime_arr[m] = False

    b_candidates = [b for b in range(2, max_abs_b + 1) if is_prime_arr[b]]

    max_n = 0
    best_product = 0
    best_a = 0
    best_b = 0

    for b in b_candidates:
        for a in range(-max_abs_a, max_abs_a + 1):
            if b > 2 and a % 2 == 0:
                continue

            # Pruning check
            test_val = max_n * max_n + a * max_n + b
            if test_val <= 1 or test_val > sieve_limit or not is_prime_arr[test_val]:
                continue

            n = 0
            while True:
                val = n * n + a * n + b
                if val <= 1 or val > sieve_limit or not is_prime_arr[val]:
                    break
                n += 1

            if n > max_n:
                max_n = n
                best_product = a * b
                best_a = a
                best_b = b

    print(f"best_a: {best_a}, best_b: {best_b}, max_n: {max_n}, product: {best_product}")
    return best_product

if __name__ == "__main__":
    t0 = time.perf_counter()
    res = solve()
    t1 = time.perf_counter()
    print(f"Result: {res}, Time: {t1-t0:.6f}s")
