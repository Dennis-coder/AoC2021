def refactor_indata(indata):
    nodes, folds = indata.split("\n\n")
    nodes = set([(*[int(x) for x in y.split(",")],) for y in nodes.split("\n")])
    folds = (*[y.split("=") for y in folds.split("\n")],)
    return (nodes, folds)

def calc_a(indata):
    nodes, folds = indata
    axis, val = folds[0]
    val = int(val)
    new_nodes = set()
    for node in nodes:
        new_node = [node[0], node[1]]
        if axis == "fold along x":
            new_node[0] = node[0] if node[0] < val else val - (node[0] - val)
        elif axis == "fold along y":
            new_node[1] = node[1] if node[1] < val else val - (node[1] - val)
        new_nodes.add((new_node[0], new_node[1]))
    return len(new_nodes)  

def calc_b(indata):
    nodes, folds = indata
    for (axis, val) in folds:
        val = int(val)
        new_nodes = set()
        for node in nodes:
            new_node = [node[0], node[1]]
            if axis == "fold along x":
                new_node[0] = node[0] if node[0] < val else val - (node[0] - val)
            elif axis == "fold along y":
                new_node[1] = node[1] if node[1] < val else val - (node[1] - val)
            new_nodes.add((new_node[0], new_node[1]))
        nodes = new_nodes
    
    w = max(nodes, key=lambda x: x[0])[0]
    h = max(nodes, key=lambda x: x[1])[1]
    matrix = [["#" if (x,y) in nodes else " " for x in range(w + 1)] for y in range(h + 1)]
    return "".join(["\n" + "".join(row) for row in matrix])