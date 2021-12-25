def refactor_indata(indata):
    indata = [[int(x) for x in y] for y in indata.split("\n")]
    return indata

def calc_a(indata):
    risk_level = 0
    for y in range(len(indata)):
        for x in range(len(indata[0])):
            neighbours = []
            if x > 0:
                neighbours.append([-1,0])
            if x < len(indata[0]) - 1:
                neighbours.append([1,0])
            if y > 0:
                neighbours.append([0,-1])
            if y < len(indata) - 1:
                neighbours.append([0,1])

            lowest_point = True
            for n in neighbours:
                if indata[y + n[1]][x + n[0]] <= indata[y][x]:
                    lowest_point = False
                    break

            if lowest_point:
                risk_level += indata[y][x] + 1

    return risk_level

def pathfinding(point, indata, seen={}):
    neighbours = []
    if point[0] > 0:
        neighbours.append([-1,0])
    if point[0] < len(indata[0]) - 1:
        neighbours.append([1,0])
    if point[1] > 0:
        neighbours.append([0,-1])
    if point[1] < len(indata) - 1:
        neighbours.append([0,1])

    for n in neighbours:
        cur_point = [point[0] + n[0],point[1] + n[1]]
        if f"{cur_point[0]},{cur_point[1]}" in seen:
            continue
        elif indata[cur_point[1]][cur_point[0]] == 9:
            continue
        else:
            seen[f"{cur_point[0]},{cur_point[1]}"] = True
            pathfinding(cur_point, indata, seen)
    
    return seen

def calc_b(indata):
    low_points = []
    basins = []
    for y in range(len(indata)):
        for x in range(len(indata[0])):
            neighbours = []
            if x > 0:
                neighbours.append([-1,0])
            if x < len(indata[0]) - 1:
                neighbours.append([1,0])
            if y > 0:
                neighbours.append([0,-1])
            if y < len(indata) - 1:
                neighbours.append([0,1])

            lowest_point = True
            for n in neighbours:
                if indata[y + n[1]][x + n[0]] <= indata[y][x]:
                    lowest_point = False
                    break

            if lowest_point:
                low_points.append([x,y])

    for low_point in low_points:
        basins.append(len(pathfinding(low_point, indata, {})))
    
    basins = sorted(basins)
    return basins[-1] * basins[-2] * basins[-3]