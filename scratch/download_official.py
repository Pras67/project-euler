import urllib.request
import os

url = "https://projecteuler.net/resources/documents/0022_names.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode("utf-8")
        os.makedirs("data", exist_ok=True)
        with open("data/names.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("Success! Downloaded bytes:", len(content))
except Exception as e:
    print("Direct fetch error:", e)
