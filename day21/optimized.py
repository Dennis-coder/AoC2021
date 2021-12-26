def refactor_indata(indata):
    starting_pos = (*[int(x.split(": ")[1]) for x in indata.split("\n")],)
    return starting_pos

def calc_a(starting_pos):
    players = [[starting_pos[0], 0], [starting_pos[1], 0]]
    dice = 1
    i = 0
    while players[0][1] < 1000 and players[1][1] < 1000:
        player = players[i%2]
        movement = 0
        for _ in range(3):
            movement += dice
            dice = dice % 100 + 1
        player[0] = (player[0] + movement - 1) % 10 + 1
        player[1] += player[0]
        i += 1
    return (players[0][1] if players[0][1] < 1000 else players[1][1]) * i*3
        

def calc_b(starting_pos):
    universes = {
        (*starting_pos, 0, 0, True): 1
    }
    player_1_wins = 0
    player_2_wins = 0
    i = 0
    while universes:
        new_universes = {}
        for (p1_pos, p2_pos, p1_score, p2_score, p1_turn), n in universes.items():
            if p1_turn:
                new_states = [
                    (((p1_pos + 2) % 10 + 1, p2_pos, p1_score + ((p1_pos + 2) % 10 + 1), p2_score, False), 1),
                    (((p1_pos + 3) % 10 + 1, p2_pos, p1_score + ((p1_pos + 3) % 10 + 1), p2_score, False), 3),
                    (((p1_pos + 4) % 10 + 1, p2_pos, p1_score + ((p1_pos + 4) % 10 + 1), p2_score, False), 6),
                    (((p1_pos + 5) % 10 + 1, p2_pos, p1_score + ((p1_pos + 5) % 10 + 1), p2_score, False), 7),
                    (((p1_pos + 6) % 10 + 1, p2_pos, p1_score + ((p1_pos + 6) % 10 + 1), p2_score, False), 6),
                    (((p1_pos + 7) % 10 + 1, p2_pos, p1_score + ((p1_pos + 7) % 10 + 1), p2_score, False), 3),
                    (((p1_pos + 8) % 10 + 1, p2_pos, p1_score + ((p1_pos + 8) % 10 + 1), p2_score, False), 1),
                ]
                for state, m in new_states:
                    if state[2] >= 21:
                        player_1_wins += n*m
                    else:
                        if state not in new_universes:
                            new_universes[state] = 0
                        new_universes[state] += n*m
            else:
                new_states = [
                    ((p1_pos, (p2_pos + 2) % 10 + 1, p1_score, p2_score + ((p2_pos + 2) % 10 + 1), True), 1),
                    ((p1_pos, (p2_pos + 3) % 10 + 1, p1_score, p2_score + ((p2_pos + 3) % 10 + 1), True), 3),
                    ((p1_pos, (p2_pos + 4) % 10 + 1, p1_score, p2_score + ((p2_pos + 4) % 10 + 1), True), 6),
                    ((p1_pos, (p2_pos + 5) % 10 + 1, p1_score, p2_score + ((p2_pos + 5) % 10 + 1), True), 7),
                    ((p1_pos, (p2_pos + 6) % 10 + 1, p1_score, p2_score + ((p2_pos + 6) % 10 + 1), True), 6),
                    ((p1_pos, (p2_pos + 7) % 10 + 1, p1_score, p2_score + ((p2_pos + 7) % 10 + 1), True), 3),
                    ((p1_pos, (p2_pos + 8) % 10 + 1, p1_score, p2_score + ((p2_pos + 8) % 10 + 1), True), 1),
                ]
                for state, m in new_states:
                    if state[3] >= 21:
                        player_2_wins += n*m
                    else:
                        if state not in new_universes:
                            new_universes[state] = 0
                        new_universes[state] += n*m
        universes = new_universes
    return max((player_1_wins, player_2_wins))