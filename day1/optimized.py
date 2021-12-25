def refactor_indata(indata):
    indata = (*[int(x) for x in indata.split("\n")],)
    return indata

def calc_a(report):
    higher = 0
    for i in range(1, len(report)):
        if report[i] > report[i-1]:
            higher += 1
    return higher

def calc_b(report):
    higher = 0
    for i in range(3, len(report)):
        if report[i] > report[i-3]:
            higher += 1
    return higher