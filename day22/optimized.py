def refactor_indata(indata):
    operations = [row.split() for row in indata.split("\n")]
    for i in range(len(operations)):
        operations[i] = (operations[i][0], (*[(*[int(x) for x in bound[2:].split("..")],) for bound in operations[i][1].split(",")],))
    return (*operations,)


def calc_a(operations):
    on_cubes = set()
    for op, bounds in operations:
        if op == "on":
            func = on_cubes.add
        elif op == "off":
            func = on_cubes.discard
        ranges = [range(max(bound[0], -50), min(bound[1], 50) + 1) for bound in bounds]
        for x in ranges[0]:
            for y in ranges[1]:
                for z in ranges[2]:
                    func((x,y,z))
    return len(on_cubes)

def calc_b(operations):
    on_cubes = set()
    for op, bounds in operations:
        if op == "on":
            func = on_cubes.add
        elif op == "off":
            func = on_cubes.discard
        ranges = [range(bound[0], bound[1] + 1) for bound in bounds]
        for x in ranges[0]:
            for y in ranges[1]:
                for z in ranges[2]:
                    func((x,y,z))
    return len(on_cubes)