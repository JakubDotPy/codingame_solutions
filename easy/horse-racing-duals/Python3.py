import sys
import math
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = sorted(int(input()) for i in range(n))

min_dist = sys.maxsize
for a, b in zip(s, s[1:]):
    dist = b - a
    if dist < min_dist:
        min_dist = dist

print(min_dist)
