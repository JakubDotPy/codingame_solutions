import sys
import math
import binascii
from itertools import groupby

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
encoded = ''.join(f'{ord(c):07b}' for c in message)


parts = []
for num, group in groupby(encoded):
    msg = '0' if num == '1' else '00'
    msg += ' '
    msg += '0' * len(list(group))
    parts.append(msg)

print(' '.join(parts))
