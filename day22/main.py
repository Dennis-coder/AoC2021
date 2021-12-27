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

class Cube:

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
    
    def __repr__(self):
        return f"{self.x1=}, {self.x2=}, {self.y1=}, {self.y2=}, {self.z1=}, {self.z2=}"

    def size(self):
        return (
            (self.x2 - self.x1) *
            (self.y2 - self.y1) *
            (self.z2 - self.z1)
        )
    
    def intersects(self, other):
        return (
            self.x1 < other.x2 and
            self.x2 > other.x1 and
            self.y1 < other.y2 and
            self.y2 > other.y1 and
            self.z1 < other.z2 and
            self.z2 > other.z1
        )

    def contains(self, other):
        return (
            self.x1 <= other.x1 and
            self.x2 >= other.x2 and
            self.y1 <= other.y1 and
            self.y2 >= other.y2 and
            self.z1 <= other.z1 and
            self.z2 >= other.z2
        )
    
    def subtract(self, other):
        if not self.intersects(other):
            return [self]
        elif other.contains(self):
            return []

        xs = sorted((self.x1, self.x2, other.x1, other.x2))
        ys = sorted((self.y1, self.y2, other.y1, other.y2))
        zs = sorted((self.z1, self.z2, other.z1, other.z2))

        ret = []
        for x1, x2 in zip(xs, xs[1:]):
            for y1, y2 in zip(ys, ys[1:]):
                for z1, z2 in zip(zs, zs[1:]):
                    cube = Cube(x1,x2,y1,y2,z1,z2)
                    if self.contains(cube) and not cube.intersects(other):
                        ret.append(cube)
        return ret

def calc_b(operations):
    reboots = [[op[0] == "on", Cube(*sum([[x + i for i, x in enumerate(bound)] for bound in op[1]], []))] for op in operations]
    cubes = []
    for on, step_cube in reboots:
        cubes = [
            part
            for cube in cubes
            for part in cube.subtract(step_cube)
        ]
        if on:
            cubes.append(step_cube)
    return sum(cube.size() for cube in cubes)