from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [int(x) for x in indata.split("\n")]
    return indata

def calc_a(reports):
    higher = 0
    for i in range(1, len(reports)):
        if reports[i] > reports[i-1]:
            higher += 1
    return higher

def calc_b(reports):
    higher = 0
    last_sum = reports[0] + reports[1] + reports[2]
    for i in range(3, len(reports)):
        this_sum = reports[i] + reports[i-1] + reports[i-2]
        if this_sum > last_sum:
            higher += 1
        last_sum = this_sum
    return higher

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