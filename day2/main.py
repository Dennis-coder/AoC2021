def refactor_indata(indata):
    indata = indata.split("\n")
    indata = [x.split(" ") for x in indata]
    return indata

def calc_a(indata):
    horizontonal = 0
    depth = 0
    for (command, val) in indata:
        if command == "forward":
            horizontonal += int(val)
        elif command == "down":
            depth += int(val)
        elif command == "up":
            depth -= int(val)
    return horizontonal*depth

def calc_b(indata):
    horizontonal = 0
    depth = 0
    aim = 0
    for (command, val) in indata:
        if command == "forward":
            horizontonal += int(val)
            depth += aim * int(val)
        elif command == "down":
            aim += int(val)
        elif command == "up":
            aim -= int(val)
    return horizontonal*depth