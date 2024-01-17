import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

order = input()
side = input()

if order[-1] == side:
    print(1)
    exit()

u = d = l = r = 1

def U():
    global u, d, l, r
    d = d + u
    u = 1
    l *= 2
    r *= 2

def D():
    global u, d, l, r
    u = u + d
    d = 1
    l *= 2
    r *= 2

def L():
    global u, d, l, r
    u *= 2
    d *= 2
    r = r + l
    l = 1
    

def R():
    global u, d, l, r
    u *= 2
    d *= 2
    l = l + r
    r = 1


for o in order:
    locals()[o]()
    print(o, locals(), file=sys.stderr, flush=True)

print(locals()[side.lower()])