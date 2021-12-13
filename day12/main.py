from copy import deepcopy


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
    print(len(paths))

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
    print(len(paths))

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    calcA(indata)
    calcB(indata)

if __name__ == "__main__":
    main()