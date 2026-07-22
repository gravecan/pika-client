import re

INPUT_FILE = "custom_26.1.hpp"
OUTPUT_FILE = "Libmujina.dll"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = f.read()

bytes_list = re.findall(r'0x([0-9A-Fa-f]{2})', data)

binary = bytes(int(b, 16) for b in bytes_list)

with open(OUTPUT_FILE, "wb") as f:
    f.write(binary)

print(f"Done! Wrote {len(binary)} bytes to {OUTPUT_FILE}")