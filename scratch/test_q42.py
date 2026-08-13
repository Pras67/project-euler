import math
from pathlib import Path

def word_value(word: str) -> int:
    return sum(ord(c) - ord('A') + 1 for c in word)

def is_triangle_number(n: int) -> bool:
    s = math.isqrt(8 * n + 1)
    return s * s == (8 * n + 1)

words_file = Path('data/p042_words.txt')
words = [w.strip('"') for w in words_file.read_text().split(',')]

count = sum(1 for w in words if is_triangle_number(word_value(w)))
print(f"Count: {count}")
