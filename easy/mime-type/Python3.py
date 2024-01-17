import sys
import math
from pathlib import Path
from functools import partial

debug = partial(print, file=sys.stderr)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

types = dict(input().split() for _ in range(n))
types = {k.lower(): v for k, v in types.items()}
debug(types)


for _ in range(q):
    f = input().lower()
    sfx = f.split('.')
    if not sfx or '.' not in f:
        print('UNKNOWN')
        continue
    last_sfx = sfx[-1]
    debug('>>>', f, sfx, last_sfx)
    f_type = types.get(last_sfx, 'UNKNOWN')
    print(f_type)