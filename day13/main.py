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

def calcA(indata):
    nodes = deepcopy(indata[0])
    folds = indata[1]
    for (axis, val) in folds[0:1]:
        val = int(val)
        if axis == "fold along x":
            nodes = [[node[0] if node[0] < val else val - (node[0] - val), node[1]] for node in nodes]
        elif axis == "fold along y":
            nodes = [[node[0], node[1] if node[1] < val else val - (node[1] - val)] for node in nodes]
        new_nodes = []
        for node in nodes:
            if node not in new_nodes:
                new_nodes.append(node)
        nodes = new_nodes
    print(len(nodes))

def calcB(indata):
    nodes = deepcopy(indata[0])
    folds = indata[1]
    for (axis, val) in folds:
        val = int(val)
        if axis == "fold along x":
            nodes = [[node[0] if node[0] < val else val - (node[0] - val), node[1]] for node in nodes]
        elif axis == "fold along y":
            nodes = [[node[0], node[1] if node[1] < val else val - (node[1] - val)] for node in nodes]
        new_nodes = []
        for node in nodes:
            if node not in new_nodes:
                new_nodes.append(node)
        nodes = new_nodes
    w, h, = 0, 0
    for (x,y) in nodes:
        w = max(w, x)
        h = max(h, y)
    matrix = [[" " for x in range(w + 1)] for y in range(h + 1)]
    for (x,y) in nodes:
        matrix[y][x] = "#"
    for row in matrix:
        print("".join(row))

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    calcA(indata)
    calcB(indata)

if __name__ == "__main__":
    main()