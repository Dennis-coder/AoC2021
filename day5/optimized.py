from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in indata.split("\n")]
    return indata

def calc_a(indata):
    count_dict = {}
    count = 0
    for ((start_x, start_y), (stop_x, stop_y)) in indata:
        if start_x == stop_x:
            x = start_x
            it = range(start_y, stop_y + 1) if start_y < stop_y else range(stop_y, start_y + 1)
            for y in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1
        elif start_y == stop_y:
            y = start_y
            it = range(start_x, stop_x + 1) if start_x < stop_x else range(stop_x, start_x + 1)
            for x in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1

    return count

def calc_b(indata):
    count_dict = {}
    count = 0
    for ((start_x, start_y), (stop_x, stop_y)) in indata:
        if start_x == stop_x:
            x = start_x
            it = range(start_y, stop_y + 1) if start_y < stop_y else range(stop_y, start_y + 1)
            for y in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1
        elif start_y == stop_y:
            y = start_y
            it = range(start_x, stop_x + 1) if start_x < stop_x else range(stop_x, start_x + 1)
            for x in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1
        else:
            for i in range(abs(start_x - stop_x) + 1):
                x = start_x + i if start_x < stop_x else start_x - i
                y = start_y + i if start_y < stop_y else start_y - i
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1

    return count

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