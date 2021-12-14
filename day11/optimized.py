from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[int(x) for x in y] for y in indata.split("\n")]
    return indata

def flash(point, flash_indexes, indata):
    (x, y) = point
    flash_indexes.append((x,y))
    neighbours = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for n in neighbours:
        x2, y2 = x + n[0], y + n[1]
        if x2 < 0 or x2 == len(indata[0]) or y2 < 0 or y2 == len(indata):
            continue
        indata[y2][x2] += 1
        if indata[y2][x2] > 9 and (x2,y2) not in flash_indexes:
            flash([x2, y2], flash_indexes, indata)

def calcA(indata):
    count_flashes = 0
    for _ in range(100):
        flash_indexes = []
        for y in range(len(indata)):
            for x in range(len(indata[0])):
                indata[y][x] += 1
                if indata[y][x] > 9 and (x,y) not in flash_indexes:
                    flash([x, y], flash_indexes, indata)
        count_flashes += len(flash_indexes)
        for (x,y) in flash_indexes:
            indata[y][x] = 0
    return count_flashes

def calcB(indata):
    i = 1
    while True:
        flash_indexes = []
        for y in range(len(indata)):
            for x in range(len(indata[0])):
                indata[y][x] += 1
                if indata[y][x] > 9 and (x,y) not in flash_indexes:
                    flash([x, y], flash_indexes, indata)
        for (x,y) in flash_indexes:
            indata[y][x] = 0
        if len(flash_indexes) == len(indata) * len(indata[0]):
            break
        i += 1
    return i

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