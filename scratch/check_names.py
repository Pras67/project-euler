import urllib.request
import os

with open('data/names.txt', 'r', encoding='utf-8') as f:
    content = f.read()

names = [n.strip('"') for n in content.split(',')]
print("Names in pasted file:", len(names))
sorted_names = sorted(names)

def score(n):
    return sum(ord(c) - ord('A') + 1 for c in n)

total = sum(i * score(n) for i, n in enumerate(sorted_names, 1))
print("Computed total:", total)

# Let's check where COLIN is:
if "COLIN" in sorted_names:
    pos = sorted_names.index("COLIN") + 1
    val = score("COLIN")
    print(f"COLIN: pos={pos}, val={val}, score={pos*val}")
