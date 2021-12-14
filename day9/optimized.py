from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[int(x) for x in y] for y in indata.split("\n")]
    return indata

def calcA(indata):
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
            

def calcB(indata):
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

def main():
    total_start = perf_counter()
    indata = read_indata()
    refactor_start = perf_counter()
    indata = refactor_indata(indata)
    refactor_end = perf_counter()
    part1_start = perf_counter()
    a = calcA(indata)
    part1_end = perf_counter()
    part2_start = perf_counter()
    b = calcB(indata)
    part2_end = perf_counter()
    total_end = perf_counter()
    print(f"Refactoring time: {time_to_str(refactor_end - refactor_start)}")
    print(f"Part 1 calc time: {time_to_str(part1_end - part1_start)}")
    print(f"Part 2 calc time: {time_to_str(part2_end - part2_start)}")
    print(f"Total time:       {time_to_str(total_end - total_start)}")
    print(f"Answer part 1:    {a}")
    print(f"Answer part 2:    {b}")

def time_to_str(time):
    suffixes = {
        "s": 1,
        "ms": 0.001,
        "µs": 0.000001,
        "ns": 0.000000001,
    }
    for suffix in suffixes:
        if time > suffixes[suffix]:
            return f"{(time/suffixes[suffix]):.2f}" + suffix
    return f"{time}"


if __name__ == "__main__":
    main()