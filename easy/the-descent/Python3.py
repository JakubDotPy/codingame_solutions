import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    heights = [int(input()) for _ in range(8)]  # represents the height of one mountain.
    max_h = max(heights)
    ind_m = heights.index(max_h)
    print(ind_m)
