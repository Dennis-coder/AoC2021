def refactor_indata(indata):
    indata = indata.split(",")
    indata = [int(x) for x in indata]
    return indata

def calc(indata, iterations):
    fishes = [0] * 9
    for fish in indata:
        fishes[fish] += 1

    for _ in range(iterations):
        fishes = [fishes[1], fishes[2], fishes[3], fishes[4], fishes[5], fishes[6], fishes[7] + fishes[0], fishes[8], fishes[0]]
    
    return sum(fishes)

def calc_a(indata):
    return calc(indata, 80)

def calc_b(indata):
    return calc(indata, 256)