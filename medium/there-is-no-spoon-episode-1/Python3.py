import sys
import math
from functools import partial
debug = partial(print, file=sys.stderr, flush=True)

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grid = [
    (x, y)
    for y in range(height)
    for x, c in enumerate(input())
    if c == '0'
]

for i, (cx, cy) in enumerate(grid):
    msg = [cx, cy]
    
    right = list(filter(lambda c: c[0] > cx and c[1] == cy, grid))
    bottom = list(filter(lambda c: c[0] == cx and c[1] > cy, grid))

    if right:
        msg.extend(right[0])
    else:
        msg.extend([-1, -1])

    if bottom:
        msg.extend(bottom[0])
    else:
        msg.extend([-1, -1])

    res = ' '.join(map(str, msg))
    print(res)

