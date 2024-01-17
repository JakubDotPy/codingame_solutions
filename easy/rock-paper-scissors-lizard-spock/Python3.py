import sys
import math
from collections import deque
from collections import defaultdict
from itertools import islice

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

def is_winner(p1_s, p2_s):
    rules = (('R', 'L'), ('P', 'R'), ('C', 'P'), ('L', 'S'), ('S', 'C'), ('C', 'L'), ('L', 'P'), ('P', 'S'), ('S', 'R'), ('R', 'C'))
    return (p1_s, p2_s) in rules


n = int(input())

player_signs = {
    int((parts:=input().split())[0]): parts[1]
    for _ in range(n)
}

rules = {
    'R': 'L',  # Rock crushes Lizard
    'P': 'R',  # Paper covers Rock
    'C': 'P',  # Scissors cuts Paper
    'L': 'S',  # Lizard poisons Spock
    'S': 'C',  # Spock smashes Scissors
    'C': 'L',  # Scissors decapitates Lizard
    'L': 'P',  # Lizard eats Paper
    'P': 'S',  # Paper disproves Spock
    'S': 'R',  # Spock vaporizes Rock
    'R': 'C'   # Rock crushes Scissors
}

queue = deque(player_signs.items())

wins = defaultdict(list)

while True:
    new_round_queue = deque()
    print(queue, file=sys.stderr, flush=True)
    if len(queue) == 1:
        break

    for (p1_n, p1_s), (p2_n, p2_s) in batched(queue, 2):
        if is_winner(p1_s, p2_s):  # p1 wins
            wins[p1_n].append(p2_n)
            new_round_queue.append((p1_n, p1_s))
        elif is_winner(p2_s, p1_s):  # p2 wins
            wins[p2_n].append(p1_n)
            new_round_queue.append((p2_n, p2_s))
        else:
            # tie
            if p1_n < p2_n:
                wins[p1_n].append(p2_n)
                new_round_queue.append((p1_n, p1_s))
            else:
                wins[p2_n].append(p1_n)
                new_round_queue.append((p2_n, p2_s))
    queue = new_round_queue

winner_n, winner_s = queue.popleft()

print(winner_n)
print(*wins[winner_n])
    