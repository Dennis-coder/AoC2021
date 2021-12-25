def refactor_indata(indata):
    indata = [int(x) for x in indata.split(",")]
    return indata

def calc_a(indata):
    crabs = sorted(indata)
    left = crabs[0]
    right = crabs[-1]
    costs = {}
    while True:
        mid = (left + right) // 2
        if mid not in costs:
            costs[mid] = sum([abs(crab - mid) for crab in crabs])
        if (mid - 1) not in costs:
            costs[mid - 1] = sum([abs(crab - (mid - 1)) for crab in crabs])
        if (mid + 1) not in costs:
            costs[mid + 1] = sum([abs(crab - (mid + 1)) for crab in crabs])
        if costs[mid - 1] < costs[mid]:
            right = mid - 1
        elif costs[mid + 1] < costs[mid]:
            left = mid + 1
        else:
            return costs[mid]

def calc_b(indata):
    crabs = sorted(indata)
    left = crabs[0]
    right = crabs[-1]
    costs = {}
    while True:
        mid = (left + right) // 2
        if mid not in costs:
            costs[mid] = sum([abs(crab - mid) * (abs(crab - mid) + 1) // 2 for crab in crabs])
        if (mid - 1) not in costs:
            costs[mid - 1] = sum([abs(crab - (mid - 1)) * (abs(crab - (mid - 1)) + 1) // 2 for crab in crabs])
        if (mid + 1) not in costs:
            costs[mid + 1] = sum([abs(crab - (mid + 1)) * (abs(crab - (mid + 1)) + 1) // 2 for crab in crabs])
        if costs[mid - 1] < costs[mid]:
            right = mid - 1
        elif costs[mid + 1] < costs[mid]:
            left = mid + 1
        else:
            return costs[mid]