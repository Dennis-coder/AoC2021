def refactor_indata(indata):
    indata = indata.split("\n")
    indata = [int(x) for x in indata]
    return indata

def calc_a(reports):
    higher = 0
    for i in range(1, len(reports)):
        if reports[i] > reports[i-1]:
            higher += 1
    return higher

def calc_b(reports):
    higher = 0
    for i in range(3, len(reports)):
        if reports[i] + reports[i-1] + reports[i-2] > reports[i-1] + reports[i-2] + reports[i-3]:
            higher += 1
    return higher