import time

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def solve(target: int = 200, coin_list: list[int] = None) -> int:
    if coin_list is None:
        coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coin_list:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]

if __name__ == "__main__":
    t0 = time.perf_counter()
    ans = solve(200)
    t1 = time.perf_counter()
    print("Answer for 200p (£2):", ans)
    print(f"Execution Time: {t1-t0:.8f}s")
