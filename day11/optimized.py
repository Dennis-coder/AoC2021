from copy import deepcopy

def refactor_indata(indata):
    octopus = [[int(x) for x in y] for y in indata.split("\n")]
    return octopus

def calc_a(octopus):
    octopus = deepcopy(octopus)
    w, h = len(octopus[0]), len(octopus)
    count_flashes = 0
    neighbours = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    todo = []
    for _ in range(100):
        for y in range(h):
            for x in range(w):
                octopus[y][x] += 1
                if octopus[y][x] > 9:
                    todo.append((x,y))

        while todo:
            (x, y) = todo.pop()
            if octopus[y][x] == 0:
                continue
            count_flashes += 1
            octopus[y][x] = 0
            for dx, dy in neighbours:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < w and 0 <= y2 < h and octopus[y2][x2] != 0:
                    octopus[y2][x2] += 1
                    if octopus[y2][x2] > 9:
                        todo.append((x2,y2))
    return count_flashes

def calc_b(octopus):
    w, h = len(octopus[0]), len(octopus)
    i = 0
    neighbours = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    todo = []
    while True:
        i += 1
        for y in range(h):
            for x in range(w):
                octopus[y][x] += 1
                if octopus[y][x] > 9:
                    todo.append((x,y))

        flashes = 0

        while todo:
            (x, y) = todo.pop()
            if octopus[y][x] == 0:
                continue
            octopus[y][x] = 0
            flashes += 1
            for dx, dy in neighbours:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < w and 0 <= y2 < h and octopus[y2][x2] != 0:
                    octopus[y2][x2] += 1
                    if octopus[y2][x2] > 9:
                        todo.append((x2,y2))

        if flashes == w*h:
            return i