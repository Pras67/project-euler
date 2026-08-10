import time

def is_pandigital_identity(a: int, b: int, c: int) -> bool:
    s = f"{a}{b}{c}"
    return len(s) == 9 and set(s) == set("123456789")

def solve() -> int:
    products = set()

    # 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1000, 10000):
            c = a * b
            if is_pandigital_identity(a, b, c):
                products.add(c)

    # 2-digit * 3-digit = 4-digit
    for a in range(10, 100):
        for b in range(100, 1000):
            c = a * b
            if is_pandigital_identity(a, b, c):
                products.add(c)

    return sum(products)

if __name__ == "__main__":
    t0 = time.perf_counter()
    ans = solve()
    t1 = time.perf_counter()
    print("Answer:", ans)
    print(f"Execution Time: {t1-t0:.6f}s")
