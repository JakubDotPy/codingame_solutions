import sys
import math
from collections import namedtuple
from functools import partial
from operator import and_
from operator import or_
from operator import xor

debug = partial(print, file=sys.stderr, flush=True)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())

signals = {}
for _ in range(n):
    n, s = input().split()
    signals[n] = s.replace("_", '0').replace('-', '1')

Operation = namedtuple('Operation', ['out_name', 'type_', 'in_1', 'in_2'])
ops = [Operation(*input().split()) for _ in range(m)]

op_fns = {
    'AND': and_,
    'OR': or_,
    'XOR': xor,
    'NAND': lambda x, y: ~and_(x, y) + 2,
    'NOR': lambda x, y: ~or_(x, y) + 2,
    'NXOR': lambda x, y: ~xor(x, y) + 2,
}

def to_symbol(num):
    return str(num).replace('1', '-').replace('0', '_')

for op in ops:
    fn = op_fns[op.type_]
    res = ''.join(
        str(fn(int(a), int(b)))
        for a, b in zip(signals[op.in_1], signals[op.in_2])
    )
    print(op.out_name, res.replace('1', '-').replace('0', '_'))