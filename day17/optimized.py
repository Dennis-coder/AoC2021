from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[int(y) for y in x.split("=")[1].split("..")] for x in indata.split(": ")[1].split(", ")]
    return indata

def calc_a(indata):
    y = abs(indata[1][0]) - 1 if indata[1][1] < 0 else indata[1][1] if indata[1][1] > 0 else None
    return (y*(y+1)//2)

def sim(x_vel, y_vel, target):
    x, y = 0, 0
    while x < target[0][0] or y > target[1][1]:
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    if target[0][0] <= x and x <= target[0][1] and target[1][0] <= y and y <= target[1][1]:
        return True
    else:
        return False

def calc_b(indata):
    lowest_x = 0
    while (lowest_x*(lowest_x+1)//2) < indata[0][0]:
        lowest_x += 1
    highest_x = indata[0][1]
    lowest_y = indata[1][0]
    highest_y = abs(indata[1][0]) - 1 if indata[1][1] < 0 else indata[1][1] if indata[1][1] > 0 else None
    
    vel = []
    for x in range(lowest_x, highest_x + 1):
        for y in range(lowest_y, highest_y + 1):
            if sim(x, y, indata):
                vel.append([x,y])

    return len(vel)

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