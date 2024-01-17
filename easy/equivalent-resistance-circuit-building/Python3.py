import sys
import math
import re

n = int(input())

rs = {}
for i in range(n):
    inputs = input().split()
    rs[inputs[0]] = int(inputs[1])

circuit = input()

def series(m):
    nums = m.groups()[0].split()
    return str(sum(map(float, nums)))

def paralel(m):
    nums = m.groups()[0].split()
    nums = map(float, nums)
    return str(1 / sum(1 / n for n in nums))

re_ser = re.compile(r'\( ((\d+(.\d+)? )+)\)')
re_par = re.compile(r'\[ ((\d+(.\d+)? )+)\]')

has_brackets = lambda c: '[' in c or '(' in c 

for k, v in rs.items():
    circuit = re.sub(k, str(v), circuit)

while has_brackets(circuit):
    circuit = re_ser.sub(series, circuit)
    circuit = re_par.sub(paralel, circuit)

print(round(float(circuit), 1))
