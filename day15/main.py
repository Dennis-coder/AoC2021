from collections import defaultdict
import math

def refactor_indata(indata):
    indata = [[int(x) for x in y] for y in indata.split("\n")]
    return indata

def astar(indata, start, goal, h):
    open_set = {start}
    came_from = {}

    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0

    f_score = defaultdict(lambda: math.inf)
    f_score[start] = h(start)

    while open_set:
        current = min(open_set, key=f_score.get)
        if current == goal:
            return g_score[current]

        open_set.remove(current)
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        for n in neighbors:
            pos = (current[0] + n[0], current[1] + n[1])
            if pos[0] < 0 or pos[0] == len(indata[0]) or pos[1] < 0 or pos[1] == len(indata):
                continue
            tentative_g_score = g_score[current] + indata[pos[1]][pos[0]]
            if tentative_g_score < g_score[pos]:
                came_from[pos] = current
                g_score[pos] = tentative_g_score
                f_score[pos] = tentative_g_score + h(pos)
                if pos not in open_set:
                    open_set.add(pos)

def calc_a(indata):
    def h(pos):
        return (len(indata) + len(indata[0]) - 2) * 5
    return astar(indata, (0,0), (len(indata) - 1, len(indata[0]) - 1), h)

def calc_b(indata):
    new_map = []
    for x in range(5):
        for row in indata:
            new_row = []
            for y in range(5):
                new_row += [((el + x + y - 1) % 9) + 1 for el in row]
            new_map.append(new_row)

    def h(pos):
        return (len(new_map) + len(new_map[0]) - 2) * 5
    return astar(new_map, (0,0), (len(new_map) - 1, len(new_map[0]) - 1), h)