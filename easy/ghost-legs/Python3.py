import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

full_grid = [list(input()) for _ in range(h)]
grid = [
    [c for i, c in enumerate(row, start=1) if i % 3 != 0]
    for row in full_grid
]

start_row, end_row = grid[0], grid[-1]

for start_idx in range(0, w, 2):
    print(start_row[start_idx], end='')
    idx = start_idx
    for row in grid[1:-1]:
        try:
            l = row[idx - 1]
        except IndexError:
            l = ' '
        try:
            r = row[idx + 1]
        except IndexError:
            r = ' '
        if l == '-':
            idx -= 2
            continue
        if r == '-':
            idx += 2
            continue
    print(end_row[idx])

