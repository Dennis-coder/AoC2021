from copy import deepcopy

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
    total_volume = 0
    volumes = []
    for op, ((x1,x2),(y1,y2),(z1,z2)) in operations:
        for op2, ((x3,x4),(y3,y4),(z3,z4)) in deepcopy(volumes):
            ((x5,x6),(y5,y6),(z5,z6)) = ((max(x1,x3),min(x2,x4)),(max(y1,y3),min(y2,y4)),(max(z1,z3),min(z2,z4)))
            if x6-x5 == 0 or y6-y5 == 0 or z6-z5 == 0:
                continue
            if op == "on" and op2 == "on":
                total_volume -= (x6-x5+1) * (y6-y5+1) * (z6-z5+1)
                volumes.append(("off", ((x5,x6),(y5,y6),(z5,z6))))
            elif op == "on" and op2 == "off":
                total_volume += (x6-x5+1) * (y6-y5+1) * (z6-z5+1)
                volumes.append(("on", ((x5,x6),(y5,y6),(z5,z6))))
            elif op == "off" and op2 == "on":
                total_volume -= (x6-x5+1) * (y6-y5+1) * (z6-z5+1)
                volumes.append(("off", ((x5,x6),(y5,y6),(z5,z6))))
            elif op == "off" and op2 == "off":
                total_volume += (x6-x5+1) * (y6-y5+1) * (z6-z5+1)
                volumes.append(("on", ((x5,x6),(y5,y6),(z5,z6))))
        if op == "on":
            total_volume += (x2-x1+1) * (y2-y1+1) * (z2-z1+1)
            volumes.append((op, ((x1,x2),(y1,y2),(z1,z2))))
    return total_volume