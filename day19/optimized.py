def refactor_indata(indata):
    scanners = (*[(*[(*[int(z) for z in y.split(",")],) for y in x.split("\n")[1:]],) for x in indata.split("\n\n")],)
    return scanners

def calc_a(scanners):
    # all_offsets = []
    # for scanner in scanners:
    #     scanner_offsets = set()
    #     for i in range(len(scanner) - 1):
    #         for j in range(i + 1, len(scanner)):
    #             offset = []
    #             for k in range(len(scanner[i])):
    #                 offset.append(abs(scanner[i][k] - scanner[j][k]))
    #             scanner_offsets.add(set(offset))
    #     all_offsets.append(scanner_offsets)
    pass
    
    

def calc_b(scanners):
    pass
