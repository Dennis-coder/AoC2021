from time import perf_counter
from copy import deepcopy

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n\n")
    indata[0] = [[int(x) for x in y.split(",")] for y in indata[0].split("\n")]
    indata[1] = [y.split("=") for y in indata[1].split("\n")]
    return indata

def calc_a(indata):
    nodes = deepcopy(indata[0])
    folds = indata[1]
    count = 0
    axis, val = folds[0]
    val = int(val)
    occupied_coords = {}
    for node in nodes:
        if axis == "fold along x":
            node[0] = node[0] if node[0] < val else val - (node[0] - val)
        elif axis == "fold along y":
            node[1] = node[1] if node[1] < val else val - (node[1] - val)
        key = f"{node[0]},{node[1]}"
        if key not in occupied_coords:
            occupied_coords[key] = True
            count += 1
    return count

def calc_b(indata):
    nodes = deepcopy(indata[0])
    folds = indata[1]
    for (axis, val) in folds:
        val = int(val)
        occupied_coords = {}
        new_nodes = []
        for node in nodes:
            if axis == "fold along x":
                node[0] = node[0] if node[0] < val else val - (node[0] - val)
            elif axis == "fold along y":
                node[1] = node[1] if node[1] < val else val - (node[1] - val)
            key = f"{node[0]},{node[1]}"
            if key not in occupied_coords:
                occupied_coords[key] = True
                new_nodes.append(node)
        nodes = new_nodes
    
    w = max(nodes, key=lambda x: x[0])[0]
    h = max(nodes, key=lambda x: x[1])[1]
    matrix = [["#" if [x,y] in nodes else " " for x in range(w + 1)] for y in range(h + 1)]
    return "".join(["\n" + "".join(row) for row in matrix])

def main():
    total_start = perf_counter()
    indata = read_indata()
    refactor_start = perf_counter()
    indata = refactor_indata(indata)
    refactor_end = perf_counter()
    part1_start = perf_counter()
    a = calc_a(indata)
    part1_end = perf_counter()
    part2_start = perf_counter()
    b = calc_b(indata)
    part2_end = perf_counter()
    total_end = perf_counter()
    print(f"Refactoring time: {time_to_str(refactor_end - refactor_start)}")
    print(f"Part 1 calc time: {time_to_str(part1_end - part1_start)}")
    print(f"Part 2 calc time: {time_to_str(part2_end - part2_start)}")
    print(f"Total time:       {time_to_str(total_end - total_start)}")
    print(f"Answer part 1:    {a}")
    # print(f"Answer part 2:    {b}")

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