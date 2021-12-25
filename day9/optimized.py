def refactor_indata(indata):
    map = (*[(*[int(x) for x in y],) for y in indata.split("\n")],)
    return map

def calc_a(map):
    risk_level = 0
    seen = {}
    w, h = len(map[0]), len(map)
    neighbours = [[0,1],[1,0],[0,-1],[-1,0]]
    for y in range(h):
        for x in range(w):
            if (x,y) in seen:
                continue
            seen[(x,y)] = True
            lowest_point = True
            for dx, dy in neighbours:
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 == w or y2 < 0 or y2 == h:
                    continue
                if map[y2][x2] <= map[y][x]:
                    lowest_point = False
                    break
                seen[(x2,y2)] = True

            if lowest_point:
                risk_level += map[y][x] + 1

    return risk_level

def pathfinding(minima, map):
    neighbours = [[0,1],[1,0],[0,-1],[-1,0]]
    seen = set()
    todo = [minima]
    w, h = len(map[0]), len(map)
    while todo:
        x, y = todo.pop()
        seen.add((x,y))
        for dx,dy in neighbours:
            x2, y2 = x + dx, y + dy
            if (x2,y2) not in seen and 0 <= x2 <= w - 1 and 0 <= y2 <= h - 1 and map[y2][x2] < 9:
                todo.append((x2,y2))
    return len(seen)

def calc_b(map):
    minimas = []
    seen = {}
    w, h = len(map[0]), len(map)
    neighbours = [[0,1],[1,0],[0,-1],[-1,0]]
    for y in range(h):
        for x in range(w):
            if (x,y) in seen:
                continue
            seen[(x,y)] = True
            is_minima = True
            for dx, dy in neighbours:
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 == w or y2 < 0 or y2 == h:
                    continue
                if map[y2][x2] <= map[y][x]:
                    is_minima = False
                    break
                seen[(x2,y2)] = True

            if is_minima:
                minimas.append((x,y))

    basin_sizes = []
    for minima in minimas:
        basin_sizes.append(pathfinding(minima, map))
    
    basins = sorted(basin_sizes)
    return basins[-1] * basins[-2] * basins[-3]