from functools import cache
from itertools import cycle

def refactor_indata(indata):
    starting_pos = (*[int(x.split(": ")[1]) for x in indata.split("\n")],)
    return starting_pos

def calc_a(starting_pos):
    players = [[starting_pos[0], 0], [starting_pos[1], 0]]
    dice = cycle(range(1, 101))
    turn = cycle([0,1])
    i = 0
    while players[0][1] < 1000 and players[1][1] < 1000:
        player = players[next(turn)]
        movement = next(dice) + next(dice) + next(dice)
        player[0] = (player[0] + movement - 1) % 10 + 1
        player[1] += player[0]
        i += 3
    (_, p1_score), (_, p2_score) = players
    return min(p1_score, p2_score) * i


rolls = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
@cache
def compute_wins(p1, p1_score, p2, p2_score):
    p1_wins = p2_wins = 0
    for roll, ct in rolls.items():
        new_p1 = (p1 + roll - 1) % 10 + 1
        new_p1_score = p1_score + new_p1
        if new_p1_score >= 21:
            p1_wins += ct
        else:
            tmp_p2_wins, tmp_p1_wins = compute_wins(p2, p2_score, new_p1, new_p1_score)
            p1_wins += tmp_p1_wins * ct
            p2_wins += tmp_p2_wins * ct

    return p1_wins, p2_wins

def calc_b(starting_pos):
    p1, p2 = starting_pos
    p1_wins, p2_wins = compute_wins(p1, 0, p2, 0)
    return max(p1_wins, p2_wins)