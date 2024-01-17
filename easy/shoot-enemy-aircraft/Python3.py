import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

planes = []

n = int(input())
for y in range(n):
    for x, c in enumerate(input()):
        if c in '<>':
            planes.append((x, y))
        elif c == '^' :
            rx, ry = x, y

dists = {
    abs(rx - x) + abs(ry - y) - (ry - y) * 2
    for x, y in planes
}

for i in range(1, max(dists) + 1):
    print('SHOOT' if i in dists else 'WAIT')
