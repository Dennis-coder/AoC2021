from functools import cache

def refactor_indata(indata):
    edges = [x.split("-") for x in indata.split("\n")]
    nodes = {}
    for edge in edges:
        for node in edge:
            if node not in nodes:
                nodes[node] = []
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])
    return nodes
        
def calc_a(nodes):
    @cache
    def count_next_paths(cur_node, seen):
        if cur_node.islower():
            seen = seen.union({cur_node})
        n_paths = 0
        for node in nodes[cur_node]:
            if node == "end":
                n_paths += 1
            elif node not in seen:
                n_paths += count_next_paths(node, seen)
        return n_paths
    return count_next_paths("start", frozenset())

def calc_b(nodes):
    @cache
    def count_next_paths(cur_node, seen, twice):
        if cur_node.islower():
            seen = seen.union({cur_node})
        n_paths = 0
        for node in nodes[cur_node]:
            if node == "end":
                n_paths += 1
            elif node not in seen:
                n_paths += count_next_paths(node, seen, twice)
            elif node != "start" and twice:
                n_paths += count_next_paths(node, seen, False)
        return n_paths
    return count_next_paths("start", frozenset(), True)