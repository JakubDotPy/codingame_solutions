from math import floor, ceil

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

y_min, y_max = 0, h
x_min, x_max = 0, w

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if 'U' in bomb_dir:
        y_max = y
        y = y - ceil((y - y_min) / 2)

    if 'D' in bomb_dir:
        y_min = y
        y = y + (y_max - y) // 2

    if 'R' in bomb_dir:
        x_min = x
        x = x + (x_max - x) // 2

    if 'L' in bomb_dir:
        x_max = x
        x = x - ceil((x - x_min) / 2)
    
    print(x, y)
