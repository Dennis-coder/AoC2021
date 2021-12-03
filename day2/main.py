def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n")
    indata = [x.split(" ") for x in indata]
    return indata

def calcA(indata):
    horizontonal = 0
    depth = 0
    for (command, val) in indata:
        if command == "forward":
            horizontonal += int(val)
        elif command == "down":
            depth += int(val)
        elif command == "up":
            depth -= int(val)
    print(horizontonal*depth)

def calcB(indata):
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
    print(horizontonal*depth)

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    calcA(indata)
    calcB(indata)

if __name__ == "__main__":
    main()