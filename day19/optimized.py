def refactor_indata(indata):
    indata = [[[int(z) for z in y.split(",")] for y in x.split("\n")[1:]] for x in indata.split("\n\n")]
    return indata

def calc_a(indata):
    all_offsets = []
    for scanner in indata:
        scanner_offsets = []
        for i in range(len(scanner) - 1):
            for j in range(i + 1, len(scanner)):
                offset = []
                for k in range(len(scanner[i])):
                    offset.append(abs(scanner[i][k] - scanner[j][k]))
                scanner_offsets.append(set(offset))
        all_offsets.append(scanner_offsets)

def calc_b(indata):
    pass
