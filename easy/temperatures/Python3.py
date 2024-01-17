import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = list(map(int, input().split()))

if not temps:
    print(0)

temps.sort(key=lambda t: (abs(t), t<0))

print(temps[0])
