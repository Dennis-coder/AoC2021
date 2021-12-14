from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n\n")
    indata[1] = [x.split(" -> ") for x in indata[1].split("\n")]
    return indata

def calc(indata, iterations):
    start_val = indata[0]
    new_val = dict(indata[1])
    pairs = dict([[x[0], [x[0][0] + x[1], x[1] + x[0][1]]] for x in indata[1]])

    count_pairs = {}
    for i in range(len(start_val) - 1):
        pair = start_val[i] + start_val[i+1]
        if pair in count_pairs:
            count_pairs[pair] += 1
        else:
            count_pairs[pair] = 1

    count = {}
    for char in start_val:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for _ in range(iterations):
        new_count_pairs = {}
        for pair in count_pairs.keys():
            if new_val[pair] in count:
                count[new_val[pair]] += count_pairs[pair]
            else:
                count[new_val[pair]] = 1
            for new_pair in pairs[pair]:
                if new_pair in new_count_pairs:
                    new_count_pairs[new_pair] += count_pairs[pair]
                else:
                    new_count_pairs[new_pair] = count_pairs[pair]
        count_pairs = new_count_pairs

    most_common = max(count, key=count.get)
    least_common = min(count, key=count.get)
    return count[most_common] - count[least_common]

def main():
    total_start = perf_counter()
    indata = read_indata()
    refactor_start = perf_counter()
    indata = refactor_indata(indata)
    refactor_end = perf_counter()
    part1_start = perf_counter()
    a = calc(indata, 10)
    part1_end = perf_counter()
    part2_start = perf_counter()
    b = calc(indata, 40)
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