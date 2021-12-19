from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

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