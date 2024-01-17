import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sp_chars = {
    'sp': ' ',
    'bS': '\\',
    'sQ': '\'',
    'nl': '\n',
}

for instr in input().split():

    if 'nl' in instr:
        print()
        continue

    if instr.isdigit():
        *num, char = instr
        print(int(''.join(num)) * char, end='')
        continue

    num, char = filter(None, re.split(r'(\d{1,2})', instr, maxsplit=1))
    print(int(num) * sp_chars.get(char, char), end='')
