def refactor_indata(indata):
    commands = (*[(*x.split(" "),) for x in indata.split("\n")],)
    return commands

def calc_a(commands):
    horizontonal = 0
    depth = 0
    for (command, val) in commands:
        if command == "forward":
            horizontonal += int(val)
        elif command == "down":
            depth += int(val)
        elif command == "up":
            depth -= int(val)
    return horizontonal*depth

def calc_b(commands):
    horizontonal = 0
    depth = 0
    aim = 0
    for (command, val) in commands:
        if command == "forward":
            horizontonal += int(val)
            depth += aim * int(val)
        elif command == "down":
            aim += int(val)
        elif command == "up":
            aim -= int(val)      
    return horizontonal*depth