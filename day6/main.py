def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split(",")
    indata = [int(x) for x in indata]
    return indata

def calcA(indata):
    fishes = [0] * 9
    for fish in indata:
        fishes[fish] += 1

    for _ in range(80):
        fishes = [fishes[1], fishes[2], fishes[3], fishes[4], fishes[5], fishes[6], fishes[7] + fishes[0], fishes[8], fishes[0]]
    
    return sum(fishes)


def calcB(indata):
    fishes = [0] * 9
    for fish in indata:
        fishes[fish] += 1

    for _ in range(256):
        fishes = [fishes[1], fishes[2], fishes[3], fishes[4], fishes[5], fishes[6], fishes[7] + fishes[0], fishes[8], fishes[0]]

    return sum(fishes)

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calcA(indata)
    b = calcB(indata)
    print(a,b)

if __name__ == "__main__":
    main()