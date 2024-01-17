import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = [
    input()
    for _ in range(h)
]


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

available_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
for row in rows:
    line = ''
    for char in t.upper():
        try:
            i = available_chars.index(char)
        except ValueError:
            i = len(available_chars) - 1
        line += ''.join(row[i * l:(i * l) + l])
    print(line)
