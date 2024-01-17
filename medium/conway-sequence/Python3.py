import sys
import math
from itertools import groupby

r = int(input())
l_num = int(input())

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

line = [r]

for _ in range(l_num - 1):
    new_line = []
    for n, gr in groupby(line):
        new_line.extend([len(list(gr)), n])
    line = new_line

print(*line)
        