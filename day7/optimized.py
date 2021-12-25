from statistics import mean, median

def refactor_indata(indata):
    crabs = [int(x) for x in indata.split(",")]
    return (*sorted(crabs),)

def calc_a(crabs):
    cur_pos = int(median(crabs))
    costs = {}
    while True:
        if cur_pos not in costs:
            costs[cur_pos] = sum([abs(crab - cur_pos) for crab in crabs])
        if (cur_pos - 1) not in costs:
            costs[cur_pos - 1] = sum([abs(crab - (cur_pos - 1)) for crab in crabs])
        if (cur_pos + 1) not in costs:
            costs[cur_pos + 1] = sum([abs(crab - (cur_pos + 1)) for crab in crabs])
        if costs[cur_pos - 1] < costs[cur_pos]:
            cur_pos -= 1
        elif costs[cur_pos + 1] < costs[cur_pos]:
            cur_pos += 1
        else:
            return costs[cur_pos]

def calc_b(crabs):
    cur_pos = int(mean(crabs))
    costs = {}
    while True:
        if cur_pos not in costs:
            costs[cur_pos] = sum([abs(crab - cur_pos) * (abs(crab - cur_pos) + 1) // 2 for crab in crabs])
        if (cur_pos - 1) not in costs:
            costs[cur_pos - 1] = sum([abs(crab - (cur_pos - 1)) * (abs(crab - (cur_pos - 1)) + 1) // 2 for crab in crabs])
        if (cur_pos + 1) not in costs:
            costs[cur_pos + 1] = sum([abs(crab - (cur_pos + 1)) * (abs(crab - (cur_pos + 1)) + 1) // 2 for crab in crabs])
        if costs[cur_pos - 1] < costs[cur_pos]:
            cur_pos -= 1
        elif costs[cur_pos + 1] < costs[cur_pos]:
            cur_pos += 1
        else:
            return costs[cur_pos]