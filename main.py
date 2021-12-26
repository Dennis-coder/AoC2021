from time import perf_counter
import sys
from importlib import import_module
from test import test

def read_indata(day):
    with open(f"day{day}/indata.txt") as file:
        data = file.read()
    return data

def time_to_str(time):
    suffixes = {
        "s": 1,
        "ms": 0.001,
        "µs": 0.000001,
        "ns": 0.000000001,
    }
    for suffix in suffixes:
        if time >= suffixes[suffix]:
            return f"{(time/suffixes[suffix]):.2f}" + suffix
    return f"{time}"

def import_functions(day, type):
    path = f"day{day}.{type}"
    imp = import_module(path)
    return (getattr(imp, "refactor_indata"), getattr(imp, "calc_a"), getattr(imp, "calc_b"))

def timeit(fun, *args):
    start = perf_counter()
    res = fun(*args)
    end = perf_counter()
    return time_to_str(end - start), res

def time_one_day(day):
    refactor_indata, calc_a, calc_b = import_functions(day, "optimized")
    print(f"Day {day}:")

    total_start = perf_counter()
    indata = read_indata(day)
    refactor_time, indata = timeit(refactor_indata, indata)
    part1_time, a = timeit(calc_a, indata)
    part2_time, b = timeit(calc_b, indata)
    total_end = perf_counter()

    print(f"Refactored in {refactor_time}")
    print(f"Part 1 is {a} in {part1_time}")
    print(f"Part 2 is {b} in {part2_time}")
    print(f"Total time for day {day} is {time_to_str(total_end - total_start)}")

def time_all_days(type):
    times = []
    nr_of_days = 19
    for day in range(1, nr_of_days + 1):
        print(f"Now calculating day {day}", end="\r")
        refactor_indata, calc_a, calc_b = import_functions(day, type)
        start = perf_counter()
        indata = read_indata(day)
        refactor_time, indata = timeit(refactor_indata, indata)
        part1_time, a = timeit(calc_a, indata)
        part2_time, b = timeit(calc_b, indata)
        end = perf_counter()
        times.append((day, refactor_time, part1_time, part2_time, end-start))
    
    print("________________________________________________________")
    print("|Day|Refactor| Part 1 | Part 2 |  Total  |Running total|")
    print("|---|--------|--------|--------|---------|-------------|")
    running_total = 0
    for day, refactor, part1, part2, total in times:
        running_total += total
        out = "| " + (" " if day < 10 else "") + str(day) + "|" + (" " * (8-len(refactor))) + refactor + "|" + (" " * (8-len(part1))) + part1 + "|" + (" " * (8-len(part2))) + part2 + "| " + (" " * (8-len(time_to_str(total)))) + time_to_str(total) + "|     " + (" " * (8-len(time_to_str(running_total)))) + time_to_str(running_total) + "|"
        print(out + f"")
    print("|___|________|________|________|_________|_____________|")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "test":
            print(timeit(test)[0])
        elif arg == "main":
            time_all_days("main")
        else:
            day = int(arg)
            time_one_day(day)
    else:
        time_all_days("optimized")