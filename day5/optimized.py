from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in indata.split("\n")]
    return indata

def calcA(indata):
    count_dict = {}
    for line in indata:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            continue
        if line[0][0] == line[1][0]:
            x = line[0][0]
            it = range(line[0][1], line[1][1] + 1) if line[0][1] < line[1][1] else range(line[1][1], line[0][1] + 1)
            for y in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            it = range(line[0][0], line[1][0] + 1) if line[0][0] < line[1][0] else range(line[1][0], line[0][0] + 1)
            for x in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
    count = 0
    for key in count_dict.keys():
        if count_dict[key] > 1:
            count += 1
    return count

def calcB(indata):
    count_dict = {}
    for line in indata:
        if line[0][0] == line[1][0]:
            x = line[0][0]
            it = range(line[0][1], line[1][1] + 1) if line[0][1] < line[1][1] else range(line[1][1], line[0][1] + 1)
            for y in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            it = range(line[0][0], line[1][0] + 1) if line[0][0] < line[1][0] else range(line[1][0], line[0][0] + 1)
            for x in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        else:
            for i in range(abs(line[0][0] - line[1][0]) + 1):
                x = line[0][0] + i if line[0][0] < line[1][0] else line[0][0] - i
                y = line[0][1] + i if line[0][1] < line[1][1] else line[0][1] - i
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1

    count = 0
    for key in count_dict.keys():
        if count_dict[key] > 1:
            count += 1
    return count

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