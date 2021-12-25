def refactor_indata(indata):
    fishes = (*[int(x) for x in indata.split(",")],)
    return fishes

def calc(in_fishes, iterations):
    fishes = [0] * 9
    for fish in in_fishes:
        fishes[fish] += 1

    for _ in range(iterations):
        fishes = [fishes[1], fishes[2], fishes[3], fishes[4], fishes[5], fishes[6], fishes[7] + fishes[0], fishes[8], fishes[0]]
    
    return sum(fishes)

def calc_a(fishes):
    return calc(fishes, 80)

def calc_b(fishes):
    return calc(fishes, 256)