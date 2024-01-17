import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
lst = map(int, input().split())
minscan = 0
solution = min([x - (minscan := max(minscan,x)) for x in lst])
print(solution)