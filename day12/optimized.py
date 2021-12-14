from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [x.split("-") for x in indata.split("\n")]
    return indata

def pathfinding_a(nodes, cur_node, cur_path, paths, seen):
    for node in nodes[cur_node]:
        if node in seen and node == node.lower():
            continue
        cur_node = node
        cur_path.append(node)
        seen.append(node)
        if cur_path[0] == "start" and cur_path[-1] == "end":
            paths.append(cur_path)
        else:
            pathfinding_a(nodes, cur_node, deepcopy(cur_path), paths, deepcopy(seen))
        cur_path = cur_path[:-1]
        seen = seen[:-1]
        
def calcA(indata):
    nodes = {}
    for edge in indata:
        for node in edge:
            if node not in nodes:
                nodes[node] = []
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])
    paths = []
    seen = ["start"]
    cur_node = "start"
    cur_path = ["start"]
    pathfinding_a(nodes, cur_node, cur_path, paths, seen)
    return len(paths)

def pathfinding_b(nodes, cur_node, cur_path, paths, seen, small_cave_has_been_visited_twice=False):
    for node in nodes[cur_node]:
        this_cave = False
        if node in seen and node == node.lower() and (node == "start" or small_cave_has_been_visited_twice):
            continue
        elif node in seen and node == node.lower():
            small_cave_has_been_visited_twice = True
            this_cave = True
        cur_node = node
        cur_path.append(node)
        seen.append(node)
        if cur_path[0] == "start" and cur_path[-1] == "end":
            paths.append(cur_path)
        else:
            pathfinding_b(nodes, cur_node, deepcopy(cur_path), paths, deepcopy(seen), small_cave_has_been_visited_twice)
        cur_path = cur_path[:-1]
        seen = seen[:-1]
        if this_cave:
            small_cave_has_been_visited_twice = False

def calcB(indata):
    nodes = {}
    for edge in indata:
        for node in edge:
            if node not in nodes:
                nodes[node] = []
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])
    paths = []
    seen = ["start"]
    cur_node = "start"
    cur_path = ["start"]
    pathfinding_b(nodes, cur_node, cur_path, paths, seen)
    return len(paths)

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