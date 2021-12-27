from time import perf_counter_ns
import sys
from importlib import import_module
from test import test

def read_indata(day):
    with open(f"day{day}/indata.txt") as file:
        data = file.read()
    return data

def time_to_str(time):
    suffixes = {
        "s": 1000000000,
        "ms": 1000000,
        "µs": 1000,
        "ns": 1,
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
    start = perf_counter_ns()
    res = fun(*args)
    end = perf_counter_ns()
    return time_to_str(end - start), res

def time_one_day(day, file):
    refactor_indata, calc_a, calc_b = import_functions(day, file)
    print(f"Day {day}:")

    total_start = perf_counter_ns()
    indata = read_indata(day)
    refactor_time, indata = timeit(refactor_indata, indata)
    part1_time, a = timeit(calc_a, indata)
    part2_time, b = timeit(calc_b, indata)
    total_end = perf_counter_ns()

    print(f"Refactored in {refactor_time}")
    print(f"Part 1 is {a} in {part1_time}")
    print(f"Part 2 is {b} in {part2_time}")
    print(f"Total time for day {day} is {time_to_str(total_end - total_start)}")

def time_all_days(type):
    times = []
    nr_of_days = 25
    running_total_start = perf_counter_ns()
    for day in range(1, nr_of_days + 1):
        print(f"Now calculating day {day}", end="\r")
        refactor_indata, calc_a, calc_b = import_functions(day, type)
        start = perf_counter_ns()
        indata = read_indata(day)
        refactor_time, indata = timeit(refactor_indata, indata)
        part1_time, a = timeit(calc_a, indata)
        if not a:
            part1_time = "N/A"
        part2_time, b = timeit(calc_b, indata)
        if not b:
            part2_time = "N/A"
        end = perf_counter_ns()
        times.append((day, refactor_time, part1_time, part2_time, time_to_str(end-start), time_to_str(end - running_total_start)))
    
    print("________________________________________________________")
    print("|Day|Refactor| Part 1 | Part 2 |  Total  |Running total|")
    print("|---|--------|--------|--------|---------|-------------|")
    for day, refactor, part1, part2, total, running_total in times:
        out = "| " + (" " if day < 10 else "") + str(day) + "|" + (" " * (8-len(refactor))) + refactor + "|" + (" " * (8-len(part1))) + part1 + "|" + (" " * (8-len(part2))) + part2 + "| " + (" " * (8-len(total))) + total + "|     " + (" " * (8-len(running_total))) + running_total + "|"
        print(out + f"")
    print("|___|________|________|________|_________|_____________|")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "test":
            print(timeit(test)[0])
        elif arg == "main":
            time_all_days("main")
        elif len(sys.argv) > 2:
            day = int(arg)
            time_one_day(day, sys.argv[2])
        else:
            day = int(arg)
            time_one_day(day, "optimized")
    else:
        time_all_days("optimized")