"""One Letter for Your Day: exactly one letter."""
import os

# Z: the day was zonked, slept through on the inside while walking around on the outside.
LETTER = "Z"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LETTER)
